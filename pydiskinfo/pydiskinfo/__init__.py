# pydiskinfo - Lightweight cross-platform disk info library
# Copyright (C) 2026 Your Name (alebo Meno/Viliam Schneider)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even theoretical WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.

import platform
import os
from .models import DiskInfo

__version__ = "1.0.0"

def get_disks() -> list[DiskInfo]:
    """Vráti zoznam všetkých pripojených diskov/partícií pre aktuálny OS."""
    system = platform.system()
    if system == "Windows":
        from .windows import get_disks_windows
        return get_disks_windows()
    elif system == "Linux":
        from .linux import get_disks_linux
        return get_disks_linux()
    elif system == "Darwin":
        from .macos import get_disks_macos
        return get_disks_macos()
    else:
        return []

def get_disk_by_path(path: str) -> DiskInfo | None:
    """Nájde disk, na ktorom sa nachádza zadaná cesta."""
    abs_path = os.path.abspath(path)
    disks = get_disks()
    
    # Zoradíme od najdlhšej cesty po najkratšiu pre presný match
    disks.sort(key=lambda d: len(d.mount), reverse=True)
    
    for disk in disks:
        if abs_path.lower().startswith(disk.mount.lower()):
            return disk
    return None

def get_directory_size(dir_path: str) -> dict:
    """Vráti veľkosť priečinka v bajtoch a zoznam položiek."""
    total_size = 0
    all_items = []
    if not os.path.exists(dir_path):
        return {"size_bytes": 0, "items": []}

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for f in files:
            fp = os.path.join(root, f)
            all_items.append(fp)
            try:
                total_size += os.path.getsize(fp)
            except OSError:
                pass
        for d in dirs:
            all_items.append(os.path.join(root, d))
            
    all_items.append(dir_path)
    return {"size_bytes": total_size, "items": all_items}

import platform
import os
from .models import DiskInfo

__version__ = "1.0.0"

def get_disks() -> list[DiskInfo]:
    """Vráti zoznam všetkých pripojených diskov/partícií pre aktuálny OS."""
    system = platform.system()
    if system == "Windows":
        from .windows import get_disks_windows
        return get_disks_windows()
    elif system == "Linux":
        from .linux import get_disks_linux
        return get_disks_linux()
    elif system == "Darwin":
        from .macos import get_disks_macos
        return get_disks_macos()
    else:
        return []

def get_disk_by_path(path: str) -> DiskInfo | None:
    """Nájde disk, na ktorom sa nachádza zadaná cesta."""
    abs_path = os.path.abspath(path)
    disks = get_disks()
    
    # Zoradíme od najdlhšej cesty po najkratšiu pre presný match
    disks.sort(key=lambda d: len(d.mount), reverse=True)
    
    for disk in disks:
        if abs_path.lower().startswith(disk.mount.lower()):
            return disk
    return None

def get_directory_size(dir_path: str) -> dict:
    """Vráti veľkosť priečinka v bajtoch a zoznam položiek."""
    total_size = 0
    all_items = []
    if not os.path.exists(dir_path):
        return {"size_bytes": 0, "items": []}

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for f in files:
            fp = os.path.join(root, f)
            all_items.append(fp)
            try:
                total_size += os.path.getsize(fp)
            except OSError:
                pass
        for d in dirs:
            all_items.append(os.path.join(root, d))
            
    all_items.append(dir_path)
    return {"size_bytes": total_size, "items": all_items}
