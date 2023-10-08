from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *

class selectbasics:
    @staticmethod
    def MaxOwnerPriority() -> int: ...
    @staticmethod
    def MinOwnerPriority() -> int: ...

class SelectBasics_PickResult:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, theDepth: float, theDistToCenter: float, theObjPickedPnt: gp_Pnt
    ) -> None: ...
    def Depth(self) -> float: ...
    def DistToGeomCenter(self) -> float: ...
    def HasPickedPoint(self) -> bool: ...
    def Invalidate(self) -> None: ...
    def IsValid(self) -> bool: ...
    @staticmethod
    def Min(
        thePickResult1: SelectBasics_PickResult, thePickResult2: SelectBasics_PickResult
    ) -> SelectBasics_PickResult: ...
    def PickedPoint(self) -> gp_Pnt: ...
    def SetDepth(self, theDepth: float) -> None: ...
    def SetDistToGeomCenter(self, theDistToCenter: float) -> None: ...
    def SetPickedPoint(self, theObjPickedPnt: gp_Pnt) -> None: ...
    @overload
    def SetSurfaceNormal(self, theNormal: float) -> None: ...
    @overload
    def SetSurfaceNormal(self, theNormal: gp_Vec) -> None: ...
    def SurfaceNormal(self) -> float: ...

class SelectBasics_SelectingVolumeManager:
    def DetectedPoint(self, theDepth: float) -> gp_Pnt: ...
    def DistToGeometryCenter(self, theCOG: gp_Pnt) -> float: ...
    def GetActiveSelectionType(self) -> int: ...
    def GetFarPickedPnt(self) -> gp_Pnt: ...
    def GetMousePosition(self) -> gp_Pnt2d: ...
    def GetNearPickedPnt(self) -> gp_Pnt: ...
    def GetViewRayDirection(self) -> gp_Dir: ...
    def IsOverlapAllowed(self) -> bool: ...
    def IsScalableActiveVolume(self) -> bool: ...
    @overload
    def Overlaps(
        self, thePnt: gp_Pnt, thePickResult: SelectBasics_PickResult
    ) -> bool: ...
    @overload
    def Overlaps(self, thePnt: gp_Pnt) -> bool: ...
    @overload
    def Overlaps(
        self,
        theArrayOfPts: TColgp_HArray1OfPnt,
        theSensType: int,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    @overload
    def Overlaps(
        self,
        theArrayOfPts: TColgp_Array1OfPnt,
        theSensType: int,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    @overload
    def Overlaps(
        self, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePickResult: SelectBasics_PickResult
    ) -> bool: ...
    @overload
    def Overlaps(
        self,
        thePnt1: gp_Pnt,
        thePnt2: gp_Pnt,
        thePnt3: gp_Pnt,
        theSensType: int,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    @overload
    def OverlapsCircle(
        self,
        theRadius: float,
        theTrsf: gp_Trsf,
        theIsFilled: bool,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    @overload
    def OverlapsCircle(
        self,
        theRadius: float,
        theTrsf: gp_Trsf,
        theIsFilled: bool,
        theInside: Optional[bool] = None,
    ) -> bool: ...
    @overload
    def OverlapsCylinder(
        self,
        theBottomRad: float,
        theTopRad: float,
        theHeight: float,
        theTrsf: gp_Trsf,
        theIsHollow: bool,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    @overload
    def OverlapsCylinder(
        self,
        theBottomRad: float,
        theTopRad: float,
        theHeight: float,
        theTrsf: gp_Trsf,
        theIsHollow: bool,
        theInside: Optional[bool] = None,
    ) -> bool: ...
    @overload
    def OverlapsPoint(
        self, thePnt: gp_Pnt, thePickResult: SelectBasics_PickResult
    ) -> bool: ...
    @overload
    def OverlapsPoint(self, thePnt: gp_Pnt) -> bool: ...
    def OverlapsPolygon(
        self,
        theArrayOfPts: TColgp_Array1OfPnt,
        theSensType: int,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    def OverlapsSegment(
        self, thePt1: gp_Pnt, thePt2: gp_Pnt, thePickResult: SelectBasics_PickResult
    ) -> bool: ...
    @overload
    def OverlapsSphere(
        self,
        theCenter: gp_Pnt,
        theRadius: float,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...
    @overload
    def OverlapsSphere(
        self, theCenter: gp_Pnt, theRadius: float, theInside: Optional[bool] = None
    ) -> bool: ...
    def OverlapsTriangle(
        self,
        thePt1: gp_Pnt,
        thePt2: gp_Pnt,
        thePt3: gp_Pnt,
        theSensType: int,
        thePickResult: SelectBasics_PickResult,
    ) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes
