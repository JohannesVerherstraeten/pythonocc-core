from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.XmlMDF import *
from OCC.Core.Message import *
from OCC.Core.TDF import *
from OCC.Core.XmlObjMgt import *

class xmlmdatastd:
    @staticmethod
    def AddDrivers(
        aDriverTable: XmlMDF_ADriverTable, anMsgDrv: Message_Messenger
    ) -> None: ...

class XmlMDataStd_AsciiStringDriver(XmlMDF_ADriver):
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

class XmlMDataStd_BooleanArrayDriver(XmlMDF_ADriver):
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

class XmlMDataStd_BooleanListDriver(XmlMDF_ADriver):
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

class XmlMDataStd_ByteArrayDriver(XmlMDF_ADriver):
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

class XmlMDataStd_ExpressionDriver(XmlMDF_ADriver):
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

class XmlMDataStd_ExtStringArrayDriver(XmlMDF_ADriver):
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

class XmlMDataStd_ExtStringListDriver(XmlMDF_ADriver):
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

class XmlMDataStd_GenericEmptyDriver(XmlMDF_ADriver):
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
    def SourceType(self) -> Standard_Type: ...

class XmlMDataStd_GenericExtStringDriver(XmlMDF_ADriver):
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
    def SourceType(self) -> Standard_Type: ...

class XmlMDataStd_IntPackedMapDriver(XmlMDF_ADriver):
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

class XmlMDataStd_IntegerArrayDriver(XmlMDF_ADriver):
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

class XmlMDataStd_IntegerDriver(XmlMDF_ADriver):
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

class XmlMDataStd_IntegerListDriver(XmlMDF_ADriver):
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

class XmlMDataStd_NamedDataDriver(XmlMDF_ADriver):
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

class XmlMDataStd_RealArrayDriver(XmlMDF_ADriver):
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

class XmlMDataStd_RealDriver(XmlMDF_ADriver):
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

class XmlMDataStd_RealListDriver(XmlMDF_ADriver):
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

class XmlMDataStd_ReferenceArrayDriver(XmlMDF_ADriver):
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

class XmlMDataStd_ReferenceListDriver(XmlMDF_ADriver):
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

class XmlMDataStd_TreeNodeDriver(XmlMDF_ADriver):
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

class XmlMDataStd_UAttributeDriver(XmlMDF_ADriver):
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

class XmlMDataStd_VariableDriver(XmlMDF_ADriver):
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
