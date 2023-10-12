from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.XmlMDF import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.XmlObjMgt import *

class xmlmdataxtd:
    @staticmethod
    def AddDrivers(
        aDriverTable: XmlMDF_ADriverTable, anMsgDrv: Message_Messenger
    ) -> None: ...
    @staticmethod
    def DocumentVersion() -> int: ...
    @staticmethod
    def SetDocumentVersion(DocVersion: int) -> None: ...

class XmlMDataXtd_ConstraintDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: XmlObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: XmlObjMgt_Persistent,
        RelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMDataXtd_GeometryDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: XmlObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: XmlObjMgt_Persistent,
        RelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMDataXtd_PatternStdDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: XmlObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: XmlObjMgt_Persistent,
        RelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMDataXtd_PositionDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: XmlObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: XmlObjMgt_Persistent,
        RelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMDataXtd_PresentationDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: XmlObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: XmlObjMgt_Persistent,
        RelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMDataXtd_TriangulationDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: XmlObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: XmlObjMgt_Persistent,
        RelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
