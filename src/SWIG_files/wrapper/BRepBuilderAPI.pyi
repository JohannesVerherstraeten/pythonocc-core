from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.BRepTools import *
from OCC.Core.Message import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.Geom2d import *
from OCC.Core.Poly import *

# the following typedef cannot be wrapped as is
BRepBuilderAPI_BndBoxTree = NewType("BRepBuilderAPI_BndBoxTree", Any)
# the following typedef cannot be wrapped as is
BRepBuilderAPI_CellFilter = NewType("BRepBuilderAPI_CellFilter", Any)
# the following typedef cannot be wrapped as is
VectorOfPoint = NewType("VectorOfPoint", Any)

class BRepBuilderAPI_EdgeError(IntEnum):
    BRepBuilderAPI_EdgeDone: int = ...
    BRepBuilderAPI_PointProjectionFailed: int = ...
    BRepBuilderAPI_ParameterOutOfRange: int = ...
    BRepBuilderAPI_DifferentPointsOnClosedCurve: int = ...
    BRepBuilderAPI_PointWithInfiniteParameter: int = ...
    BRepBuilderAPI_DifferentsPointAndParameter: int = ...
    BRepBuilderAPI_LineThroughIdenticPoints: int = ...

BRepBuilderAPI_EdgeDone = BRepBuilderAPI_EdgeError.BRepBuilderAPI_EdgeDone
BRepBuilderAPI_PointProjectionFailed = (
    BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointProjectionFailed
)
BRepBuilderAPI_ParameterOutOfRange = (
    BRepBuilderAPI_EdgeError.BRepBuilderAPI_ParameterOutOfRange
)
BRepBuilderAPI_DifferentPointsOnClosedCurve = (
    BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentPointsOnClosedCurve
)
BRepBuilderAPI_PointWithInfiniteParameter = (
    BRepBuilderAPI_EdgeError.BRepBuilderAPI_PointWithInfiniteParameter
)
BRepBuilderAPI_DifferentsPointAndParameter = (
    BRepBuilderAPI_EdgeError.BRepBuilderAPI_DifferentsPointAndParameter
)
BRepBuilderAPI_LineThroughIdenticPoints = (
    BRepBuilderAPI_EdgeError.BRepBuilderAPI_LineThroughIdenticPoints
)

class BRepBuilderAPI_FaceError(IntEnum):
    BRepBuilderAPI_FaceDone: int = ...
    BRepBuilderAPI_NoFace: int = ...
    BRepBuilderAPI_NotPlanar: int = ...
    BRepBuilderAPI_CurveProjectionFailed: int = ...
    BRepBuilderAPI_ParametersOutOfRange: int = ...

BRepBuilderAPI_FaceDone = BRepBuilderAPI_FaceError.BRepBuilderAPI_FaceDone
BRepBuilderAPI_NoFace = BRepBuilderAPI_FaceError.BRepBuilderAPI_NoFace
BRepBuilderAPI_NotPlanar = BRepBuilderAPI_FaceError.BRepBuilderAPI_NotPlanar
BRepBuilderAPI_CurveProjectionFailed = (
    BRepBuilderAPI_FaceError.BRepBuilderAPI_CurveProjectionFailed
)
BRepBuilderAPI_ParametersOutOfRange = (
    BRepBuilderAPI_FaceError.BRepBuilderAPI_ParametersOutOfRange
)

class BRepBuilderAPI_PipeError(IntEnum):
    BRepBuilderAPI_PipeDone: int = ...
    BRepBuilderAPI_PipeNotDone: int = ...
    BRepBuilderAPI_PlaneNotIntersectGuide: int = ...
    BRepBuilderAPI_ImpossibleContact: int = ...

BRepBuilderAPI_PipeDone = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeDone
BRepBuilderAPI_PipeNotDone = BRepBuilderAPI_PipeError.BRepBuilderAPI_PipeNotDone
BRepBuilderAPI_PlaneNotIntersectGuide = (
    BRepBuilderAPI_PipeError.BRepBuilderAPI_PlaneNotIntersectGuide
)
BRepBuilderAPI_ImpossibleContact = (
    BRepBuilderAPI_PipeError.BRepBuilderAPI_ImpossibleContact
)

