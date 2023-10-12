from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *

class TopClass_SolidExplorer:
    def CurrentFace(self) -> TopoDS_Face: ...
    def InitFace(self) -> None: ...
    def InitShell(self) -> None: ...
    def MoreFaces(self) -> bool: ...
    def MoreShells(self) -> bool: ...
    def NextFace(self) -> None: ...
    def NextShell(self) -> None: ...
    def OtherSegment(self, P: gp_Pnt, L: gp_Lin) -> float: ...
    def Reject(self, P: gp_Pnt) -> bool: ...
    def RejectFace(self, L: gp_Lin, Par: float) -> bool: ...
    def RejectShell(self, L: gp_Lin, Par: float) -> bool: ...
    def Segment(self, P: gp_Pnt, L: gp_Lin) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes
