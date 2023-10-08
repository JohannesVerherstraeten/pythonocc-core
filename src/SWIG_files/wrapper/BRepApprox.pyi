from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Approx import *
from OCC.Core.math import *
from OCC.Core.AppParCurves import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *
from OCC.Core.IntSurf import *
from OCC.Core.TColStd import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.IntImp import *
from OCC.Core.gp import *
from OCC.Core.ApproxInt import *
from OCC.Core.TColgp import *

class BRepApprox_Approx:
    def __init__(self) -> None: ...
    def IsDone(self) -> bool: ...
    def NbMultiCurves(self) -> int: ...
    @staticmethod
    def Parameters(
        Line: BRepApprox_TheMultiLineOfApprox,
        firstP: int,
        lastP: int,
        Par: Approx_ParametrizationType,
        TheParameters: math_Vector,
    ) -> None: ...
    def SetParameters(
        self,
        Tol3d: float,
        Tol2d: float,
        DegMin: int,
        DegMax: int,
        NbIterMax: int,
        NbPntMax: Optional[int] = 30,
        ApproxWithTangency: Optional[bool] = True,
        Parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
    ) -> None: ...
    def TolReached2d(self) -> float: ...
    def TolReached3d(self) -> float: ...
    def Value(self, Index: int) -> AppParCurves_MultiBSpCurve: ...

class BRepApprox_ApproxLine(Standard_Transient):
    @overload
    def __init__(
        self,
        CurveXYZ: Geom_BSplineCurve,
        CurveUV1: Geom2d_BSplineCurve,
        CurveUV2: Geom2d_BSplineCurve,
    ) -> None: ...
    @overload
    def __init__(
        self, lin: IntSurf_LineOn2S, theTang: Optional[bool] = False
    ) -> None: ...
    def NbPnts(self) -> int: ...
    def Point(self, Index: int) -> IntSurf_PntOn2S: ...

class BRepApprox_BSpGradient_BFGSOfMyBSplGradientOfTheComputeLineOfApprox(math_BFGS):
    def __init__(
        self,
        F: math_MultipleVarFunctionWithGradient,
        StartingPoint: math_Vector,
        Tolerance3d: float,
        Tolerance2d: float,
        Eps: float,
        NbIterations: Optional[int] = 200,
    ) -> None: ...
    def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class BRepApprox_BSpParFunctionOfMyBSplGradientOfTheComputeLineOfApprox(
    math_MultipleVarFunctionWithGradient
):
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        NbPol: int,
    ) -> None: ...
    def CurveValue(self) -> AppParCurves_MultiBSpCurve: ...
    def DerivativeFunctionMatrix(self) -> math_Matrix: ...
    def Error(self, IPoint: int, CurveIndex: int) -> float: ...
    def FirstConstraint(
        self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int
    ) -> AppParCurves_Constraint: ...
    def FunctionMatrix(self) -> math_Matrix: ...
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def Index(self) -> math_IntegerVector: ...
    def LastConstraint(
        self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int
    ) -> AppParCurves_Constraint: ...
    def MaxError2d(self) -> float: ...
    def MaxError3d(self) -> float: ...
    def NbVariables(self) -> int: ...
    def NewParameters(self) -> math_Vector: ...
    def SetFirstLambda(self, l1: float) -> None: ...
    def SetLastLambda(self, l2: float) -> None: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class BRepApprox_BSpParLeastSquareOfMyBSplGradientOfTheComputeLineOfApprox:
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Parameters: math_Vector,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Parameters: math_Vector,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        NbPol: int,
    ) -> None: ...
    def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
    def BezierValue(self) -> AppParCurves_MultiCurve: ...
    def DerivativeFunctionMatrix(self) -> math_Matrix: ...
    def Distance(self) -> math_Matrix: ...
    def Error(self) -> Tuple[float, float, float]: ...
    def ErrorGradient(self, Grad: math_Vector) -> Tuple[float, float, float]: ...
    def FirstLambda(self) -> float: ...
    def FunctionMatrix(self) -> math_Matrix: ...
    def IsDone(self) -> bool: ...
    def KIndex(self) -> math_IntegerVector: ...
    def LastLambda(self) -> float: ...
    @overload
    def Perform(self, Parameters: math_Vector) -> None: ...
    @overload
    def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
    @overload
    def Perform(
        self,
        Parameters: math_Vector,
        V1t: math_Vector,
        V2t: math_Vector,
        l1: float,
        l2: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        Parameters: math_Vector,
        V1t: math_Vector,
        V2t: math_Vector,
        V1c: math_Vector,
        V2c: math_Vector,
        l1: float,
        l2: float,
    ) -> None: ...
    def Points(self) -> math_Matrix: ...
    def Poles(self) -> math_Matrix: ...

class BRepApprox_Gradient_BFGSOfMyGradientOfTheComputeLineBezierOfApprox(math_BFGS):
    def __init__(
        self,
        F: math_MultipleVarFunctionWithGradient,
        StartingPoint: math_Vector,
        Tolerance3d: float,
        Tolerance2d: float,
        Eps: float,
        NbIterations: Optional[int] = 200,
    ) -> None: ...
    def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class BRepApprox_Gradient_BFGSOfMyGradientbisOfTheComputeLineOfApprox(math_BFGS):
    def __init__(
        self,
        F: math_MultipleVarFunctionWithGradient,
        StartingPoint: math_Vector,
        Tolerance3d: float,
        Tolerance2d: float,
        Eps: float,
        NbIterations: Optional[int] = 200,
    ) -> None: ...
    def IsSolutionReached(self, F: math_MultipleVarFunctionWithGradient) -> bool: ...

class BRepApprox_MyBSplGradientOfTheComputeLineOfApprox:
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        Deg: int,
        Tol3d: float,
        Tol2d: float,
        NbIterations: Optional[int] = 1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        Deg: int,
        Tol3d: float,
        Tol2d: float,
        NbIterations: int,
        lambda1: float,
        lambda2: float,
    ) -> None: ...
    def AverageError(self) -> float: ...
    def Error(self, Index: int) -> float: ...
    def IsDone(self) -> bool: ...
    def MaxError2d(self) -> float: ...
    def MaxError3d(self) -> float: ...
    def Value(self) -> AppParCurves_MultiBSpCurve: ...

class BRepApprox_MyGradientOfTheComputeLineBezierOfApprox:
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Deg: int,
        Tol3d: float,
        Tol2d: float,
        NbIterations: Optional[int] = 200,
    ) -> None: ...
    def AverageError(self) -> float: ...
    def Error(self, Index: int) -> float: ...
    def IsDone(self) -> bool: ...
    def MaxError2d(self) -> float: ...
    def MaxError3d(self) -> float: ...
    def Value(self) -> AppParCurves_MultiCurve: ...

class BRepApprox_MyGradientbisOfTheComputeLineOfApprox:
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Deg: int,
        Tol3d: float,
        Tol2d: float,
        NbIterations: Optional[int] = 200,
    ) -> None: ...
    def AverageError(self) -> float: ...
    def Error(self, Index: int) -> float: ...
    def IsDone(self) -> bool: ...
    def MaxError2d(self) -> float: ...
    def MaxError3d(self) -> float: ...
    def Value(self) -> AppParCurves_MultiCurve: ...

class BRepApprox_ParFunctionOfMyGradientOfTheComputeLineBezierOfApprox(
    math_MultipleVarFunctionWithGradient
):
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Deg: int,
    ) -> None: ...
    def CurveValue(self) -> AppParCurves_MultiCurve: ...
    def Error(self, IPoint: int, CurveIndex: int) -> float: ...
    def FirstConstraint(
        self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int
    ) -> AppParCurves_Constraint: ...
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def LastConstraint(
        self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int
    ) -> AppParCurves_Constraint: ...
    def MaxError2d(self) -> float: ...
    def MaxError3d(self) -> float: ...
    def NbVariables(self) -> int: ...
    def NewParameters(self) -> math_Vector: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class BRepApprox_ParFunctionOfMyGradientbisOfTheComputeLineOfApprox(
    math_MultipleVarFunctionWithGradient
):
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        TheConstraints: AppParCurves_HArray1OfConstraintCouple,
        Parameters: math_Vector,
        Deg: int,
    ) -> None: ...
    def CurveValue(self) -> AppParCurves_MultiCurve: ...
    def Error(self, IPoint: int, CurveIndex: int) -> float: ...
    def FirstConstraint(
        self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, FirstPoint: int
    ) -> AppParCurves_Constraint: ...
    def Gradient(self, X: math_Vector, G: math_Vector) -> bool: ...
    def LastConstraint(
        self, TheConstraints: AppParCurves_HArray1OfConstraintCouple, LastPoint: int
    ) -> AppParCurves_Constraint: ...
    def MaxError2d(self) -> float: ...
    def MaxError3d(self) -> float: ...
    def NbVariables(self) -> int: ...
    def NewParameters(self) -> math_Vector: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...
    def Values(self, X: math_Vector, G: math_Vector) -> Tuple[bool, float]: ...

