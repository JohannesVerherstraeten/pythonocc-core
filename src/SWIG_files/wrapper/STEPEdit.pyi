from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.IFSelect import *
from OCC.Core.Interface import *
from OCC.Core.TCollection import *

class stepedit:
    @staticmethod
    def NewModel() -> StepData_StepModel: ...
    @staticmethod
    def NewSelectPlacedItem() -> IFSelect_SelectSignature: ...
    @staticmethod
    def NewSelectSDR() -> IFSelect_SelectSignature: ...
    @staticmethod
    def NewSelectShapeRepr() -> IFSelect_SelectSignature: ...
    @staticmethod
    def Protocol() -> Interface_Protocol: ...
    @staticmethod
    def SignType() -> IFSelect_Signature: ...

class STEPEdit_EditContext(IFSelect_Editor):
    def __init__(self) -> None: ...
    def Apply(
        self,
        form: IFSelect_EditForm,
        ent: Standard_Transient,
        model: Interface_InterfaceModel,
    ) -> bool: ...
    def Label(self) -> str: ...
    def Load(
        self,
        form: IFSelect_EditForm,
        ent: Standard_Transient,
        model: Interface_InterfaceModel,
    ) -> bool: ...
    def Recognize(self, form: IFSelect_EditForm) -> bool: ...
    def StringValue(
        self, form: IFSelect_EditForm, num: int
    ) -> TCollection_HAsciiString: ...

class STEPEdit_EditSDR(IFSelect_Editor):
    def __init__(self) -> None: ...
    def Apply(
        self,
        form: IFSelect_EditForm,
        ent: Standard_Transient,
        model: Interface_InterfaceModel,
    ) -> bool: ...
    def Label(self) -> str: ...
    def Load(
        self,
        form: IFSelect_EditForm,
        ent: Standard_Transient,
        model: Interface_InterfaceModel,
    ) -> bool: ...
    def Recognize(self, form: IFSelect_EditForm) -> bool: ...
    def StringValue(
        self, form: IFSelect_EditForm, num: int
    ) -> TCollection_HAsciiString: ...

# harray1 classes
# harray2 classes
# hsequence classes