class BRepBuilderAPI_ShapeModification(IntEnum):
    BRepBuilderAPI_Preserved: int = ...
    BRepBuilderAPI_Deleted: int = ...
    BRepBuilderAPI_Trimmed: int = ...
    BRepBuilderAPI_Merged: int = ...
    BRepBuilderAPI_BoundaryModified: int = ...

BRepBuilderAPI_Preserved = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Preserved
BRepBuilderAPI_Deleted = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Deleted
BRepBuilderAPI_Trimmed = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Trimmed
BRepBuilderAPI_Merged = BRepBuilderAPI_ShapeModification.BRepBuilderAPI_Merged
BRepBuilderAPI_BoundaryModified = (
    BRepBuilderAPI_ShapeModification.BRepBuilderAPI_BoundaryModified
)

class BRepBuilderAPI_ShellError(IntEnum):
    BRepBuilderAPI_ShellDone: int = ...
    BRepBuilderAPI_EmptyShell: int = ...
    BRepBuilderAPI_DisconnectedShell: int = ...
    BRepBuilderAPI_ShellParametersOutOfRange: int = ...

BRepBuilderAPI_ShellDone = BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellDone
BRepBuilderAPI_EmptyShell = BRepBuilderAPI_ShellError.BRepBuilderAPI_EmptyShell
BRepBuilderAPI_DisconnectedShell = (
    BRepBuilderAPI_ShellError.BRepBuilderAPI_DisconnectedShell
)
BRepBuilderAPI_ShellParametersOutOfRange = (
    BRepBuilderAPI_ShellError.BRepBuilderAPI_ShellParametersOutOfRange
)

class BRepBuilderAPI_TransitionMode(IntEnum):
    BRepBuilderAPI_Transformed: int = ...
    BRepBuilderAPI_RightCorner: int = ...
    BRepBuilderAPI_RoundCorner: int = ...

BRepBuilderAPI_Transformed = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_Transformed
BRepBuilderAPI_RightCorner = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RightCorner
BRepBuilderAPI_RoundCorner = BRepBuilderAPI_TransitionMode.BRepBuilderAPI_RoundCorner

class BRepBuilderAPI_WireError(IntEnum):
    BRepBuilderAPI_WireDone: int = ...
    BRepBuilderAPI_EmptyWire: int = ...
    BRepBuilderAPI_DisconnectedWire: int = ...
    BRepBuilderAPI_NonManifoldWire: int = ...

BRepBuilderAPI_WireDone = BRepBuilderAPI_WireError.BRepBuilderAPI_WireDone
BRepBuilderAPI_EmptyWire = BRepBuilderAPI_WireError.BRepBuilderAPI_EmptyWire
BRepBuilderAPI_DisconnectedWire = (
    BRepBuilderAPI_WireError.BRepBuilderAPI_DisconnectedWire
)
BRepBuilderAPI_NonManifoldWire = BRepBuilderAPI_WireError.BRepBuilderAPI_NonManifoldWire

class brepbuilderapi:
    @overload
    @staticmethod
    def Plane(P: Geom_Plane) -> None: ...
    @overload
    @staticmethod
    def Plane() -> Geom_Plane: ...
    @overload
    @staticmethod
    def Precision(P: float) -> None: ...
    @overload
    @staticmethod
    def Precision() -> float: ...

class BRepBuilderAPI_Collect:
    def __init__(self) -> None: ...
    def Add(self, SI: TopoDS_Shape, MKS: BRepBuilderAPI_MakeShape) -> None: ...
    def AddGenerated(self, S: TopoDS_Shape, Gen: TopoDS_Shape) -> None: ...
    def AddModif(self, S: TopoDS_Shape, Mod: TopoDS_Shape) -> None: ...
    def Filter(self, SF: TopoDS_Shape) -> None: ...
    def Generated(self) -> TopTools_DataMapOfShapeListOfShape: ...
    def Modification(self) -> TopTools_DataMapOfShapeListOfShape: ...

class BRepBuilderAPI_Command:
    def Check(self) -> None: ...
    def IsDone(self) -> bool: ...

class BRepBuilderAPI_FastSewing(Standard_Transient):
    def __init__(self, theTolerance: Optional[float] = 1.0e-06) -> None: ...
    @overload
    def Add(self, theShape: TopoDS_Shape) -> bool: ...
    @overload
    def Add(self, theSurface: Geom_Surface) -> bool: ...
    def GetResult(self) -> TopoDS_Shape: ...
    def GetTolerance(self) -> float: ...
    def Perform(self) -> None: ...
    def SetTolerance(self, theToler: float) -> None: ...