class BRepApprox_ParLeastSquareOfMyGradientOfTheComputeLineBezierOfApprox:
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Parameters: math_Vector,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Parameters: math_Vector,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        NbPol: int,
    ) -> None: ...
    def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
    def BezierValue(self) -> AppParCurves_MultiCurve: ...
    def DerivativeFunctionMatrix(self) -> math_Matrix: ...
    def Distance(self) -> math_Matrix: ...
    def Error(self) -> Tuple[float, float, float]: ...
    def ErrorGradient(self, Grad: math_Vector) -> Tuple[float, float, float]: ...
    def FirstLambda(self) -> float: ...
    def FunctionMatrix(self) -> math_Matrix: ...
    def IsDone(self) -> bool: ...
    def KIndex(self) -> math_IntegerVector: ...
    def LastLambda(self) -> float: ...
    @overload
    def Perform(self, Parameters: math_Vector) -> None: ...
    @overload
    def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
    @overload
    def Perform(
        self,
        Parameters: math_Vector,
        V1t: math_Vector,
        V2t: math_Vector,
        l1: float,
        l2: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        Parameters: math_Vector,
        V1t: math_Vector,
        V2t: math_Vector,
        V1c: math_Vector,
        V2c: math_Vector,
        l1: float,
        l2: float,
    ) -> None: ...
    def Points(self) -> math_Matrix: ...
    def Poles(self) -> math_Matrix: ...

class BRepApprox_ParLeastSquareOfMyGradientbisOfTheComputeLineOfApprox:
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Parameters: math_Vector,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        Parameters: math_Vector,
        NbPol: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Knots: TColStd_Array1OfReal,
        Mults: TColStd_Array1OfInteger,
        FirstPoint: int,
        LastPoint: int,
        FirstCons: AppParCurves_Constraint,
        LastCons: AppParCurves_Constraint,
        NbPol: int,
    ) -> None: ...
    def BSplineValue(self) -> AppParCurves_MultiBSpCurve: ...
    def BezierValue(self) -> AppParCurves_MultiCurve: ...
    def DerivativeFunctionMatrix(self) -> math_Matrix: ...
    def Distance(self) -> math_Matrix: ...
    def Error(self) -> Tuple[float, float, float]: ...
    def ErrorGradient(self, Grad: math_Vector) -> Tuple[float, float, float]: ...
    def FirstLambda(self) -> float: ...
    def FunctionMatrix(self) -> math_Matrix: ...
    def IsDone(self) -> bool: ...
    def KIndex(self) -> math_IntegerVector: ...
    def LastLambda(self) -> float: ...
    @overload
    def Perform(self, Parameters: math_Vector) -> None: ...
    @overload
    def Perform(self, Parameters: math_Vector, l1: float, l2: float) -> None: ...
    @overload
    def Perform(
        self,
        Parameters: math_Vector,
        V1t: math_Vector,
        V2t: math_Vector,
        l1: float,
        l2: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        Parameters: math_Vector,
        V1t: math_Vector,
        V2t: math_Vector,
        V1c: math_Vector,
        V2c: math_Vector,
        l1: float,
        l2: float,
    ) -> None: ...
    def Points(self) -> math_Matrix: ...
    def Poles(self) -> math_Matrix: ...

