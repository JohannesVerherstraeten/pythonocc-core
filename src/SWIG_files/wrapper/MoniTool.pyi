from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.Message import *
from OCC.Core.OSD import *
from OCC.Core.TColStd import *

# the following typedef cannot be wrapped as is
MoniTool_IndexedDataMapOfShapeTransient = NewType(
    "MoniTool_IndexedDataMapOfShapeTransient", Any
)

class MoniTool_SequenceOfElement:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class MoniTool_ValueType(IntEnum):
    MoniTool_ValueMisc: int = ...
    MoniTool_ValueInteger: int = ...
    MoniTool_ValueReal: int = ...
    MoniTool_ValueIdent: int = ...
    MoniTool_ValueVoid: int = ...
    MoniTool_ValueText: int = ...
    MoniTool_ValueEnum: int = ...
    MoniTool_ValueLogical: int = ...
    MoniTool_ValueSub: int = ...
    MoniTool_ValueHexa: int = ...
    MoniTool_ValueBinary: int = ...

MoniTool_ValueMisc = MoniTool_ValueType.MoniTool_ValueMisc
MoniTool_ValueInteger = MoniTool_ValueType.MoniTool_ValueInteger
MoniTool_ValueReal = MoniTool_ValueType.MoniTool_ValueReal
MoniTool_ValueIdent = MoniTool_ValueType.MoniTool_ValueIdent
MoniTool_ValueVoid = MoniTool_ValueType.MoniTool_ValueVoid
MoniTool_ValueText = MoniTool_ValueType.MoniTool_ValueText
MoniTool_ValueEnum = MoniTool_ValueType.MoniTool_ValueEnum
MoniTool_ValueLogical = MoniTool_ValueType.MoniTool_ValueLogical
MoniTool_ValueSub = MoniTool_ValueType.MoniTool_ValueSub
MoniTool_ValueHexa = MoniTool_ValueType.MoniTool_ValueHexa
MoniTool_ValueBinary = MoniTool_ValueType.MoniTool_ValueBinary

class MoniTool_AttrList:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: MoniTool_AttrList) -> None: ...
    def AttrList(self) -> False: ...
    def Attribute(self, name: str) -> Standard_Transient: ...
    def AttributeType(self, name: str) -> MoniTool_ValueType: ...
    def GetAttribute(
        self, name: str, type: Standard_Type, val: Standard_Transient
    ) -> bool: ...
    def GetAttributes(
        self,
        other: MoniTool_AttrList,
        fromname: Optional[str] = "",
        copied: Optional[bool] = True,
    ) -> None: ...
    def GetIntegerAttribute(self, name: str) -> Tuple[bool, int]: ...
    def GetRealAttribute(self, name: str) -> Tuple[bool, float]: ...
    def GetStringAttribute(self, name: str, val: str) -> bool: ...
    def IntegerAttribute(self, name: str) -> int: ...
    def RealAttribute(self, name: str) -> float: ...
    def RemoveAttribute(self, name: str) -> bool: ...
    def SameAttributes(self, other: MoniTool_AttrList) -> None: ...
    def SetAttribute(self, name: str, val: Standard_Transient) -> None: ...
    def SetIntegerAttribute(self, name: str, val: int) -> None: ...
    def SetRealAttribute(self, name: str, val: float) -> None: ...
    def SetStringAttribute(self, name: str, val: str) -> None: ...
    def StringAttribute(self, name: str) -> str: ...

