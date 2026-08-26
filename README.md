# pydiskinfo

[![PyPI version](https://img.shields.io/pypi/v/pydiskinfo.svg)](https://pypi.org/project/pydiskinfo/)
[![Python versions](https://img.shields.io/pypi/pyversions/pydiskinfo.svg)](https://pypi.org/project/pydiskinfo/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A lightweight, zero-dependency, cross-platform Python library to inspect disk drives, storage metrics, filesystem types, and Hardware Volume UUIDs on Windows, Linux, and macOS.

## Features

- Zero External Dependencies: Built purely on native OS APIs (ctypes, /proc/mounts, statvfs, and macOS diskutil).
- Hardware Volume Serial / UUID Support: Directly extracts the hardware Volume Serial Number on Windows, /dev/disk/by-uuid on Linux, and Volume UUID on macOS.
- Lightweight & Portable: Ideal for embedded systems, minimalist Docker containers, and portable Python runtimes without requiring a C compiler.
- Strong Typing & Dataclasses: Clean and modern auto-calculated properties (total_gb, free_gb, used_gb, percent_used).

## Installation

pip install pydiskinfo

## Quick Start

### 1. List All Mounted Disks and Partitions

import pydiskinfo

disks = pydiskinfo.get_disks()

for disk in disks:
    print(f"Mount Point:  {disk.mount}")
    print(f"Volume UUID:  {disk.uuid}")
    print(f"Filesystem:   {disk.filesystem}")
    print(f"Total Space:  {disk.total_gb} GB")
    print(f"Free Space:   {disk.free_gb} GB")
    print(f"Used Space:   {disk.used_gb} GB ({disk.percent_used}% used)")
    print("-" * 40)

### 2. Find Which Disk Contains a Specific Path

import pydiskinfo

disk = pydiskinfo.get_disk_by_path("/var/log/syslog")
if disk:
    print(f"Located on drive: {disk.mount} (UUID: {disk.uuid})")

### 3. Calculate Directory Size & File Count

import pydiskinfo

info = pydiskinfo.get_directory_size("./my_project")
print(f"Total Size: {info['size_bytes']} bytes")
print(f"Total Items: {len(info['items'])}")

## Platform Implementation Details

| Operating System | Mechanism | Native Dependency |
| :--- | :--- | :--- |
| Windows | Win32 API (GetVolumeInformationW, GetDiskFreeSpaceExW) via ctypes | None (kernel32.dll) |
| Linux | /proc/mounts, /dev/disk/by-uuid/, os.statvfs | None (Standard VFS) |
| macOS | diskutil plist output, os.statvfs | None (Darwin OS tools) |

## License

This project is licensed under the MIT License.