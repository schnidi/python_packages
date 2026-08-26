from dataclasses import dataclass

@dataclass
class DiskInfo:
    mount: str
    uuid: str
    filesystem: str
    total_bytes: int
    free_bytes: int

    @property
    def used_bytes(self) -> int:
        return max(0, self.total_bytes - self.free_bytes)

    @property
    def total_gb(self) -> float:
        return round(self.total_bytes / (1024 ** 3), 2)

    @property
    def free_gb(self) -> float:
        return round(self.free_bytes / (1024 ** 3), 2)

    @property
    def used_gb(self) -> float:
        return round(self.used_bytes / (1024 ** 3), 2)

    @property
    def percent_used(self) -> float:
        if self.total_bytes == 0:
            return 0.0
        return round((self.used_bytes / self.total_bytes) * 100, 1)

    def __repr__(self) -> str:
        return (f"<DiskInfo mount='{self.mount}' uuid='{self.uuid}' "
                f"fs='{self.filesystem}' free='{self.free_gb} GB' total='{self.total_gb} GB'>")