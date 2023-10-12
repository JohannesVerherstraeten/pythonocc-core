from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *

class elslib:
    @staticmethod
    def ConeD0(
        U: float, V: float, Pos: gp_Ax3, Radius: float, SAngle: float, P: gp_Pnt
    ) -> None: ...
    @staticmethod
    def ConeD1(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        SAngle: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def ConeD2(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        SAngle: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def ConeD3(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        SAngle: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def ConeDN(
        U: float, V: float, Pos: gp_Ax3, Radius: float, SAngle: float, Nu: int, Nv: int
    ) -> gp_Vec: ...
    @staticmethod
    def ConeParameters(
        Pos: gp_Ax3, Radius: float, SAngle: float, P: gp_Pnt
    ) -> Tuple[float, float]: ...
    @staticmethod
    def ConeUIso(Pos: gp_Ax3, Radius: float, SAngle: float, U: float) -> gp_Lin: ...
    @staticmethod
    def ConeVIso(Pos: gp_Ax3, Radius: float, SAngle: float, V: float) -> gp_Circ: ...
    @staticmethod
    def ConeValue(
        U: float, V: float, Pos: gp_Ax3, Radius: float, SAngle: float
    ) -> gp_Pnt: ...
    @staticmethod
    def CylinderD0(
        U: float, V: float, Pos: gp_Ax3, Radius: float, P: gp_Pnt
    ) -> None: ...
    @staticmethod
    def CylinderD1(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def CylinderD2(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def CylinderD3(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def CylinderDN(
        U: float, V: float, Pos: gp_Ax3, Radius: float, Nu: int, Nv: int
    ) -> gp_Vec: ...
    @staticmethod
    def CylinderParameters(
        Pos: gp_Ax3, Radius: float, P: gp_Pnt
    ) -> Tuple[float, float]: ...
    @staticmethod
    def CylinderUIso(Pos: gp_Ax3, Radius: float, U: float) -> gp_Lin: ...
    @staticmethod
    def CylinderVIso(Pos: gp_Ax3, Radius: float, V: float) -> gp_Circ: ...
    @staticmethod
    def CylinderValue(U: float, V: float, Pos: gp_Ax3, Radius: float) -> gp_Pnt: ...
    @overload
    @staticmethod
    def D0(U: float, V: float, Pl: gp_Pln, P: gp_Pnt) -> None: ...
    @overload
    @staticmethod
    def D0(U: float, V: float, C: gp_Cone, P: gp_Pnt) -> None: ...
    @overload
    @staticmethod
    def D0(U: float, V: float, C: gp_Cylinder, P: gp_Pnt) -> None: ...
    @overload
    @staticmethod
    def D0(U: float, V: float, S: gp_Sphere, P: gp_Pnt) -> None: ...
    @overload
    @staticmethod
    def D0(U: float, V: float, T: gp_Torus, P: gp_Pnt) -> None: ...
    @overload
    @staticmethod
    def D1(
        U: float, V: float, Pl: gp_Pln, P: gp_Pnt, Vu: gp_Vec, Vv: gp_Vec
    ) -> None: ...
    @overload
    @staticmethod
    def D1(
        U: float, V: float, C: gp_Cone, P: gp_Pnt, Vu: gp_Vec, Vv: gp_Vec
    ) -> None: ...
    @overload
    @staticmethod
    def D1(
        U: float, V: float, C: gp_Cylinder, P: gp_Pnt, Vu: gp_Vec, Vv: gp_Vec
    ) -> None: ...
    @overload
    @staticmethod
    def D1(
        U: float, V: float, S: gp_Sphere, P: gp_Pnt, Vu: gp_Vec, Vv: gp_Vec
    ) -> None: ...
    @overload
    @staticmethod
    def D1(
        U: float, V: float, T: gp_Torus, P: gp_Pnt, Vu: gp_Vec, Vv: gp_Vec
    ) -> None: ...
    @overload
    @staticmethod
    def D2(
        U: float,
        V: float,
        C: gp_Cone,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D2(
        U: float,
        V: float,
        C: gp_Cylinder,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D2(
        U: float,
        V: float,
        S: gp_Sphere,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D2(
        U: float,
        V: float,
        T: gp_Torus,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D3(
        U: float,
        V: float,
        C: gp_Cone,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D3(
        U: float,
        V: float,
        C: gp_Cylinder,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D3(
        U: float,
        V: float,
        S: gp_Sphere,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def D3(
        U: float,
        V: float,
        T: gp_Torus,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @overload
    @staticmethod
    def DN(U: float, V: float, Pl: gp_Pln, Nu: int, Nv: int) -> gp_Vec: ...
    @overload
    @staticmethod
    def DN(U: float, V: float, C: gp_Cone, Nu: int, Nv: int) -> gp_Vec: ...
    @overload
    @staticmethod
    def DN(U: float, V: float, C: gp_Cylinder, Nu: int, Nv: int) -> gp_Vec: ...
    @overload
    @staticmethod
    def DN(U: float, V: float, S: gp_Sphere, Nu: int, Nv: int) -> gp_Vec: ...
    @overload
    @staticmethod
    def DN(U: float, V: float, T: gp_Torus, Nu: int, Nv: int) -> gp_Vec: ...
    @overload
    @staticmethod
    def Parameters(Pl: gp_Pln, P: gp_Pnt) -> Tuple[float, float]: ...
    @overload
    @staticmethod
    def Parameters(C: gp_Cylinder, P: gp_Pnt) -> Tuple[float, float]: ...
    @overload
    @staticmethod
    def Parameters(C: gp_Cone, P: gp_Pnt) -> Tuple[float, float]: ...
    @overload
    @staticmethod
    def Parameters(S: gp_Sphere, P: gp_Pnt) -> Tuple[float, float]: ...
    @overload
    @staticmethod
    def Parameters(T: gp_Torus, P: gp_Pnt) -> Tuple[float, float]: ...
    @staticmethod
    def PlaneD0(U: float, V: float, Pos: gp_Ax3, P: gp_Pnt) -> None: ...
    @staticmethod
    def PlaneD1(
        U: float, V: float, Pos: gp_Ax3, P: gp_Pnt, Vu: gp_Vec, Vv: gp_Vec
    ) -> None: ...
    @staticmethod
    def PlaneDN(U: float, V: float, Pos: gp_Ax3, Nu: int, Nv: int) -> gp_Vec: ...
    @staticmethod
    def PlaneParameters(Pos: gp_Ax3, P: gp_Pnt) -> Tuple[float, float]: ...
    @staticmethod
    def PlaneUIso(Pos: gp_Ax3, U: float) -> gp_Lin: ...
    @staticmethod
    def PlaneVIso(Pos: gp_Ax3, V: float) -> gp_Lin: ...
    @staticmethod
    def PlaneValue(U: float, V: float, Pos: gp_Ax3) -> gp_Pnt: ...
    @staticmethod
    def SphereD0(U: float, V: float, Pos: gp_Ax3, Radius: float, P: gp_Pnt) -> None: ...
    @staticmethod
    def SphereD1(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def SphereD2(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def SphereD3(
        U: float,
        V: float,
        Pos: gp_Ax3,
        Radius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def SphereDN(
        U: float, V: float, Pos: gp_Ax3, Radius: float, Nu: int, Nv: int
    ) -> gp_Vec: ...
    @staticmethod
    def SphereParameters(
        Pos: gp_Ax3, Radius: float, P: gp_Pnt
    ) -> Tuple[float, float]: ...
    @staticmethod
    def SphereUIso(Pos: gp_Ax3, Radius: float, U: float) -> gp_Circ: ...
    @staticmethod
    def SphereVIso(Pos: gp_Ax3, Radius: float, V: float) -> gp_Circ: ...
    @staticmethod
    def SphereValue(U: float, V: float, Pos: gp_Ax3, Radius: float) -> gp_Pnt: ...
    @staticmethod
    def TorusD0(
        U: float,
        V: float,
        Pos: gp_Ax3,
        MajorRadius: float,
        MinorRadius: float,
        P: gp_Pnt,
    ) -> None: ...
    @staticmethod
    def TorusD1(
        U: float,
        V: float,
        Pos: gp_Ax3,
        MajorRadius: float,
        MinorRadius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def TorusD2(
        U: float,
        V: float,
        Pos: gp_Ax3,
        MajorRadius: float,
        MinorRadius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def TorusD3(
        U: float,
        V: float,
        Pos: gp_Ax3,
        MajorRadius: float,
        MinorRadius: float,
        P: gp_Pnt,
        Vu: gp_Vec,
        Vv: gp_Vec,
        Vuu: gp_Vec,
        Vvv: gp_Vec,
        Vuv: gp_Vec,
        Vuuu: gp_Vec,
        Vvvv: gp_Vec,
        Vuuv: gp_Vec,
        Vuvv: gp_Vec,
    ) -> None: ...
    @staticmethod
    def TorusDN(
        U: float,
        V: float,
        Pos: gp_Ax3,
        MajorRadius: float,
        MinorRadius: float,
        Nu: int,
        Nv: int,
    ) -> gp_Vec: ...
    @staticmethod
    def TorusParameters(
        Pos: gp_Ax3, MajorRadius: float, MinorRadius: float, P: gp_Pnt
    ) -> Tuple[float, float]: ...
    @staticmethod
    def TorusUIso(
        Pos: gp_Ax3, MajorRadius: float, MinorRadius: float, U: float
    ) -> gp_Circ: ...
    @staticmethod
    def TorusVIso(
        Pos: gp_Ax3, MajorRadius: float, MinorRadius: float, V: float
    ) -> gp_Circ: ...
    @staticmethod
    def TorusValue(
        U: float, V: float, Pos: gp_Ax3, MajorRadius: float, MinorRadius: float
    ) -> gp_Pnt: ...
    @overload
    @staticmethod
    def Value(U: float, V: float, Pl: gp_Pln) -> gp_Pnt: ...
    @overload
    @staticmethod
    def Value(U: float, V: float, C: gp_Cone) -> gp_Pnt: ...
    @overload
    @staticmethod
    def Value(U: float, V: float, C: gp_Cylinder) -> gp_Pnt: ...
    @overload
    @staticmethod
    def Value(U: float, V: float, S: gp_Sphere) -> gp_Pnt: ...
    @overload
    @staticmethod
    def Value(U: float, V: float, T: gp_Torus) -> gp_Pnt: ...

# harray1 classes
# harray2 classes
# hsequence classes
