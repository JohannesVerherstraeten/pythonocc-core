from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.Geom2d import *
from OCC.Core.Extrema import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.Approx import *

class geomapi:
    @staticmethod
    def To2d(C: Geom_Curve, P: gp_Pln) -> Geom2d_Curve: ...
    @staticmethod
    def To3d(C: Geom2d_Curve, P: gp_Pln) -> Geom_Curve: ...

class GeomAPI_ExtremaCurveCurve:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C1: Geom_Curve, C2: Geom_Curve) -> None: ...
    @overload
    def __init__(
        self,
        C1: Geom_Curve,
        C2: Geom_Curve,
        U1min: float,
        U1max: float,
        U2min: float,
        U2max: float,
    ) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtCC: ...
    @overload
    def Init(self, C1: Geom_Curve, C2: Geom_Curve) -> None: ...
    @overload
    def Init(
        self,
        C1: Geom_Curve,
        C2: Geom_Curve,
        U1min: float,
        U1max: float,
        U2min: float,
        U2max: float,
    ) -> None: ...
    def IsParallel(self) -> bool: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameters(self) -> Tuple[float, float]: ...
    def NbExtrema(self) -> int: ...
    def NearestPoints(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    def Parameters(self, Index: int) -> Tuple[float, float]: ...
    def Points(self, Index: int, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    def TotalLowerDistance(self) -> float: ...
    def TotalLowerDistanceParameters(self) -> Tuple[bool, float, float]: ...
    def TotalNearestPoints(self, P1: gp_Pnt, P2: gp_Pnt) -> bool: ...

class GeomAPI_ExtremaCurveSurface:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Curve: Geom_Curve, Surface: Geom_Surface) -> None: ...
    @overload
    def __init__(
        self,
        Curve: Geom_Curve,
        Surface: Geom_Surface,
        Wmin: float,
        Wmax: float,
        Umin: float,
        Umax: float,
        Vmin: float,
        Vmax: float,
    ) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtCS: ...
    @overload
    def Init(self, Curve: Geom_Curve, Surface: Geom_Surface) -> None: ...
    @overload
    def Init(
        self,
        Curve: Geom_Curve,
        Surface: Geom_Surface,
        Wmin: float,
        Wmax: float,
        Umin: float,
        Umax: float,
        Vmin: float,
        Vmax: float,
    ) -> None: ...
    def IsParallel(self) -> bool: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameters(self) -> Tuple[float, float, float]: ...
    def NbExtrema(self) -> int: ...
    def NearestPoints(self, PC: gp_Pnt, PS: gp_Pnt) -> None: ...
    def Parameters(self, Index: int) -> Tuple[float, float, float]: ...
    def Points(self, Index: int, P1: gp_Pnt, P2: gp_Pnt) -> None: ...

class GeomAPI_ExtremaSurfaceSurface:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S1: Geom_Surface, S2: Geom_Surface) -> None: ...
    @overload
    def __init__(
        self,
        S1: Geom_Surface,
        S2: Geom_Surface,
        U1min: float,
        U1max: float,
        V1min: float,
        V1max: float,
        U2min: float,
        U2max: float,
        V2min: float,
        V2max: float,
    ) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtSS: ...
    @overload
    def Init(self, S1: Geom_Surface, S2: Geom_Surface) -> None: ...
    @overload
    def Init(
        self,
        S1: Geom_Surface,
        S2: Geom_Surface,
        U1min: float,
        U1max: float,
        V1min: float,
        V1max: float,
        U2min: float,
        U2max: float,
        V2min: float,
        V2max: float,
    ) -> None: ...
    def IsParallel(self) -> bool: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameters(self) -> Tuple[float, float, float, float]: ...
    def NbExtrema(self) -> int: ...
    def NearestPoints(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    def Parameters(self, Index: int) -> Tuple[float, float, float, float]: ...
    def Points(self, Index: int, P1: gp_Pnt, P2: gp_Pnt) -> None: ...

class GeomAPI_IntCS:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Geom_Curve, S: Geom_Surface) -> None: ...
    def IsDone(self) -> bool: ...
    def NbPoints(self) -> int: ...
    def NbSegments(self) -> int: ...
    @overload
    def Parameters(self, Index: int) -> Tuple[float, float, float]: ...
    @overload
    def Parameters(self, Index: int) -> Tuple[float, float, float, float]: ...
    def Perform(self, C: Geom_Curve, S: Geom_Surface) -> None: ...
    def Point(self, Index: int) -> gp_Pnt: ...
    def Segment(self, Index: int) -> Geom_Curve: ...

class GeomAPI_IntSS:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S1: Geom_Surface, S2: Geom_Surface, Tol: float) -> None: ...
    def IsDone(self) -> bool: ...
    def Line(self, Index: int) -> Geom_Curve: ...
    def NbLines(self) -> int: ...
    def Perform(self, S1: Geom_Surface, S2: Geom_Surface, Tol: float) -> None: ...

class GeomAPI_Interpolate:
    @overload
    def __init__(
        self, Points: TColgp_HArray1OfPnt, PeriodicFlag: bool, Tolerance: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_HArray1OfPnt,
        Parameters: TColStd_HArray1OfReal,
        PeriodicFlag: bool,
        Tolerance: float,
    ) -> None: ...
    def Curve(self) -> Geom_BSplineCurve: ...
    def IsDone(self) -> bool: ...
    @overload
    def Load(
        self, InitialTangent: gp_Vec, FinalTangent: gp_Vec, Scale: Optional[bool] = True
    ) -> None: ...
    @overload
    def Load(
        self,
        Tangents: TColgp_Array1OfVec,
        TangentFlags: TColStd_HArray1OfBoolean,
        Scale: Optional[bool] = True,
    ) -> None: ...
    def Perform(self) -> None: ...

