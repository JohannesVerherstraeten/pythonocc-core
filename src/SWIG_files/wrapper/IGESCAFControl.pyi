from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Quantity import *
from OCC.Core.TColStd import *
from OCC.Core.TCollection import *
from OCC.Core.TDocStd import *
from OCC.Core.XSControl import *
from OCC.Core.Message import *
from OCC.Core.TopoDS import *
from OCC.Core.IGESControl import *
from OCC.Core.TDF import *

class igescafcontrol:
    @staticmethod
    def DecodeColor(col: int) -> Quantity_Color: ...
    @staticmethod
    def EncodeColor(col: Quantity_Color) -> int: ...

class IGESCAFControl_ConfigurationNode(DE_ConfigurationNode):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theNode: IGESCAFControl_ConfigurationNode) -> None: ...
    def BuildProvider(self) -> False: ...
    def CheckContent(self, theBuffer: NCollection_Buffer) -> bool: ...
    def Copy(self) -> False: ...
    def GetExtensions(self) -> TColStd_ListOfAsciiString: ...
    def GetFormat(self) -> str: ...
    def GetVendor(self) -> str: ...
    def IsExportSupported(self) -> bool: ...
    def IsImportSupported(self) -> bool: ...
    def Save(self) -> str: ...

class IGESCAFControl_Provider(DE_Provider):
    @overload
    def __init__(self) -> None: ...
    def GetFormat(self) -> str: ...
    def GetVendor(self) -> str: ...
    @overload
    def Read(
        self,
        thePath: str,
        theDocument: TDocStd_Document,
        theWS: XSControl_WorkSession,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Read(
        self,
        thePath: str,
        theDocument: TDocStd_Document,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Read(
        self,
        thePath: str,
        theShape: TopoDS_Shape,
        theWS: XSControl_WorkSession,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Read(
        self,
        thePath: str,
        theShape: TopoDS_Shape,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Write(
        self,
        thePath: str,
        theDocument: TDocStd_Document,
        theWS: XSControl_WorkSession,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Write(
        self,
        thePath: str,
        theDocument: TDocStd_Document,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Write(
        self,
        thePath: str,
        theShape: TopoDS_Shape,
        theWS: XSControl_WorkSession,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Write(
        self,
        thePath: str,
        theShape: TopoDS_Shape,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...

class IGESCAFControl_Reader(IGESControl_Reader):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, theWS: XSControl_WorkSession, FromScratch: Optional[bool] = True
    ) -> None: ...
    def GetColorMode(self) -> bool: ...
    def GetLayerMode(self) -> bool: ...
    def GetNameMode(self) -> bool: ...
    @overload
    def Perform(
        self,
        theFileName: str,
        theDoc: TDocStd_Document,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Perform(
        self,
        theFileName: str,
        theDoc: TDocStd_Document,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    def SetColorMode(self, theMode: bool) -> None: ...
    def SetLayerMode(self, theMode: bool) -> None: ...
    def SetNameMode(self, theMode: bool) -> None: ...
    def Transfer(
        self,
        theDoc: TDocStd_Document,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...

class IGESCAFControl_Writer(IGESControl_Writer):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, WS: XSControl_WorkSession, scratch: Optional[bool] = True
    ) -> None: ...
    def GetColorMode(self) -> bool: ...
    def GetLayerMode(self) -> bool: ...
    def GetNameMode(self) -> bool: ...
    @overload
    def Perform(
        self,
        doc: TDocStd_Document,
        filename: str,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Perform(
        self,
        doc: TDocStd_Document,
        filename: str,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    def SetColorMode(self, colormode: bool) -> None: ...
    def SetLayerMode(self, layermode: bool) -> None: ...
    def SetNameMode(self, namemode: bool) -> None: ...
    @overload
    def Transfer(
        self,
        doc: TDocStd_Document,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Transfer(
        self,
        labels: TDF_LabelSequence,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @overload
    def Transfer(
        self,
        label: TDF_Label,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...

# harray1 classes
# harray2 classes
# hsequence classes
