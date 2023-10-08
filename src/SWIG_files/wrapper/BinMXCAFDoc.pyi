from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BinMDF import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.BinObjMgt import *
from OCC.Core.BinMNaming import *
from OCC.Core.TopLoc import *

class binmxcafdoc:
    @staticmethod
    def AddDrivers(
        theDriverTable: BinMDF_ADriverTable, theMsgDrv: Message_Messenger
    ) -> None: ...

class BinMXCAFDoc_AssemblyItemRefDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_CentroidDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_ColorDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_DatumDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_DimTolDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_GraphNodeDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_LengthUnitDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_LocationDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...
    def SetNSDriver(self, theNSDriver: BinMNaming_NamedShapeDriver) -> None: ...
    @overload
    def Translate(
        self,
        theSource: BinObjMgt_Persistent,
        theLoc: TopLoc_Location,
        theMap: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Translate(
        self,
        theLoc: TopLoc_Location,
        theTarget: BinObjMgt_Persistent,
        theMap: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_MaterialDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_NoteDriver(BinMDF_ADriver):
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_VisMaterialDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_VisMaterialToolDriver(BinMDF_ADriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_NoteBinDataDriver(BinMXCAFDoc_NoteDriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinMXCAFDoc_NoteCommentDriver(BinMXCAFDoc_NoteDriver):
    def __init__(self, theMsgDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        theSource: BinObjMgt_Persistent,
        theTarget: TDF_Attribute,
        theRelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        theSource: TDF_Attribute,
        theTarget: BinObjMgt_Persistent,
        theRelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
