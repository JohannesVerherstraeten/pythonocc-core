from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRep import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.Geom import *
from OCC.Core.Geom2d import *

class BRepPrim_Direction(IntEnum):
    BRepPrim_XMin: int = ...
    BRepPrim_XMax: int = ...
    BRepPrim_YMin: int = ...
    BRepPrim_YMax: int = ...
    BRepPrim_ZMin: int = ...
    BRepPrim_ZMax: int = ...

BRepPrim_XMin = BRepPrim_Direction.BRepPrim_XMin
BRepPrim_XMax = BRepPrim_Direction.BRepPrim_XMax
BRepPrim_YMin = BRepPrim_Direction.BRepPrim_YMin
BRepPrim_YMax = BRepPrim_Direction.BRepPrim_YMax
BRepPrim_ZMin = BRepPrim_Direction.BRepPrim_ZMin
BRepPrim_ZMax = BRepPrim_Direction.BRepPrim_ZMax

class BRepPrim_Builder:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, B: BRep_Builder) -> None: ...
    @overload
    def AddEdgeVertex(
        self, E: TopoDS_Edge, V: TopoDS_Vertex, P: float, direct: bool
    ) -> None: ...
    @overload
    def AddEdgeVertex(
        self, E: TopoDS_Edge, V: TopoDS_Vertex, P1: float, P2: float
    ) -> None: ...
    def AddFaceWire(self, F: TopoDS_Face, W: TopoDS_Wire) -> None: ...
    def AddShellFace(self, Sh: TopoDS_Shell, F: TopoDS_Face) -> None: ...
    def AddWireEdge(self, W: TopoDS_Wire, E: TopoDS_Edge, direct: bool) -> None: ...
    def Builder(self) -> BRep_Builder: ...
    def CompleteEdge(self, E: TopoDS_Edge) -> None: ...
    def CompleteFace(self, F: TopoDS_Face) -> None: ...
    def CompleteShell(self, S: TopoDS_Shell) -> None: ...
    def CompleteWire(self, W: TopoDS_Wire) -> None: ...
    def MakeDegeneratedEdge(self, E: TopoDS_Edge) -> None: ...
    @overload
    def MakeEdge(self, E: TopoDS_Edge, L: gp_Lin) -> None: ...
    @overload
    def MakeEdge(self, E: TopoDS_Edge, C: gp_Circ) -> None: ...
    def MakeFace(self, F: TopoDS_Face, P: gp_Pln) -> None: ...
    def MakeShell(self, S: TopoDS_Shell) -> None: ...
    def MakeVertex(self, V: TopoDS_Vertex, P: gp_Pnt) -> None: ...
    def MakeWire(self, W: TopoDS_Wire) -> None: ...
    def ReverseFace(self, F: TopoDS_Face) -> None: ...
    @overload
    def SetPCurve(self, E: TopoDS_Edge, F: TopoDS_Face, L: gp_Lin2d) -> None: ...
    @overload
    def SetPCurve(
        self, E: TopoDS_Edge, F: TopoDS_Face, L1: gp_Lin2d, L2: gp_Lin2d
    ) -> None: ...
    @overload
    def SetPCurve(self, E: TopoDS_Edge, F: TopoDS_Face, C: gp_Circ2d) -> None: ...
    def SetParameters(
        self, E: TopoDS_Edge, V: TopoDS_Vertex, P1: float, P2: float
    ) -> None: ...

class BRepPrim_FaceBuilder:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, B: BRep_Builder, S: Geom_Surface) -> None: ...
    @overload
    def __init__(
        self,
        B: BRep_Builder,
        S: Geom_Surface,
        UMin: float,
        UMax: float,
        VMin: float,
        VMax: float,
    ) -> None: ...
    def Edge(self, I: int) -> TopoDS_Edge: ...
    def Face(self) -> TopoDS_Face: ...
    @overload
    def Init(self, B: BRep_Builder, S: Geom_Surface) -> None: ...
    @overload
    def Init(
        self,
        B: BRep_Builder,
        S: Geom_Surface,
        UMin: float,
        UMax: float,
        VMin: float,
        VMax: float,
    ) -> None: ...
    def Vertex(self, I: int) -> TopoDS_Vertex: ...

class BRepPrim_GWedge:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, B: BRepPrim_Builder, Axes: gp_Ax2, dx: float, dy: float, dz: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        B: BRepPrim_Builder,
        Axes: gp_Ax2,
        dx: float,
        dy: float,
        dz: float,
        ltx: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        B: BRepPrim_Builder,
        Axes: gp_Ax2,
        xmin: float,
        ymin: float,
        zmin: float,
        z2min: float,
        x2min: float,
        xmax: float,
        ymax: float,
        zmax: float,
        z2max: float,
        x2max: float,
    ) -> None: ...
    def Axes(self) -> gp_Ax2: ...
    def Close(self, d1: BRepPrim_Direction) -> None: ...
    def Edge(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction) -> TopoDS_Edge: ...
    def Face(self, d1: BRepPrim_Direction) -> TopoDS_Face: ...
    def GetX2Max(self) -> float: ...
    def GetX2Min(self) -> float: ...
    def GetXMax(self) -> float: ...
    def GetXMin(self) -> float: ...
    def GetYMax(self) -> float: ...
    def GetYMin(self) -> float: ...
    def GetZ2Max(self) -> float: ...
    def GetZ2Min(self) -> float: ...
    def GetZMax(self) -> float: ...
    def GetZMin(self) -> float: ...
    def HasEdge(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction) -> bool: ...
    def HasFace(self, d1: BRepPrim_Direction) -> bool: ...
    def HasVertex(
        self, d1: BRepPrim_Direction, d2: BRepPrim_Direction, d3: BRepPrim_Direction
    ) -> bool: ...
    def HasWire(self, d1: BRepPrim_Direction) -> bool: ...
    def IsDegeneratedShape(self) -> bool: ...
    def IsInfinite(self, d1: BRepPrim_Direction) -> bool: ...
    def Line(self, d1: BRepPrim_Direction, d2: BRepPrim_Direction) -> gp_Lin: ...
    def Open(self, d1: BRepPrim_Direction) -> None: ...
    def Plane(self, d1: BRepPrim_Direction) -> gp_Pln: ...
    def Point(
        self, d1: BRepPrim_Direction, d2: BRepPrim_Direction, d3: BRepPrim_Direction
    ) -> gp_Pnt: ...
    def Shell(self) -> TopoDS_Shell: ...
    def Vertex(
        self, d1: BRepPrim_Direction, d2: BRepPrim_Direction, d3: BRepPrim_Direction
    ) -> TopoDS_Vertex: ...
    def Wire(self, d1: BRepPrim_Direction) -> TopoDS_Wire: ...

class BRepPrim_OneAxis:
    @overload
    def Angle(self) -> float: ...
    @overload
    def Angle(self, A: float) -> None: ...
    @overload
    def Axes(self) -> gp_Ax2: ...
    @overload
    def Axes(self, A: gp_Ax2) -> None: ...
    def AxisBottomVertex(self) -> TopoDS_Vertex: ...
    def AxisEdge(self) -> TopoDS_Edge: ...
    def AxisEndWire(self) -> TopoDS_Wire: ...
    def AxisStartWire(self) -> TopoDS_Wire: ...
    def AxisTopVertex(self) -> TopoDS_Vertex: ...
    def BottomEdge(self) -> TopoDS_Edge: ...
    def BottomEndVertex(self) -> TopoDS_Vertex: ...
    def BottomFace(self) -> TopoDS_Face: ...
    def BottomStartVertex(self) -> TopoDS_Vertex: ...
    def BottomWire(self) -> TopoDS_Wire: ...
    def EndBottomEdge(self) -> TopoDS_Edge: ...
    def EndEdge(self) -> TopoDS_Edge: ...
    def EndFace(self) -> TopoDS_Face: ...
    def EndTopEdge(self) -> TopoDS_Edge: ...
    def EndWire(self) -> TopoDS_Wire: ...
    def HasBottom(self) -> bool: ...
    def HasSides(self) -> bool: ...
    def HasTop(self) -> bool: ...
    def LateralEndWire(self) -> TopoDS_Wire: ...
    def LateralFace(self) -> TopoDS_Face: ...
    def LateralStartWire(self) -> TopoDS_Wire: ...
    def LateralWire(self) -> TopoDS_Wire: ...
    def MakeEmptyLateralFace(self) -> TopoDS_Face: ...
    def MakeEmptyMeridianEdge(self, Ang: float) -> TopoDS_Edge: ...
    def MeridianClosed(self) -> bool: ...
    def MeridianOnAxis(self, V: float) -> bool: ...
    def MeridianValue(self, V: float) -> gp_Pnt2d: ...
    def SetMeridianOffset(self, MeridianOffset: Optional[float] = 0) -> None: ...
    def SetMeridianPCurve(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
    def Shell(self) -> TopoDS_Shell: ...
    def StartBottomEdge(self) -> TopoDS_Edge: ...
    def StartEdge(self) -> TopoDS_Edge: ...
    def StartFace(self) -> TopoDS_Face: ...
    def StartTopEdge(self) -> TopoDS_Edge: ...
    def StartWire(self) -> TopoDS_Wire: ...
    def TopEdge(self) -> TopoDS_Edge: ...
    def TopEndVertex(self) -> TopoDS_Vertex: ...
    def TopFace(self) -> TopoDS_Face: ...
    def TopStartVertex(self) -> TopoDS_Vertex: ...
    def TopWire(self) -> TopoDS_Wire: ...
    @overload
    def VMax(self) -> float: ...
    @overload
    def VMax(self, V: float) -> None: ...
    def VMaxInfinite(self) -> bool: ...
    @overload
    def VMin(self) -> float: ...
    @overload
    def VMin(self, V: float) -> None: ...
    def VMinInfinite(self) -> bool: ...

class BRepPrim_Revolution(BRepPrim_OneAxis):
    def __init__(
        self, A: gp_Ax2, VMin: float, VMax: float, M: Geom_Curve, PM: Geom2d_Curve
    ) -> None: ...
    def MakeEmptyLateralFace(self) -> TopoDS_Face: ...
    def MakeEmptyMeridianEdge(self, Ang: float) -> TopoDS_Edge: ...
    def MeridianValue(self, V: float) -> gp_Pnt2d: ...
    def SetMeridianPCurve(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...

class BRepPrim_Wedge(BRepPrim_GWedge):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, Axes: gp_Ax2, dx: float, dy: float, dz: float) -> None: ...
    @overload
    def __init__(
        self, Axes: gp_Ax2, dx: float, dy: float, dz: float, ltx: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        Axes: gp_Ax2,
        xmin: float,
        ymin: float,
        zmin: float,
        z2min: float,
        x2min: float,
        xmax: float,
        ymax: float,
        zmax: float,
        z2max: float,
        x2max: float,
    ) -> None: ...

class BRepPrim_Cone(BRepPrim_Revolution):
    @overload
    def __init__(
        self, Angle: float, Position: gp_Ax2, Height: float, Radius: Optional[float] = 0
    ) -> None: ...
    @overload
    def __init__(self, Angle: float) -> None: ...
    @overload
    def __init__(self, Angle: float, Apex: gp_Pnt) -> None: ...
    @overload
    def __init__(self, Angle: float, Axes: gp_Ax2) -> None: ...
    @overload
    def __init__(self, R1: float, R2: float, H: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, R1: float, R2: float, H: float) -> None: ...
    @overload
    def __init__(self, Axes: gp_Ax2, R1: float, R2: float, H: float) -> None: ...
    def MakeEmptyLateralFace(self) -> TopoDS_Face: ...

class BRepPrim_Cylinder(BRepPrim_Revolution):
    @overload
    def __init__(self, Position: gp_Ax2, Radius: float, Height: float) -> None: ...
    @overload
    def __init__(self, Radius: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, Radius: float) -> None: ...
    @overload
    def __init__(self, Axes: gp_Ax2, Radius: float) -> None: ...
    @overload
    def __init__(self, R: float, H: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, R: float, H: float) -> None: ...
    def MakeEmptyLateralFace(self) -> TopoDS_Face: ...

class BRepPrim_Sphere(BRepPrim_Revolution):
    @overload
    def __init__(self, Radius: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, Radius: float) -> None: ...
    @overload
    def __init__(self, Axes: gp_Ax2, Radius: float) -> None: ...
    def MakeEmptyLateralFace(self) -> TopoDS_Face: ...

class BRepPrim_Torus(BRepPrim_Revolution):
    @overload
    def __init__(self, Position: gp_Ax2, Major: float, Minor: float) -> None: ...
    @overload
    def __init__(self, Major: float, Minor: float) -> None: ...
    @overload
    def __init__(self, Center: gp_Pnt, Major: float, Minor: float) -> None: ...
    def MakeEmptyLateralFace(self) -> TopoDS_Face: ...

# harray1 classes
# harray2 classes
# hsequence classes
