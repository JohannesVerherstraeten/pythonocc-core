from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BinMDF import *
from OCC.Core.Message import *
from OCC.Core.TDocStd import *
from OCC.Core.BinLDrivers import *
from OCC.Core.TDF import *
from OCC.Core.BinObjMgt import *

class bintobjdrivers:
    @staticmethod
    def AddDrivers(
        aDriverTable: BinMDF_ADriverTable, aMsgDrv: Message_Messenger
    ) -> None: ...
    @staticmethod
    def DefineFormat(theApp: TDocStd_Application) -> None: ...
    @staticmethod
    def Factory(aGUID: Standard_GUID) -> Standard_Transient: ...

class BinTObjDrivers_DocumentRetrievalDriver(BinLDrivers_DocumentRetrievalDriver):
    def __init__(self) -> None: ...
    def AttributeDrivers(
        self, theMsgDriver: Message_Messenger
    ) -> BinMDF_ADriverTable: ...

class BinTObjDrivers_DocumentStorageDriver(BinLDrivers_DocumentStorageDriver):
    def __init__(self) -> None: ...
    def AttributeDrivers(
        self, theMsgDriver: Message_Messenger
    ) -> BinMDF_ADriverTable: ...

class BinTObjDrivers_IntSparseArrayDriver(BinMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
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

class BinTObjDrivers_ModelDriver(BinMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: BinObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: BinObjMgt_Persistent,
        RelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinTObjDrivers_ObjectDriver(BinMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: BinObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: BinObjMgt_Persistent,
        RelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinTObjDrivers_ReferenceDriver(BinMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
    def NewEmpty(self) -> TDF_Attribute: ...
    @overload
    def Paste(
        self,
        Source: BinObjMgt_Persistent,
        Target: TDF_Attribute,
        RelocTable: BinObjMgt_RRelocationTable,
    ) -> bool: ...
    @overload
    def Paste(
        self,
        Source: TDF_Attribute,
        Target: BinObjMgt_Persistent,
        RelocTable: BinObjMgt_SRelocationTable,
    ) -> None: ...

class BinTObjDrivers_XYZDriver(BinMDF_ADriver):
    def __init__(self, theMessageDriver: Message_Messenger) -> None: ...
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
