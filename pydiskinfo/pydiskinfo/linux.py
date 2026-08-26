import os
from .models import DiskInfo

def _get_linux_uuid(device: str) -> str:
    try:
        base = os.path.basename(device)
        for entry in os.scandir('/dev/disk/by-uuid/'):
            target = os.readlink(entry.path)
            if target == device or target == base or target == os.path.join('..', '..', device):
                return entry.name
    except (FileNotFoundError, OSError):
        pass
    return ""

def get_disks_linux() -> list[DiskInfo]:
    mounts = []
    try:
        with open('/proc/mounts', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.split()
                if len(parts) < 6:
                    continue
                device, mountpoint, fstype = parts[0], parts[1], parts[2]

                if any(x in mountpoint for x in ['/dev', '/proc', '/sys', '/run', '/snap', '/var/lib/docker']):
                    continue
                if not device.startswith('/dev/'):
                    continue
                if device.startswith('/dev/loop'):
                    continue

                uuid = _get_linux_uuid(device)

                try:
                    stat = os.statvfs(mountpoint)
                    total_bytes = stat.f_blocks * stat.f_frsize
                    free_bytes = stat.f_bavail * stat.f_frsize
                except OSError:
                    total_bytes, free_bytes = 0, 0

                mounts.append(DiskInfo(
                    mount=mountpoint,
                    uuid=uuid,
                    filesystem=fstype,
                    total_bytes=total_bytes,
                    free_bytes=free_bytes
                ))
    except FileNotFoundError:
        pass
    return mounts