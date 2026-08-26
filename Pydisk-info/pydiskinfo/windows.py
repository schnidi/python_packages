import os
import ctypes
from ctypes import wintypes
from .models import DiskInfo

def get_disks_windows() -> list[DiskInfo]:
    kernel32 = ctypes.windll.kernel32
    drives = []
    bitmask = kernel32.GetLogicalDrives()

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if bitmask & 1:
            drive = f"{letter}:\\"

            serial = wintypes.DWORD()
            fs_name = ctypes.create_unicode_buffer(256)
            vol_name = ctypes.create_unicode_buffer(256)
            
            success = kernel32.GetVolumeInformationW(
                drive, vol_name, 256, ctypes.byref(serial), None, None,
                fs_name, 256
            )
            
            if success:
                uuid = f"{serial.value:08X}" if serial.value else ""
                fs_type = fs_name.value

                free_avail = ctypes.c_ulonglong(0)
                total_bytes = ctypes.c_ulonglong(0)
                free_total = ctypes.c_ulonglong(0)
                
                kernel32.GetDiskFreeSpaceExW(
                    drive,
                    ctypes.byref(free_avail),
                    ctypes.byref(total_bytes),
                    ctypes.byref(free_total)
                )

                drives.append(DiskInfo(
                    mount=f"{letter}:",
                    uuid=uuid,
                    filesystem=fs_type,
                    total_bytes=total_bytes.value,
                    free_bytes=free_avail.value
                ))
        bitmask >>= 1
    return drives