# BuffOps 🦄🎮
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Unreal Engine](https://img.shields.io/badge/Unreal%20Engine-5.x-black.svg)](https://www.unrealengine.com/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

**BuffOps** is a lightweight **CLI** and **Unreal Engine** integration for creating, managing, and validating  
**buff/debuff systems** in games — built for **Game Designers** and **Developers** who love **data-driven gameplay balancing**.

---

## 🚀 Why BuffOps?
Game balancing often becomes a mess of spreadsheets, version conflicts, and manual imports.  
**BuffOps** automates that process:
- Convert **CSV → TSV** for Unreal DataTables
- Validate buffs & debuffs before they hit your game
- Keep your designers and devs in sync

---

## 🖼️ Preview
 

---

## 📦 Installation
```bash
# Clone repository
git clone https://github.com/johannesgottschalk/buffops.git
cd buffops

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage
```bash
# Convert CSV → TSV for Unreal
python convert.py buffs.csv buffs_output.tsv --format csv

# Validate a buffs file
python validate.py buffs.csv
```

---

## ✨ Features
- **CLI Tools** for conversion & validation
- **Unreal Engine Integration** (DataTables, JSON runtime loading planned)
- **Web Preview** in development
- Modular design — plug into your existing pipeline

---

## 🗺️ Roadmap
- [x] CSV → TSV converter
- [x] Unreal DataTable import
- [ ] JSON runtime loader
- [ ] Unreal plugin with UI preview
- [ ] Web-based preview & editor

---

## 🤝 Contributing
PRs welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License
[MIT](LICENSE) © 2025 Johannes Gottschalk
