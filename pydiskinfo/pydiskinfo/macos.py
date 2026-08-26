import os
import subprocess
import plistlib
from .models import DiskInfo

def get_disks_macos() -> list[DiskInfo]:
    disks = []
    try:
        # Použijeme štandardný macOS nástroj diskutil s výstupom vo formáte plist (XML)
        res = subprocess.run(["diskutil", "list", "-plist"], capture_output=True, check=True)
        data = plistlib.loads(res.stdout)
        
        all_disks = data.get("AllDisksAndPartitions", [])
        for entry in all_disks:
            partitions = entry.get("Partitions", [entry])
            for part in partitions:
                mount = part.get("MountPoint")
                if not mount:
                    continue
                
                # Získanie podrobných informácií vrátane Volume UUID
                part_id = part.get("DeviceIdentifier")
                uuid = ""
                fs_type = part.get("Content", "Unknown")
                
                if part_id:
                    try:
                        info_res = subprocess.run(["diskutil", "info", "-plist", part_id], capture_output=True)
                        if info_res.returncode == 0:
                            p_info = plistlib.loads(info_res.stdout)
                            uuid = p_info.get("VolumeUUID", "")
                            fs_type = p_info.get("FilesystemType", fs_type)
                    except Exception:
                        pass

                try:
                    stat = os.statvfs(mount)
                    total_bytes = stat.f_blocks * stat.f_frsize
                    free_bytes = stat.f_bavail * stat.f_frsize
                except OSError:
                    total_bytes, free_bytes = 0, 0

                disks.append(DiskInfo(
                    mount=mount,
                    uuid=uuid,
                    filesystem=fs_type,
                    total_bytes=total_bytes,
                    free_bytes=free_bytes
                ))
    except Exception:
        pass
    return disks