class BRepApprox_ResConstraintOfMyGradientOfTheComputeLineBezierOfApprox:
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        SCurv: AppParCurves_MultiCurve,
        FirstPoint: int,
        LastPoint: int,
        Constraints: AppParCurves_HArray1OfConstraintCouple,
        Bern: math_Matrix,
        DerivativeBern: math_Matrix,
        Tolerance: Optional[float] = 1.0e-10,
    ) -> None: ...
    def ConstraintDerivative(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Parameters: math_Vector,
        Deg: int,
        DA: math_Matrix,
    ) -> math_Matrix: ...
    def ConstraintMatrix(self) -> math_Matrix: ...
    def Duale(self) -> math_Vector: ...
    def InverseMatrix(self) -> math_Matrix: ...
    def IsDone(self) -> bool: ...

class BRepApprox_ResConstraintOfMyGradientbisOfTheComputeLineOfApprox:
    def __init__(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        SCurv: AppParCurves_MultiCurve,
        FirstPoint: int,
        LastPoint: int,
        Constraints: AppParCurves_HArray1OfConstraintCouple,
        Bern: math_Matrix,
        DerivativeBern: math_Matrix,
        Tolerance: Optional[float] = 1.0e-10,
    ) -> None: ...
    def ConstraintDerivative(
        self,
        SSP: BRepApprox_TheMultiLineOfApprox,
        Parameters: math_Vector,
        Deg: int,
        DA: math_Matrix,
    ) -> math_Matrix: ...
    def ConstraintMatrix(self) -> math_Matrix: ...
    def Duale(self) -> math_Vector: ...
    def InverseMatrix(self) -> math_Matrix: ...
    def IsDone(self) -> bool: ...

class BRepApprox_TheComputeLineBezierOfApprox:
    @overload
    def __init__(
        self,
        Line: BRepApprox_TheMultiLineOfApprox,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-3,
        Tolerance2d: Optional[float] = 1.0e-6,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
        Squares: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Line: BRepApprox_TheMultiLineOfApprox,
        Parameters: math_Vector,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        Squares: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Parameters: math_Vector,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        Squares: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
        Squares: Optional[bool] = False,
    ) -> None: ...
    def ChangeValue(self, Index: Optional[int] = 1) -> AppParCurves_MultiCurve: ...
    def Error(self, Index: int) -> Tuple[float, float]: ...
    def Init(
        self,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
        Squares: Optional[bool] = False,
    ) -> None: ...
    def IsAllApproximated(self) -> bool: ...
    def IsToleranceReached(self) -> bool: ...
    def NbMultiCurves(self) -> int: ...
    def Parameters(self, Index: Optional[int] = 1) -> TColStd_Array1OfReal: ...
    def Parametrization(self) -> Approx_ParametrizationType: ...
    def Perform(self, Line: BRepApprox_TheMultiLineOfApprox) -> None: ...
    def SetConstraints(
        self, firstC: AppParCurves_Constraint, lastC: AppParCurves_Constraint
    ) -> None: ...
    def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
    def SplineValue(self) -> AppParCurves_MultiBSpCurve: ...
    def Value(self, Index: Optional[int] = 1) -> AppParCurves_MultiCurve: ...