class MoniTool_CaseData(Standard_Transient):
    def __init__(
        self, caseid: Optional[str] = "", name: Optional[str] = ""
    ) -> None: ...
    def AddAny(self, val: Standard_Transient, name: Optional[str] = "") -> None: ...
    def AddCPU(
        self, lastCPU: float, curCPU: Optional[float] = 0, name: Optional[str] = ""
    ) -> None: ...
    def AddData(
        self, val: Standard_Transient, kind: int, name: Optional[str] = ""
    ) -> None: ...
    def AddEntity(self, ent: Standard_Transient, name: Optional[str] = "") -> None: ...
    def AddGeom(self, geom: Standard_Transient, name: Optional[str] = "") -> None: ...
    def AddInteger(self, val: int, name: Optional[str] = "") -> None: ...
    def AddRaised(
        self, theException: Standard_Failure, name: Optional[str] = ""
    ) -> None: ...
    def AddReal(self, val: float, name: Optional[str] = "") -> None: ...
    def AddReals(self, v1: float, v2: float, name: Optional[str] = "") -> None: ...
    def AddShape(self, sh: TopoDS_Shape, name: Optional[str] = "") -> None: ...
    def AddText(self, text: str, name: Optional[str] = "") -> None: ...
    def AddXY(self, aXY: gp_XY, name: Optional[str] = "") -> None: ...
    def AddXYZ(self, aXYZ: gp_XYZ, name: Optional[str] = "") -> None: ...
    def CaseId(self) -> str: ...
    def Data(self, nd: int) -> Standard_Transient: ...
    @staticmethod
    def DefCheck(acode: str) -> int: ...
    @staticmethod
    def DefMsg(casecode: str) -> str: ...
    def GetCPU(self) -> float: ...
    def GetData(
        self, nd: int, type: Standard_Type, val: Standard_Transient
    ) -> bool: ...
    def Integer(self, nd: int) -> Tuple[bool, int]: ...
    def IsCheck(self) -> bool: ...
    def IsFail(self) -> bool: ...
    def IsWarning(self) -> bool: ...
    def Kind(self, nd: int) -> int: ...
    def LargeCPU(
        self, maxCPU: float, lastCPU: float, curCPU: Optional[float] = 0
    ) -> bool: ...
    def Msg(self) -> Message_Msg: ...
    @overload
    def Name(self) -> str: ...
    @overload
    def Name(self, nd: int) -> str: ...
    def NameNum(self, name: str) -> int: ...
    def NbData(self) -> int: ...
    def Real(self, nd: int) -> Tuple[bool, float]: ...
    def Reals(self, nd: int) -> Tuple[bool, float, float]: ...
    def RemoveData(self, num: int) -> None: ...
    def ResetCheck(self) -> None: ...
    def SetCaseId(self, caseid: str) -> None: ...
    def SetChange(self) -> None: ...
    @staticmethod
    def SetDefFail(acode: str) -> None: ...
    @staticmethod
    def SetDefMsg(casecode: str, mesdef: str) -> None: ...
    @staticmethod
    def SetDefWarning(acode: str) -> None: ...
    def SetFail(self) -> None: ...
    def SetName(self, name: str) -> None: ...
    def SetReplace(self, num: int) -> None: ...
    def SetWarning(self) -> None: ...
    def Shape(self, nd: int) -> TopoDS_Shape: ...
    def Text(self, nd: int, text: str) -> bool: ...
    def XY(self, nd: int, val: gp_XY) -> bool: ...
    def XYZ(self, nd: int, val: gp_XYZ) -> bool: ...

class MoniTool_DataInfo:
    @staticmethod
    def Type(ent: Standard_Transient) -> Standard_Type: ...
    @staticmethod
    def TypeName(ent: Standard_Transient) -> str: ...

class MoniTool_ElemHasher:
    @staticmethod
    def HashCode(theElement: MoniTool_Element, theUpperBound: int) -> int: ...
    @staticmethod
    def IsEqual(K1: MoniTool_Element, K2: MoniTool_Element) -> bool: ...

class MoniTool_Element(Standard_Transient):
    def ChangeAttr(self) -> MoniTool_AttrList: ...
    def Equates(self, other: MoniTool_Element) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ListAttr(self) -> MoniTool_AttrList: ...
    def ValueType(self) -> Standard_Type: ...
    def ValueTypeName(self) -> str: ...

class MoniTool_IntVal(Standard_Transient):
    def __init__(self, val: Optional[int] = 0) -> None: ...
    def GetCValue(self) -> int: ...
    def SetCValue(self, value: int) -> None: ...
    def Value(self) -> int: ...

class MoniTool_MTHasher:
    @staticmethod
    def HashCode(theString: str, theUpperBound: int) -> int: ...
    @staticmethod
    def IsEqual(Str1: str, Str2: str) -> bool: ...

class MoniTool_RealVal(Standard_Transient):
    def __init__(self, val: Optional[float] = 0.0) -> None: ...
    def GetCValue(self) -> float: ...
    def SetCValue(self, value: float) -> None: ...
    def Value(self) -> float: ...

class MoniTool_SignText(Standard_Transient):
    def Name(self) -> str: ...
    def Text(self, ent: Standard_Transient, context: Standard_Transient) -> str: ...
    def TextAlone(self, ent: Standard_Transient) -> str: ...

class MoniTool_Stat:
    @overload
    def __init__(self, title: Optional[str] = "") -> None: ...
    @overload
    def __init__(self, other: MoniTool_Stat) -> None: ...
    def Add(self, nb: Optional[int] = 1) -> None: ...
    def AddEnd(self) -> None: ...
    def AddSub(self, nb: Optional[int] = 1) -> None: ...
    def Close(self, id: int) -> None: ...
    @staticmethod
    def Current() -> MoniTool_Stat: ...
    def Level(self) -> int: ...
    def Open(self, nb: Optional[int] = 100) -> int: ...
    def OpenMore(self, id: int, nb: int) -> None: ...
    def Percent(self, fromlev: Optional[int] = 0) -> float: ...

class MoniTool_Timer(Standard_Transient):
    def __init__(self) -> None: ...
    def Amend(self) -> float: ...
    def CPU(self) -> float: ...
    @staticmethod
    def ClearTimers() -> None: ...
    @staticmethod
    def ComputeAmendments() -> None: ...
    def Count(self) -> int: ...
    @staticmethod
    def Dictionary() -> MoniTool_DataMapOfTimer: ...
    @staticmethod
    def GetAmendments() -> Tuple[float, float, float, float]: ...
    def IsRunning(self) -> int: ...
    def Reset(self) -> None: ...
    @overload
    def Start(self) -> None: ...
    @overload
    @staticmethod
    def Start(name: str) -> None: ...
    @overload
    def Stop(self) -> None: ...
    @overload
    @staticmethod
    def Stop(name: str) -> None: ...
    @overload
    def Timer(self) -> OSD_Timer: ...
    @overload
    def Timer(self) -> OSD_Timer: ...
    @overload
    @staticmethod
    def Timer(name: str) -> MoniTool_Timer: ...

class MoniTool_TimerSentry:
    @overload
    def __init__(self, cname: str) -> None: ...
    @overload
    def __init__(self, timer: MoniTool_Timer) -> None: ...
    def Stop(self) -> None: ...
    def Timer(self) -> MoniTool_Timer: ...

