from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColgp import *
from OCC.Core.gp import *
from OCC.Core.math import *
from OCC.Core.TColStd import *

class CSLib_DerivativeStatus(IntEnum):
    CSLib_Done: int = ...
    CSLib_D1uIsNull: int = ...
    CSLib_D1vIsNull: int = ...
    CSLib_D1IsNull: int = ...
    CSLib_D1uD1vRatioIsNull: int = ...
    CSLib_D1vD1uRatioIsNull: int = ...
    CSLib_D1uIsParallelD1v: int = ...

CSLib_Done = CSLib_DerivativeStatus.CSLib_Done
CSLib_D1uIsNull = CSLib_DerivativeStatus.CSLib_D1uIsNull
CSLib_D1vIsNull = CSLib_DerivativeStatus.CSLib_D1vIsNull
CSLib_D1IsNull = CSLib_DerivativeStatus.CSLib_D1IsNull
CSLib_D1uD1vRatioIsNull = CSLib_DerivativeStatus.CSLib_D1uD1vRatioIsNull
CSLib_D1vD1uRatioIsNull = CSLib_DerivativeStatus.CSLib_D1vD1uRatioIsNull
CSLib_D1uIsParallelD1v = CSLib_DerivativeStatus.CSLib_D1uIsParallelD1v

class CSLib_NormalStatus(IntEnum):
    CSLib_Singular: int = ...
    CSLib_Defined: int = ...
    CSLib_InfinityOfSolutions: int = ...
    CSLib_D1NuIsNull: int = ...
    CSLib_D1NvIsNull: int = ...
    CSLib_D1NIsNull: int = ...
    CSLib_D1NuNvRatioIsNull: int = ...
    CSLib_D1NvNuRatioIsNull: int = ...
    CSLib_D1NuIsParallelD1Nv: int = ...

CSLib_Singular = CSLib_NormalStatus.CSLib_Singular
CSLib_Defined = CSLib_NormalStatus.CSLib_Defined
CSLib_InfinityOfSolutions = CSLib_NormalStatus.CSLib_InfinityOfSolutions
CSLib_D1NuIsNull = CSLib_NormalStatus.CSLib_D1NuIsNull
CSLib_D1NvIsNull = CSLib_NormalStatus.CSLib_D1NvIsNull
CSLib_D1NIsNull = CSLib_NormalStatus.CSLib_D1NIsNull
CSLib_D1NuNvRatioIsNull = CSLib_NormalStatus.CSLib_D1NuNvRatioIsNull
CSLib_D1NvNuRatioIsNull = CSLib_NormalStatus.CSLib_D1NvNuRatioIsNull
CSLib_D1NuIsParallelD1Nv = CSLib_NormalStatus.CSLib_D1NuIsParallelD1Nv

class cslib:
    @overload
    @staticmethod
    def DNNUV(Nu: int, Nv: int, DerSurf: TColgp_Array2OfVec) -> gp_Vec: ...
    @overload
    @staticmethod
    def DNNUV(
        Nu: int, Nv: int, DerSurf1: TColgp_Array2OfVec, DerSurf2: TColgp_Array2OfVec
    ) -> gp_Vec: ...
    @staticmethod
    def DNNormal(
        Nu: int,
        Nv: int,
        DerNUV: TColgp_Array2OfVec,
        Iduref: Optional[int] = 0,
        Idvref: Optional[int] = 0,
    ) -> gp_Vec: ...
    @overload
    @staticmethod
    def Normal(
        D1U: gp_Vec, D1V: gp_Vec, SinTol: float, Normal: gp_Dir
    ) -> CSLib_DerivativeStatus: ...
    @overload
    @staticmethod
    def Normal(
        D1U: gp_Vec,
        D1V: gp_Vec,
        D2U: gp_Vec,
        D2V: gp_Vec,
        D2UV: gp_Vec,
        SinTol: float,
        Normal: gp_Dir,
    ) -> Tuple[bool, CSLib_NormalStatus]: ...
    @overload
    @staticmethod
    def Normal(
        D1U: gp_Vec, D1V: gp_Vec, MagTol: float, Normal: gp_Dir
    ) -> CSLib_NormalStatus: ...
    @overload
    @staticmethod
    def Normal(
        MaxOrder: int,
        DerNUV: TColgp_Array2OfVec,
        MagTol: float,
        U: float,
        V: float,
        Umin: float,
        Umax: float,
        Vmin: float,
        Vmax: float,
        Normal: gp_Dir,
    ) -> Tuple[CSLib_NormalStatus, int, int]: ...

class CSLib_Class2d:
    @overload
    def __init__(
        self,
        thePnts2d: TColgp_Array1OfPnt2d,
        theTolU: float,
        theTolV: float,
        theUMin: float,
        theVMin: float,
        theUMax: float,
        theVMax: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        thePnts2d: TColgp_SequenceOfPnt2d,
        theTolU: float,
        theTolV: float,
        theUMin: float,
        theVMin: float,
        theUMax: float,
        theVMax: float,
    ) -> None: ...
    def InternalSiDans(self, X: float, Y: float) -> int: ...
    def InternalSiDansOuOn(self, X: float, Y: float) -> int: ...
    def SiDans(self, P: gp_Pnt2d) -> int: ...
    def SiDans_OnMode(self, P: gp_Pnt2d, Tol: float) -> int: ...

class CSLib_NormalPolyDef(math_FunctionWithDerivative):
    def __init__(self, k0: int, li: TColStd_Array1OfReal) -> None: ...
    def Derivative(self, X: float) -> Tuple[bool, float]: ...
    def Value(self, X: float) -> Tuple[bool, float]: ...
    def Values(self, X: float) -> Tuple[bool, float, float]: ...

# harray1 classes
# harray2 classes
# hsequence classes