class BRepApprox_TheComputeLineOfApprox:
    @overload
    def __init__(
        self,
        Line: BRepApprox_TheMultiLineOfApprox,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-3,
        Tolerance2d: Optional[float] = 1.0e-6,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
        Squares: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Line: BRepApprox_TheMultiLineOfApprox,
        Parameters: math_Vector,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        Squares: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Parameters: math_Vector,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        Squares: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
        Squares: Optional[bool] = False,
    ) -> None: ...
    def ChangeValue(self) -> AppParCurves_MultiBSpCurve: ...
    def Error(self) -> Tuple[float, float]: ...
    def Init(
        self,
        degreemin: Optional[int] = 4,
        degreemax: Optional[int] = 8,
        Tolerance3d: Optional[float] = 1.0e-03,
        Tolerance2d: Optional[float] = 1.0e-06,
        NbIterations: Optional[int] = 5,
        cutting: Optional[bool] = True,
        parametrization: Optional[Approx_ParametrizationType] = Approx_ChordLength,
        Squares: Optional[bool] = False,
    ) -> None: ...
    def Interpol(self, Line: BRepApprox_TheMultiLineOfApprox) -> None: ...
    def IsAllApproximated(self) -> bool: ...
    def IsToleranceReached(self) -> bool: ...
    def Parameters(self) -> TColStd_Array1OfReal: ...
    def Perform(self, Line: BRepApprox_TheMultiLineOfApprox) -> None: ...
    def SetConstraints(
        self, firstC: AppParCurves_Constraint, lastC: AppParCurves_Constraint
    ) -> None: ...
    def SetContinuity(self, C: int) -> None: ...
    def SetDegrees(self, degreemin: int, degreemax: int) -> None: ...
    def SetKnots(self, Knots: TColStd_Array1OfReal) -> None: ...
    def SetKnotsAndMultiplicities(
        self, Knots: TColStd_Array1OfReal, Mults: TColStd_Array1OfInteger
    ) -> None: ...
    def SetParameters(self, ThePar: math_Vector) -> None: ...
    def SetPeriodic(self, thePeriodic: bool) -> None: ...
    def SetTolerances(self, Tolerance3d: float, Tolerance2d: float) -> None: ...
    def Value(self) -> AppParCurves_MultiBSpCurve: ...

class BRepApprox_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfApprox(
    math_FunctionSetWithDerivatives
):
    def __init__(self, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface) -> None: ...
    def AuxillarSurface1(self) -> BRepAdaptor_Surface: ...
    def AuxillarSurface2(self) -> BRepAdaptor_Surface: ...
    def ComputeParameters(
        self,
        ChoixIso: IntImp_ConstIsoparametric,
        Param: TColStd_Array1OfReal,
        UVap: math_Vector,
        BornInf: math_Vector,
        BornSup: math_Vector,
        Tolerance: math_Vector,
    ) -> None: ...
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def Direction(self) -> gp_Dir: ...
    def DirectionOnS1(self) -> gp_Dir2d: ...
    def DirectionOnS2(self) -> gp_Dir2d: ...
    def IsTangent(
        self, UVap: math_Vector, Param: TColStd_Array1OfReal
    ) -> Tuple[bool, IntImp_ConstIsoparametric]: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Point(self) -> gp_Pnt: ...
    def Root(self) -> float: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepApprox_TheImpPrmSvSurfacesOfApprox(ApproxInt_SvSurfaces):
    @overload
    def __init__(self, Surf1: BRepAdaptor_Surface, Surf2: IntSurf_Quadric) -> None: ...
    @overload
    def __init__(self, Surf1: IntSurf_Quadric, Surf2: BRepAdaptor_Surface) -> None: ...
    def Compute(
        self, Pt: gp_Pnt, Tg: gp_Vec, Tguv1: gp_Vec2d, Tguv2: gp_Vec2d
    ) -> Tuple[bool, float, float, float, float]: ...
    def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: gp_Pnt) -> None: ...
    def SeekPoint(
        self, u1: float, v1: float, u2: float, v2: float, Point: IntSurf_PntOn2S
    ) -> bool: ...
    def Tangency(
        self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec
    ) -> bool: ...
    def TangencyOnSurf1(
        self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d
    ) -> bool: ...
    def TangencyOnSurf2(
        self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d
    ) -> bool: ...

class BRepApprox_TheInt2SOfThePrmPrmSvSurfacesOfApprox:
    @overload
    def __init__(
        self,
        Param: TColStd_Array1OfReal,
        S1: BRepAdaptor_Surface,
        S2: BRepAdaptor_Surface,
        TolTangency: float,
    ) -> None: ...
    @overload
    def __init__(
        self, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface, TolTangency: float
    ) -> None: ...
    def ChangePoint(self) -> IntSurf_PntOn2S: ...
    def Direction(self) -> gp_Dir: ...
    def DirectionOnS1(self) -> gp_Dir2d: ...
    def DirectionOnS2(self) -> gp_Dir2d: ...
    def Function(
        self,
    ) -> BRepApprox_TheFunctionOfTheInt2SOfThePrmPrmSvSurfacesOfApprox: ...
    def IsDone(self) -> bool: ...
    def IsEmpty(self) -> bool: ...
    def IsTangent(self) -> bool: ...
    @overload
    def Perform(
        self, Param: TColStd_Array1OfReal, Rsnld: math_FunctionSetRoot
    ) -> IntImp_ConstIsoparametric: ...
    @overload
    def Perform(
        self,
        Param: TColStd_Array1OfReal,
        Rsnld: math_FunctionSetRoot,
        ChoixIso: IntImp_ConstIsoparametric,
    ) -> IntImp_ConstIsoparametric: ...
    def Point(self) -> IntSurf_PntOn2S: ...

