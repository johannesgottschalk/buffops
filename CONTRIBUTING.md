# Contributing to BuffOps 🦄

Thanks for your interest in contributing! BuffOps is a lightweight toolset for **buff/debuff systems** in games (CLI + Unreal integration + Web Preview).  
We welcome issues, pull requests, docs improvements, and discussion.

---

## 📬 How to Propose a Change

1. **Open an issue** describing the problem/feature first (bug report, feature request, or design proposal).
2. Wait for **maintainer feedback** to align on scope/approach.
3. Fork the repo & create a **feature branch** from `main`:
   ```bash
   git checkout -b feat/short-description
   ```
4. Implement the change with tests/docs where applicable.
5. Open a **pull request** referencing the issue (e.g., `Fixes #123`).

> Small PRs with a clear scope are easier to review and merge.

---

## ✅ Pull Request Checklist

- [ ] Clear title using **Conventional Commits** (see below)
- [ ] Linked issue (e.g., `Fixes #123`)
- [ ] Tests added/updated (if logic changes)
- [ ] Documentation updated (`README.md` / `docs/`)
- [ ] Lint & format pass locally
- [ ] No secrets/keys committed
- [ ] Works on Windows (PowerShell) and POSIX (bash) where applicable

---

## ✍️ Commit Message Style (Conventional Commits)

Use one of the following types in your commit titles:

- `feat:` a new user-facing feature
- `fix:` a bug fix
- `docs:` documentation only
- `refactor:` code change that neither fixes a bug nor adds a feature
- `test:` adding or fixing tests
- `chore:` tooling, CI, dependencies, build
- `perf:` performance improvement
- `ci:` CI configuration

Examples:
```
feat(cli): add CSV → TSV converter with delimiter option
fix(validate): handle empty rows gracefully
docs(readme): add usage examples for Unreal DataTables
```

---

## 🧰 Project Setup

### Python (CLI)
1. Use Python **3.10+**.
2. Create a virtual environment and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. (Optional) Install dev tools:
   ```bash
   pip install -r requirements-dev.txt  # e.g., black, isort, flake8, pytest
   ```

### Unreal Integration
- Place exported **TSV** files into your Unreal project’s `Content/` (or data folder) and import as **DataTable**.
- For C++ structs, keep field names/types in sync with TSV headers.
- If PR affects Unreal integration, include a minimal example or screenshots under `docs/`.

### Web Preview (optional module)
- If editing the web preview, provide a short **setup guide** in `docs/web-preview.md` and include a demo GIF if possible.

---

## 🧪 Testing

- Use **pytest** for CLI tests under `tests/`:
  ```bash
  pytest -q
  ```
- Add tests for new flags, parsers, validators, and edge cases.
- Keep sample data small and deterministic (put under `tests/fixtures/`).

---

## 🧹 Code Style & Linting

- Format with **black**; organize imports with **isort**.
- Lint with **flake8** (or ruff if configured).
- Run before committing:
  ```bash
  black .
  isort .
  flake8 .
  ```
> If `requirements-dev.txt` is not present, feel free to propose it in your PR.

---

## 🔐 Security

- Do not commit secrets or credentials.
- Report vulnerabilities privately via a **Security advisory** or by contacting the maintainer.

---

## 📦 Releases & Versioning

- We aim for **SemVer** (MAJOR.MINOR.PATCH).
- Changelogs are generated from Conventional Commits when possible.

---

## 🗂️ Documentation

- Update `README.md` for user-facing changes.
- Place extended docs, screenshots, and examples in `docs/`.
- Name images descriptively (e.g., `cli_example.png`, `unreal_datatable.png`).

---

## 🤝 Code of Conduct

This project follows a **Contributor Covenant**-style code of conduct.  
Be respectful, helpful, and constructive. Harassment or discrimination is not tolerated.

---

## 💬 Getting Help

- Open a GitHub Issue with a clear description and reproduction steps.
- For quick questions, start a discussion in the **Issues** or **Discussions** tab.

Thanks again for contributing — happy hacking! 🦄🎮
