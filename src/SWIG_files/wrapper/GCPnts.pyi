from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Adaptor2d import *
from OCC.Core.math import *
from OCC.Core.GeomAbs import *
from OCC.Core.gp import *

class GCPnts_AbscissaType(IntEnum):
    GCPnts_LengthParametrized: int = ...
    GCPnts_Parametrized: int = ...
    GCPnts_AbsComposite: int = ...

GCPnts_LengthParametrized = GCPnts_AbscissaType.GCPnts_LengthParametrized
GCPnts_Parametrized = GCPnts_AbscissaType.GCPnts_Parametrized
GCPnts_AbsComposite = GCPnts_AbscissaType.GCPnts_AbsComposite

class GCPnts_DeflectionType(IntEnum):
    GCPnts_Linear: int = ...
    GCPnts_Circular: int = ...
    GCPnts_Curved: int = ...
    GCPnts_DefComposite: int = ...

GCPnts_Linear = GCPnts_DeflectionType.GCPnts_Linear
GCPnts_Circular = GCPnts_DeflectionType.GCPnts_Circular
GCPnts_Curved = GCPnts_DeflectionType.GCPnts_Curved
GCPnts_DefComposite = GCPnts_DeflectionType.GCPnts_DefComposite

class GCPnts_AbscissaPoint:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor3d_Curve, theAbscissa: float, theU0: float
    ) -> None: ...
    @overload
    def __init__(
        self, theTol: float, theC: Adaptor3d_Curve, theAbscissa: float, theU0: float
    ) -> None: ...
    @overload
    def __init__(
        self, theTol: float, theC: Adaptor2d_Curve2d, theAbscissa: float, theU0: float
    ) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor2d_Curve2d, theAbscissa: float, theU0: float
    ) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor3d_Curve, theAbscissa: float, theU0: float, theUi: float
    ) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor2d_Curve2d, theAbscissa: float, theU0: float, theUi: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theAbscissa: float,
        theU0: float,
        theUi: float,
        theTol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theAbscissa: float,
        theU0: float,
        theUi: float,
        theTol: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    @overload
    @staticmethod
    def Length(theC: Adaptor3d_Curve) -> float: ...
    @overload
    @staticmethod
    def Length(theC: Adaptor2d_Curve2d) -> float: ...
    @overload
    @staticmethod
    def Length(theC: Adaptor3d_Curve, theTol: float) -> float: ...
    @overload
    @staticmethod
    def Length(theC: Adaptor2d_Curve2d, theTol: float) -> float: ...
    @overload
    @staticmethod
    def Length(theC: Adaptor3d_Curve, theU1: float, theU2: float) -> float: ...
    @overload
    @staticmethod
    def Length(theC: Adaptor2d_Curve2d, theU1: float, theU2: float) -> float: ...
    @overload
    @staticmethod
    def Length(
        theC: Adaptor3d_Curve, theU1: float, theU2: float, theTol: float
    ) -> float: ...
    @overload
    @staticmethod
    def Length(
        theC: Adaptor2d_Curve2d, theU1: float, theU2: float, theTol: float
    ) -> float: ...
    def Parameter(self) -> float: ...

class GCPnts_DistFunction2dMV(math_MultipleVarFunction):
    def __init__(self, theCurvLinDist: GCPnts_DistFunction2d) -> None: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...

class GCPnts_DistFunctionMV(math_MultipleVarFunction):
    def __init__(self, theCurvLinDist: GCPnts_DistFunction) -> None: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector) -> Tuple[bool, float]: ...

