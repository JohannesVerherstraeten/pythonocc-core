from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.AppParCurves import *
from OCC.Core.math import *

class AppCont_Function:
    def FirstParameter(self) -> float: ...
    def GetNbOf2dPoints(self) -> int: ...
    def GetNbOf3dPoints(self) -> int: ...
    def GetNumberOfPoints(self) -> Tuple[int, int]: ...
    def LastParameter(self) -> float: ...

class AppCont_LeastSquare:
    def __init__(
        self,
        SSP: AppCont_Function,
        U0: float,
        U1: float,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Deg: int,
        NbPoints: int,
    ) -> None: ...
    def Error(self) -> Tuple[float, float, float]: ...
    def IsDone(self) -> bool: ...
    def Value(self) -> AppParCurves_MultiCurve: ...

# harray1 classes
# harray2 classes
# hsequence classes