class BRepApprox_TheMultiLineOfApprox:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        line: BRepApprox_ApproxLine,
        PtrSvSurfaces: None,
        NbP3d: int,
        NbP2d: int,
        ApproxU1V1: bool,
        ApproxU2V2: bool,
        xo: float,
        yo: float,
        zo: float,
        u1o: float,
        v1o: float,
        u2o: float,
        v2o: float,
        P2DOnFirst: bool,
        IndMin: Optional[int] = 0,
        IndMax: Optional[int] = 0,
    ) -> None: ...
    @overload
    def __init__(
        self,
        line: BRepApprox_ApproxLine,
        NbP3d: int,
        NbP2d: int,
        ApproxU1V1: bool,
        ApproxU2V2: bool,
        xo: float,
        yo: float,
        zo: float,
        u1o: float,
        v1o: float,
        u2o: float,
        v2o: float,
        P2DOnFirst: bool,
        IndMin: Optional[int] = 0,
        IndMax: Optional[int] = 0,
    ) -> None: ...
    def Dump(self) -> None: ...
    def FirstPoint(self) -> int: ...
    def LastPoint(self) -> int: ...
    def MakeMLBetween(
        self, Low: int, High: int, NbPointsToInsert: int
    ) -> BRepApprox_TheMultiLineOfApprox: ...
    def MakeMLOneMorePoint(
        self,
        Low: int,
        High: int,
        indbad: int,
        OtherLine: BRepApprox_TheMultiLineOfApprox,
    ) -> bool: ...
    def NbP2d(self) -> int: ...
    def NbP3d(self) -> int: ...
    @overload
    def Tangency(self, MPointIndex: int, tabV: TColgp_Array1OfVec) -> bool: ...
    @overload
    def Tangency(self, MPointIndex: int, tabV2d: TColgp_Array1OfVec2d) -> bool: ...
    @overload
    def Tangency(
        self, MPointIndex: int, tabV: TColgp_Array1OfVec, tabV2d: TColgp_Array1OfVec2d
    ) -> bool: ...
    @overload
    def Value(self, MPointIndex: int, tabPt: TColgp_Array1OfPnt) -> None: ...
    @overload
    def Value(self, MPointIndex: int, tabPt2d: TColgp_Array1OfPnt2d) -> None: ...
    @overload
    def Value(
        self, MPointIndex: int, tabPt: TColgp_Array1OfPnt, tabPt2d: TColgp_Array1OfPnt2d
    ) -> None: ...
    def WhatStatus(self) -> Approx_Status: ...

