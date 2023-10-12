from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *

class gce_ErrorType(IntEnum):
    gce_Done: int = ...
    gce_ConfusedPoints: int = ...
    gce_NegativeRadius: int = ...
    gce_ColinearPoints: int = ...
    gce_IntersectionError: int = ...
    gce_NullAxis: int = ...
    gce_NullAngle: int = ...
    gce_NullRadius: int = ...
    gce_InvertAxis: int = ...
    gce_BadAngle: int = ...
    gce_InvertRadius: int = ...
    gce_NullFocusLength: int = ...
    gce_NullVector: int = ...
    gce_BadEquation: int = ...

gce_Done = gce_ErrorType.gce_Done
gce_ConfusedPoints = gce_ErrorType.gce_ConfusedPoints
gce_NegativeRadius = gce_ErrorType.gce_NegativeRadius
gce_ColinearPoints = gce_ErrorType.gce_ColinearPoints
gce_IntersectionError = gce_ErrorType.gce_IntersectionError
gce_NullAxis = gce_ErrorType.gce_NullAxis
gce_NullAngle = gce_ErrorType.gce_NullAngle
gce_NullRadius = gce_ErrorType.gce_NullRadius
gce_InvertAxis = gce_ErrorType.gce_InvertAxis
gce_BadAngle = gce_ErrorType.gce_BadAngle
gce_InvertRadius = gce_ErrorType.gce_InvertRadius
gce_NullFocusLength = gce_ErrorType.gce_NullFocusLength
gce_NullVector = gce_ErrorType.gce_NullVector
gce_BadEquation = gce_ErrorType.gce_BadEquation

class gce_MakeMirror:
    @overload
    def __init__(self, Point: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax1) -> None: ...
    @overload
    def __init__(self, Line: gp_Lin) -> None: ...
    @overload
    def __init__(self, Point: gp_Pnt, Direc: gp_Dir) -> None: ...
    @overload
    def __init__(self, Plane: gp_Pln) -> None: ...
    @overload
    def __init__(self, Plane: gp_Ax2) -> None: ...
    def Operator(self) -> gp_Trsf: ...
    def Value(self) -> gp_Trsf: ...

class gce_MakeMirror2d:
    @overload
    def __init__(self, Point: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax2d) -> None: ...
    @overload
    def __init__(self, Line: gp_Lin2d) -> None: ...
    @overload
    def __init__(self, Point: gp_Pnt2d, Direc: gp_Dir2d) -> None: ...
    def Operator(self) -> gp_Trsf2d: ...
    def Value(self) -> gp_Trsf2d: ...

class gce_MakeRotation:
    @overload
    def __init__(self, Line: gp_Lin, Angle: float) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax1, Angle: float) -> None: ...
    @overload
    def __init__(self, Point: gp_Pnt, Direc: gp_Dir, Angle: float) -> None: ...
    def Operator(self) -> gp_Trsf: ...
    def Value(self) -> gp_Trsf: ...

class gce_MakeRotation2d:
    @overload
    def __init__(self, Point: gp_Pnt2d, Angle: float) -> None: ...
    def Operator(self) -> gp_Trsf2d: ...
    def Value(self) -> gp_Trsf2d: ...

class gce_MakeScale:
    @overload
    def __init__(self, Point: gp_Pnt, Scale: float) -> None: ...
    def Operator(self) -> gp_Trsf: ...
    def Value(self) -> gp_Trsf: ...

class gce_MakeScale2d:
    @overload
    def __init__(self, Point: gp_Pnt2d, Scale: float) -> None: ...
    def Operator(self) -> gp_Trsf2d: ...
    def Value(self) -> gp_Trsf2d: ...

class gce_MakeTranslation:
    @overload
    def __init__(self, Vect: gp_Vec) -> None: ...
    @overload
    def __init__(self, Point1: gp_Pnt, Point2: gp_Pnt) -> None: ...
    def Operator(self) -> gp_Trsf: ...
    def Value(self) -> gp_Trsf: ...

class gce_MakeTranslation2d:
    @overload
    def __init__(self, Vect: gp_Vec2d) -> None: ...
    @overload
    def __init__(self, Point1: gp_Pnt2d, Point2: gp_Pnt2d) -> None: ...
    def Operator(self) -> gp_Trsf2d: ...
    def Value(self) -> gp_Trsf2d: ...

class gce_Root:
    def IsDone(self) -> bool: ...
    def Status(self) -> gce_ErrorType: ...

class gce_MakeCirc(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2, Radius: float) -> None: ...
    @overload
    def __init__(self, Circ: gp_Circ, Dist: float) -> None: ...
    @overload
    def __init__(self, Circ: gp_Circ, Point: gp_Pnt) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, Norm: gp_Dir, Radius: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, Plane: gp_Pln, Radius: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, Ptaxis: gp_Pnt, Radius: float) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax1, Radius: float) -> None: ...
    def Operator(self) -> gp_Circ: ...
    def Value(self) -> gp_Circ: ...

class gce_MakeCirc2d(gce_Root):
    @overload
    def __init__(
        self, XAxis: gp_Ax2d, Radius: float, Sense: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax22d, Radius: float) -> None: ...
    @overload
    def __init__(self, Circ: gp_Circ2d, Dist: float) -> None: ...
    @overload
    def __init__(self, Circ: gp_Circ2d, Point: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt2d, P2: gp_Pnt2d, P3: gp_Pnt2d) -> None: ...
    @overload
    def __init__(
        self, Center: gp_Pnt2d, Radius: float, Sense: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, Center: gp_Pnt2d, Point: gp_Pnt2d, Sense: Optional[bool] = True
    ) -> None: ...
    def Operator(self) -> gp_Circ2d: ...
    def Value(self) -> gp_Circ2d: ...

