from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.Interface import *
from OCC.Core.TColStd import *
from OCC.Core.Resource import *


class StepData_Array1OfField:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> StepData_Field: ...
    def __setitem__(self, index: int, value: StepData_Field) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[StepData_Field]: ...
    def next(self) -> StepData_Field: ...
    __next__ = next
    def Init(self, theValue: StepData_Field) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> StepData_Field: ...
    def Last(self) -> StepData_Field: ...
    def Value(self, theIndex: int) -> StepData_Field: ...
    def SetValue(self, theIndex: int, theValue: StepData_Field) -> None: ...

class StepData_Logical(IntEnum):
    StepData_LFalse: int = ...
    StepData_LTrue: int = ...
    StepData_LUnknown: int = ...

StepData_LFalse = StepData_Logical.StepData_LFalse
StepData_LTrue = StepData_Logical.StepData_LTrue
StepData_LUnknown = StepData_Logical.StepData_LUnknown

class stepdata:
    @staticmethod
    def AddHeaderProtocol(headerproto: StepData_Protocol) -> None: ...
    @staticmethod
    def HeaderProtocol() -> StepData_Protocol: ...
    @staticmethod
    def Init() -> None: ...
    @staticmethod
    def Protocol() -> StepData_Protocol: ...

class StepData_ConfParameters:
    def __init__(self) -> None: ...
    def InitFromStatic(self) -> None: ...
    def Reset(self) -> None: ...

class StepData_Described(Standard_Transient):
    def As(self, steptype: str) -> StepData_Simple: ...
    def CField(self, name: str) -> StepData_Field: ...
    def Check(self, ach: Interface_Check) -> None: ...
    def Description(self) -> StepData_EDescr: ...
    def Field(self, name: str) -> StepData_Field: ...
    def HasField(self, name: str) -> bool: ...
    def IsComplex(self) -> bool: ...
    def Matches(self, steptype: str) -> bool: ...
    def Shared(self, list: Interface_EntityIterator) -> None: ...

class StepData_EDescr(Standard_Transient):
    def IsComplex(self) -> bool: ...
    def Matches(self, steptype: str) -> bool: ...
    def NewEntity(self) -> StepData_Described: ...

class StepData_EnumTool:
    def __init__(self, e0: Optional[str] = "", e1: Optional[str] = "", e2: Optional[str] = "", e3: Optional[str] = "", e4: Optional[str] = "", e5: Optional[str] = "", e6: Optional[str] = "", e7: Optional[str] = "", e8: Optional[str] = "", e9: Optional[str] = "", e10: Optional[str] = "", e11: Optional[str] = "", e12: Optional[str] = "", e13: Optional[str] = "", e14: Optional[str] = "", e15: Optional[str] = "", e16: Optional[str] = "", e17: Optional[str] = "", e18: Optional[str] = "", e19: Optional[str] = "", e20: Optional[str] = "", e21: Optional[str] = "", e22: Optional[str] = "", e23: Optional[str] = "", e24: Optional[str] = "", e25: Optional[str] = "", e26: Optional[str] = "", e27: Optional[str] = "", e28: Optional[str] = "", e29: Optional[str] = "", e30: Optional[str] = "", e31: Optional[str] = "", e32: Optional[str] = "", e33: Optional[str] = "", e34: Optional[str] = "", e35: Optional[str] = "", e36: Optional[str] = "", e37: Optional[str] = "", e38: Optional[str] = "", e39: Optional[str] = "") -> None: ...
    def AddDefinition(self, term: str) -> None: ...
    def IsSet(self) -> bool: ...
    def MaxValue(self) -> int: ...
    def NullValue(self) -> int: ...
    def Optional(self, mode: bool) -> None: ...
    def Text(self, num: int) -> str: ...
    @overload
    def Value(self, txt: str) -> int: ...
    @overload
    def Value(self, txt: str) -> int: ...

class StepData_Factors:
    def __init__(self) -> None: ...
    def CascadeUnit(self) -> float: ...
    def FactorDegreeRadian(self) -> float: ...
    def FactorRadianDegree(self) -> float: ...
    def InitializeFactors(self, theLengthFactor: float, thePlaneAngleFactor: float, theSolidAngleFactor: float) -> None: ...
    def LengthFactor(self) -> float: ...
    def PlaneAngleFactor(self) -> float: ...
    def SetCascadeUnit(self, theUnit: float) -> None: ...
    def SolidAngleFactor(self) -> float: ...

