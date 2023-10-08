from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom2dAdaptor import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *
from OCC.Core.GccAna import *
from OCC.Core.GccEnt import *
from OCC.Core.math import *

class Geom2dGcc_Type1(IntEnum):
    Geom2dGcc_CuCuCu: int = ...
    Geom2dGcc_CiCuCu: int = ...
    Geom2dGcc_CiCiCu: int = ...
    Geom2dGcc_CiLiCu: int = ...
    Geom2dGcc_LiLiCu: int = ...
    Geom2dGcc_LiCuCu: int = ...

Geom2dGcc_CuCuCu = Geom2dGcc_Type1.Geom2dGcc_CuCuCu
Geom2dGcc_CiCuCu = Geom2dGcc_Type1.Geom2dGcc_CiCuCu
Geom2dGcc_CiCiCu = Geom2dGcc_Type1.Geom2dGcc_CiCiCu
Geom2dGcc_CiLiCu = Geom2dGcc_Type1.Geom2dGcc_CiLiCu
Geom2dGcc_LiLiCu = Geom2dGcc_Type1.Geom2dGcc_LiLiCu
Geom2dGcc_LiCuCu = Geom2dGcc_Type1.Geom2dGcc_LiCuCu

class Geom2dGcc_Type2(IntEnum):
    Geom2dGcc_CuCuOnCu: int = ...
    Geom2dGcc_CiCuOnCu: int = ...
    Geom2dGcc_LiCuOnCu: int = ...
    Geom2dGcc_CuPtOnCu: int = ...
    Geom2dGcc_CuCuOnLi: int = ...
    Geom2dGcc_CiCuOnLi: int = ...
    Geom2dGcc_LiCuOnLi: int = ...
    Geom2dGcc_CuPtOnLi: int = ...
    Geom2dGcc_CuCuOnCi: int = ...
    Geom2dGcc_CiCuOnCi: int = ...
    Geom2dGcc_LiCuOnCi: int = ...
    Geom2dGcc_CuPtOnCi: int = ...

Geom2dGcc_CuCuOnCu = Geom2dGcc_Type2.Geom2dGcc_CuCuOnCu
Geom2dGcc_CiCuOnCu = Geom2dGcc_Type2.Geom2dGcc_CiCuOnCu
Geom2dGcc_LiCuOnCu = Geom2dGcc_Type2.Geom2dGcc_LiCuOnCu
Geom2dGcc_CuPtOnCu = Geom2dGcc_Type2.Geom2dGcc_CuPtOnCu
Geom2dGcc_CuCuOnLi = Geom2dGcc_Type2.Geom2dGcc_CuCuOnLi
Geom2dGcc_CiCuOnLi = Geom2dGcc_Type2.Geom2dGcc_CiCuOnLi
Geom2dGcc_LiCuOnLi = Geom2dGcc_Type2.Geom2dGcc_LiCuOnLi
Geom2dGcc_CuPtOnLi = Geom2dGcc_Type2.Geom2dGcc_CuPtOnLi
Geom2dGcc_CuCuOnCi = Geom2dGcc_Type2.Geom2dGcc_CuCuOnCi
Geom2dGcc_CiCuOnCi = Geom2dGcc_Type2.Geom2dGcc_CiCuOnCi
Geom2dGcc_LiCuOnCi = Geom2dGcc_Type2.Geom2dGcc_LiCuOnCi
Geom2dGcc_CuPtOnCi = Geom2dGcc_Type2.Geom2dGcc_CuPtOnCi

class Geom2dGcc_Type3(IntEnum):
    Geom2dGcc_CuCu: int = ...
    Geom2dGcc_CiCu: int = ...

Geom2dGcc_CuCu = Geom2dGcc_Type3.Geom2dGcc_CuCu
Geom2dGcc_CiCu = Geom2dGcc_Type3.Geom2dGcc_CiCu

