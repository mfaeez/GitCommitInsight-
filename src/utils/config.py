
from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class CommitSizeConfig:
    max_files_changed: int = 10
    max_lines_changed: int = 500


@dataclass(frozen=True)
class WorkHoursConfig:
    work_start: time = time(9, 0)
    work_end: time = time(18, 0)


@dataclass(frozen=True)
class AppConfig:
    commit_size: CommitSizeConfig = CommitSizeConfig()
    work_hours: WorkHoursConfig = WorkHoursConfig()
    output_dir: str = "output"


# Global config instance
CONFIG = AppConfig()
