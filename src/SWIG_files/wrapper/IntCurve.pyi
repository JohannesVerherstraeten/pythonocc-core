from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.IntRes2d import *
from OCC.Core.TColStd import *
from OCC.Core.math import *
from OCC.Core.GeomAbs import *

class IntCurve_IConicTool:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, IT: IntCurve_IConicTool) -> None: ...
    @overload
    def __init__(self, E: gp_Elips2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d) -> None: ...
    @overload
    def __init__(self, C: gp_Circ2d) -> None: ...
    @overload
    def __init__(self, P: gp_Parab2d) -> None: ...
    @overload
    def __init__(self, H: gp_Hypr2d) -> None: ...
    def D1(self, U: float, P: gp_Pnt2d, T: gp_Vec2d) -> None: ...
    def D2(self, U: float, P: gp_Pnt2d, T: gp_Vec2d, N: gp_Vec2d) -> None: ...
    def Distance(self, P: gp_Pnt2d) -> float: ...
    def FindParameter(self, P: gp_Pnt2d) -> float: ...
    def GradDistance(self, P: gp_Pnt2d) -> gp_Vec2d: ...
    def Value(self, X: float) -> gp_Pnt2d: ...

class IntCurve_IntConicConic(IntRes2d_Intersection):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        L1: gp_Lin2d,
        D1: IntRes2d_Domain,
        L2: gp_Lin2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C1: gp_Circ2d,
        D1: IntRes2d_Domain,
        C2: gp_Circ2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        E1: gp_Elips2d,
        D1: IntRes2d_Domain,
        E2: gp_Elips2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        P1: gp_Parab2d,
        D1: IntRes2d_Domain,
        P2: gp_Parab2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        H1: gp_Hypr2d,
        D1: IntRes2d_Domain,
        H2: gp_Hypr2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        L1: gp_Lin2d,
        D1: IntRes2d_Domain,
        L2: gp_Lin2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        L: gp_Lin2d,
        DL: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        C1: gp_Circ2d,
        D1: IntRes2d_Domain,
        C2: gp_Circ2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        C: gp_Circ2d,
        DC: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        E1: gp_Elips2d,
        D1: IntRes2d_Domain,
        E2: gp_Elips2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        E: gp_Elips2d,
        DE: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        P1: gp_Parab2d,
        D1: IntRes2d_Domain,
        P2: gp_Parab2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        P: gp_Parab2d,
        DP: IntRes2d_Domain,
        H: gp_Hypr2d,
        DH: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    @overload
    def Perform(
        self,
        H1: gp_Hypr2d,
        D1: IntRes2d_Domain,
        H2: gp_Hypr2d,
        D2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...

class IntCurve_IntImpConicParConic(IntRes2d_Intersection):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        ITool: IntCurve_IConicTool,
        Dom1: IntRes2d_Domain,
        PCurve: IntCurve_PConic,
        Dom2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...
    def And_Domaine_Objet1_Intersections(
        self,
        TheImpTool: IntCurve_IConicTool,
        TheParCurve: IntCurve_PConic,
        TheImpCurveDomain: IntRes2d_Domain,
        TheParCurveDomain: IntRes2d_Domain,
        Inter2_And_Domain2: TColStd_Array1OfReal,
        Inter1: TColStd_Array1OfReal,
        Resultat1: TColStd_Array1OfReal,
        Resultat2: TColStd_Array1OfReal,
        EpsNul: float,
    ) -> int: ...
    def FindU(
        self,
        parameter: float,
        point: gp_Pnt2d,
        TheParCurev: IntCurve_PConic,
        TheImpTool: IntCurve_IConicTool,
    ) -> float: ...
    def FindV(
        self,
        parameter: float,
        point: gp_Pnt2d,
        TheImpTool: IntCurve_IConicTool,
        ParCurve: IntCurve_PConic,
        TheParCurveDomain: IntRes2d_Domain,
        V0: float,
        V1: float,
        Tolerance: float,
    ) -> float: ...
    def Perform(
        self,
        ITool: IntCurve_IConicTool,
        Dom1: IntRes2d_Domain,
        PCurve: IntCurve_PConic,
        Dom2: IntRes2d_Domain,
        TolConf: float,
        Tol: float,
    ) -> None: ...

class IntCurve_MyImpParToolOfIntImpConicParConic(math_FunctionWithDerivative):
    def __init__(self, IT: IntCurve_IConicTool, PC: IntCurve_PConic) -> None: ...
    def Derivative(self, Param: float) -> Tuple[bool, float]: ...
    def Value(self, Param: float) -> Tuple[bool, float]: ...
    def Values(self, Param: float) -> Tuple[bool, float, float]: ...

class IntCurve_PConic:
    @overload
    def __init__(self, PC: IntCurve_PConic) -> None: ...
    @overload
    def __init__(self, E: gp_Elips2d) -> None: ...
    @overload
    def __init__(self, C: gp_Circ2d) -> None: ...
    @overload
    def __init__(self, P: gp_Parab2d) -> None: ...
    @overload
    def __init__(self, H: gp_Hypr2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d) -> None: ...
    def Accuracy(self) -> int: ...
    def Axis2(self) -> gp_Ax22d: ...
    def EpsX(self) -> float: ...
    def Param1(self) -> float: ...
    def Param2(self) -> float: ...
    def SetAccuracy(self, Nb: int) -> None: ...
    def SetEpsX(self, EpsDist: float) -> None: ...
    def TypeCurve(self) -> GeomAbs_CurveType: ...

class IntCurve_PConicTool:
    @staticmethod
    def D1(C: IntCurve_PConic, U: float, P: gp_Pnt2d, T: gp_Vec2d) -> None: ...
    @staticmethod
    def D2(
        C: IntCurve_PConic, U: float, P: gp_Pnt2d, T: gp_Vec2d, N: gp_Vec2d
    ) -> None: ...
    @staticmethod
    def EpsX(C: IntCurve_PConic) -> float: ...
    @overload
    @staticmethod
    def NbSamples(C: IntCurve_PConic) -> int: ...
    @overload
    @staticmethod
    def NbSamples(C: IntCurve_PConic, U0: float, U1: float) -> int: ...
    @staticmethod
    def Value(C: IntCurve_PConic, X: float) -> gp_Pnt2d: ...

class IntCurve_ProjectOnPConicTool:
    @overload
    @staticmethod
    def FindParameter(C: IntCurve_PConic, Pnt: gp_Pnt2d, Tol: float) -> float: ...
    @overload
    @staticmethod
    def FindParameter(
        C: IntCurve_PConic,
        Pnt: gp_Pnt2d,
        LowParameter: float,
        HighParameter: float,
        Tol: float,
    ) -> float: ...

# harray1 classes
# harray2 classes
# hsequence classes
