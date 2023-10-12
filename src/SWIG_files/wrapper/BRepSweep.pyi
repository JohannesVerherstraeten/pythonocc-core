from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRep import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.Sweep import *
from OCC.Core.gp import *
from OCC.Core.TopLoc import *

class BRepSweep_Builder:
    def __init__(self, aBuilder: BRep_Builder) -> None: ...
    @overload
    def Add(
        self, aShape1: TopoDS_Shape, aShape2: TopoDS_Shape, Orient: TopAbs_Orientation
    ) -> None: ...
    @overload
    def Add(self, aShape1: TopoDS_Shape, aShape2: TopoDS_Shape) -> None: ...
    def Builder(self) -> BRep_Builder: ...
    def MakeCompSolid(self, aCompSolid: TopoDS_Shape) -> None: ...
    def MakeCompound(self, aCompound: TopoDS_Shape) -> None: ...
    def MakeShell(self, aShell: TopoDS_Shape) -> None: ...
    def MakeSolid(self, aSolid: TopoDS_Shape) -> None: ...
    def MakeWire(self, aWire: TopoDS_Shape) -> None: ...

class BRepSweep_Iterator:
    def __init__(self) -> None: ...
    def Init(self, aShape: TopoDS_Shape) -> None: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Orientation(self) -> TopAbs_Orientation: ...
    def Value(self) -> TopoDS_Shape: ...