class GCPnts_QuasiUniformAbscissa:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theC: Adaptor3d_Curve, theNbPoints: int) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor3d_Curve, theNbPoints: int, theU1: float, theU2: float
    ) -> None: ...
    @overload
    def __init__(self, theC: Adaptor2d_Curve2d, theNbPoints: int) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor2d_Curve2d, theNbPoints: int, theU1: float, theU2: float
    ) -> None: ...
    @overload
    def Initialize(self, theC: Adaptor3d_Curve, theNbPoints: int) -> None: ...
    @overload
    def Initialize(
        self, theC: Adaptor3d_Curve, theNbPoints: int, theU1: float, theU2: float
    ) -> None: ...
    @overload
    def Initialize(self, theC: Adaptor2d_Curve2d, theNbPoints: int) -> None: ...
    @overload
    def Initialize(
        self, theC: Adaptor2d_Curve2d, theNbPoints: int, theU1: float, theU2: float
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbPoints(self) -> int: ...
    def Parameter(self, Index: int) -> float: ...

class GCPnts_QuasiUniformDeflection:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    def Deflection(self) -> float: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theContinuity: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbPoints(self) -> int: ...
    def Parameter(self, Index: int) -> float: ...
    def Value(self, Index: int) -> gp_Pnt: ...

class GCPnts_TCurveTypes:
    pass

class GCPnts_TCurveTypes:
    pass

class GCPnts_TangentialDeflection:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theFirstParameter: float,
        theLastParameter: float,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theFirstParameter: float,
        theLastParameter: float,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    def AddPoint(
        self, thePnt: gp_Pnt, theParam: float, theIsReplace: Optional[bool] = True
    ) -> int: ...
    @staticmethod
    def ArcAngularStep(
        theRadius: float,
        theLinearDeflection: float,
        theAngularDeflection: float,
        theMinLength: float,
    ) -> float: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theFirstParameter: float,
        theLastParameter: float,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theFirstParameter: float,
        theLastParameter: float,
        theAngularDeflection: float,
        theCurvatureDeflection: float,
        theMinimumOfPoints: Optional[int] = 2,
        theUTol: Optional[float] = 1.0e-9,
        theMinLen: Optional[float] = 1.0e-7,
    ) -> None: ...
    def NbPoints(self) -> int: ...
    def Parameter(self, I: int) -> float: ...
    def Value(self, I: int) -> gp_Pnt: ...

class GCPnts_UniformAbscissa:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor3d_Curve, theAbscissa: float, theToler: Optional[float] = -1
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theAbscissa: float,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor3d_Curve, theNbPoints: int, theToler: Optional[float] = -1
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theNbPoints: int,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theAbscissa: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theAbscissa: float,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def __init__(
        self, theC: Adaptor2d_Curve2d, theNbPoints: int, theToler: Optional[float] = -1
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theNbPoints: int,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    def Abscissa(self) -> float: ...
    @overload
    def Initialize(
        self, theC: Adaptor3d_Curve, theAbscissa: float, theToler: Optional[float] = -1
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theAbscissa: float,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def Initialize(
        self, theC: Adaptor3d_Curve, theNbPoints: int, theToler: Optional[float] = -1
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theNbPoints: int,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theAbscissa: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theAbscissa: float,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    @overload
    def Initialize(
        self, theC: Adaptor2d_Curve2d, theNbPoints: int, theToler: Optional[float] = -1
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theNbPoints: int,
        theU1: float,
        theU2: float,
        theToler: Optional[float] = -1,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbPoints(self) -> int: ...
    def Parameter(self, Index: int) -> float: ...

class GCPnts_UniformDeflection:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    @overload
    def __init__(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    def Deflection(self) -> float: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor3d_Curve,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    @overload
    def Initialize(
        self,
        theC: Adaptor2d_Curve2d,
        theDeflection: float,
        theU1: float,
        theU2: float,
        theWithControl: Optional[bool] = True,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbPoints(self) -> int: ...
    def Parameter(self, Index: int) -> float: ...
    def Value(self, Index: int) -> gp_Pnt: ...

# classnotwrapped
class GCPnts_DistFunction: ...

# classnotwrapped
class GCPnts_DistFunction2d: ...

# classnotwrapped
class GCPnts_TCurveTypes: ...

# harray1 classes
# harray2 classes
# hsequence classes