class BRepBuilderAPI_FindPlane:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, Tol: Optional[float] = -1) -> None: ...
    def Found(self) -> bool: ...
    def Init(self, S: TopoDS_Shape, Tol: Optional[float] = -1) -> None: ...
    def Plane(self) -> Geom_Plane: ...

class BRepBuilderAPI_Sewing(Standard_Transient):
    def __init__(
        self,
        tolerance: Optional[float] = 1.0e-06,
        option1: Optional[bool] = True,
        option2: Optional[bool] = True,
        option3: Optional[bool] = True,
        option4: Optional[bool] = False,
    ) -> None: ...
    def Add(self, shape: TopoDS_Shape) -> None: ...
    def ContigousEdge(self, index: int) -> TopoDS_Edge: ...
    def ContigousEdgeCouple(self, index: int) -> TopTools_ListOfShape: ...
    def DegeneratedShape(self, index: int) -> TopoDS_Shape: ...
    def DeletedFace(self, index: int) -> TopoDS_Face: ...
    def Dump(self) -> None: ...
    def FaceMode(self) -> bool: ...
    def FloatingEdgesMode(self) -> bool: ...
    def FreeEdge(self, index: int) -> TopoDS_Edge: ...
    def GetContext(self) -> BRepTools_ReShape: ...
    def Init(
        self,
        tolerance: Optional[float] = 1.0e-06,
        option1: Optional[bool] = True,
        option2: Optional[bool] = True,
        option3: Optional[bool] = True,
        option4: Optional[bool] = False,
    ) -> None: ...
    def IsDegenerated(self, shape: TopoDS_Shape) -> bool: ...
    def IsModified(self, shape: TopoDS_Shape) -> bool: ...
    def IsModifiedSubShape(self, shape: TopoDS_Shape) -> bool: ...
    def IsSectionBound(self, section: TopoDS_Edge) -> bool: ...
    def Load(self, shape: TopoDS_Shape) -> None: ...
    def LocalTolerancesMode(self) -> bool: ...
    def MaxTolerance(self) -> float: ...
    def MinTolerance(self) -> float: ...
    def Modified(self, shape: TopoDS_Shape) -> TopoDS_Shape: ...
    def ModifiedSubShape(self, shape: TopoDS_Shape) -> TopoDS_Shape: ...
    def MultipleEdge(self, index: int) -> TopoDS_Edge: ...
    def NbContigousEdges(self) -> int: ...
    def NbDegeneratedShapes(self) -> int: ...
    def NbDeletedFaces(self) -> int: ...
    def NbFreeEdges(self) -> int: ...
    def NbMultipleEdges(self) -> int: ...
    def NonManifoldMode(self) -> bool: ...
    def Perform(
        self, theProgress: Optional[Message_ProgressRange] = Message_ProgressRange()
    ) -> None: ...
    def SameParameterMode(self) -> bool: ...
    def SectionToBoundary(self, section: TopoDS_Edge) -> TopoDS_Edge: ...
    def SetContext(self, theContext: BRepTools_ReShape) -> None: ...
    def SetFaceMode(self, theFaceMode: bool) -> None: ...
    def SetFloatingEdgesMode(self, theFloatingEdgesMode: bool) -> None: ...
    def SetLocalTolerancesMode(self, theLocalTolerancesMode: bool) -> None: ...
    def SetMaxTolerance(self, theMaxToler: float) -> None: ...
    def SetMinTolerance(self, theMinToler: float) -> None: ...
    def SetNonManifoldMode(self, theNonManifoldMode: bool) -> None: ...
    def SetSameParameterMode(self, SameParameterMode: bool) -> None: ...
    def SetTolerance(self, theToler: float) -> None: ...
    def SewedShape(self) -> TopoDS_Shape: ...
    def Tolerance(self) -> float: ...
    def WhichFace(
        self, theEdg: TopoDS_Edge, index: Optional[int] = 1
    ) -> TopoDS_Face: ...

class BRepBuilderAPI_VertexInspector(NCollection_CellFilter_InspectorXYZ):
    def __init__(self, theTol: float) -> None: ...
    def Add(self, thePnt: gp_XYZ) -> None: ...
    def ClearResList(self) -> None: ...
    def Inspect(self, theTarget: int) -> NCollection_CellFilter_Action: ...
    def ResInd(self) -> TColStd_ListOfInteger: ...
    def SetCurrent(self, theCurPnt: gp_XYZ) -> None: ...

class BRepBuilderAPI_BndBoxTreeSelector:
    def __init__(self) -> None: ...
    def Accept(self, theObj: int) -> bool: ...
    def ClearResList(self) -> None: ...
    def Reject(self, theBox: Bnd_Box) -> bool: ...
    def ResInd(self) -> TColStd_ListOfInteger: ...
    def SetCurrent(self, theBox: Bnd_Box) -> None: ...

class BRepBuilderAPI_MakeShape(BRepBuilderAPI_Command):
    def Build(
        self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()
    ) -> None: ...
    def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def IsDeleted(self, S: TopoDS_Shape) -> bool: ...
    def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def Shape(self) -> TopoDS_Shape: ...

class BRepBuilderAPI_MakeEdge(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Lin) -> None: ...
    @overload
    def __init__(self, L: gp_Lin, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Lin, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Lin, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Circ) -> None: ...
    @overload
    def __init__(self, L: gp_Circ, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Circ, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Circ, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Elips) -> None: ...
    @overload
    def __init__(self, L: gp_Elips, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Elips, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Elips, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Parab) -> None: ...
    @overload
    def __init__(self, L: gp_Parab, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Parab, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: gp_Parab, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(self, L: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(
        self, L: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float
    ) -> None: ...
    @overload
    def __init__(
        self, L: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float
    ) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, S: Geom_Surface) -> None: ...
    @overload
    def __init__(
        self, L: Geom2d_Curve, S: Geom_Surface, p1: float, p2: float
    ) -> None: ...
    @overload
    def __init__(
        self, L: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt
    ) -> None: ...
    @overload
    def __init__(
        self, L: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: Geom2d_Curve,
        S: Geom_Surface,
        P1: gp_Pnt,
        P2: gp_Pnt,
        p1: float,
        p2: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: Geom2d_Curve,
        S: Geom_Surface,
        V1: TopoDS_Vertex,
        V2: TopoDS_Vertex,
        p1: float,
        p2: float,
    ) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Error(self) -> BRepBuilderAPI_EdgeError: ...
    @overload
    def Init(self, C: Geom_Curve) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def Init(self, C: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def Init(
        self, C: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float
    ) -> None: ...
    @overload
    def Init(
        self, C: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float
    ) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, S: Geom_Surface, p1: float, p2: float) -> None: ...
    @overload
    def Init(
        self, C: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt
    ) -> None: ...
    @overload
    def Init(
        self, C: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex
    ) -> None: ...
    @overload
    def Init(
        self,
        C: Geom2d_Curve,
        S: Geom_Surface,
        P1: gp_Pnt,
        P2: gp_Pnt,
        p1: float,
        p2: float,
    ) -> None: ...
    @overload
    def Init(
        self,
        C: Geom2d_Curve,
        S: Geom_Surface,
        V1: TopoDS_Vertex,
        V2: TopoDS_Vertex,
        p1: float,
        p2: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def Vertex1(self) -> TopoDS_Vertex: ...
    def Vertex2(self) -> TopoDS_Vertex: ...

class BRepBuilderAPI_MakeEdge2d(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Lin2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Circ2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Elips2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Hypr2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(self, L: gp_Parab2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, p1: float, p2: float) -> None: ...
    @overload
    def __init__(self, L: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def __init__(
        self, L: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex
    ) -> None: ...
    @overload
    def __init__(
        self, L: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d, p1: float, p2: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        L: Geom2d_Curve,
        V1: TopoDS_Vertex,
        V2: TopoDS_Vertex,
        p1: float,
        p2: float,
    ) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Error(self) -> BRepBuilderAPI_EdgeError: ...
    @overload
    def Init(self, C: Geom2d_Curve) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, p1: float, p2: float) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
    @overload
    def Init(self, C: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def Init(
        self, C: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d, p1: float, p2: float
    ) -> None: ...
    @overload
    def Init(
        self,
        C: Geom2d_Curve,
        V1: TopoDS_Vertex,
        V2: TopoDS_Vertex,
        p1: float,
        p2: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def Vertex1(self) -> TopoDS_Vertex: ...
    def Vertex2(self) -> TopoDS_Vertex: ...

class BRepBuilderAPI_MakeFace(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, F: TopoDS_Face) -> None: ...
    @overload
    def __init__(self, P: gp_Pln) -> None: ...
    @overload
    def __init__(self, C: gp_Cylinder) -> None: ...
    @overload
    def __init__(self, C: gp_Cone) -> None: ...
    @overload
    def __init__(self, S: gp_Sphere) -> None: ...
    @overload
    def __init__(self, C: gp_Torus) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, TolDegen: float) -> None: ...
    @overload
    def __init__(
        self, P: gp_Pln, UMin: float, UMax: float, VMin: float, VMax: float
    ) -> None: ...
    @overload
    def __init__(
        self, C: gp_Cylinder, UMin: float, UMax: float, VMin: float, VMax: float
    ) -> None: ...
    @overload
    def __init__(
        self, C: gp_Cone, UMin: float, UMax: float, VMin: float, VMax: float
    ) -> None: ...
    @overload
    def __init__(
        self, S: gp_Sphere, UMin: float, UMax: float, VMin: float, VMax: float
    ) -> None: ...
    @overload
    def __init__(
        self, C: gp_Torus, UMin: float, UMax: float, VMin: float, VMax: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        S: Geom_Surface,
        UMin: float,
        UMax: float,
        VMin: float,
        VMax: float,
        TolDegen: float,
    ) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, OnlyPlane: Optional[bool] = False) -> None: ...
    @overload
    def __init__(
        self, P: gp_Pln, W: TopoDS_Wire, Inside: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, C: gp_Cylinder, W: TopoDS_Wire, Inside: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, C: gp_Cone, W: TopoDS_Wire, Inside: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, S: gp_Sphere, W: TopoDS_Wire, Inside: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, C: gp_Torus, W: TopoDS_Wire, Inside: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(
        self, S: Geom_Surface, W: TopoDS_Wire, Inside: Optional[bool] = True
    ) -> None: ...
    @overload
    def __init__(self, F: TopoDS_Face, W: TopoDS_Wire) -> None: ...
    def Add(self, W: TopoDS_Wire) -> None: ...
    def Error(self) -> BRepBuilderAPI_FaceError: ...
    def Face(self) -> TopoDS_Face: ...
    @overload
    def Init(self, F: TopoDS_Face) -> None: ...
    @overload
    def Init(self, S: Geom_Surface, Bound: bool, TolDegen: float) -> None: ...
    @overload
    def Init(
        self,
        S: Geom_Surface,
        UMin: float,
        UMax: float,
        VMin: float,
        VMax: float,
        TolDegen: float,
    ) -> None: ...
    def IsDone(self) -> bool: ...

class BRepBuilderAPI_MakePolygon(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
    @overload
    def __init__(
        self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, Close: Optional[bool] = False
    ) -> None: ...
    @overload
    def __init__(
        self,
        P1: gp_Pnt,
        P2: gp_Pnt,
        P3: gp_Pnt,
        P4: gp_Pnt,
        Close: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @overload
    def __init__(
        self,
        V1: TopoDS_Vertex,
        V2: TopoDS_Vertex,
        V3: TopoDS_Vertex,
        Close: Optional[bool] = False,
    ) -> None: ...
    @overload
    def __init__(
        self,
        V1: TopoDS_Vertex,
        V2: TopoDS_Vertex,
        V3: TopoDS_Vertex,
        V4: TopoDS_Vertex,
        Close: Optional[bool] = False,
    ) -> None: ...
    @overload
    def Add(self, P: gp_Pnt) -> None: ...
    @overload
    def Add(self, V: TopoDS_Vertex) -> None: ...
    def Added(self) -> bool: ...
    def Close(self) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def FirstVertex(self) -> TopoDS_Vertex: ...
    def IsDone(self) -> bool: ...
    def LastVertex(self) -> TopoDS_Vertex: ...
    def Wire(self) -> TopoDS_Wire: ...

class BRepBuilderAPI_MakeShapeOnMesh(BRepBuilderAPI_MakeShape):
    def __init__(self, theMesh: Poly_Triangulation) -> None: ...
    def Build(
        self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()
    ) -> None: ...

class BRepBuilderAPI_MakeShell(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: Geom_Surface, Segment: Optional[bool] = False) -> None: ...
    @overload
    def __init__(
        self,
        S: Geom_Surface,
        UMin: float,
        UMax: float,
        VMin: float,
        VMax: float,
        Segment: Optional[bool] = False,
    ) -> None: ...
    def Error(self) -> BRepBuilderAPI_ShellError: ...
    def Init(
        self,
        S: Geom_Surface,
        UMin: float,
        UMax: float,
        VMin: float,
        VMax: float,
        Segment: Optional[bool] = False,
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def Shell(self) -> TopoDS_Shell: ...

class BRepBuilderAPI_MakeSolid(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_CompSolid) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shell) -> None: ...
    @overload
    def __init__(self, S1: TopoDS_Shell, S2: TopoDS_Shell) -> None: ...
    @overload
    def __init__(
        self, S1: TopoDS_Shell, S2: TopoDS_Shell, S3: TopoDS_Shell
    ) -> None: ...
    @overload
    def __init__(self, So: TopoDS_Solid) -> None: ...
    @overload
    def __init__(self, So: TopoDS_Solid, S: TopoDS_Shell) -> None: ...
    def Add(self, S: TopoDS_Shell) -> None: ...
    def IsDeleted(self, S: TopoDS_Shape) -> bool: ...
    def IsDone(self) -> bool: ...
    def Solid(self) -> TopoDS_Solid: ...

class BRepBuilderAPI_MakeVertex(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self, P: gp_Pnt) -> None: ...
    def Vertex(self) -> TopoDS_Vertex: ...

class BRepBuilderAPI_MakeWire(BRepBuilderAPI_MakeShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, E: TopoDS_Edge) -> None: ...
    @overload
    def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> None: ...
    @overload
    def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge, E3: TopoDS_Edge) -> None: ...
    @overload
    def __init__(
        self, E1: TopoDS_Edge, E2: TopoDS_Edge, E3: TopoDS_Edge, E4: TopoDS_Edge
    ) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire) -> None: ...
    @overload
    def __init__(self, W: TopoDS_Wire, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, E: TopoDS_Edge) -> None: ...
    @overload
    def Add(self, W: TopoDS_Wire) -> None: ...
    @overload
    def Add(self, L: TopTools_ListOfShape) -> None: ...
    def Edge(self) -> TopoDS_Edge: ...
    def Error(self) -> BRepBuilderAPI_WireError: ...
    def IsDone(self) -> bool: ...
    def Vertex(self) -> TopoDS_Vertex: ...
    def Wire(self) -> TopoDS_Wire: ...

class BRepBuilderAPI_ModifyShape(BRepBuilderAPI_MakeShape):
    def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def ModifiedShape(self, S: TopoDS_Shape) -> TopoDS_Shape: ...

class BRepBuilderAPI_Copy(BRepBuilderAPI_ModifyShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        S: TopoDS_Shape,
        copyGeom: Optional[bool] = True,
        copyMesh: Optional[bool] = False,
    ) -> None: ...
    def Perform(
        self,
        S: TopoDS_Shape,
        copyGeom: Optional[bool] = True,
        copyMesh: Optional[bool] = False,
    ) -> None: ...

class BRepBuilderAPI_GTransform(BRepBuilderAPI_ModifyShape):
    @overload
    def __init__(self, T: gp_GTrsf) -> None: ...
    @overload
    def __init__(
        self, S: TopoDS_Shape, T: gp_GTrsf, Copy: Optional[bool] = False
    ) -> None: ...
    def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def ModifiedShape(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
    def Perform(self, S: TopoDS_Shape, Copy: Optional[bool] = False) -> None: ...

class BRepBuilderAPI_NurbsConvert(BRepBuilderAPI_ModifyShape):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, S: TopoDS_Shape, Copy: Optional[bool] = False) -> None: ...
    def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def ModifiedShape(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
    def Perform(self, S: TopoDS_Shape, Copy: Optional[bool] = False) -> None: ...

class BRepBuilderAPI_Transform(BRepBuilderAPI_ModifyShape):
    @overload
    def __init__(self, T: gp_Trsf) -> None: ...
    @overload
    def __init__(
        self,
        theShape: TopoDS_Shape,
        theTrsf: gp_Trsf,
        theCopyGeom: Optional[bool] = False,
        theCopyMesh: Optional[bool] = False,
    ) -> None: ...
    def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def ModifiedShape(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
    def Perform(
        self,
        theShape: TopoDS_Shape,
        theCopyGeom: Optional[bool] = False,
        theCopyMesh: Optional[bool] = False,
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
