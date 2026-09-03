# Python Packages Collection (`python_packages`)

This repository serves as the home directory for a collection of custom Python packages. All packages in this repository are ready to be installed via `pip` (directly from Git) or copied directly (copy-paste) into your own projects.

---

## 📦 Package Overview

| Package | Dependencies | Platforms | Description |
| :--- | :--- | :--- | :--- |
| [**pydiskinfo**](pydiskinfo/README.md) | Zero-dependency | Windows, Linux, macOS | Retrieve information about mounted disks, partitions, filesystems, and directory sizes. |

*(More packages will be added gradually)*

---

## 🚀 Installation and Usage Methods

Each package in the repository can be used in several ways:

### 1. Installation via `pip` (from Git repository)

The package is not published on PyPI, but it is ready for direct installation from the Git repository:

```bash
pip install git+https://github.com/schnidi/python_packages.git#subdirectory=pydiskinfo
```

Or for local development in "editable" mode:

```bash
git clone https://github.com/schnidi/python_packages.git
cd python_packages/pydiskinfo
pip install -e .
```

For **VenvHub Pro** users: install the package via the venv context menu → `✏️ Local packages (pip -e)` → `➕ Install from folder (pip -e)` and select the `pydiskinfo` folder.

### 2. Direct Copy to Project (Copy-Paste)

If you don't want to manage the package via pip, simply copy the source code subdirectory (e.g., `python_packages/pydiskinfo/pydiskinfo`) directly into your project and import it locally.