class gce_MakeCone(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2, Ang: float, Radius: float) -> None: ...
    @overload
    def __init__(self, Cone: gp_Cone, Point: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Cone: gp_Cone, Dist: float) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, P4: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax1, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Axis: gp_Lin, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, R1: float, R2: float) -> None: ...
    def Operator(self) -> gp_Cone: ...
    def Value(self) -> gp_Cone: ...

class gce_MakeCylinder(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2, Radius: float) -> None: ...
    @overload
    def __init__(self, Cyl: gp_Cylinder, Point: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Cyl: gp_Cylinder, Dist: float) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax1, Radius: float) -> None: ...
    @overload
    def __init__(self, Circ: gp_Circ) -> None: ...
    def Operator(self) -> gp_Cylinder: ...
    def Value(self) -> gp_Cylinder: ...

class gce_MakeDir(gce_Root):
    @overload
    def __init__(self, V: gp_Vec) -> None: ...
    @overload
    def __init__(self, Coord: gp_XYZ) -> None: ...
    @overload
    def __init__(self, Xv: float, Yv: float, Zv: float) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    def Operator(self) -> gp_Dir: ...
    def Value(self) -> gp_Dir: ...

class gce_MakeDir2d(gce_Root):
    @overload
    def __init__(self, V: gp_Vec2d) -> None: ...
    @overload
    def __init__(self, Coord: gp_XY) -> None: ...
    @overload
    def __init__(self, Xv: float, Yv: float) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    def Operator(self) -> gp_Dir2d: ...
    def Value(self) -> gp_Dir2d: ...

class gce_MakeElips(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2, MajorRadius: float, MinorRadius: float) -> None: ...
    @overload
    def __init__(self, S1: gp_Pnt, S2: gp_Pnt, Center: gp_Pnt) -> None: ...
    def Operator(self) -> gp_Elips: ...
    def Value(self) -> gp_Elips: ...

class gce_MakeElips2d(gce_Root):
    @overload
    def __init__(
        self,
        MajorAxis: gp_Ax2d,
        MajorRadius: float,
        MinorRadius: float,
        Sense: Optional[bool] = True,
    ) -> None: ...
    @overload
    def __init__(self, A: gp_Ax22d, MajorRadius: float, MinorRadius: float) -> None: ...
    @overload
    def __init__(self, S1: gp_Pnt2d, S2: gp_Pnt2d, Center: gp_Pnt2d) -> None: ...
    def Operator(self) -> gp_Elips2d: ...
    def Value(self) -> gp_Elips2d: ...

class gce_MakeHypr(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2, MajorRadius: float, MinorRadius: float) -> None: ...
    @overload
    def __init__(self, S1: gp_Pnt, S2: gp_Pnt, Center: gp_Pnt) -> None: ...
    def Operator(self) -> gp_Hypr: ...
    def Value(self) -> gp_Hypr: ...

class gce_MakeHypr2d(gce_Root):
    @overload
    def __init__(self, S1: gp_Pnt2d, S2: gp_Pnt2d, Center: gp_Pnt2d) -> None: ...
    @overload
    def __init__(
        self, MajorAxis: gp_Ax2d, MajorRadius: float, MinorRadius: float, Sense: bool
    ) -> None: ...
    @overload
    def __init__(self, A: gp_Ax22d, MajorRadius: float, MinorRadius: float) -> None: ...
    def Operator(self) -> gp_Hypr2d: ...
    def Value(self) -> gp_Hypr2d: ...

class gce_MakeLin(gce_Root):
    @overload
    def __init__(self, A1: gp_Ax1) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt, V: gp_Dir) -> None: ...
    @overload
    def __init__(self, Lin: gp_Lin, Point: gp_Pnt) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    def Operator(self) -> gp_Lin: ...
    def Value(self) -> gp_Lin: ...

class gce_MakeLin2d(gce_Root):
    @overload
    def __init__(self, A: gp_Ax2d) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt2d, V: gp_Dir2d) -> None: ...
    @overload
    def __init__(self, A: float, B: float, C: float) -> None: ...
    @overload
    def __init__(self, Lin: gp_Lin2d, Dist: float) -> None: ...
    @overload
    def __init__(self, Lin: gp_Lin2d, Point: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    def Operator(self) -> gp_Lin2d: ...
    def Value(self) -> gp_Lin2d: ...

class gce_MakeParab(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2, Focal: float) -> None: ...
    @overload
    def __init__(self, D: gp_Ax1, F: gp_Pnt) -> None: ...
    def Operator(self) -> gp_Parab: ...
    def Value(self) -> gp_Parab: ...

class gce_MakeParab2d(gce_Root):
    @overload
    def __init__(
        self, MirrorAxis: gp_Ax2d, Focal: float, Sense: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(self, A: gp_Ax22d, Focal: float) -> None: ...
    @overload
    def __init__(
        self, D: gp_Ax2d, F: gp_Pnt2d, Sense: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, S1: gp_Pnt2d, Center: gp_Pnt2d, Sense: Optional[bool] = True
    ) -> None: ...
    def Operator(self) -> gp_Parab2d: ...
    def Value(self) -> gp_Parab2d: ...

class gce_MakePln(gce_Root):
    @overload
    def __init__(self, A2: gp_Ax2) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt, V: gp_Dir) -> None: ...
    @overload
    def __init__(self, A: float, B: float, C: float, D: float) -> None: ...
    @overload
    def __init__(self, Pln: gp_Pln, Point: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Pln: gp_Pln, Dist: float) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Axis: gp_Ax1) -> None: ...
    def Operator(self) -> gp_Pln: ...
    def Value(self) -> gp_Pln: ...

# harray1 classes
# harray2 classes
# hsequence classes