class MoniTool_TypedValue(Standard_Transient):
    @overload
    def __init__(
        self,
        name: str,
        type: Optional[MoniTool_ValueType] = MoniTool_ValueText,
        init: Optional[str] = "",
    ) -> None: ...
    @overload
    def __init__(self, other: MoniTool_TypedValue) -> None: ...
    def AddDef(self, initext: str) -> bool: ...
    def AddEnum(
        self,
        v1: Optional[str] = "",
        v2: Optional[str] = "",
        v3: Optional[str] = "",
        v4: Optional[str] = "",
        v5: Optional[str] = "",
        v6: Optional[str] = "",
        v7: Optional[str] = "",
        v8: Optional[str] = "",
        v9: Optional[str] = "",
        v10: Optional[str] = "",
    ) -> None: ...
    def AddEnumValue(self, val: str, num: int) -> None: ...
    @staticmethod
    def AddLib(tv: MoniTool_TypedValue, def_: Optional[str] = "") -> bool: ...
    def CStringValue(self) -> str: ...
    def ClearValue(self) -> None: ...
    def Definition(self) -> str: ...
    def EnumCase(self, val: str) -> int: ...
    def EnumDef(self) -> Tuple[bool, int, int, bool]: ...
    def EnumVal(self, num: int) -> str: ...
    @staticmethod
    def FromLib(def_: str) -> MoniTool_TypedValue: ...
    def GetObjectValue(self, val: Standard_Transient) -> None: ...
    def HStringValue(self) -> TCollection_HAsciiString: ...
    def HasInterpret(self) -> bool: ...
    def IntegerLimit(self, max: bool) -> Tuple[bool, int]: ...
    def IntegerValue(self) -> int: ...
    def Interpret(
        self, hval: TCollection_HAsciiString, native: bool
    ) -> TCollection_HAsciiString: ...
    def IsSetValue(self) -> bool: ...
    def Label(self) -> str: ...
    @staticmethod
    def Lib(def_: str) -> MoniTool_TypedValue: ...
    @staticmethod
    def LibList() -> TColStd_HSequenceOfAsciiString: ...
    def MaxLength(self) -> int: ...
    def Name(self) -> str: ...
    def ObjectType(self) -> Standard_Type: ...
    def ObjectTypeName(self) -> str: ...
    def ObjectValue(self) -> Standard_Transient: ...
    def RealLimit(self, max: bool) -> Tuple[bool, float]: ...
    def RealValue(self) -> float: ...
    def Satisfies(self, hval: TCollection_HAsciiString) -> bool: ...
    def SatisfiesName(self) -> str: ...
    def SetCStringValue(self, val: str) -> bool: ...
    def SetDefinition(self, deftext: str) -> None: ...
    def SetHStringValue(self, hval: TCollection_HAsciiString) -> bool: ...
    def SetIntegerLimit(self, max: bool, val: int) -> None: ...
    def SetIntegerValue(self, ival: int) -> bool: ...
    def SetInterpret(self, func: MoniTool_ValueInterpret) -> None: ...
    def SetLabel(self, label: str) -> None: ...
    def SetMaxLength(self, max: int) -> None: ...
    def SetObjectType(self, typ: Standard_Type) -> None: ...
    def SetObjectValue(self, obj: Standard_Transient) -> bool: ...
    def SetRealLimit(self, max: bool, val: float) -> None: ...
    def SetRealValue(self, rval: float) -> bool: ...
    def SetSatisfies(self, func: MoniTool_ValueSatisfies, name: str) -> None: ...
    def SetUnitDef(self, def_: str) -> None: ...
    def StartEnum(
        self, start: Optional[int] = 0, match: Optional[bool] = True
    ) -> None: ...
    @staticmethod
    def StaticValue(name: str) -> MoniTool_TypedValue: ...
    def UnitDef(self) -> str: ...
    def ValueType(self) -> MoniTool_ValueType: ...

class MoniTool_SignShape(MoniTool_SignText):
    def __init__(self) -> None: ...
    def Name(self) -> str: ...
    def Text(self, ent: Standard_Transient, context: Standard_Transient) -> str: ...

class MoniTool_TransientElem(MoniTool_Element):
    def __init__(self, akey: Standard_Transient) -> None: ...
    def Equates(self, other: MoniTool_Element) -> bool: ...
    def Value(self) -> Standard_Transient: ...
    def ValueType(self) -> Standard_Type: ...
    def ValueTypeName(self) -> str: ...

# harray1 classes
# harray2 classes
# hsequence classes

class MoniTool_HSequenceOfElement(MoniTool_SequenceOfElement, Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: MoniTool_SequenceOfElement) -> None: ...
    def Sequence(self) -> MoniTool_SequenceOfElement: ...
    def Append(self, theSequence: MoniTool_SequenceOfElement) -> None: ...
