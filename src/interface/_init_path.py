import sys
from pathlib import Path

path = str(Path(__file__).parent.parent.parent)
if len(sys.path) == 0 or sys.path[-1] != path:
    sys.path.append(path)
