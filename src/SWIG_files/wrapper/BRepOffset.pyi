from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.TopoDS import *
from OCC.Core.TopTools import *
from OCC.Core.ChFiDS import *
from OCC.Core.Message import *
from OCC.Core.BRepAlgo import *
from OCC.Core.TopAbs import *
from OCC.Core.GeomAbs import *
from OCC.Core.TCollection import *
from OCC.Core.BRepTools import *
from OCC.Core.TopLoc import *
from OCC.Core.Geom2d import *
from OCC.Core.gp import *

class BRepOffset_ListOfInterval:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> BRepOffset_Interval: ...
    def Last(self) -> BRepOffset_Interval: ...
    def Append(self, theItem: BRepOffset_Interval) -> BRepOffset_Interval: ...
    def Prepend(self, theItem: BRepOffset_Interval) -> BRepOffset_Interval: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> BRepOffset_Interval: ...
    def SetValue(self, theIndex: int, theValue: BRepOffset_Interval) -> None: ...

class BRepOffsetSimple_Status(IntEnum):
    BRepOffsetSimple_OK: int = ...
    BRepOffsetSimple_NullInputShape: int = ...
    BRepOffsetSimple_ErrorOffsetComputation: int = ...
    BRepOffsetSimple_ErrorWallFaceComputation: int = ...
    BRepOffsetSimple_ErrorInvalidNbShells: int = ...
    BRepOffsetSimple_ErrorNonClosedShell: int = ...

BRepOffsetSimple_OK = BRepOffsetSimple_Status.BRepOffsetSimple_OK
BRepOffsetSimple_NullInputShape = (
    BRepOffsetSimple_Status.BRepOffsetSimple_NullInputShape
)
BRepOffsetSimple_ErrorOffsetComputation = (
    BRepOffsetSimple_Status.BRepOffsetSimple_ErrorOffsetComputation
)
BRepOffsetSimple_ErrorWallFaceComputation = (
    BRepOffsetSimple_Status.BRepOffsetSimple_ErrorWallFaceComputation
)
BRepOffsetSimple_ErrorInvalidNbShells = (
    BRepOffsetSimple_Status.BRepOffsetSimple_ErrorInvalidNbShells
)
BRepOffsetSimple_ErrorNonClosedShell = (
    BRepOffsetSimple_Status.BRepOffsetSimple_ErrorNonClosedShell
)

class BRepOffset_Error(IntEnum):
    BRepOffset_NoError: int = ...
    BRepOffset_UnknownError: int = ...
    BRepOffset_BadNormalsOnGeometry: int = ...
    BRepOffset_C0Geometry: int = ...
    BRepOffset_NullOffset: int = ...
    BRepOffset_NotConnectedShell: int = ...
    BRepOffset_CannotTrimEdges: int = ...
    BRepOffset_CannotFuseVertices: int = ...
    BRepOffset_CannotExtentEdge: int = ...
    BRepOffset_UserBreak: int = ...
    BRepOffset_MixedConnectivity: int = ...

BRepOffset_NoError = BRepOffset_Error.BRepOffset_NoError
BRepOffset_UnknownError = BRepOffset_Error.BRepOffset_UnknownError
BRepOffset_BadNormalsOnGeometry = BRepOffset_Error.BRepOffset_BadNormalsOnGeometry
BRepOffset_C0Geometry = BRepOffset_Error.BRepOffset_C0Geometry
BRepOffset_NullOffset = BRepOffset_Error.BRepOffset_NullOffset
BRepOffset_NotConnectedShell = BRepOffset_Error.BRepOffset_NotConnectedShell
BRepOffset_CannotTrimEdges = BRepOffset_Error.BRepOffset_CannotTrimEdges
BRepOffset_CannotFuseVertices = BRepOffset_Error.BRepOffset_CannotFuseVertices
BRepOffset_CannotExtentEdge = BRepOffset_Error.BRepOffset_CannotExtentEdge
BRepOffset_UserBreak = BRepOffset_Error.BRepOffset_UserBreak
BRepOffset_MixedConnectivity = BRepOffset_Error.BRepOffset_MixedConnectivity

class BRepOffset_Mode(IntEnum):
    BRepOffset_Skin: int = ...
    BRepOffset_Pipe: int = ...
    BRepOffset_RectoVerso: int = ...

BRepOffset_Skin = BRepOffset_Mode.BRepOffset_Skin
BRepOffset_Pipe = BRepOffset_Mode.BRepOffset_Pipe
BRepOffset_RectoVerso = BRepOffset_Mode.BRepOffset_RectoVerso

class BRepOffset_Status(IntEnum):
    BRepOffset_Good: int = ...
    BRepOffset_Reversed: int = ...
    BRepOffset_Degenerated: int = ...
    BRepOffset_Unknown: int = ...

BRepOffset_Good = BRepOffset_Status.BRepOffset_Good
BRepOffset_Reversed = BRepOffset_Status.BRepOffset_Reversed
BRepOffset_Degenerated = BRepOffset_Status.BRepOffset_Degenerated
BRepOffset_Unknown = BRepOffset_Status.BRepOffset_Unknown

class brepoffset:
    @staticmethod
    def CollapseSingularities(
        theSurface: Geom_Surface, theFace: TopoDS_Face, thePrecision: float
    ) -> Geom_Surface: ...
    @staticmethod
    def Surface(
        Surface: Geom_Surface, Offset: float, allowC0: Optional[bool] = False
    ) -> Tuple[Geom_Surface, BRepOffset_Status]: ...

class BRepOffset_Analyse:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theS: TopoDS_Shape, theAngle: float) -> None: ...
    @overload
    def AddFaces(
        self,
        theFace: TopoDS_Face,
        theCo: TopoDS_Compound,
        theMap: TopTools_MapOfShape,
        theType: ChFiDS_TypeOfConcavity,
    ) -> None: ...
    @overload
    def AddFaces(
        self,
        theFace: TopoDS_Face,
        theCo: TopoDS_Compound,
        theMap: TopTools_MapOfShape,
        theType1: ChFiDS_TypeOfConcavity,
        theType2: ChFiDS_TypeOfConcavity,
    ) -> None: ...
    def Ancestors(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def Clear(self) -> None: ...
    def Descendants(
        self, theS: TopoDS_Shape, theUpdate: Optional[bool] = False
    ) -> TopTools_ListOfShape: ...
    def EdgeReplacement(
        self, theFace: TopoDS_Face, theEdge: TopoDS_Edge
    ) -> TopoDS_Edge: ...
    @overload
    def Edges(
        self,
        theV: TopoDS_Vertex,
        theType: ChFiDS_TypeOfConcavity,
        theL: TopTools_ListOfShape,
    ) -> None: ...
    @overload
    def Edges(
        self,
        theF: TopoDS_Face,
        theType: ChFiDS_TypeOfConcavity,
        theL: TopTools_ListOfShape,
    ) -> None: ...
    @overload
    def Explode(
        self, theL: TopTools_ListOfShape, theType: ChFiDS_TypeOfConcavity
    ) -> None: ...
    @overload
    def Explode(
        self,
        theL: TopTools_ListOfShape,
        theType1: ChFiDS_TypeOfConcavity,
        theType2: ChFiDS_TypeOfConcavity,
    ) -> None: ...
    def Generated(self, theS: TopoDS_Shape) -> TopoDS_Shape: ...
    def HasAncestor(self, theS: TopoDS_Shape) -> bool: ...
    def HasGenerated(self, theS: TopoDS_Shape) -> bool: ...
    def IsDone(self) -> bool: ...
    def NewFaces(self) -> TopTools_ListOfShape: ...
    def Perform(
        self,
        theS: TopoDS_Shape,
        theAngle: float,
        theRange: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> None: ...
    def SetFaceOffsetMap(self, theMap: TopTools_DataMapOfShapeReal) -> None: ...
    def SetOffsetValue(self, theOffset: float) -> None: ...
    def TangentEdges(
        self,
        theEdge: TopoDS_Edge,
        theVertex: TopoDS_Vertex,
        theEdges: TopTools_ListOfShape,
    ) -> None: ...
    def Type(self, theE: TopoDS_Edge) -> BRepOffset_ListOfInterval: ...

class BRepOffset_Inter2d:
    @staticmethod
    def Compute(
        AsDes: BRepAlgo_AsDes,
        F: TopoDS_Face,
        NewEdges: TopTools_IndexedMapOfShape,
        Tol: float,
        theEdgeIntEdges: TopTools_DataMapOfShapeListOfShape,
        theDMVV: TopTools_IndexedDataMapOfShapeListOfShape,
        theRange: Message_ProgressRange,
    ) -> None: ...
    @staticmethod
    def ConnexIntByInt(
        FI: TopoDS_Face,
        OFI: BRepOffset_Offset,
        MES: TopTools_DataMapOfShapeShape,
        Build: TopTools_DataMapOfShapeShape,
        theAsDes: BRepAlgo_AsDes,
        AsDes2d: BRepAlgo_AsDes,
        Offset: float,
        Tol: float,
        Analyse: BRepOffset_Analyse,
        FacesWithVerts: TopTools_IndexedMapOfShape,
        theImageVV: BRepAlgo_Image,
        theEdgeIntEdges: TopTools_DataMapOfShapeListOfShape,
        theDMVV: TopTools_IndexedDataMapOfShapeListOfShape,
        theRange: Message_ProgressRange,
    ) -> bool: ...
    @staticmethod
    def ConnexIntByIntInVert(
        FI: TopoDS_Face,
        OFI: BRepOffset_Offset,
        MES: TopTools_DataMapOfShapeShape,
        Build: TopTools_DataMapOfShapeShape,
        AsDes: BRepAlgo_AsDes,
        AsDes2d: BRepAlgo_AsDes,
        Tol: float,
        Analyse: BRepOffset_Analyse,
        theDMVV: TopTools_IndexedDataMapOfShapeListOfShape,
        theRange: Message_ProgressRange,
    ) -> None: ...
    @staticmethod
    def ExtentEdge(E: TopoDS_Edge, NE: TopoDS_Edge, theOffset: float) -> bool: ...
    @staticmethod
    def FuseVertices(
        theDMVV: TopTools_IndexedDataMapOfShapeListOfShape,
        theAsDes: BRepAlgo_AsDes,
        theImageVV: BRepAlgo_Image,
    ) -> bool: ...

class BRepOffset_Inter3d:
    @overload
    def __init__(
        self, AsDes: BRepAlgo_AsDes, Side: TopAbs_State, Tol: float
    ) -> None: ...
    def CompletInt(
        self,
        SetOfFaces: TopTools_ListOfShape,
        InitOffsetFace: BRepAlgo_Image,
        theRange: Message_ProgressRange,
    ) -> None: ...
    def ConnexIntByArc(
        self,
        SetOfFaces: TopTools_ListOfShape,
        ShapeInit: TopoDS_Shape,
        Analyse: BRepOffset_Analyse,
        InitOffsetFace: BRepAlgo_Image,
        theRange: Message_ProgressRange,
    ) -> None: ...
    def ConnexIntByInt(
        self,
        SI: TopoDS_Shape,
        MapSF: BRepOffset_DataMapOfShapeOffset,
        A: BRepOffset_Analyse,
        MES: TopTools_DataMapOfShapeShape,
        Build: TopTools_DataMapOfShapeShape,
        Failed: TopTools_ListOfShape,
        theRange: Message_ProgressRange,
        bIsPlanar: Optional[bool] = False,
    ) -> None: ...
    def ContextIntByArc(
        self,
        ContextFaces: TopTools_IndexedMapOfShape,
        ExtentContext: bool,
        Analyse: BRepOffset_Analyse,
        InitOffsetFace: BRepAlgo_Image,
        InitOffsetEdge: BRepAlgo_Image,
        theRange: Message_ProgressRange,
    ) -> None: ...
    def ContextIntByInt(
        self,
        ContextFaces: TopTools_IndexedMapOfShape,
        ExtentContext: bool,
        MapSF: BRepOffset_DataMapOfShapeOffset,
        A: BRepOffset_Analyse,
        MES: TopTools_DataMapOfShapeShape,
        Build: TopTools_DataMapOfShapeShape,
        Failed: TopTools_ListOfShape,
        theRange: Message_ProgressRange,
        bIsPlanar: Optional[bool] = False,
    ) -> None: ...
    def FaceInter(
        self, F1: TopoDS_Face, F2: TopoDS_Face, InitOffsetFace: BRepAlgo_Image
    ) -> None: ...
    def IsDone(self, F1: TopoDS_Face, F2: TopoDS_Face) -> bool: ...
    def NewEdges(self) -> TopTools_IndexedMapOfShape: ...
    def SetDone(self, F1: TopoDS_Face, F2: TopoDS_Face) -> None: ...
    def TouchedFaces(self) -> TopTools_IndexedMapOfShape: ...

class BRepOffset_Interval:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, U1: float, U2: float, Type: ChFiDS_TypeOfConcavity) -> None: ...
    @overload
    def First(self, U: float) -> None: ...
    @overload
    def First(self) -> float: ...
    @overload
    def Last(self, U: float) -> None: ...
    @overload
    def Last(self) -> float: ...
    @overload
    def Type(self, T: ChFiDS_TypeOfConcavity) -> None: ...
    @overload
    def Type(self) -> ChFiDS_TypeOfConcavity: ...

class BRepOffset_MakeLoops:
    def __init__(self) -> None: ...
    def Build(
        self,
        LF: TopTools_ListOfShape,
        AsDes: BRepAlgo_AsDes,
        Image: BRepAlgo_Image,
        theImageVV: BRepAlgo_Image,
        theRange: Message_ProgressRange,
    ) -> None: ...
    def BuildFaces(
        self,
        LF: TopTools_ListOfShape,
        AsDes: BRepAlgo_AsDes,
        Image: BRepAlgo_Image,
        theRange: Message_ProgressRange,
    ) -> None: ...
    def BuildOnContext(
        self,
        LContext: TopTools_ListOfShape,
        Analyse: BRepOffset_Analyse,
        AsDes: BRepAlgo_AsDes,
        Image: BRepAlgo_Image,
        InSide: bool,
        theRange: Message_ProgressRange,
    ) -> None: ...

class BRepOffset_MakeOffset:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        S: TopoDS_Shape,
        Offset: float,
        Tol: float,
        Mode: Optional[BRepOffset_Mode] = BRepOffset_Skin,
        Intersection: Optional[bool] = False,
        SelfInter: Optional[bool] = False,
        Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc,
        Thickening: Optional[bool] = False,
        RemoveIntEdges: Optional[bool] = False,
        theRange: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> None: ...
    def AddFace(self, F: TopoDS_Face) -> None: ...
    def AllowLinearization(self, theIsAllowed: bool) -> None: ...
    def CheckInputData(self, theRange: Message_ProgressRange) -> bool: ...
    def Clear(self) -> None: ...
    def ClosingFaces(self) -> TopTools_IndexedMapOfShape: ...
    def Error(self) -> BRepOffset_Error: ...
    def Generated(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def GetBadShape(self) -> TopoDS_Shape: ...
    def GetJoinType(self) -> GeomAbs_JoinType: ...
    def InitShape(self) -> TopoDS_Shape: ...
    def Initialize(
        self,
        S: TopoDS_Shape,
        Offset: float,
        Tol: float,
        Mode: Optional[BRepOffset_Mode] = BRepOffset_Skin,
        Intersection: Optional[bool] = False,
        SelfInter: Optional[bool] = False,
        Join: Optional[GeomAbs_JoinType] = GeomAbs_Arc,
        Thickening: Optional[bool] = False,
        RemoveIntEdges: Optional[bool] = False,
    ) -> None: ...
    def IsDeleted(self, S: TopoDS_Shape) -> bool: ...
    def IsDone(self) -> bool: ...
    def MakeOffsetShape(
        self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()
    ) -> None: ...
    def MakeThickSolid(
        self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()
    ) -> None: ...
    def Modified(self, theS: TopoDS_Shape) -> TopTools_ListOfShape: ...
    def OffsetEdgesFromShapes(self) -> BRepAlgo_Image: ...
    def OffsetFacesFromShapes(self) -> BRepAlgo_Image: ...
    def SetOffsetOnFace(self, F: TopoDS_Face, Off: float) -> None: ...
    def Shape(self) -> TopoDS_Shape: ...

class BRepOffset_MakeSimpleOffset:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theInputShape: TopoDS_Shape, theOffsetValue: float) -> None: ...
    def Generated(self, theShape: TopoDS_Shape) -> TopoDS_Shape: ...
    def GetBuildSolidFlag(self) -> bool: ...
    def GetError(self) -> False: ...
    def GetErrorMessage(self) -> str: ...
    def GetOffsetValue(self) -> float: ...
    def GetResultShape(self) -> TopoDS_Shape: ...
    def GetTolerance(self) -> float: ...
    def Initialize(
        self, theInputShape: TopoDS_Shape, theOffsetValue: float
    ) -> None: ...
    def IsDone(self) -> bool: ...
    def Modified(self, theShape: TopoDS_Shape) -> TopoDS_Shape: ...
    def Perform(self) -> None: ...
    def SetBuildSolidFlag(self, theBuildFlag: bool) -> None: ...
    def SetOffsetValue(self, theOffsetValue: float) -> None: ...
    def SetTolerance(self, theValue: float) -> None: ...

class BRepOffset_Offset:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        Face: TopoDS_Face,
        Offset: float,
        OffsetOutside: Optional[bool] = True,
        JoinType: Optional[GeomAbs_JoinType] = GeomAbs_Arc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Face: TopoDS_Face,
        Offset: float,
        Created: TopTools_DataMapOfShapeShape,
        OffsetOutside: Optional[bool] = True,
        JoinType: Optional[GeomAbs_JoinType] = GeomAbs_Arc,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Path: TopoDS_Edge,
        Edge1: TopoDS_Edge,
        Edge2: TopoDS_Edge,
        Offset: float,
        Polynomial: Optional[bool] = False,
        Tol: Optional[float] = 1.0e-4,
        Conti: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Path: TopoDS_Edge,
        Edge1: TopoDS_Edge,
        Edge2: TopoDS_Edge,
        Offset: float,
        FirstEdge: TopoDS_Edge,
        LastEdge: TopoDS_Edge,
        Polynomial: Optional[bool] = False,
        Tol: Optional[float] = 1.0e-4,
        Conti: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def __init__(
        self,
        Vertex: TopoDS_Vertex,
        LEdge: TopTools_ListOfShape,
        Offset: float,
        Polynomial: Optional[bool] = False,
        Tol: Optional[float] = 1.0e-4,
        Conti: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    def Face(self) -> TopoDS_Face: ...
    def Generated(self, Shape: TopoDS_Shape) -> TopoDS_Shape: ...
    @overload
    def Init(
        self,
        Face: TopoDS_Face,
        Offset: float,
        OffsetOutside: Optional[bool] = True,
        JoinType: Optional[GeomAbs_JoinType] = GeomAbs_Arc,
    ) -> None: ...
    @overload
    def Init(
        self,
        Face: TopoDS_Face,
        Offset: float,
        Created: TopTools_DataMapOfShapeShape,
        OffsetOutside: Optional[bool] = True,
        JoinType: Optional[GeomAbs_JoinType] = GeomAbs_Arc,
    ) -> None: ...
    @overload
    def Init(
        self,
        Path: TopoDS_Edge,
        Edge1: TopoDS_Edge,
        Edge2: TopoDS_Edge,
        Offset: float,
        Polynomial: Optional[bool] = False,
        Tol: Optional[float] = 1.0e-4,
        Conti: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def Init(
        self,
        Path: TopoDS_Edge,
        Edge1: TopoDS_Edge,
        Edge2: TopoDS_Edge,
        Offset: float,
        FirstEdge: TopoDS_Edge,
        LastEdge: TopoDS_Edge,
        Polynomial: Optional[bool] = False,
        Tol: Optional[float] = 1.0e-4,
        Conti: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def Init(
        self,
        Vertex: TopoDS_Vertex,
        LEdge: TopTools_ListOfShape,
        Offset: float,
        Polynomial: Optional[bool] = False,
        Tol: Optional[float] = 1.0e-4,
        Conti: Optional[GeomAbs_Shape] = GeomAbs_C1,
    ) -> None: ...
    @overload
    def Init(self, Edge: TopoDS_Edge, Offset: float) -> None: ...
    def InitialShape(self) -> TopoDS_Shape: ...
    def Status(self) -> BRepOffset_Status: ...

class BRepOffset_SimpleOffset(BRepTools_Modification):
    def __init__(
        self, theInputShape: TopoDS_Shape, theOffsetValue: float, theTolerance: float
    ) -> None: ...
    def Continuity(
        self,
        E: TopoDS_Edge,
        F1: TopoDS_Face,
        F2: TopoDS_Face,
        NewE: TopoDS_Edge,
        NewF1: TopoDS_Face,
        NewF2: TopoDS_Face,
    ) -> GeomAbs_Shape: ...
    def NewCurve(
        self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location
    ) -> Tuple[bool, float]: ...
    def NewCurve2d(
        self,
        E: TopoDS_Edge,
        F: TopoDS_Face,
        NewE: TopoDS_Edge,
        NewF: TopoDS_Face,
        C: Geom2d_Curve,
    ) -> Tuple[bool, float]: ...
    def NewParameter(
        self, V: TopoDS_Vertex, E: TopoDS_Edge
    ) -> Tuple[bool, float, float]: ...
    def NewPoint(self, V: TopoDS_Vertex, P: gp_Pnt) -> Tuple[bool, float]: ...
    def NewSurface(
        self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location
    ) -> Tuple[bool, float, bool, bool]: ...

class BRepOffset_Tool:
    @staticmethod
    def BuildNeighbour(
        W: TopoDS_Wire,
        F: TopoDS_Face,
        NOnV1: TopTools_DataMapOfShapeShape,
        NOnV2: TopTools_DataMapOfShapeShape,
    ) -> None: ...
    @staticmethod
    def CheckBounds(
        F: TopoDS_Face, Analyse: BRepOffset_Analyse
    ) -> Tuple[bool, bool, bool]: ...
    @staticmethod
    def CheckPlanesNormals(
        theFace1: TopoDS_Face, theFace2: TopoDS_Face, theTolAng: Optional[float] = 1e-8
    ) -> bool: ...
    @staticmethod
    def CorrectOrientation(
        SI: TopoDS_Shape,
        NewEdges: TopTools_IndexedMapOfShape,
        AsDes: BRepAlgo_AsDes,
        InitOffset: BRepAlgo_Image,
        Offset: float,
    ) -> None: ...
    @staticmethod
    def Deboucle3D(S: TopoDS_Shape, Boundary: TopTools_MapOfShape) -> TopoDS_Shape: ...
    @staticmethod
    def EdgeVertices(E: TopoDS_Edge, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
    @staticmethod
    def EnLargeFace(
        F: TopoDS_Face,
        NF: TopoDS_Face,
        ChangeGeom: bool,
        UpDatePCurve: Optional[bool] = False,
        enlargeU: Optional[bool] = True,
        enlargeVfirst: Optional[bool] = True,
        enlargeVlast: Optional[bool] = True,
        theExtensionMode: Optional[int] = 1,
        theLenBeforeUfirst: Optional[float] = -1,
        theLenAfterUlast: Optional[float] = -1,
        theLenBeforeVfirst: Optional[float] = -1,
        theLenAfterVlast: Optional[float] = -1,
    ) -> bool: ...
    @staticmethod
    def ExtentFace(
        F: TopoDS_Face,
        ConstShapes: TopTools_DataMapOfShapeShape,
        ToBuild: TopTools_DataMapOfShapeShape,
        Side: TopAbs_State,
        TolConf: float,
        NF: TopoDS_Face,
    ) -> None: ...
    @overload
    @staticmethod
    def FindCommonShapes(
        theF1: TopoDS_Face,
        theF2: TopoDS_Face,
        theLE: TopTools_ListOfShape,
        theLV: TopTools_ListOfShape,
    ) -> bool: ...
    @overload
    @staticmethod
    def FindCommonShapes(
        theS1: TopoDS_Shape,
        theS2: TopoDS_Shape,
        theType: TopAbs_ShapeEnum,
        theLSC: TopTools_ListOfShape,
    ) -> bool: ...
    @staticmethod
    def Gabarit(aCurve: Geom_Curve) -> float: ...
    @staticmethod
    def Inter2d(
        F: TopoDS_Face,
        E1: TopoDS_Edge,
        E2: TopoDS_Edge,
        LV: TopTools_ListOfShape,
        Tol: float,
    ) -> None: ...
    @staticmethod
    def Inter3D(
        F1: TopoDS_Face,
        F2: TopoDS_Face,
        LInt1: TopTools_ListOfShape,
        LInt2: TopTools_ListOfShape,
        Side: TopAbs_State,
        RefEdge: TopoDS_Edge,
        RefFace1: TopoDS_Face,
        RefFace2: TopoDS_Face,
    ) -> None: ...
    @staticmethod
    def InterOrExtent(
        F1: TopoDS_Face,
        F2: TopoDS_Face,
        LInt1: TopTools_ListOfShape,
        LInt2: TopTools_ListOfShape,
        Side: TopAbs_State,
    ) -> None: ...
    @staticmethod
    def MapVertexEdges(
        S: TopoDS_Shape, MVE: TopTools_DataMapOfShapeListOfShape
    ) -> None: ...
    @staticmethod
    def OrientSection(
        E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face
    ) -> Tuple[TopAbs_Orientation, TopAbs_Orientation]: ...
    @staticmethod
    def PipeInter(
        F1: TopoDS_Face,
        F2: TopoDS_Face,
        LInt1: TopTools_ListOfShape,
        LInt2: TopTools_ListOfShape,
        Side: TopAbs_State,
    ) -> None: ...
    @staticmethod
    def TryProject(
        F1: TopoDS_Face,
        F2: TopoDS_Face,
        Edges: TopTools_ListOfShape,
        LInt1: TopTools_ListOfShape,
        LInt2: TopTools_ListOfShape,
        Side: TopAbs_State,
        TolConf: float,
    ) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes
