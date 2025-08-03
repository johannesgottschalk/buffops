from flask import Flask, render_template, request, send_file, redirect, flash
import os
from werkzeug.utils import secure_filename
from logic.validator import validate_buffs
import csv
import yaml
import json
import io

UPLOAD_FOLDER = 'buffs'
ALLOWED_EXTENSIONS = {'yaml', 'yml', 'json', 'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'  # ändere für Deployment

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('buff_file')
        if not file or not allowed_file(file.filename):
            flash('Ungültiges Dateiformat. Erlaubt: .yaml, .yml, .json, .csv')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Parsen
        ext = filename.rsplit('.', 1)[1].lower()
        if ext in ('yaml', 'yml'):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        elif ext == 'json':
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        elif ext == 'csv':
            with open(filepath, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
        else:
            data = []

        # Falls YAML/JSON als dict mit Schlüssel „buffs“ kommt
        if isinstance(data, dict):
            data = data.get('buffs', [])

        # Validieren
        errors = validate_buffs(data)
        if errors:
            return render_template('index.html', errors=errors)

        # TSV erzeugen (gleiche Spaltenreihenfolge wie Input)
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=list(data[0].keys()), delimiter='\t')
        writer.writeheader()
        writer.writerows(data)
        output.seek(0)

        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/tab-separated-values',
            download_name='validated_buffs.tsv',
            as_attachment=True
        )

    return render_template('index.html')

if __name__ == '__main__':
    # Lokaler Start
    app.run(debug=True)
