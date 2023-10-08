from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *

class Resource_FormatType(IntEnum):
    Resource_FormatType_SJIS: int = ...
    Resource_FormatType_EUC: int = ...
    Resource_FormatType_NoConversion: int = ...
    Resource_FormatType_GB: int = ...
    Resource_FormatType_UTF8: int = ...
    Resource_FormatType_SystemLocale: int = ...
    Resource_FormatType_CP1250: int = ...
    Resource_FormatType_CP1251: int = ...
    Resource_FormatType_CP1252: int = ...
    Resource_FormatType_CP1253: int = ...
    Resource_FormatType_CP1254: int = ...
    Resource_FormatType_CP1255: int = ...
    Resource_FormatType_CP1256: int = ...
    Resource_FormatType_CP1257: int = ...
    Resource_FormatType_CP1258: int = ...
    Resource_FormatType_iso8859_1: int = ...
    Resource_FormatType_iso8859_2: int = ...
    Resource_FormatType_iso8859_3: int = ...
    Resource_FormatType_iso8859_4: int = ...
    Resource_FormatType_iso8859_5: int = ...
    Resource_FormatType_iso8859_6: int = ...
    Resource_FormatType_iso8859_7: int = ...
    Resource_FormatType_iso8859_8: int = ...
    Resource_FormatType_iso8859_9: int = ...
    Resource_FormatType_CP850: int = ...
    Resource_FormatType_GBK: int = ...
    Resource_FormatType_Big5: int = ...
    Resource_FormatType_ANSI: int = ...
    Resource_SJIS: int = ...
    Resource_EUC: int = ...
    Resource_ANSI: int = ...
    Resource_GB: int = ...

Resource_FormatType_SJIS = Resource_FormatType.Resource_FormatType_SJIS
Resource_FormatType_EUC = Resource_FormatType.Resource_FormatType_EUC
Resource_FormatType_NoConversion = Resource_FormatType.Resource_FormatType_NoConversion
Resource_FormatType_GB = Resource_FormatType.Resource_FormatType_GB
Resource_FormatType_UTF8 = Resource_FormatType.Resource_FormatType_UTF8
Resource_FormatType_SystemLocale = Resource_FormatType.Resource_FormatType_SystemLocale
Resource_FormatType_CP1250 = Resource_FormatType.Resource_FormatType_CP1250
Resource_FormatType_CP1251 = Resource_FormatType.Resource_FormatType_CP1251
Resource_FormatType_CP1252 = Resource_FormatType.Resource_FormatType_CP1252
Resource_FormatType_CP1253 = Resource_FormatType.Resource_FormatType_CP1253
Resource_FormatType_CP1254 = Resource_FormatType.Resource_FormatType_CP1254
Resource_FormatType_CP1255 = Resource_FormatType.Resource_FormatType_CP1255
Resource_FormatType_CP1256 = Resource_FormatType.Resource_FormatType_CP1256
Resource_FormatType_CP1257 = Resource_FormatType.Resource_FormatType_CP1257
Resource_FormatType_CP1258 = Resource_FormatType.Resource_FormatType_CP1258
Resource_FormatType_iso8859_1 = Resource_FormatType.Resource_FormatType_iso8859_1
Resource_FormatType_iso8859_2 = Resource_FormatType.Resource_FormatType_iso8859_2
Resource_FormatType_iso8859_3 = Resource_FormatType.Resource_FormatType_iso8859_3
Resource_FormatType_iso8859_4 = Resource_FormatType.Resource_FormatType_iso8859_4
Resource_FormatType_iso8859_5 = Resource_FormatType.Resource_FormatType_iso8859_5
Resource_FormatType_iso8859_6 = Resource_FormatType.Resource_FormatType_iso8859_6
Resource_FormatType_iso8859_7 = Resource_FormatType.Resource_FormatType_iso8859_7
Resource_FormatType_iso8859_8 = Resource_FormatType.Resource_FormatType_iso8859_8
Resource_FormatType_iso8859_9 = Resource_FormatType.Resource_FormatType_iso8859_9
Resource_FormatType_CP850 = Resource_FormatType.Resource_FormatType_CP850
Resource_FormatType_GBK = Resource_FormatType.Resource_FormatType_GBK
Resource_FormatType_Big5 = Resource_FormatType.Resource_FormatType_Big5
Resource_FormatType_ANSI = Resource_FormatType.Resource_FormatType_ANSI
Resource_SJIS = Resource_FormatType.Resource_SJIS
Resource_EUC = Resource_FormatType.Resource_EUC
Resource_ANSI = Resource_FormatType.Resource_ANSI
Resource_GB = Resource_FormatType.Resource_GB

