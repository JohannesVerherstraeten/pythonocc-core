from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.XmlMDF import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.XmlObjMgt import *
from OCC.Core.TopTools import *
from OCC.Core.TopLoc import *

class xmlmxcafdoc:
    @staticmethod
    def AddDrivers(
        aDriverTable: XmlMDF_ADriverTable, anMsgDrv: Message_Messenger
    ) -> None: ...

class XmlMXCAFDoc_AssemblyItemRefDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMXCAFDoc_CentroidDriver(XmlMDF_ADriver):
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

class XmlMXCAFDoc_ColorDriver(XmlMDF_ADriver):
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

class XmlMXCAFDoc_DatumDriver(XmlMDF_ADriver):
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

class XmlMXCAFDoc_DimTolDriver(XmlMDF_ADriver):
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

class XmlMXCAFDoc_GraphNodeDriver(XmlMDF_ADriver):
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

class XmlMXCAFDoc_LengthUnitDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMXCAFDoc_LocationDriver(XmlMDF_ADriver):
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
    def SetSharedLocations(self, theLocations: TopTools_LocationSetPtr) -> None: ...
    @overload
    def Translate(
        self,
        theLoc: TopLoc_Location,
        theParent: XmlObjMgt_Element,
        theMap: XmlObjMgt_SRelocationTable,
    ) -> None: ...
    @overload
    def Translate(
        self,
        theParent: XmlObjMgt_Element,
        theLoc: TopLoc_Location,
        theMap: XmlObjMgt_RRelocationTable,
    ) -> bool: ...

class XmlMXCAFDoc_MaterialDriver(XmlMDF_ADriver):
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

class XmlMXCAFDoc_NoteDriver(XmlMDF_ADriver):
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMXCAFDoc_VisMaterialDriver(XmlMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMXCAFDoc_VisMaterialToolDriver(XmlMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMXCAFDoc_NoteBinDataDriver(XmlMXCAFDoc_NoteDriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

class XmlMXCAFDoc_NoteCommentDriver(XmlMXCAFDoc_NoteDriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: XmlObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: XmlObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: XmlObjMgt_Persistent,
        theRelocTable: XmlObjMgt_SRelocationTable,
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
