from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor2d import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *

class geom2dadaptor:
    @staticmethod
    def MakeCurve(HC: Adaptor2d_Curve2d) -> Geom2d_Curve: ...

class Geom2dAdaptor_Curve(Adaptor2d_Curve2d):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Geom2d_Curve) -> None: ...
    @overload
    def __init__(self, C: Geom2d_Curve, UFirst: float, ULast: float) -> None: ...
    def BSpline(self) -> Geom2d_BSplineCurve: ...
    def Bezier(self) -> Geom2d_BezierCurve: ...
    def Circle(self) -> gp_Circ2d: ...
    def Continuity(self) -> GeomAbs_Shape: ...
    def Curve(self) -> Geom2d_Curve: ...
    def D0(self, U: float, P: gp_Pnt2d) -> None: ...
    def D1(self, U: float, P: gp_Pnt2d, V: gp_Vec2d) -> None: ...
    def D2(self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d) -> None: ...
    def D3(
        self, U: float, P: gp_Pnt2d, V1: gp_Vec2d, V2: gp_Vec2d, V3: gp_Vec2d
    ) -> None: ...
    def DN(self, U: float, N: int) -> gp_Vec2d: ...
    def Degree(self) -> int: ...
    def Ellipse(self) -> gp_Elips2d: ...
    def FirstParameter(self) -> float: ...
    def GetType(self) -> GeomAbs_CurveType: ...
    def Hyperbola(self) -> gp_Hypr2d: ...
    def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
    def IsClosed(self) -> bool: ...
    def IsPeriodic(self) -> bool: ...
    def IsRational(self) -> bool: ...
    def LastParameter(self) -> float: ...
    def Line(self) -> gp_Lin2d: ...
    @overload
    def Load(self, theCurve: Geom2d_Curve) -> None: ...
    @overload
    def Load(
        self, theCurve: Geom2d_Curve, theUFirst: float, theULast: float
    ) -> None: ...
    def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
    def NbKnots(self) -> int: ...
    def NbPoles(self) -> int: ...
    def NbSamples(self) -> int: ...
    def Parabola(self) -> gp_Parab2d: ...
    def Period(self) -> float: ...
    def Reset(self) -> None: ...
    def Resolution(self, Ruv: float) -> float: ...
    def Trim(self, First: float, Last: float, Tol: float) -> Adaptor2d_Curve2d: ...
    def Value(self, U: float) -> gp_Pnt2d: ...

# harray1 classes
# harray2 classes
# hsequence classes
