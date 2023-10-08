from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.HeaderSection import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *

class rwheadersection:
    @staticmethod
    def Init() -> None: ...

class RWHeaderSection_GeneralModule(StepData_GeneralModule):
    def __init__(self) -> None: ...
    def CheckCase(
        self,
        CN: int,
        ent: Standard_Transient,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def CopyCase(
        self,
        CN: int,
        entfrom: Standard_Transient,
        entto: Standard_Transient,
        TC: Interface_CopyTool,
    ) -> None: ...
    def FillSharedCase(
        self, CN: int, ent: Standard_Transient, iter: Interface_EntityIterator
    ) -> None: ...
    def NewVoid(self, CN: int, ent: Standard_Transient) -> bool: ...

class RWHeaderSection_RWFileDescription:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: HeaderSection_FileDescription,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: HeaderSection_FileDescription
    ) -> None: ...

class RWHeaderSection_RWFileName:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: HeaderSection_FileName,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: HeaderSection_FileName
    ) -> None: ...

class RWHeaderSection_RWFileSchema:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: HeaderSection_FileSchema,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: HeaderSection_FileSchema
    ) -> None: ...

class RWHeaderSection_ReadWriteModule(StepData_ReadWriteModule):
    def __init__(self) -> None: ...
    @overload
    def CaseStep(self, atype: str) -> int: ...
    @overload
    def CaseStep(self, types: TColStd_SequenceOfAsciiString) -> int: ...
    def IsComplex(self, CN: int) -> bool: ...
    def ReadStep(
        self,
        CN: int,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: Standard_Transient,
    ) -> None: ...
    def StepType(self, CN: int) -> str: ...
    def WriteStep(
        self, CN: int, SW: StepData_StepWriter, ent: Standard_Transient
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
