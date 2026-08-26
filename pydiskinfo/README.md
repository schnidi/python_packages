# pydiskinfo

A lightweight, zero-dependency, cross-platform Python library for retrieving information about mounted disks, partitions, file systems, and directory sizes on Windows, Linux, and macOS.

## Installation

This package is currently in development and hosted directly in a Git repository. To install it locally in editable mode:

1. Clone the repository:
```bash
git clone https://github.com/schnidi/python_packages.git
cd python_packages/pydiskinfo
```

2. Install in editable mode via pip:
```bash
pip install -e .
```

## Quick Start

### 1. Get all mounted disks

```python
import pydiskinfo

disks = pydiskinfo.get_disks()

for disk in disks:
    print(f"Mount Point: {disk.mount}")
    print(f"UUID:        {disk.uuid}")
    print(f"Filesystem:  {disk.filesystem}")
    print(f"Total:       {disk.total_gb} GB")
    print(f"Used:        {disk.used_gb} GB ({disk.percent_used}%)")
    print(f"Free:        {disk.free_gb} GB")
    print("-" * 30)
```

### 2. Find disk by path

Identify which disk or partition contains a specific file or folder:

```python
import pydiskinfo

disk = pydiskinfo.get_disk_by_path("./my_folder/file.txt")

if disk:
    print(f"Disk Mount: {disk.mount}")
    print(f"Free Space: {disk.free_gb} GB")
```

### 3. Calculate directory size

Recursively compute total directory size in bytes and retrieve all contained paths:

```python
import pydiskinfo

data = pydiskinfo.get_directory_size("./my_project")

size_mb = round(data["size_bytes"] / (1024 ** 2), 2)
print(f"Size: {size_mb} MB")
print(f"Total items: {len(data['items'])}")
```

## Data Model (`DiskInfo`)

Each drive is returned as a `DiskInfo` instance with the following fields and properties:

| Field / Property | Type | Description |
| :--- | :--- | :--- |
| `mount` | `str` | Mount point / drive letter (e.g. `C:` on Windows, `/` on Linux) |
| `uuid` | `str` | Unique partition/volume identifier (if available) |
| `filesystem` | `str` | Filesystem type (e.g. `NTFS`, `ext4`, `apfs`) |
| `total_bytes` | `int` | Total capacity in bytes |
| `free_bytes` | `int` | Free space in bytes |
| `used_bytes` | `int` | Used space in bytes |
| `total_gb` | `float` | Total capacity in gigabytes (rounded to 2 decimal places) |
| `free_gb` | `float` | Available free space in gigabytes (rounded to 2 decimal places) |
| `used_gb` | `float` | Used space in gigabytes (rounded to 2 decimal places) |
| `percent_used` | `float` | Percentage of space currently used (e.g. `45.2`) |

## Platform Implementations

- **Windows**: Native Win32 API via `ctypes` (`GetLogicalDrives`, `GetVolumeInformationW`, `GetDiskFreeSpaceExW`).
- **Linux**: Standard filesystem inspection via `/proc/mounts`, `/dev/disk/by-uuid`, and `os.statvfs`.
- **macOS**: System plist output via `diskutil list/info -plist` and `os.statvfs`.