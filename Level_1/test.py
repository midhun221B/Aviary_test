#Example:1

from pathlib import Path
import aviary.api as av # pyright: ignore[reportMissingImports]

base = Path(r'D:\Archived_150126\GIT\Aviary_test\Test_1')

prob = av.run_aviary(
    aircraft_data=str(base / 'advanced_single_aisle_FLOPS.csv'),
    phase_info=str(base / 'phase_info'),
)