class geom2dgcc:
    @staticmethod
    def Enclosed(Obj: Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: ...
    @staticmethod
    def Enclosing(Obj: Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: ...
    @staticmethod
    def Outside(Obj: Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: ...
    @staticmethod
    def Unqualified(Obj: Geom2dAdaptor_Curve) -> Geom2dGcc_QualifiedCurve: ...

class Geom2dGcc_Circ2d2TanOn:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Qualified2: Geom2dGcc_QualifiedCurve,
        OnCurve: Geom2dAdaptor_Curve,
        Tolerance: float,
        Param1: float,
        Param2: float,
        ParamOn: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Point: Geom2d_Point,
        OnCurve: Geom2dAdaptor_Curve,
        Tolerance: float,
        Param1: float,
        ParamOn: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Point1: Geom2d_Point,
        Point2: Geom2d_Point,
        OnCurve: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    def CenterOn3(self, Index: int, PntSol: gp_Pnt2d) -> float: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def IsTheSame2(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    @overload
    def Results(self, Circ: GccAna_Circ2d2TanOn) -> None: ...
    @overload
    def Results(self, Circ: Geom2dGcc_Circ2d2TanOnGeo) -> None: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2d2TanOnGeo:
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: GccEnt_QualifiedCirc,
        OnCurv: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: GccEnt_QualifiedLin,
        OnCurv: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Point2: gp_Pnt2d,
        OnCurv: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: GccEnt_QualifiedLin,
        OnCurv: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: gp_Pnt2d,
        OnCurv: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Point1: gp_Pnt2d,
        Point2: gp_Pnt2d,
        OnCurv: Geom2dAdaptor_Curve,
        Tolerance: float,
    ) -> None: ...
    def CenterOn3(self, Index: int, PntSol: gp_Pnt2d) -> float: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def IsTheSame2(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2d2TanOnIter:
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        OnLine: gp_Lin2d,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: Geom2dGcc_QCurve,
        OnLine: gp_Lin2d,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        OnLine: gp_Lin2d,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Point2: gp_Pnt2d,
        OnLine: gp_Lin2d,
        Param1: float,
        Param2: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        OnCirc: gp_Circ2d,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: Geom2dGcc_QCurve,
        OnCirc: gp_Circ2d,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        OnCirc: gp_Circ2d,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Point2: gp_Pnt2d,
        OnCirc: gp_Circ2d,
        Param1: float,
        Param2: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        OnCurv: Geom2dAdaptor_Curve,
        Param1: float,
        Param2: float,
        ParamOn: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: Geom2dGcc_QCurve,
        OnCurve: Geom2dAdaptor_Curve,
        Param1: float,
        Param2: float,
        ParamOn: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Point2: gp_Pnt2d,
        OnCurve: Geom2dAdaptor_Curve,
        Param1: float,
        ParamOn: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        OnCurve: Geom2dAdaptor_Curve,
        Param1: float,
        Param2: float,
        ParamOn: float,
        Tolerance: float,
    ) -> None: ...
    def CenterOn3(self, PntSol: gp_Pnt2d) -> float: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self) -> bool: ...
    def IsTheSame2(self) -> bool: ...
    def Tangency1(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self) -> gp_Circ2d: ...
    def WhichQualifier(self) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2d2TanRad:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Qualified2: Geom2dGcc_QualifiedCurve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Point: Geom2d_Point,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Point1: Geom2d_Point,
        Point2: Geom2d_Point,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def IsTheSame2(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    @overload
    def Results(self, Circ: GccAna_Circ2d2TanRad) -> None: ...
    @overload
    def Results(self, Circ: Geom2dGcc_Circ2d2TanRadGeo) -> None: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2d2TanRadGeo:
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: Geom2dGcc_QCurve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Point2: gp_Pnt2d,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def IsTheSame2(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2d3Tan:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Qualified2: Geom2dGcc_QualifiedCurve,
        Qualified3: Geom2dGcc_QualifiedCurve,
        Tolerance: float,
        Param1: float,
        Param2: float,
        Param3: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Qualified2: Geom2dGcc_QualifiedCurve,
        Point: Geom2d_Point,
        Tolerance: float,
        Param1: float,
        Param2: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Point1: Geom2d_Point,
        Point2: Geom2d_Point,
        Tolerance: float,
        Param1: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Point1: Geom2d_Point,
        Point2: Geom2d_Point,
        Point3: Geom2d_Point,
        Tolerance: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def IsTheSame2(self, Index: int) -> bool: ...
    def IsTheSame3(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Results(
        self, Circ: GccAna_Circ2d3Tan, Rank1: int, Rank2: int, Rank3: int
    ) -> None: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency3(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(
        self, Index: int
    ) -> Tuple[GccEnt_Position, GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2d3TanIter:
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: GccEnt_QualifiedCirc,
        Qualified3: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        Qualified3: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: GccEnt_QualifiedLin,
        Qualified3: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        Point3: gp_Pnt2d,
        Param1: float,
        Param2: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: GccEnt_QualifiedLin,
        Qualified3: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: Geom2dGcc_QCurve,
        Qualified3: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        Qualified2: Geom2dGcc_QCurve,
        Point3: gp_Pnt2d,
        Param1: float,
        Param2: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Point1: gp_Pnt2d,
        Point2: gp_Pnt2d,
        Param1: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        Point2: gp_Pnt2d,
        Param1: float,
        Param2: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        Qualified3: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Param3: float,
        Tolerance: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self) -> bool: ...
    def IsTheSame2(self) -> bool: ...
    def IsTheSame3(self) -> bool: ...
    def Tangency1(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency3(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self) -> gp_Circ2d: ...
    def WhichQualifier(
        self,
    ) -> Tuple[GccEnt_Position, GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Circ2dTanCen:
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Pcenter: Geom2d_Point,
        Tolerance: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> GccEnt_Position: ...

class Geom2dGcc_Circ2dTanCenGeo:
    def __init__(
        self, Qualified1: Geom2dGcc_QCurve, Pcenter: gp_Pnt2d, Tolerance: float
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> GccEnt_Position: ...

class Geom2dGcc_Circ2dTanOnRad:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        OnCurv: Geom2dAdaptor_Curve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Point1: Geom2d_Point,
        OnCurv: Geom2dAdaptor_Curve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    def CenterOn3(self, Index: int, PntSol: gp_Pnt2d) -> float: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    @overload
    def Results(self, Circ: GccAna_Circ2dTanOnRad) -> None: ...
    @overload
    def Results(self, Circ: Geom2dGcc_Circ2dTanOnRadGeo) -> None: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> GccEnt_Position: ...

class Geom2dGcc_Circ2dTanOnRadGeo:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        OnLine: gp_Lin2d,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        OnCirc: gp_Circ2d,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        OnCurv: Geom2dAdaptor_Curve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedLin,
        OnCurv: Geom2dAdaptor_Curve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        OnCurv: Geom2dAdaptor_Curve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Point1: gp_Pnt2d,
        OnCurv: Geom2dAdaptor_Curve,
        Radius: float,
        Tolerance: float,
    ) -> None: ...
    def CenterOn3(self, Index: int, PntSol: gp_Pnt2d) -> float: ...
    def IsDone(self) -> bool: ...
    def IsTheSame1(self, Index: int) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Circ2d: ...
    def WhichQualifier(self, Index: int) -> GccEnt_Position: ...

class Geom2dGcc_CurveTool:
    @staticmethod
    def D1(C: Geom2dAdaptor_Curve, U: float, P: gp_Pnt2d, T: gp_Vec2d) -> None: ...
    @staticmethod
    def D2(
        C: Geom2dAdaptor_Curve, U: float, P: gp_Pnt2d, T: gp_Vec2d, N: gp_Vec2d
    ) -> None: ...
    @staticmethod
    def D3(
        C: Geom2dAdaptor_Curve,
        U: float,
        P: gp_Pnt2d,
        T: gp_Vec2d,
        N: gp_Vec2d,
        dN: gp_Vec2d,
    ) -> None: ...
    @staticmethod
    def EpsX(C: Geom2dAdaptor_Curve, Tol: float) -> float: ...
    @staticmethod
    def FirstParameter(C: Geom2dAdaptor_Curve) -> float: ...
    @staticmethod
    def LastParameter(C: Geom2dAdaptor_Curve) -> float: ...
    @staticmethod
    def NbSamples(C: Geom2dAdaptor_Curve) -> int: ...
    @staticmethod
    def Value(C: Geom2dAdaptor_Curve, X: float) -> gp_Pnt2d: ...

class Geom2dGcc_FunctionTanCirCu(math_FunctionWithDerivative):
    def __init__(self, Circ: gp_Circ2d, Curv: Geom2dAdaptor_Curve) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Geom2dGcc_FunctionTanCuCu(math_FunctionSetWithDerivatives):
    @overload
    def __init__(
        self, Curv1: Geom2dAdaptor_Curve, Curv2: Geom2dAdaptor_Curve
    ) -> None: ...
    @overload
    def __init__(self, Circ1: gp_Circ2d, Curv2: Geom2dAdaptor_Curve) -> None: ...
    def Derivatives(self, X: math_Vector, Deriv: math_Matrix) -> bool: ...
    def InitDerivative(
        self,
        X: math_Vector,
        Point1: gp_Pnt2d,
        Point2: gp_Pnt2d,
        Tan1: gp_Vec2d,
        Tan2: gp_Vec2d,
        D21: gp_Vec2d,
        D22: gp_Vec2d,
    ) -> None: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, Deriv: math_Matrix) -> bool: ...

class Geom2dGcc_FunctionTanCuCuOnCu(math_FunctionSetWithDerivatives):
    @overload
    def __init__(
        self,
        C1: Geom2dAdaptor_Curve,
        C2: Geom2dAdaptor_Curve,
        OnCi: gp_Circ2d,
        Rad: float,
    ) -> None: ...
    @overload
    def __init__(
        self, C1: gp_Circ2d, C2: Geom2dAdaptor_Curve, OnCi: gp_Circ2d, Rad: float
    ) -> None: ...
    @overload
    def __init__(
        self, L1: gp_Lin2d, C2: Geom2dAdaptor_Curve, OnCi: gp_Circ2d, Rad: float
    ) -> None: ...
    @overload
    def __init__(
        self, C1: Geom2dAdaptor_Curve, P2: gp_Pnt2d, OnCi: gp_Circ2d, Rad: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        C1: Geom2dAdaptor_Curve,
        C2: Geom2dAdaptor_Curve,
        OnLi: gp_Lin2d,
        Rad: float,
    ) -> None: ...
    @overload
    def __init__(
        self, C1: gp_Circ2d, C2: Geom2dAdaptor_Curve, OnLi: gp_Lin2d, Rad: float
    ) -> None: ...
    @overload
    def __init__(
        self, L1: gp_Lin2d, C2: Geom2dAdaptor_Curve, OnLi: gp_Lin2d, Rad: float
    ) -> None: ...
    @overload
    def __init__(
        self, C1: Geom2dAdaptor_Curve, P2: gp_Pnt2d, OnLi: gp_Lin2d, Rad: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        C1: Geom2dAdaptor_Curve,
        C2: Geom2dAdaptor_Curve,
        OnCu: Geom2dAdaptor_Curve,
        Rad: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C1: gp_Circ2d,
        C2: Geom2dAdaptor_Curve,
        OnCu: Geom2dAdaptor_Curve,
        Rad: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        L1: gp_Lin2d,
        C2: Geom2dAdaptor_Curve,
        OnCu: Geom2dAdaptor_Curve,
        Rad: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        C1: Geom2dAdaptor_Curve,
        P1: gp_Pnt2d,
        OnCu: Geom2dAdaptor_Curve,
        Rad: float,
    ) -> None: ...
    def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
    def InitDerivative(
        self,
        X: math_Vector,
        Point1: gp_Pnt2d,
        Point2: gp_Pnt2d,
        Point3: gp_Pnt2d,
        Tan1: gp_Vec2d,
        Tan2: gp_Vec2d,
        Tan3: gp_Vec2d,
        D21: gp_Vec2d,
        D22: gp_Vec2d,
        D23: gp_Vec2d,
    ) -> None: ...
    def NbEquations(self) -> int: ...
    def NbVariables(self) -> int: ...
    def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
    def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class Geom2dGcc_FunctionTanCuPnt(math_FunctionWithDerivative):
    def __init__(self, C: Geom2dAdaptor_Curve, Point: gp_Pnt2d) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Geom2dGcc_FunctionTanObl(math_FunctionWithDerivative):
    def __init__(self, Curve: Geom2dAdaptor_Curve, Dir: gp_Dir2d) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

class Geom2dGcc_Lin2d2Tan:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Qualified2: Geom2dGcc_QualifiedCurve,
        Tolang: float,
    ) -> None: ...
    @overload
    def __init__(
        self, Qualified1: Geom2dGcc_QualifiedCurve, ThePoint: gp_Pnt2d, Tolang: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        Qualified2: Geom2dGcc_QualifiedCurve,
        Tolang: float,
        Param1: float,
        Param2: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        ThePoint: gp_Pnt2d,
        Tolang: float,
        Param1: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Lin2d: ...
    def WhichQualifier(self, Index: int) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Lin2d2TanIter:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        ThePoint: gp_Pnt2d,
        Param1: float,
        Tolang: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: GccEnt_QualifiedCirc,
        Qualified2: Geom2dGcc_QCurve,
        Param2: float,
        Tolang: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        Qualified2: Geom2dGcc_QCurve,
        Param1: float,
        Param2: float,
        Tolang: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def Tangency1(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def Tangency2(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self) -> gp_Lin2d: ...
    def WhichQualifier(self) -> Tuple[GccEnt_Position, GccEnt_Position]: ...

class Geom2dGcc_Lin2dTanObl:
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        TheLin: gp_Lin2d,
        TolAng: float,
        Angle: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Qualified1: Geom2dGcc_QualifiedCurve,
        TheLin: gp_Lin2d,
        TolAng: float,
        Param1: float,
        Angle: float,
    ) -> None: ...
    def Intersection2(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def IsDone(self) -> bool: ...
    def NbSolutions(self) -> int: ...
    def Tangency1(self, Index: int, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self, Index: int) -> gp_Lin2d: ...
    def WhichQualifier(self, Index: int) -> GccEnt_Position: ...

class Geom2dGcc_Lin2dTanOblIter:
    def __init__(
        self,
        Qualified1: Geom2dGcc_QCurve,
        TheLin: gp_Lin2d,
        Param1: float,
        TolAng: float,
        Angle: Optional[float] = 0,
    ) -> None: ...
    def Intersection2(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def IsDone(self) -> bool: ...
    def IsParallel2(self) -> bool: ...
    def Tangency1(self, PntSol: gp_Pnt2d) -> Tuple[float, float]: ...
    def ThisSolution(self) -> gp_Lin2d: ...
    def WhichQualifier(self) -> GccEnt_Position: ...

class Geom2dGcc_QCurve:
    def __init__(
        self, Curve: Geom2dAdaptor_Curve, Qualifier: GccEnt_Position
    ) -> None: ...
    def IsEnclosed(self) -> bool: ...
    def IsEnclosing(self) -> bool: ...
    def IsOutside(self) -> bool: ...
    def IsUnqualified(self) -> bool: ...
    def Qualified(self) -> Geom2dAdaptor_Curve: ...
    def Qualifier(self) -> GccEnt_Position: ...

class Geom2dGcc_QualifiedCurve:
    def __init__(
        self, Curve: Geom2dAdaptor_Curve, Qualifier: GccEnt_Position
    ) -> None: ...
    def IsEnclosed(self) -> bool: ...
    def IsEnclosing(self) -> bool: ...
    def IsOutside(self) -> bool: ...
    def IsUnqualified(self) -> bool: ...
    def Qualified(self) -> Geom2dAdaptor_Curve: ...
    def Qualifier(self) -> GccEnt_Position: ...

# classnotwrapped
class Geom2dGcc_FunctionTanCuCuCu: ...

# harray1 classes
# harray2 classes
# hsequence classes