class BRepSweep_NumLinearRegularSweep:
    def Closed(self) -> bool: ...
    def DirectSolid(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopAbs_Orientation: ...
    @overload
    def FirstShape(self) -> TopoDS_Shape: ...
    @overload
    def FirstShape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    def GDDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
        aSubDirS: Sweep_NumShape,
    ) -> bool: ...
    def GGDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def GenIsUsed(self, theS: TopoDS_Shape) -> bool: ...
    def HasShape(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> bool: ...
    def IsInvariant(self, aGenS: TopoDS_Shape) -> bool: ...
    def IsUsed(self, aGenS: TopoDS_Shape) -> bool: ...
    @overload
    def LastShape(self) -> TopoDS_Shape: ...
    @overload
    def LastShape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    def MakeEmptyDirectingEdge(
        self, aGenV: TopoDS_Shape, aDirE: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyFace(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyGeneratingEdge(
        self, aGenE: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyVertex(
        self, aGenV: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def SeparatedWires(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def SetContinuity(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> None: ...
    def SetDirectingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetDirectingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetGeneratingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetGeneratingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetParameters(
        self,
        aNewFace: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    @overload
    def Shape(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> TopoDS_Shape: ...
    @overload
    def Shape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...
    def SplitShell(self, aNewShape: TopoDS_Shape) -> TopoDS_Shape: ...

class BRepSweep_Prism:
    @overload
    def __init__(
        self,
        S: TopoDS_Shape,
        V: gp_Vec,
        Copy: Optional[bool] = False,
        Canonize: Optional[bool] = True,
    ) -> None: ...
    @overload
    def __init__(
        self,
        S: TopoDS_Shape,
        D: gp_Dir,
        Inf: Optional[bool] = True,
        Copy: Optional[bool] = False,
        Canonize: Optional[bool] = True,
    ) -> None: ...
    @overload
    def FirstShape(self) -> TopoDS_Shape: ...
    @overload
    def FirstShape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    def GenIsUsed(self, theS: TopoDS_Shape) -> bool: ...
    def IsUsed(self, aGenS: TopoDS_Shape) -> bool: ...
    @overload
    def LastShape(self) -> TopoDS_Shape: ...
    @overload
    def LastShape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...
    @overload
    def Shape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    def Vec(self) -> gp_Vec: ...

class BRepSweep_Revol:
    @overload
    def __init__(
        self, S: TopoDS_Shape, A: gp_Ax1, D: float, C: Optional[bool] = False
    ) -> None: ...
    @overload
    def __init__(
        self, S: TopoDS_Shape, A: gp_Ax1, C: Optional[bool] = False
    ) -> None: ...
    def Angle(self) -> float: ...
    def Axe(self) -> gp_Ax1: ...
    @overload
    def FirstShape(self) -> TopoDS_Shape: ...
    @overload
    def FirstShape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    def IsUsed(self, aGenS: TopoDS_Shape) -> bool: ...
    @overload
    def LastShape(self) -> TopoDS_Shape: ...
    @overload
    def LastShape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...
    @overload
    def Shape(self) -> TopoDS_Shape: ...
    @overload
    def Shape(self, aGenS: TopoDS_Shape) -> TopoDS_Shape: ...

class BRepSweep_Tool:
    def __init__(self, aShape: TopoDS_Shape) -> None: ...
    def Index(self, aShape: TopoDS_Shape) -> int: ...
    def NbShapes(self) -> int: ...
    def Orientation(self, aShape: TopoDS_Shape) -> TopAbs_Orientation: ...
    def SetOrientation(self, aShape: TopoDS_Shape, Or: TopAbs_Orientation) -> None: ...
    def Shape(self, anIndex: int) -> TopoDS_Shape: ...
    def Type(self, aShape: TopoDS_Shape) -> TopAbs_ShapeEnum: ...

class BRepSweep_Trsf(BRepSweep_NumLinearRegularSweep):
    def GDDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
        aSubDirS: Sweep_NumShape,
    ) -> bool: ...
    def GGDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def HasShape(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> bool: ...
    def Init(self) -> None: ...
    def IsInvariant(self, aGenS: TopoDS_Shape) -> bool: ...
    def MakeEmptyDirectingEdge(
        self, aGenV: TopoDS_Shape, aDirE: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyFace(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyGeneratingEdge(
        self, aGenE: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyVertex(
        self, aGenV: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def Process(self, aGenS: TopoDS_Shape, aDirV: Sweep_NumShape) -> bool: ...
    def SeparatedWires(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def SetContinuity(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> None: ...
    def SetDirectingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetDirectingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetGeneratingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetGeneratingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetParameters(
        self,
        aNewFace: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...

class BRepSweep_Rotation(BRepSweep_Trsf):
    def __init__(
        self,
        S: TopoDS_Shape,
        N: Sweep_NumShape,
        L: TopLoc_Location,
        A: gp_Ax1,
        D: float,
        C: bool,
    ) -> None: ...
    def Angle(self) -> float: ...
    def Axe(self) -> gp_Ax1: ...
    def DirectSolid(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopAbs_Orientation: ...
    def GDDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
        aSubDirS: Sweep_NumShape,
    ) -> bool: ...
    def GGDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def HasShape(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> bool: ...
    def IsInvariant(self, aGenS: TopoDS_Shape) -> bool: ...
    def MakeEmptyDirectingEdge(
        self, aGenV: TopoDS_Shape, aDirE: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyFace(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyGeneratingEdge(
        self, aGenE: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyVertex(
        self, aGenV: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def SeparatedWires(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def SetDirectingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetDirectingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetGeneratingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetGeneratingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetParameters(
        self,
        aNewFace: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SplitShell(self, aNewShape: TopoDS_Shape) -> TopoDS_Shape: ...

class BRepSweep_Translation(BRepSweep_Trsf):
    def __init__(
        self,
        S: TopoDS_Shape,
        N: Sweep_NumShape,
        L: TopLoc_Location,
        V: gp_Vec,
        C: bool,
        Canonize: Optional[bool] = True,
    ) -> None: ...
    def DirectSolid(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopAbs_Orientation: ...
    def GDDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
        aSubDirS: Sweep_NumShape,
    ) -> bool: ...
    def GGDShapeIsToAdd(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def HasShape(self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape) -> bool: ...
    def IsInvariant(self, aGenS: TopoDS_Shape) -> bool: ...
    def MakeEmptyDirectingEdge(
        self, aGenV: TopoDS_Shape, aDirE: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyFace(
        self, aGenS: TopoDS_Shape, aDirS: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyGeneratingEdge(
        self, aGenE: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def MakeEmptyVertex(
        self, aGenV: TopoDS_Shape, aDirV: Sweep_NumShape
    ) -> TopoDS_Shape: ...
    def SeparatedWires(
        self,
        aNewShape: TopoDS_Shape,
        aNewSubShape: TopoDS_Shape,
        aGenS: TopoDS_Shape,
        aSubGenS: TopoDS_Shape,
        aDirS: Sweep_NumShape,
    ) -> bool: ...
    def SetDirectingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetDirectingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetGeneratingPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirE: Sweep_NumShape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetGeneratingParameter(
        self,
        aNewEdge: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def SetPCurve(
        self,
        aNewFace: TopoDS_Shape,
        aNewEdge: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenE: TopoDS_Shape,
        aDirV: Sweep_NumShape,
        orien: TopAbs_Orientation,
    ) -> None: ...
    def SetParameters(
        self,
        aNewFace: TopoDS_Shape,
        aNewVertex: TopoDS_Shape,
        aGenF: TopoDS_Shape,
        aGenV: TopoDS_Shape,
        aDirV: Sweep_NumShape,
    ) -> None: ...
    def Vec(self) -> gp_Vec: ...

# harray1 classes
# harray2 classes
# hsequence classes
