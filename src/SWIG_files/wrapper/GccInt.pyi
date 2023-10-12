from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *

class GccInt_IType(IntEnum):
    GccInt_Lin: int = ...
    GccInt_Cir: int = ...
    GccInt_Ell: int = ...
    GccInt_Par: int = ...
    GccInt_Hpr: int = ...
    GccInt_Pnt: int = ...

GccInt_Lin = GccInt_IType.GccInt_Lin
GccInt_Cir = GccInt_IType.GccInt_Cir
GccInt_Ell = GccInt_IType.GccInt_Ell
GccInt_Par = GccInt_IType.GccInt_Par
GccInt_Hpr = GccInt_IType.GccInt_Hpr
GccInt_Pnt = GccInt_IType.GccInt_Pnt

class GccInt_Bisec(Standard_Transient):
    def ArcType(self) -> GccInt_IType: ...
    def Circle(self) -> gp_Circ2d: ...
    def Ellipse(self) -> gp_Elips2d: ...
    def Hyperbola(self) -> gp_Hypr2d: ...
    def Line(self) -> gp_Lin2d: ...
    def Parabola(self) -> gp_Parab2d: ...
    def Point(self) -> gp_Pnt2d: ...

class GccInt_BCirc(GccInt_Bisec):
    def __init__(self, Circ: gp_Circ2d) -> None: ...
    def ArcType(self) -> GccInt_IType: ...
    def Circle(self) -> gp_Circ2d: ...

class GccInt_BElips(GccInt_Bisec):
    def __init__(self, Ellipse: gp_Elips2d) -> None: ...
    def ArcType(self) -> GccInt_IType: ...
    def Ellipse(self) -> gp_Elips2d: ...

class GccInt_BHyper(GccInt_Bisec):
    def __init__(self, Hyper: gp_Hypr2d) -> None: ...
    def ArcType(self) -> GccInt_IType: ...
    def Hyperbola(self) -> gp_Hypr2d: ...

class GccInt_BLine(GccInt_Bisec):
    def __init__(self, Line: gp_Lin2d) -> None: ...
    def ArcType(self) -> GccInt_IType: ...
    def Line(self) -> gp_Lin2d: ...

class GccInt_BParab(GccInt_Bisec):
    def __init__(self, Parab: gp_Parab2d) -> None: ...
    def ArcType(self) -> GccInt_IType: ...
    def Parabola(self) -> gp_Parab2d: ...

class GccInt_BPoint(GccInt_Bisec):
    def __init__(self, Point: gp_Pnt2d) -> None: ...
    def ArcType(self) -> GccInt_IType: ...
    def Point(self) -> gp_Pnt2d: ...

# harray1 classes
# harray2 classes
# hsequence classes
