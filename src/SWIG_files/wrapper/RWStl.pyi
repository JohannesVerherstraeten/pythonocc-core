from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.OSD import *
from OCC.Core.Message import *
from OCC.Core.Poly import *
from OCC.Core.TColStd import *
from OCC.Core.TCollection import *
from OCC.Core.TDocStd import *
from OCC.Core.XSControl import *
from OCC.Core.TopoDS import *

class rwstl:
    @staticmethod
    def ReadAscii(
        thePath: OSD_Path,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> Poly_Triangulation: ...
    @staticmethod
    def ReadBinary(
        thePath: OSD_Path,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> Poly_Triangulation: ...
    @overload
    @staticmethod
    def ReadFile(
        theFile: OSD_Path,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> Poly_Triangulation: ...
    @overload
    @staticmethod
    def ReadFile(
        theFile: str,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> Poly_Triangulation: ...
    @overload
    @staticmethod
    def ReadFile(
        theFile: str,
        theMergeAngle: float,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> Poly_Triangulation: ...
    @staticmethod
    def WriteAscii(
        theMesh: Poly_Triangulation,
        thePath: OSD_Path,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...
    @staticmethod
    def WriteBinary(
        theMesh: Poly_Triangulation,
        thePath: OSD_Path,
        theProgress: Optional[Message_ProgressRange] = Message_ProgressRange(),
    ) -> bool: ...

class RWStl_ConfigurationNode(DE_ConfigurationNode):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theNode: RWStl_ConfigurationNode) -> None: ...
    def BuildProvider(self) -> False: ...
    def CheckContent(self, theBuffer: NCollection_Buffer) -> bool: ...
    def Copy(self) -> False: ...
    def GetExtensions(self) -> TColStd_ListOfAsciiString: ...
    def GetFormat(self) -> str: ...
    def GetVendor(self) -> str: ...
    def IsExportSupported(self) -> bool: ...
    def IsImportSupported(self) -> bool: ...
    def Save(self) -> str: ...

class RWStl_Provider(DE_Provider):
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

# classnotwrapped
class RWStl_Reader: ...

# harray1 classes
# harray2 classes
# hsequence classes