class Resource_LexicalCompare:
    def __init__(self) -> None: ...
    def IsLower(self, Left: str, Right: str) -> bool: ...

class Resource_Manager(Standard_Transient):
    @overload
    def __init__(self, aName: str, Verbose: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        theName: str,
        theDefaultsDirectory: str,
        theUserDefaultsDirectory: str,
        theIsVerbose: Optional[bool] = False,
    ) -> None: ...
    def ExtValue(self, aResourceName: str) -> Standard_ExtString: ...
    @overload
    def Find(self, aResource: str) -> bool: ...
    @overload
    def Find(self, theResource: str, theValue: str) -> bool: ...
    def GetMap(
        self, theRefMap: Optional[bool] = True
    ) -> Resource_DataMapOfAsciiStringAsciiString: ...
    @staticmethod
    def GetResourcePath(aPath: str, aName: str, isUserDefaults: bool) -> None: ...
    def Integer(self, aResourceName: str) -> int: ...
    def Real(self, aResourceName: str) -> float: ...
    def Save(self) -> bool: ...
    @overload
    def SetResource(self, aResourceName: str, aValue: int) -> None: ...
    @overload
    def SetResource(self, aResourceName: str, aValue: float) -> None: ...
    @overload
    def SetResource(self, aResourceName: str, aValue: str) -> None: ...
    @overload
    def SetResource(self, aResourceName: str, aValue: Standard_ExtString) -> None: ...
    def Value(self, aResourceName: str) -> str: ...

class Resource_Unicode:
    @staticmethod
    def ConvertBig5ToUnicode(fromstr: str, tostr: str) -> bool: ...
    @staticmethod
    def ConvertEUCToUnicode(fromstr: str, tostr: str) -> None: ...
    @overload
    @staticmethod
    def ConvertFormatToUnicode(theFromStr: str, theToStr: str) -> None: ...
    @overload
    @staticmethod
    def ConvertFormatToUnicode(
        theFormat: Resource_FormatType, theFromStr: str, theToStr: str
    ) -> None: ...
    @staticmethod
    def ConvertGBKToUnicode(fromstr: str, tostr: str) -> bool: ...
    @staticmethod
    def ConvertGBToUnicode(fromstr: str, tostr: str) -> None: ...
    @staticmethod
    def ConvertSJISToUnicode(fromstr: str, tostr: str) -> None: ...
    @staticmethod
    def ConvertUnicodeToANSI(
        fromstr: str, tostr: Standard_PCharacter, maxsize: int
    ) -> bool: ...
    @staticmethod
    def ConvertUnicodeToEUC(
        fromstr: str, tostr: Standard_PCharacter, maxsize: int
    ) -> bool: ...
    @overload
    @staticmethod
    def ConvertUnicodeToFormat(
        theFormat: Resource_FormatType,
        theFromStr: str,
        theToStr: Standard_PCharacter,
        theMaxSize: int,
    ) -> bool: ...
    @overload
    @staticmethod
    def ConvertUnicodeToFormat(
        theFromStr: str, theToStr: Standard_PCharacter, theMaxSize: int
    ) -> bool: ...
    @staticmethod
    def ConvertUnicodeToGB(
        fromstr: str, tostr: Standard_PCharacter, maxsize: int
    ) -> bool: ...
    @staticmethod
    def ConvertUnicodeToSJIS(
        fromstr: str, tostr: Standard_PCharacter, maxsize: int
    ) -> bool: ...
    @staticmethod
    def GetFormat() -> Resource_FormatType: ...
    @staticmethod
    def ReadFormat() -> None: ...
    @staticmethod
    def SetFormat(typecode: Resource_FormatType) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
