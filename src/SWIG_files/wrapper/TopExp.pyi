from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.TopTools import *

TopExp_Stack = NewType("TopExp_Stack", TopoDS_Iterator)

class topexp:
    @staticmethod
    def CommonVertex(E1: TopoDS_Edge, E2: TopoDS_Edge, V: TopoDS_Vertex) -> bool: ...
    @staticmethod
    def FirstVertex(
        E: TopoDS_Edge, CumOri: Optional[bool] = False
    ) -> TopoDS_Vertex: ...
    @staticmethod
    def LastVertex(E: TopoDS_Edge, CumOri: Optional[bool] = False) -> TopoDS_Vertex: ...
    @overload
    @staticmethod
    def MapShapes(
        S: TopoDS_Shape, T: TopAbs_ShapeEnum, M: TopTools_IndexedMapOfShape
    ) -> None: ...
    @overload
    @staticmethod
    def MapShapes(
        S: TopoDS_Shape,
        M: TopTools_IndexedMapOfShape,
        cumOri: Optional[bool] = True,
        cumLoc: Optional[bool] = True,
    ) -> None: ...
    @overload
    @staticmethod
    def MapShapes(
        S: TopoDS_Shape,
        M: TopTools_MapOfShape,
        cumOri: Optional[bool] = True,
        cumLoc: Optional[bool] = True,
    ) -> None: ...
    @staticmethod
    def MapShapesAndAncestors(
        S: TopoDS_Shape,
        TS: TopAbs_ShapeEnum,
        TA: TopAbs_ShapeEnum,
        M: TopTools_IndexedDataMapOfShapeListOfShape,
    ) -> None: ...
    @staticmethod
    def MapShapesAndUniqueAncestors(
        S: TopoDS_Shape,
        TS: TopAbs_ShapeEnum,
        TA: TopAbs_ShapeEnum,
        M: TopTools_IndexedDataMapOfShapeListOfShape,
        useOrientation: Optional[bool] = False,
    ) -> None: ...
    @overload
    @staticmethod
    def Vertices(
        E: TopoDS_Edge,
        Vfirst: TopoDS_Vertex,
        Vlast: TopoDS_Vertex,
        CumOri: Optional[bool] = False,
    ) -> None: ...
    @overload
    @staticmethod
    def Vertices(
        W: TopoDS_Wire, Vfirst: TopoDS_Vertex, Vlast: TopoDS_Vertex
    ) -> None: ...

class TopExp_Explorer:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        S: TopoDS_Shape,
        ToFind: TopAbs_ShapeEnum,
        ToAvoid: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE,
    ) -> None: ...
    def Clear(self) -> None: ...
    def Current(self) -> TopoDS_Shape: ...
    def Depth(self) -> int: ...
    def ExploredShape(self) -> TopoDS_Shape: ...
    def Init(
        self,
        S: TopoDS_Shape,
        ToFind: TopAbs_ShapeEnum,
        ToAvoid: Optional[TopAbs_ShapeEnum] = TopAbs_SHAPE,
    ) -> None: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def ReInit(self) -> None: ...
    def Value(self) -> TopoDS_Shape: ...

# harray1 classes
# harray2 classes
# hsequence classes