class BRepApprox_TheMultiLineToolOfApprox:
    @overload
    @staticmethod
    def Curvature(
        ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV: TColgp_Array1OfVec
    ) -> bool: ...
    @overload
    @staticmethod
    def Curvature(
        ML: BRepApprox_TheMultiLineOfApprox,
        MPointIndex: int,
        tabV2d: TColgp_Array1OfVec2d,
    ) -> bool: ...
    @overload
    @staticmethod
    def Curvature(
        ML: BRepApprox_TheMultiLineOfApprox,
        MPointIndex: int,
        tabV: TColgp_Array1OfVec,
        tabV2d: TColgp_Array1OfVec2d,
    ) -> bool: ...
    @staticmethod
    def Dump(ML: BRepApprox_TheMultiLineOfApprox) -> None: ...
    @staticmethod
    def FirstPoint(ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
    @staticmethod
    def LastPoint(ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
    @staticmethod
    def MakeMLBetween(
        ML: BRepApprox_TheMultiLineOfApprox, I1: int, I2: int, NbPMin: int
    ) -> BRepApprox_TheMultiLineOfApprox: ...
    @staticmethod
    def MakeMLOneMorePoint(
        ML: BRepApprox_TheMultiLineOfApprox,
        I1: int,
        I2: int,
        indbad: int,
        OtherLine: BRepApprox_TheMultiLineOfApprox,
    ) -> bool: ...
    @staticmethod
    def NbP2d(ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
    @staticmethod
    def NbP3d(ML: BRepApprox_TheMultiLineOfApprox) -> int: ...
    @overload
    @staticmethod
    def Tangency(
        ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabV: TColgp_Array1OfVec
    ) -> bool: ...
    @overload
    @staticmethod
    def Tangency(
        ML: BRepApprox_TheMultiLineOfApprox,
        MPointIndex: int,
        tabV2d: TColgp_Array1OfVec2d,
    ) -> bool: ...
    @overload
    @staticmethod
    def Tangency(
        ML: BRepApprox_TheMultiLineOfApprox,
        MPointIndex: int,
        tabV: TColgp_Array1OfVec,
        tabV2d: TColgp_Array1OfVec2d,
    ) -> bool: ...
    @overload
    @staticmethod
    def Value(
        ML: BRepApprox_TheMultiLineOfApprox, MPointIndex: int, tabPt: TColgp_Array1OfPnt
    ) -> None: ...
    @overload
    @staticmethod
    def Value(
        ML: BRepApprox_TheMultiLineOfApprox,
        MPointIndex: int,
        tabPt2d: TColgp_Array1OfPnt2d,
    ) -> None: ...
    @overload
    @staticmethod
    def Value(
        ML: BRepApprox_TheMultiLineOfApprox,
        MPointIndex: int,
        tabPt: TColgp_Array1OfPnt,
        tabPt2d: TColgp_Array1OfPnt2d,
    ) -> None: ...
    @staticmethod
    def WhatStatus(
        ML: BRepApprox_TheMultiLineOfApprox, I1: int, I2: int
    ) -> Approx_Status: ...

class BRepApprox_ThePrmPrmSvSurfacesOfApprox(ApproxInt_SvSurfaces):
    def __init__(
        self, Surf1: BRepAdaptor_Surface, Surf2: BRepAdaptor_Surface
    ) -> None: ...
    def Compute(
        self, Pt: gp_Pnt, Tg: gp_Vec, Tguv1: gp_Vec2d, Tguv2: gp_Vec2d
    ) -> Tuple[bool, float, float, float, float]: ...
    def Pnt(self, u1: float, v1: float, u2: float, v2: float, P: gp_Pnt) -> None: ...
    def SeekPoint(
        self, u1: float, v1: float, u2: float, v2: float, Point: IntSurf_PntOn2S
    ) -> bool: ...
    def Tangency(
        self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec
    ) -> bool: ...
    def TangencyOnSurf1(
        self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d
    ) -> bool: ...
    def TangencyOnSurf2(
        self, u1: float, v1: float, u2: float, v2: float, Tg: gp_Vec2d
    ) -> bool: ...

class BRepApprox_TheZerImpFuncOfTheImpPrmSvSurfacesOfApprox(
    math_FunctionSetWithDerivatives
):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, PS: BRepAdaptor_Surface, IS: IntSurf_Quadric) -> None: ...
    @overload
    def __init__(self, IS: IntSurf_Quadric) -> None: ...
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def Direction2d(self) -> gp_Dir2d: ...
    def Direction3d(self) -> gp_Vec: ...
    def ISurface(self) -> IntSurf_Quadric: ...
    def IsTangent(self) -> bool: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def PSurface(self) -> BRepAdaptor_Surface: ...
    def Point(self) -> gp_Pnt: ...
    def Root(self) -> float: ...
    @overload
    def Set(self, PS: BRepAdaptor_Surface) -> None: ...
    @overload
    def Set(self, Tolerance: float) -> None: ...
    def SetImplicitSurface(self, IS: IntSurf_Quadric) -> None: ...
    def Tolerance(self) -> float: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes
