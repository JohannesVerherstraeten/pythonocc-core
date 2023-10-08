from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TColGeom import *
from OCC.Core.TColStd import *
from OCC.Core.Convert import *
from OCC.Core.GeomAbs import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *
from OCC.Core.math import *
from OCC.Core.Geom2d import *

class GeomConvert_ConvType(IntEnum):
    GeomConvert_Target: int = ...
    GeomConvert_Simplest: int = ...
    GeomConvert_MinGap: int = ...

GeomConvert_Target = GeomConvert_ConvType.GeomConvert_Target
GeomConvert_Simplest = GeomConvert_ConvType.GeomConvert_Simplest
GeomConvert_MinGap = GeomConvert_ConvType.GeomConvert_MinGap

class geomconvert:
    @overload
    @staticmethod
    def C0BSplineToArrayOfC1BSplineCurve(
        BS: Geom_BSplineCurve, tabBS: TColGeom_HArray1OfBSplineCurve, tolerance: float
    ) -> None: ...
    @overload
    @staticmethod
    def C0BSplineToArrayOfC1BSplineCurve(
        BS: Geom_BSplineCurve,
        tabBS: TColGeom_HArray1OfBSplineCurve,
        AngularTolerance: float,
        tolerance: float,
    ) -> None: ...
    @staticmethod
    def C0BSplineToC1BSplineCurve(
        BS: Geom_BSplineCurve,
        tolerance: float,
        AngularTolerance: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    @staticmethod
    def ConcatC1(
        ArrayOfCurves: TColGeom_Array1OfBSplineCurve,
        ArrayOfToler: TColStd_Array1OfReal,
        ArrayOfIndices: TColStd_HArray1OfInteger,
        ArrayOfConcatenated: TColGeom_HArray1OfBSplineCurve,
        ClosedTolerance: float,
    ) -> bool: ...
    @overload
    @staticmethod
    def ConcatC1(
        ArrayOfCurves: TColGeom_Array1OfBSplineCurve,
        ArrayOfToler: TColStd_Array1OfReal,
        ArrayOfIndices: TColStd_HArray1OfInteger,
        ArrayOfConcatenated: TColGeom_HArray1OfBSplineCurve,
        ClosedTolerance: float,
        AngularTolerance: float,
    ) -> bool: ...
    @staticmethod
    def ConcatG1(
        ArrayOfCurves: TColGeom_Array1OfBSplineCurve,
        ArrayOfToler: TColStd_Array1OfReal,
        ArrayOfConcatenated: TColGeom_HArray1OfBSplineCurve,
        ClosedTolerance: float,
    ) -> bool: ...
    @staticmethod
    def CurveToBSplineCurve(
        C: Geom_Curve,
        Parameterisation: Optional[
            Convert_ParameterisationType
        ] = Convert_TgtThetaOver2,
    ) -> Geom_BSplineCurve: ...
    @overload
    @staticmethod
    def SplitBSplineCurve(
        C: Geom_BSplineCurve,
        FromK1: int,
        ToK2: int,
        SameOrientation: Optional[bool] = True,
    ) -> Geom_BSplineCurve: ...
    @overload
    @staticmethod
    def SplitBSplineCurve(
        C: Geom_BSplineCurve,
        FromU1: float,
        ToU2: float,
        ParametricTolerance: float,
        SameOrientation: Optional[bool] = True,
    ) -> Geom_BSplineCurve: ...
    @overload
    @staticmethod
    def SplitBSplineSurface(
        S: Geom_BSplineSurface,
        FromUK1: int,
        ToUK2: int,
        FromVK1: int,
        ToVK2: int,
        SameUOrientation: Optional[bool] = True,
        SameVOrientation: Optional[bool] = True,
    ) -> Geom_BSplineSurface: ...
    @overload
    @staticmethod
    def SplitBSplineSurface(
        S: Geom_BSplineSurface,
        FromK1: int,
        ToK2: int,
        USplit: bool,
        SameOrientation: Optional[bool] = True,
    ) -> Geom_BSplineSurface: ...
    @overload
    @staticmethod
    def SplitBSplineSurface(
        S: Geom_BSplineSurface,
        FromU1: float,
        ToU2: float,
        FromV1: float,
        ToV2: float,
        ParametricTolerance: float,
        SameUOrientation: Optional[bool] = True,
        SameVOrientation: Optional[bool] = True,
    ) -> Geom_BSplineSurface: ...
    @overload
    @staticmethod
    def SplitBSplineSurface(
        S: Geom_BSplineSurface,
        FromParam1: float,
        ToParam2: float,
        USplit: bool,
        ParametricTolerance: float,
        SameOrientation: Optional[bool] = True,
    ) -> Geom_BSplineSurface: ...
    @staticmethod
    def SurfaceToBSplineSurface(S: Geom_Surface) -> Geom_BSplineSurface: ...

class GeomConvert_ApproxCurve:
    @overload
    def __init__(
        self,
        Curve: Geom_Curve,
        Tol3d: float,
        Order: GeomAbs_Shape,
        MaxSegments: int,
        MaxDegree: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Curve: Adaptor3d_Curve,
        Tol3d: float,
        Order: GeomAbs_Shape,
        MaxSegments: int,
        MaxDegree: int,
    ) -> None: ...
    def Curve(self) -> Geom_BSplineCurve: ...
    def HasResult(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def MaxError(self) -> float: ...

class GeomConvert_ApproxSurface:
    @overload
    def __init__(
        self,
        Surf: Geom_Surface,
        Tol3d: float,
        UContinuity: GeomAbs_Shape,
        VContinuity: GeomAbs_Shape,
        MaxDegU: int,
        MaxDegV: int,
        MaxSegments: int,
        PrecisCode: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Surf: Adaptor3d_Surface,
        Tol3d: float,
        UContinuity: GeomAbs_Shape,
        VContinuity: GeomAbs_Shape,
        MaxDegU: int,
        MaxDegV: int,
        MaxSegments: int,
        PrecisCode: int,
    ) -> None: ...
    def HasResult(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def MaxError(self) -> float: ...
    def Surface(self) -> Geom_BSplineSurface: ...

class GeomConvert_BSplineCurveKnotSplitting:
    def __init__(self, BasisCurve: Geom_BSplineCurve, ContinuityRange: int) -> None: ...
    def NbSplits(self) -> int: ...
    def SplitValue(self, Index: int) -> int: ...
    def Splitting(self, SplitValues: TColStd_Array1OfInteger) -> None: ...

class GeomConvert_BSplineCurveToBezierCurve:
    @overload
    def __init__(self, BasisCurve: Geom_BSplineCurve) -> None: ...
    @overload
    def __init__(
        self,
        BasisCurve: Geom_BSplineCurve,
        U1: float,
        U2: float,
        ParametricTolerance: float,
    ) -> None: ...
    def Arc(self, Index: int) -> Geom_BezierCurve: ...
    def Arcs(self, Curves: TColGeom_Array1OfBezierCurve) -> None: ...
    def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
    def NbArcs(self) -> int: ...

class GeomConvert_BSplineSurfaceKnotSplitting:
    def __init__(
        self,
        BasisSurface: Geom_BSplineSurface,
        UContinuityRange: int,
        VContinuityRange: int,
    ) -> None: ...
    def NbUSplits(self) -> int: ...
    def NbVSplits(self) -> int: ...
    def Splitting(
        self, USplit: TColStd_Array1OfInteger, VSplit: TColStd_Array1OfInteger
    ) -> None: ...
    def USplitValue(self, UIndex: int) -> int: ...
    def VSplitValue(self, VIndex: int) -> int: ...

class GeomConvert_BSplineSurfaceToBezierSurface:
    @overload
    def __init__(self, BasisSurface: Geom_BSplineSurface) -> None: ...
    @overload
    def __init__(
        self,
        BasisSurface: Geom_BSplineSurface,
        U1: float,
        U2: float,
        V1: float,
        V2: float,
        ParametricTolerance: float,
    ) -> None: ...
    def NbUPatches(self) -> int: ...
    def NbVPatches(self) -> int: ...
    def Patch(self, UIndex: int, VIndex: int) -> Geom_BezierSurface: ...
    def Patches(self, Surfaces: TColGeom_Array2OfBezierSurface) -> None: ...
    def UKnots(self, TKnots: TColStd_Array1OfReal) -> None: ...
    def VKnots(self, TKnots: TColStd_Array1OfReal) -> None: ...

class GeomConvert_CompBezierSurfacesToBSplineSurface:
    @overload
    def __init__(self, Beziers: TColGeom_Array2OfBezierSurface) -> None: ...
    @overload
    def __init__(
        self,
        Beziers: TColGeom_Array2OfBezierSurface,
        Tolerance: float,
        RemoveKnots: Optional[bool] = True,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Beziers: TColGeom_Array2OfBezierSurface,
        UKnots: TColStd_Array1OfReal,
        VKnots: TColStd_Array1OfReal,
        UContinuity: Optional[GeomAbs_Shape] = GeomAbs_C0,
        VContinuity: Optional[GeomAbs_Shape] = GeomAbs_C0,
        Tolerance: Optional[float] = 1.0e-4,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbUKnots(self) -> int: ...
    def NbUPoles(self) -> int: ...
    def NbVKnots(self) -> int: ...
    def NbVPoles(self) -> int: ...
    def Poles(self) -> TColgp_HArray2OfPnt: ...
    def UDegree(self) -> int: ...
    def UKnots(self) -> TColStd_HArray1OfReal: ...
    def UMultiplicities(self) -> TColStd_HArray1OfInteger: ...
    def VDegree(self) -> int: ...
    def VKnots(self) -> TColStd_HArray1OfReal: ...
    def VMultiplicities(self) -> TColStd_HArray1OfInteger: ...

class GeomConvert_CompCurveToBSplineCurve:
    @overload
    def __init__(
        self,
        Parameterisation: Optional[
            Convert_ParameterisationType
        ] = Convert_TgtThetaOver2,
    ) -> None: ...
    @overload
    def __init__(
        self,
        BasisCurve: Geom_BoundedCurve,
        Parameterisation: Optional[
            Convert_ParameterisationType
        ] = Convert_TgtThetaOver2,
    ) -> None: ...
    def Add(
        self,
        NewCurve: Geom_BoundedCurve,
        Tolerance: float,
        After: Optional[bool] = False,
        WithRatio: Optional[bool] = True,
        MinM: Optional[int] = 0,
    ) -> bool: ...
    def BSplineCurve(self) -> Geom_BSplineCurve: ...

class GeomConvert_CurveToAnaCurve:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, C: Geom_Curve) -> None: ...
    @staticmethod
    def ComputeCircle(
        curve: Geom_Curve, tolerance: float, c1: float, c2: float
    ) -> Tuple[Geom_Curve, float, float, float]: ...
    @staticmethod
    def ComputeCurve(
        curve: Geom_Curve,
        tolerance: float,
        c1: float,
        c2: float,
        theCurvType: Optional[GeomConvert_ConvType] = GeomConvert_MinGap,
        theTarget: Optional[GeomAbs_CurveType] = GeomAbs_Line,
    ) -> Tuple[Geom_Curve, float, float, float]: ...
    @staticmethod
    def ComputeEllipse(
        curve: Geom_Curve, tolerance: float, c1: float, c2: float
    ) -> Tuple[Geom_Curve, float, float, float]: ...
    @staticmethod
    def ComputeLine(
        curve: Geom_Curve, tolerance: float, c1: float, c2: float
    ) -> Tuple[Geom_Line, float, float, float]: ...
    def ConvertToAnalytical(
        self, theTol: float, theResultCurve: Geom_Curve, F: float, L: float
    ) -> Tuple[bool, float, float]: ...
    def Gap(self) -> float: ...
    @staticmethod
    def GetCircle(Circ: gp_Circ, P0: gp_Pnt, P1: gp_Pnt, P2: gp_Pnt) -> bool: ...
    def GetConvType(self) -> GeomConvert_ConvType: ...
    @staticmethod
    def GetLine(P1: gp_Pnt, P2: gp_Pnt) -> Tuple[gp_Lin, float, float]: ...
    def GetTarget(self) -> GeomAbs_CurveType: ...
    def Init(self, C: Geom_Curve) -> None: ...
    @staticmethod
    def IsLinear(
        aPoints: TColgp_Array1OfPnt, tolerance: float
    ) -> Tuple[bool, float]: ...
    def SetConvType(self, theConvType: GeomConvert_ConvType) -> None: ...
    def SetTarget(self, theTarget: GeomAbs_CurveType) -> None: ...

class GeomConvert_FuncConeLSDist(math_MultipleVarFunction):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePoints: TColgp_HArray1OfXYZ, theDir: gp_Dir) -> None: ...
    def NbVariables(self) -> int: ...
    def SetDir(self, theDir: gp_Dir) -> None: ...
    def SetPoints(self, thePoints: TColgp_HArray1OfXYZ) -> None: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...

class GeomConvert_FuncCylinderLSDist(math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePoints: TColgp_HArray1OfXYZ, theDir: gp_Dir) -> None: ...
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def NbVariables(self) -> int: ...
    def SetDir(self, theDir: gp_Dir) -> None: ...
    def SetPoints(self, thePoints: TColgp_HArray1OfXYZ) -> None: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class GeomConvert_FuncSphereLSDist(math_MultipleVarFunctionWithGradient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePoints: TColgp_HArray1OfXYZ) -> None: ...
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def NbVariables(self) -> int: ...
    def SetPoints(self, thePoints: TColgp_HArray1OfXYZ) -> None: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class GeomConvert_SurfToAnaSurf:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface) -> None: ...
    @overload
    def ConvertToAnalytical(self, InitialToler: float) -> Geom_Surface: ...
    @overload
    def ConvertToAnalytical(
        self, InitialToler: float, Umin: float, Umax: float, Vmin: float, Vmax: float
    ) -> Geom_Surface: ...
    def Gap(self) -> float: ...
    def Init(self, S: Geom_Surface) -> None: ...
    @staticmethod
    def IsCanonical(S: Geom_Surface) -> bool: ...
    @staticmethod
    def IsSame(S1: Geom_Surface, S2: Geom_Surface, tol: float) -> bool: ...
    def SetConvType(
        self, theConvType: Optional[GeomConvert_ConvType] = GeomConvert_Simplest
    ) -> None: ...
    def SetTarget(
        self, theSurfType: Optional[GeomAbs_SurfaceType] = GeomAbs_Plane
    ) -> None: ...

class GeomConvert_Units:
    @staticmethod
    def DegreeToRadian(
        theCurve: Geom2d_Curve,
        theSurface: Geom_Surface,
        theLengthFactor: float,
        theFactorRadianDegree: float,
    ) -> Geom2d_Curve: ...
    @staticmethod
    def MirrorPCurve(theCurve: Geom2d_Curve) -> Geom2d_Curve: ...
    @staticmethod
    def RadianToDegree(
        theCurve: Geom2d_Curve,
        theSurface: Geom_Surface,
        theLengthFactor: float,
        theFactorRadianDegree: float,
    ) -> Geom2d_Curve: ...

# harray1 classes
# harray2 classes
# hsequence classes