class GeomAPI_PointsToBSpline:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array1OfPnt,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array1OfPnt,
        ParType: Approx_ParametrizationType,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array1OfPnt,
        Parameters: TColStd_Array1OfReal,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array1OfPnt,
        Weight1: float,
        Weight2: float,
        Weight3: float,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    def Curve(self) -> Geom_BSplineCurve: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array1OfPnt,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array1OfPnt,
        ParType: Approx_ParametrizationType,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array1OfPnt,
        Parameters: TColStd_Array1OfReal,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array1OfPnt,
        Weight1: float,
        Weight2: float,
        Weight3: float,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    def IsDone(self) -> bool: ...

class GeomAPI_PointsToBSplineSurface:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array2OfPnt,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array2OfPnt,
        ParType: Approx_ParametrizationType,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Points: TColgp_Array2OfPnt,
        Weight1: float,
        Weight2: float,
        Weight3: float,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def __init__(
        self,
        ZPoints: TColStd_Array2OfReal,
        X0: float,
        dX: float,
        Y0: float,
        dY: float,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array2OfPnt,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Init(
        self,
        ZPoints: TColStd_Array2OfReal,
        X0: float,
        dX: float,
        Y0: float,
        dY: float,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array2OfPnt,
        ParType: Approx_ParametrizationType,
        DegMin: Optional[int] = 3,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
        thePeriodic: Optional[bool] = False,
    ) -> None: ...
    @overload
    def Init(
        self,
        Points: TColgp_Array2OfPnt,
        Weight1: float,
        Weight2: float,
        Weight3: float,
        DegMax: Optional[int] = 8,
        Continuity: Optional[GeomAbs_Shape] = GeomAbs_C2,
        Tol3D: Optional[float] = 1.0e-3,
    ) -> None: ...
    @overload
    def Interpolate(
        self, Points: TColgp_Array2OfPnt, thePeriodic: Optional[bool] = False
    ) -> None: ...
    @overload
    def Interpolate(
        self,
        Points: TColgp_Array2OfPnt,
        ParType: Approx_ParametrizationType,
        thePeriodic: Optional[bool] = False,
    ) -> None: ...
    @overload
    def Interpolate(
        self, ZPoints: TColStd_Array2OfReal, X0: float, dX: float, Y0: float, dY: float
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def Surface(self) -> Geom_BSplineSurface: ...

class GeomAPI_ProjectPointOnCurve:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P: gp_Pnt, Curve: Geom_Curve) -> None: ...
    @overload
    def __init__(
        self, P: gp_Pnt, Curve: Geom_Curve, Umin: float, Usup: float
    ) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtPC: ...
    @overload
    def Init(self, P: gp_Pnt, Curve: Geom_Curve) -> None: ...
    @overload
    def Init(self, P: gp_Pnt, Curve: Geom_Curve, Umin: float, Usup: float) -> None: ...
    @overload
    def Init(self, Curve: Geom_Curve, Umin: float, Usup: float) -> None: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameter(self) -> float: ...
    def NbPoints(self) -> int: ...
    def NearestPoint(self) -> gp_Pnt: ...
    @overload
    def Parameter(self, Index: int) -> float: ...
    @overload
    def Parameter(self, Index: int) -> float: ...
    def Perform(self, P: gp_Pnt) -> None: ...
    def Point(self, Index: int) -> gp_Pnt: ...

class GeomAPI_ProjectPointOnSurf:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def __init__(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Tolerance: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def __init__(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Umin: float,
        Usup: float,
        Vmin: float,
        Vsup: float,
        Tolerance: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def __init__(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Umin: float,
        Usup: float,
        Vmin: float,
        Vsup: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    def Distance(self, Index: int) -> float: ...
    def Extrema(self) -> Extrema_ExtPS: ...
    @overload
    def Init(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Tolerance: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def Init(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def Init(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Umin: float,
        Usup: float,
        Vmin: float,
        Vsup: float,
        Tolerance: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def Init(
        self,
        P: gp_Pnt,
        Surface: Geom_Surface,
        Umin: float,
        Usup: float,
        Vmin: float,
        Vsup: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def Init(
        self,
        Surface: Geom_Surface,
        Umin: float,
        Usup: float,
        Vmin: float,
        Vsup: float,
        Tolerance: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    @overload
    def Init(
        self,
        Surface: Geom_Surface,
        Umin: float,
        Usup: float,
        Vmin: float,
        Vsup: float,
        Algo: Optional[Extrema_ExtAlgo] = Extrema_ExtAlgo_Grad,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def LowerDistance(self) -> float: ...
    def LowerDistanceParameters(self) -> Tuple[float, float]: ...
    def NbPoints(self) -> int: ...
    def NearestPoint(self) -> gp_Pnt: ...
    def Parameters(self, Index: int) -> Tuple[float, float]: ...
    def Perform(self, P: gp_Pnt) -> None: ...
    def Point(self, Index: int) -> gp_Pnt: ...
    def SetExtremaAlgo(self, theAlgo: Extrema_ExtAlgo) -> None: ...
    def SetExtremaFlag(self, theExtFlag: Extrema_ExtFlag) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