class StepData_Field:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: StepData_Field, copy: Optional[bool] = False) -> None: ...
    def Arity(self) -> int: ...
    def Boolean(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> bool: ...
    def Clear(self, kind: Optional[int] = 0) -> None: ...
    def ClearItem(self, num: int) -> None: ...
    def CopyFrom(self, other: StepData_Field) -> None: ...
    def Entity(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> Standard_Transient: ...
    def Enum(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> int: ...
    def EnumText(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> str: ...
    def Int(self) -> int: ...
    def Integer(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> int: ...
    def IsSet(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> bool: ...
    def ItemKind(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> int: ...
    def Kind(self, type: Optional[bool] = True) -> int: ...
    def Length(self, index: Optional[int] = 1) -> int: ...
    def Logical(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> StepData_Logical: ...
    def Lower(self, index: Optional[int] = 1) -> int: ...
    def Real(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> float: ...
    def Set(self, val: Standard_Transient) -> None: ...
    @overload
    def SetBoolean(self, val: Optional[bool] = False) -> None: ...
    @overload
    def SetBoolean(self, num: int, val: bool) -> None: ...
    def SetDerived(self) -> None: ...
    @overload
    def SetEntity(self, val: Standard_Transient) -> None: ...
    @overload
    def SetEntity(self) -> None: ...
    @overload
    def SetEntity(self, num: int, val: Standard_Transient) -> None: ...
    @overload
    def SetEnum(self, val: Optional[int] = -1, text: Optional[str] = "") -> None: ...
    @overload
    def SetEnum(self, num: int, val: int, text: Optional[str] = "") -> None: ...
    @overload
    def SetInt(self, val: int) -> None: ...
    @overload
    def SetInt(self, num: int, val: int, kind: int) -> None: ...
    @overload
    def SetInteger(self, val: Optional[int] = 0) -> None: ...
    @overload
    def SetInteger(self, num: int, val: int) -> None: ...
    def SetList(self, size: int, first: Optional[int] = 1) -> None: ...
    def SetList2(self, siz1: int, siz2: int, f1: Optional[int] = 1, f2: Optional[int] = 1) -> None: ...
    @overload
    def SetLogical(self, val: Optional[StepData_Logical] = StepData_LFalse) -> None: ...
    @overload
    def SetLogical(self, num: int, val: StepData_Logical) -> None: ...
    @overload
    def SetReal(self, val: Optional[float] = 0.0) -> None: ...
    @overload
    def SetReal(self, num: int, val: float) -> None: ...
    def SetSelectMember(self, val: StepData_SelectMember) -> None: ...
    @overload
    def SetString(self, val: Optional[str] = "") -> None: ...
    @overload
    def SetString(self, num: int, val: str) -> None: ...
    def String(self, n1: Optional[int] = 1, n2: Optional[int] = 1) -> str: ...
    def Transient(self) -> Standard_Transient: ...

class StepData_FieldList:
    def __init__(self) -> None: ...
    def CField(self, num: int) -> StepData_Field: ...
    def Field(self, num: int) -> StepData_Field: ...
    def FillShared(self, iter: Interface_EntityIterator) -> None: ...
    def NbFields(self) -> int: ...

class StepData_FileRecognizer(Standard_Transient):
    def Add(self, reco: StepData_FileRecognizer) -> None: ...
    def Evaluate(self, akey: str, res: Standard_Transient) -> bool: ...
    def Result(self) -> Standard_Transient: ...

class StepData_GeneralModule(Interface_GeneralModule):
    def CheckCase(self, casenum: int, ent: Standard_Transient, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
    def CopyCase(self, casenum: int, entfrom: Standard_Transient, entto: Standard_Transient, TC: Interface_CopyTool) -> None: ...
    def FillSharedCase(self, casenum: int, ent: Standard_Transient, iter: Interface_EntityIterator) -> None: ...

class StepData_GlobalNodeOfWriterLib(Standard_Transient):
    def __init__(self) -> None: ...
    def Add(self, amodule: StepData_ReadWriteModule, aprotocol: StepData_Protocol) -> None: ...
    def Module(self) -> StepData_ReadWriteModule: ...
    def Next(self) -> StepData_GlobalNodeOfWriterLib: ...
    def Protocol(self) -> StepData_Protocol: ...

class StepData_NodeOfWriterLib(Standard_Transient):
    def __init__(self) -> None: ...
    def AddNode(self, anode: StepData_GlobalNodeOfWriterLib) -> None: ...
    def Module(self) -> StepData_ReadWriteModule: ...
    def Next(self) -> StepData_NodeOfWriterLib: ...
    def Protocol(self) -> StepData_Protocol: ...

class StepData_PDescr(Standard_Transient):
    def __init__(self) -> None: ...
    def AddArity(self, arity: Optional[int] = 1) -> None: ...
    def AddEnumDef(self, enumdef: str) -> None: ...
    def AddMember(self, member: StepData_PDescr) -> None: ...
    def Arity(self) -> int: ...
    def Check(self, afild: StepData_Field, ach: Interface_Check) -> None: ...
    def DescrName(self) -> str: ...
    def EnumMax(self) -> int: ...
    def EnumText(self, val: int) -> str: ...
    def EnumValue(self, name: str) -> int: ...
    def FieldName(self) -> str: ...
    def FieldRank(self) -> int: ...
    def IsBoolean(self) -> bool: ...
    def IsDerived(self) -> bool: ...
    def IsDescr(self, descr: StepData_EDescr) -> bool: ...
    def IsEntity(self) -> bool: ...
    def IsEnum(self) -> bool: ...
    def IsField(self) -> bool: ...
    def IsInteger(self) -> bool: ...
    def IsLogical(self) -> bool: ...
    def IsOptional(self) -> bool: ...
    def IsReal(self) -> bool: ...
    def IsSelect(self) -> bool: ...
    def IsString(self) -> bool: ...
    def IsType(self, atype: Standard_Type) -> bool: ...
    def Member(self, name: str) -> StepData_PDescr: ...
    def Name(self) -> str: ...
    def SetArity(self, arity: Optional[int] = 1) -> None: ...
    def SetBoolean(self) -> None: ...
    def SetDerived(self, der: Optional[bool] = True) -> None: ...
    def SetDescr(self, dscnam: str) -> None: ...
    def SetEnum(self) -> None: ...
    def SetField(self, name: str, rank: int) -> None: ...
    def SetFrom(self, other: StepData_PDescr) -> None: ...
    def SetInteger(self) -> None: ...
    def SetLogical(self) -> None: ...
    def SetMemberName(self, memname: str) -> None: ...
    def SetName(self, name: str) -> None: ...
    def SetOptional(self, opt: Optional[bool] = True) -> None: ...
    def SetReal(self) -> None: ...
    def SetSelect(self) -> None: ...
    def SetString(self) -> None: ...
    def SetType(self, atype: Standard_Type) -> None: ...
    def Simple(self) -> StepData_PDescr: ...
    def Type(self) -> Standard_Type: ...

class StepData_Protocol(Interface_Protocol):
    def __init__(self) -> None: ...
    def AddBasicDescr(self, esdescr: StepData_ESDescr) -> None: ...
    def AddDescr(self, adescr: StepData_EDescr, CN: int) -> None: ...
    def AddPDescr(self, pdescr: StepData_PDescr) -> None: ...
    def BasicDescr(self, name: str, anylevel: Optional[bool] = True) -> StepData_EDescr: ...
    def CaseNumber(self, obj: Standard_Transient) -> int: ...
    @overload
    def Descr(self, num: int) -> StepData_EDescr: ...
    @overload
    def Descr(self, name: str, anylevel: Optional[bool] = True) -> StepData_EDescr: ...
    def DescrNumber(self, adescr: StepData_EDescr) -> int: ...
    def ECDescr(self, names: TColStd_SequenceOfAsciiString, anylevel: Optional[bool] = True) -> StepData_ECDescr: ...
    def ESDescr(self, name: str, anylevel: Optional[bool] = True) -> StepData_ESDescr: ...
    def HasDescr(self) -> bool: ...
    def IsSuitableModel(self, model: Interface_InterfaceModel) -> bool: ...
    def IsUnknownEntity(self, ent: Standard_Transient) -> bool: ...
    def NbResources(self) -> int: ...
    def NewModel(self) -> Interface_InterfaceModel: ...
    def PDescr(self, name: str, anylevel: Optional[bool] = True) -> StepData_PDescr: ...
    def Resource(self, num: int) -> Interface_Protocol: ...
    def SchemaName(self) -> str: ...
    def TypeNumber(self, atype: Standard_Type) -> int: ...
    def UnknownEntity(self) -> Standard_Transient: ...

class StepData_ReadWriteModule(Interface_ReaderModule):
    def CaseNum(self, data: Interface_FileReaderData, num: int) -> int: ...
    @overload
    def CaseStep(self, atype: str) -> int: ...
    @overload
    def CaseStep(self, types: TColStd_SequenceOfAsciiString) -> int: ...
    def ComplexType(self, CN: int, types: TColStd_SequenceOfAsciiString) -> bool: ...
    def IsComplex(self, CN: int) -> bool: ...
    def Read(self, CN: int, data: Interface_FileReaderData, num: int, ach: Interface_Check, ent: Standard_Transient) -> None: ...
    def ReadStep(self, CN: int, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: Standard_Transient) -> None: ...
    def ShortType(self, CN: int) -> str: ...
    def StepType(self, CN: int) -> str: ...
    def WriteStep(self, CN: int, SW: StepData_StepWriter, ent: Standard_Transient) -> None: ...

class StepData_SelectMember(Standard_Transient):
    def __init__(self) -> None: ...
    def Boolean(self) -> bool: ...
    def Enum(self) -> int: ...
    def EnumText(self) -> str: ...
    def HasName(self) -> bool: ...
    def Int(self) -> int: ...
    def Integer(self) -> int: ...
    def Kind(self) -> int: ...
    def Logical(self) -> StepData_Logical: ...
    def Matches(self, name: str) -> bool: ...
    def Name(self) -> str: ...
    def ParamType(self) -> Interface_ParamType: ...
    def Real(self) -> float: ...
    def SetBoolean(self, val: bool) -> None: ...
    def SetEnum(self, val: int, text: Optional[str] = "") -> None: ...
    def SetEnumText(self, val: int, text: str) -> None: ...
    def SetInt(self, val: int) -> None: ...
    def SetInteger(self, val: int) -> None: ...
    def SetKind(self, kind: int) -> None: ...
    def SetLogical(self, val: StepData_Logical) -> None: ...
    def SetName(self, name: str) -> bool: ...
    def SetReal(self, val: float) -> None: ...
    def SetString(self, val: str) -> None: ...
    def String(self) -> str: ...

class StepData_SelectType:
    def Boolean(self) -> bool: ...
    def CaseMem(self, ent: StepData_SelectMember) -> int: ...
    def CaseMember(self) -> int: ...
    def CaseNum(self, ent: Standard_Transient) -> int: ...
    def CaseNumber(self) -> int: ...
    def Description(self) -> StepData_PDescr: ...
    def Int(self) -> int: ...
    def Integer(self) -> int: ...
    def IsNull(self) -> bool: ...
    def Logical(self) -> StepData_Logical: ...
    def Matches(self, ent: Standard_Transient) -> bool: ...
    def Member(self) -> StepData_SelectMember: ...
    def NewMember(self) -> StepData_SelectMember: ...
    def Nullify(self) -> None: ...
    def Real(self) -> float: ...
    def SelectName(self) -> str: ...
    def SetBoolean(self, val: bool, name: Optional[str] = "") -> None: ...
    def SetInt(self, val: int) -> None: ...
    def SetInteger(self, val: int, name: Optional[str] = "") -> None: ...
    def SetLogical(self, val: StepData_Logical, name: Optional[str] = "") -> None: ...
    def SetReal(self, val: float, name: Optional[str] = "") -> None: ...
    def SetValue(self, ent: Standard_Transient) -> None: ...
    def Type(self) -> Standard_Type: ...
    def Value(self) -> Standard_Transient: ...

class StepData_StepDumper:
    def __init__(self, amodel: StepData_StepModel, protocol: StepData_Protocol, mode: Optional[int] = 0) -> None: ...
    @overload
    def Dump(self, ent: Standard_Transient, level: int) -> Tuple[bool, str]: ...
    @overload
    def Dump(self, num: int, level: int) -> Tuple[bool, str]: ...
    def StepWriter(self) -> StepData_StepWriter: ...

class StepData_StepModel(Interface_InterfaceModel):
    def __init__(self) -> None: ...
    def AddHeaderEntity(self, ent: Standard_Transient) -> None: ...
    def ClearHeader(self) -> None: ...
    def ClearLabels(self) -> None: ...
    def DumpHeader(self, level: Optional[int] = 0) -> str: ...
    def Entity(self, num: int) -> Standard_Transient: ...
    def GetFromAnother(self, other: Interface_InterfaceModel) -> None: ...
    def HasHeaderEntity(self, atype: Standard_Type) -> bool: ...
    def Header(self) -> Interface_EntityIterator: ...
    def HeaderEntity(self, atype: Standard_Type) -> Standard_Transient: ...
    def IdentLabel(self, ent: Standard_Transient) -> int: ...
    def IsInitializedUnit(self) -> bool: ...
    def LocalLengthUnit(self) -> float: ...
    def NewEmptyModel(self) -> Interface_InterfaceModel: ...
    def PrintLabel(self, ent: Standard_Transient) -> str: ...
    def SetIdentLabel(self, ent: Standard_Transient, ident: int) -> None: ...
    def SetLocalLengthUnit(self, theUnit: float) -> None: ...
    def SetSourceCodePage(self, theCode: Resource_FormatType) -> None: ...
    def SetWriteLengthUnit(self, theUnit: float) -> None: ...
    def SourceCodePage(self) -> Resource_FormatType: ...
    def StringLabel(self, ent: Standard_Transient) -> TCollection_HAsciiString: ...
    def VerifyCheck(self, ach: Interface_Check) -> None: ...
    def WriteLengthUnit(self) -> float: ...

class StepData_StepReaderData(Interface_FileReaderData):
    def __init__(self, nbheader: int, nbtotal: int, nbpar: int, theSourceCodePage: Optional[Resource_FormatType] = Resource_FormatType_UTF8) -> None: ...
    def AddStepParam(self, num: int, aval: str, atype: Interface_ParamType, nument: Optional[int] = 0) -> None: ...
    def CType(self, num: int) -> str: ...
    def CheckDerived(self, num: int, nump: int, mess: str, ach: Interface_Check, errstat: Optional[bool] = False) -> bool: ...
    def CheckNbParams(self, num: int, nbreq: int, ach: Interface_Check, mess: Optional[str] = "") -> bool: ...
    def ComplexType(self, num: int, types: TColStd_SequenceOfAsciiString) -> None: ...
    def FailEnumValue(self, num: int, nump: int, mess: str, ach: Interface_Check) -> None: ...
    def FindNextHeaderRecord(self, num: int) -> int: ...
    def FindNextRecord(self, num: int) -> int: ...
    def GlobalCheck(self) -> Interface_Check: ...
    def IsComplex(self, num: int) -> bool: ...
    @overload
    def NamedForComplex(self, name: str, num0: int, ach: Interface_Check) -> Tuple[bool, int]: ...
    @overload
    def NamedForComplex(self, theName: str, theShortName: str, num0: int, ach: Interface_Check) -> Tuple[bool, int]: ...
    def NbEntities(self) -> int: ...
    def NextForComplex(self, num: int) -> int: ...
    def PrepareHeader(self) -> None: ...
    def ReadAny(self, num: int, nump: int, mess: str, ach: Interface_Check, descr: StepData_PDescr, val: Standard_Transient) -> bool: ...
    def ReadBoolean(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, bool]: ...
    def ReadEnum(self, num: int, nump: int, mess: str, ach: Interface_Check, enumtool: StepData_EnumTool) -> Tuple[bool, int]: ...
    def ReadEnumParam(self, num: int, nump: int, mess: str, ach: Interface_Check, text: str) -> bool: ...
    def ReadField(self, num: int, nump: int, mess: str, ach: Interface_Check, descr: StepData_PDescr, fild: StepData_Field) -> bool: ...
    def ReadInteger(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, int]: ...
    def ReadList(self, num: int, ach: Interface_Check, descr: StepData_ESDescr, list: StepData_FieldList) -> bool: ...
    def ReadLogical(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, StepData_Logical]: ...
    def ReadReal(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, float]: ...
    def ReadString(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, str]: ...
    def ReadSub(self, numsub: int, mess: str, ach: Interface_Check, descr: StepData_PDescr, val: Standard_Transient) -> int: ...
    def ReadSubList(self, num: int, nump: int, mess: str, ach: Interface_Check, optional: Optional[bool] = False, lenmin: Optional[int] = 0, lenmax: Optional[int] = 0) -> Tuple[bool, int]: ...
    def ReadTypedParam(self, num: int, nump: int, mustbetyped: bool, mess: str, ach: Interface_Check, typ: str) -> Tuple[bool, int, int]: ...
    def ReadXY(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, float, float]: ...
    def ReadXYZ(self, num: int, nump: int, mess: str, ach: Interface_Check) -> Tuple[bool, float, float, float]: ...
    def RecordIdent(self, num: int) -> int: ...
    def RecordType(self, num: int) -> str: ...
    def SetEntityNumbers(self, withmap: Optional[bool] = True) -> None: ...
    def SetRecord(self, num: int, ident: str, type: str, nbpar: int) -> None: ...
    def SubListNumber(self, num: int, nump: int, aslast: bool) -> int: ...

class StepData_StepReaderTool(Interface_FileReaderTool):
    def __init__(self, reader: StepData_StepReaderData, protocol: StepData_Protocol) -> None: ...
    def AnalyseRecord(self, num: int, anent: Standard_Transient, acheck: Interface_Check) -> bool: ...
    def BeginRead(self, amodel: Interface_InterfaceModel) -> None: ...
    def EndRead(self, amodel: Interface_InterfaceModel) -> None: ...
    @overload
    def Prepare(self, optimize: Optional[bool] = True) -> None: ...
    @overload
    def Prepare(self, reco: StepData_FileRecognizer, optimize: Optional[bool] = True) -> None: ...
    def PrepareHeader(self, reco: StepData_FileRecognizer) -> None: ...
    def Recognize(self, num: int, ach: Interface_Check, ent: Standard_Transient) -> bool: ...

class StepData_StepWriter:
    def __init__(self, amodel: StepData_StepModel) -> None: ...
    def AddParam(self) -> None: ...
    def CheckList(self) -> Interface_CheckIterator: ...
    def CloseSub(self) -> None: ...
    def Comment(self, mode: bool) -> None: ...
    def EndComplex(self) -> None: ...
    def EndEntity(self) -> None: ...
    def EndFile(self) -> None: ...
    def EndSec(self) -> None: ...
    def FloatWriter(self) -> Interface_FloatWriter: ...
    def Indent(self, onent: bool) -> None: ...
    def IsInScope(self, num: int) -> bool: ...
    def JoinLast(self, newline: bool) -> None: ...
    def GetLabelMode(self) -> int: ...
    def SetLabelMode(self, value: int) -> None: ...
    def Line(self, num: int) -> TCollection_HAsciiString: ...
    def NbLines(self) -> int: ...
    def NewLine(self, evenempty: bool) -> None: ...
    def OpenSub(self) -> None: ...
    def OpenTypedSub(self, subtype: str) -> None: ...
    def Print(self) -> Tuple[bool, str]: ...
    @overload
    def Send(self, val: int) -> None: ...
    @overload
    def Send(self, val: float) -> None: ...
    @overload
    def Send(self, val: str) -> None: ...
    @overload
    def Send(self, val: Standard_Transient) -> None: ...
    def SendArrReal(self, anArr: TColStd_HArray1OfReal) -> None: ...
    def SendBoolean(self, val: bool) -> None: ...
    @overload
    def SendComment(self, text: TCollection_HAsciiString) -> None: ...
    @overload
    def SendComment(self, text: str) -> None: ...
    def SendData(self) -> None: ...
    def SendDerived(self) -> None: ...
    def SendEndscope(self) -> None: ...
    def SendEntity(self, nument: int, lib: StepData_WriterLib) -> None: ...
    @overload
    def SendEnum(self, val: str) -> None: ...
    @overload
    def SendEnum(self, val: str) -> None: ...
    def SendField(self, fild: StepData_Field, descr: StepData_PDescr) -> None: ...
    def SendHeader(self) -> None: ...
    def SendIdent(self, ident: int) -> None: ...
    def SendList(self, list: StepData_FieldList, descr: StepData_ESDescr) -> None: ...
    def SendLogical(self, val: StepData_Logical) -> None: ...
    def SendModel(self, protocol: StepData_Protocol, headeronly: Optional[bool] = False) -> None: ...
    def SendScope(self) -> None: ...
    def SendSelect(self, sm: StepData_SelectMember, descr: StepData_PDescr) -> None: ...
    @overload
    def SendString(self, val: str) -> None: ...
    @overload
    def SendString(self, val: str) -> None: ...
    def SendUndef(self) -> None: ...
    def SetScope(self, numscope: int, numin: int) -> None: ...
    def StartComplex(self) -> None: ...
    def StartEntity(self, atype: str) -> None: ...
    def GetTypeMode(self) -> int: ...
    def SetTypeMode(self, value: int) -> None: ...

class StepData_WriterLib:
    @overload
    def __init__(self, aprotocol: StepData_Protocol) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def AddProtocol(self, aprotocol: Standard_Transient) -> None: ...
    def Clear(self) -> None: ...
    def Module(self) -> StepData_ReadWriteModule: ...
    def More(self) -> bool: ...
    def Next(self) -> None: ...
    def Protocol(self) -> StepData_Protocol: ...
    def Select(self, obj: Standard_Transient, module: StepData_ReadWriteModule) -> Tuple[bool, int]: ...
    def SetComplete(self) -> None: ...
    @staticmethod
    def SetGlobal(amodule: StepData_ReadWriteModule, aprotocol: StepData_Protocol) -> None: ...
    def Start(self) -> None: ...

class StepData_DefaultGeneral(StepData_GeneralModule):
    def __init__(self) -> None: ...
    def CheckCase(self, casenum: int, ent: Standard_Transient, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
    def CopyCase(self, casenum: int, entfrom: Standard_Transient, entto: Standard_Transient, TC: Interface_CopyTool) -> None: ...
    def FillSharedCase(self, casenum: int, ent: Standard_Transient, iter: Interface_EntityIterator) -> None: ...
    def NewVoid(self, CN: int, entto: Standard_Transient) -> bool: ...

class StepData_ECDescr(StepData_EDescr):
    def __init__(self) -> None: ...
    def Add(self, member: StepData_ESDescr) -> None: ...
    def IsComplex(self) -> bool: ...
    def Matches(self, steptype: str) -> bool: ...
    def Member(self, num: int) -> StepData_ESDescr: ...
    def NbMembers(self) -> int: ...
    def NewEntity(self) -> StepData_Described: ...
    def TypeList(self) -> TColStd_HSequenceOfAsciiString: ...

class StepData_ESDescr(StepData_EDescr):
    def __init__(self, name: str) -> None: ...
    def Base(self) -> StepData_ESDescr: ...
    def Field(self, num: int) -> StepData_PDescr: ...
    def IsComplex(self) -> bool: ...
    def IsSub(self, other: StepData_ESDescr) -> bool: ...
    def Matches(self, steptype: str) -> bool: ...
    def Name(self, num: int) -> str: ...
    def NamedField(self, name: str) -> StepData_PDescr: ...
    def NbFields(self) -> int: ...
    def NewEntity(self) -> StepData_Described: ...
    def Rank(self, name: str) -> int: ...
    def SetBase(self, base: StepData_ESDescr) -> None: ...
    def SetField(self, num: int, name: str, descr: StepData_PDescr) -> None: ...
    def SetNbFields(self, nb: int) -> None: ...
    def SetSuper(self, super: StepData_ESDescr) -> None: ...
    def StepType(self) -> str: ...
    def Super(self) -> StepData_ESDescr: ...
    def TypeName(self) -> str: ...

class StepData_FieldList1(StepData_FieldList):
    def __init__(self) -> None: ...
    def CField(self, num: int) -> StepData_Field: ...
    def Field(self, num: int) -> StepData_Field: ...
    def NbFields(self) -> int: ...

class StepData_FieldListD(StepData_FieldList):
    def __init__(self, nb: int) -> None: ...
    def CField(self, num: int) -> StepData_Field: ...
    def Field(self, num: int) -> StepData_Field: ...
    def NbFields(self) -> int: ...
    def SetNb(self, nb: int) -> None: ...

class StepData_FieldListN(StepData_FieldList):
    def __init__(self, nb: int) -> None: ...
    def CField(self, num: int) -> StepData_Field: ...
    def Field(self, num: int) -> StepData_Field: ...
    def NbFields(self) -> int: ...

class StepData_FileProtocol(StepData_Protocol):
    def __init__(self) -> None: ...
    def Add(self, protocol: StepData_Protocol) -> None: ...
    def GlobalCheck(self, G: Interface_Graph, ach: Interface_Check) -> bool: ...
    def NbResources(self) -> int: ...
    def Resource(self, num: int) -> Interface_Protocol: ...
    def SchemaName(self) -> str: ...
    def TypeNumber(self, atype: Standard_Type) -> int: ...

class StepData_Plex(StepData_Described):
    def __init__(self, descr: StepData_ECDescr) -> None: ...
    def Add(self, member: StepData_Simple) -> None: ...
    def As(self, steptype: str) -> StepData_Simple: ...
    def CField(self, name: str) -> StepData_Field: ...
    def Check(self, ach: Interface_Check) -> None: ...
    def ECDescr(self) -> StepData_ECDescr: ...
    def Field(self, name: str) -> StepData_Field: ...
    def HasField(self, name: str) -> bool: ...
    def IsComplex(self) -> bool: ...
    def Matches(self, steptype: str) -> bool: ...
    def Member(self, num: int) -> StepData_Simple: ...
    def NbMembers(self) -> int: ...
    def Shared(self, list: Interface_EntityIterator) -> None: ...
    def TypeList(self) -> TColStd_HSequenceOfAsciiString: ...

class StepData_SelectInt(StepData_SelectMember):
    def __init__(self) -> None: ...
    def Int(self) -> int: ...
    def Kind(self) -> int: ...
    def SetInt(self, val: int) -> None: ...
    def SetKind(self, kind: int) -> None: ...

class StepData_SelectNamed(StepData_SelectMember):
    def __init__(self) -> None: ...
    def CField(self) -> StepData_Field: ...
    def Field(self) -> StepData_Field: ...
    def HasName(self) -> bool: ...
    def Int(self) -> int: ...
    def Kind(self) -> int: ...
    def Name(self) -> str: ...
    def Real(self) -> float: ...
    def SetInt(self, val: int) -> None: ...
    def SetKind(self, kind: int) -> None: ...
    def SetName(self, name: str) -> bool: ...
    def SetReal(self, val: float) -> None: ...
    def SetString(self, val: str) -> None: ...
    def String(self) -> str: ...

class StepData_SelectReal(StepData_SelectMember):
    def __init__(self) -> None: ...
    def Kind(self) -> int: ...
    def Real(self) -> float: ...
    def SetReal(self, val: float) -> None: ...

class StepData_Simple(StepData_Described):
    def __init__(self, descr: StepData_ESDescr) -> None: ...
    def As(self, steptype: str) -> StepData_Simple: ...
    def CField(self, name: str) -> StepData_Field: ...
    def CFieldNum(self, num: int) -> StepData_Field: ...
    def CFields(self) -> StepData_FieldListN: ...
    def Check(self, ach: Interface_Check) -> None: ...
    def ESDescr(self) -> StepData_ESDescr: ...
    def Field(self, name: str) -> StepData_Field: ...
    def FieldNum(self, num: int) -> StepData_Field: ...
    def Fields(self) -> StepData_FieldListN: ...
    def HasField(self, name: str) -> bool: ...
    def IsComplex(self) -> bool: ...
    def Matches(self, steptype: str) -> bool: ...
    def NbFields(self) -> int: ...
    def Shared(self, list: Interface_EntityIterator) -> None: ...
    def StepType(self) -> str: ...

class StepData_SelectArrReal(StepData_SelectNamed):
    def __init__(self) -> None: ...
    def ArrReal(self) -> TColStd_HArray1OfReal: ...
    def Kind(self) -> int: ...
    def SetArrReal(self, arr: TColStd_HArray1OfReal) -> None: ...

#classnotwrapped
class StepData_FreeFormEntity: ...

#classnotwrapped
class StepData_UndefinedEntity: ...

# harray1 classes

class StepData_HArray1OfField(StepData_Array1OfField, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> StepData_Array1OfField: ...

# harray2 classes
# hsequence classes

