from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepBasic import *
from OCC.Core.TCollection import *

class RWStepBasic_RWAction:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Action,
    ) -> None: ...
    def Share(self, ent: StepBasic_Action, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Action) -> None: ...

class RWStepBasic_RWActionAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ActionAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ActionAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ActionAssignment
    ) -> None: ...

class RWStepBasic_RWActionMethod:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ActionMethod,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ActionMethod, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ActionMethod
    ) -> None: ...

class RWStepBasic_RWActionRequestAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ActionRequestAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ActionRequestAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ActionRequestAssignment
    ) -> None: ...

class RWStepBasic_RWActionRequestSolution:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ActionRequestSolution,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ActionRequestSolution, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ActionRequestSolution
    ) -> None: ...

class RWStepBasic_RWAddress:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Address,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Address) -> None: ...

class RWStepBasic_RWApplicationContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApplicationContext,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApplicationContext
    ) -> None: ...

class RWStepBasic_RWApplicationContextElement:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApplicationContextElement,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ApplicationContextElement, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApplicationContextElement
    ) -> None: ...

class RWStepBasic_RWApplicationProtocolDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApplicationProtocolDefinition,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ApplicationProtocolDefinition,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApplicationProtocolDefinition
    ) -> None: ...

class RWStepBasic_RWApproval:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Approval,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_Approval, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Approval) -> None: ...

class RWStepBasic_RWApprovalDateTime:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApprovalDateTime,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ApprovalDateTime, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApprovalDateTime
    ) -> None: ...

class RWStepBasic_RWApprovalPersonOrganization:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApprovalPersonOrganization,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ApprovalPersonOrganization, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApprovalPersonOrganization
    ) -> None: ...

class RWStepBasic_RWApprovalRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApprovalRelationship,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ApprovalRelationship, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApprovalRelationship
    ) -> None: ...

class RWStepBasic_RWApprovalRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApprovalRole,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApprovalRole
    ) -> None: ...

class RWStepBasic_RWApprovalStatus:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ApprovalStatus,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ApprovalStatus
    ) -> None: ...

class RWStepBasic_RWCalendarDate:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_CalendarDate,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_CalendarDate
    ) -> None: ...

class RWStepBasic_RWCertification:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Certification,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_Certification, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_Certification
    ) -> None: ...

class RWStepBasic_RWCertificationAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_CertificationAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_CertificationAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_CertificationAssignment
    ) -> None: ...

class RWStepBasic_RWCertificationType:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_CertificationType,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_CertificationType, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_CertificationType
    ) -> None: ...

class RWStepBasic_RWCharacterizedObject:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_CharacterizedObject,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_CharacterizedObject, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_CharacterizedObject
    ) -> None: ...

class RWStepBasic_RWContract:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Contract,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_Contract, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Contract) -> None: ...

class RWStepBasic_RWContractAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ContractAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ContractAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ContractAssignment
    ) -> None: ...

class RWStepBasic_RWContractType:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ContractType,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ContractType, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ContractType
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ConversionBasedUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnit
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndAreaUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndAreaUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndAreaUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnitAndAreaUnit
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndLengthUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndLengthUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndLengthUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnitAndLengthUnit
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndMassUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndMassUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndMassUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnitAndMassUnit
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndPlaneAngleUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndPlaneAngleUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndPlaneAngleUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_ConversionBasedUnitAndPlaneAngleUnit,
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndRatioUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndRatioUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndRatioUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnitAndRatioUnit
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndSolidAngleUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndSolidAngleUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndSolidAngleUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_ConversionBasedUnitAndSolidAngleUnit,
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndTimeUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndTimeUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndTimeUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnitAndTimeUnit
    ) -> None: ...

class RWStepBasic_RWConversionBasedUnitAndVolumeUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ConversionBasedUnitAndVolumeUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ConversionBasedUnitAndVolumeUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ConversionBasedUnitAndVolumeUnit
    ) -> None: ...

class RWStepBasic_RWCoordinatedUniversalTimeOffset:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_CoordinatedUniversalTimeOffset,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_CoordinatedUniversalTimeOffset
    ) -> None: ...

class RWStepBasic_RWDate:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Date,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Date) -> None: ...

class RWStepBasic_RWDateAndTime:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DateAndTime,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DateAndTime, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DateAndTime
    ) -> None: ...

class RWStepBasic_RWDateRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DateRole,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_DateRole) -> None: ...

class RWStepBasic_RWDateTimeRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DateTimeRole,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DateTimeRole
    ) -> None: ...

class RWStepBasic_RWDerivedUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DerivedUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DerivedUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DerivedUnit
    ) -> None: ...

class RWStepBasic_RWDerivedUnitElement:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DerivedUnitElement,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DerivedUnitElement, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DerivedUnitElement
    ) -> None: ...

class RWStepBasic_RWDimensionalExponents:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DimensionalExponents,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DimensionalExponents
    ) -> None: ...

class RWStepBasic_RWDocument:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Document,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_Document, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Document) -> None: ...

class RWStepBasic_RWDocumentFile:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentFile,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentFile, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentFile
    ) -> None: ...

class RWStepBasic_RWDocumentProductAssociation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentProductAssociation,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentProductAssociation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentProductAssociation
    ) -> None: ...

class RWStepBasic_RWDocumentProductEquivalence:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentProductEquivalence,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentProductEquivalence, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentProductEquivalence
    ) -> None: ...

class RWStepBasic_RWDocumentRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentRelationship,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentRelationship, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentRelationship
    ) -> None: ...

class RWStepBasic_RWDocumentRepresentationType:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentRepresentationType,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentRepresentationType, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentRepresentationType
    ) -> None: ...

class RWStepBasic_RWDocumentType:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentType,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentType, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentType
    ) -> None: ...

class RWStepBasic_RWDocumentUsageConstraint:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_DocumentUsageConstraint,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_DocumentUsageConstraint, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_DocumentUsageConstraint
    ) -> None: ...

class RWStepBasic_RWEffectivity:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Effectivity,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_Effectivity, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_Effectivity
    ) -> None: ...

class RWStepBasic_RWEffectivityAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_EffectivityAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_EffectivityAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_EffectivityAssignment
    ) -> None: ...

class RWStepBasic_RWEulerAngles:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_EulerAngles,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_EulerAngles, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_EulerAngles
    ) -> None: ...

class RWStepBasic_RWExternalIdentificationAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ExternalIdentificationAssignment,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ExternalIdentificationAssignment,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ExternalIdentificationAssignment
    ) -> None: ...

class RWStepBasic_RWExternalSource:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ExternalSource,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ExternalSource, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ExternalSource
    ) -> None: ...

class RWStepBasic_RWExternallyDefinedItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ExternallyDefinedItem,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ExternallyDefinedItem, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ExternallyDefinedItem
    ) -> None: ...

class RWStepBasic_RWGeneralProperty:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_GeneralProperty,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_GeneralProperty, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_GeneralProperty
    ) -> None: ...

class RWStepBasic_RWGroup:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Group,
    ) -> None: ...
    def Share(self, ent: StepBasic_Group, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Group) -> None: ...

class RWStepBasic_RWGroupAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_GroupAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_GroupAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_GroupAssignment
    ) -> None: ...

class RWStepBasic_RWGroupRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_GroupRelationship,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_GroupRelationship, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_GroupRelationship
    ) -> None: ...

class RWStepBasic_RWIdentificationAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_IdentificationAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_IdentificationAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_IdentificationAssignment
    ) -> None: ...

class RWStepBasic_RWIdentificationRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_IdentificationRole,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_IdentificationRole, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_IdentificationRole
    ) -> None: ...

class RWStepBasic_RWLengthMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_LengthMeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_LengthMeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_LengthMeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWLengthUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_LengthUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_LengthUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_LengthUnit) -> None: ...

class RWStepBasic_RWLocalTime:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_LocalTime,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_LocalTime, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_LocalTime) -> None: ...

class RWStepBasic_RWMassMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_MassMeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_MassMeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_MassMeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWMassUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_MassUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_MassUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_MassUnit) -> None: ...

class RWStepBasic_RWMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_MeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_MeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_MeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWMechanicalContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_MechanicalContext,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_MechanicalContext, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_MechanicalContext
    ) -> None: ...

class RWStepBasic_RWNameAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_NameAssignment,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_NameAssignment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_NameAssignment
    ) -> None: ...

class RWStepBasic_RWNamedUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_NamedUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_NamedUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_NamedUnit) -> None: ...

class RWStepBasic_RWObjectRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ObjectRole,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ObjectRole, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_ObjectRole) -> None: ...

class RWStepBasic_RWOrdinalDate:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_OrdinalDate,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_OrdinalDate
    ) -> None: ...

class RWStepBasic_RWOrganization:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Organization,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_Organization
    ) -> None: ...

class RWStepBasic_RWOrganizationRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_OrganizationRole,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_OrganizationRole
    ) -> None: ...

class RWStepBasic_RWOrganizationalAddress:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_OrganizationalAddress,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_OrganizationalAddress, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_OrganizationalAddress
    ) -> None: ...

class RWStepBasic_RWPerson:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Person,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Person) -> None: ...

class RWStepBasic_RWPersonAndOrganization:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_PersonAndOrganization,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_PersonAndOrganization, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_PersonAndOrganization
    ) -> None: ...

class RWStepBasic_RWPersonAndOrganizationRole:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_PersonAndOrganizationRole,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_PersonAndOrganizationRole
    ) -> None: ...

class RWStepBasic_RWPersonalAddress:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_PersonalAddress,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_PersonalAddress, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_PersonalAddress
    ) -> None: ...

class RWStepBasic_RWPlaneAngleMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_PlaneAngleMeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_PlaneAngleMeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_PlaneAngleMeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWPlaneAngleUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_PlaneAngleUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_PlaneAngleUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_PlaneAngleUnit
    ) -> None: ...

class RWStepBasic_RWProduct:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_Product,
    ) -> None: ...
    def Share(self, ent: StepBasic_Product, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_Product) -> None: ...

class RWStepBasic_RWProductCategory:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductCategory,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductCategory
    ) -> None: ...

class RWStepBasic_RWProductCategoryRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductCategoryRelationship,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductCategoryRelationship, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductCategoryRelationship
    ) -> None: ...

class RWStepBasic_RWProductConceptContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductConceptContext,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductConceptContext, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductConceptContext
    ) -> None: ...

class RWStepBasic_RWProductContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductContext,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductContext, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductContext
    ) -> None: ...

class RWStepBasic_RWProductDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductDefinition
    ) -> None: ...

class RWStepBasic_RWProductDefinitionContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionContext,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductDefinitionContext, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductDefinitionContext
    ) -> None: ...

class RWStepBasic_RWProductDefinitionEffectivity:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionEffectivity,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductDefinitionEffectivity,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductDefinitionEffectivity
    ) -> None: ...

class RWStepBasic_RWProductDefinitionFormation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionFormation,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductDefinitionFormation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductDefinitionFormation
    ) -> None: ...

class RWStepBasic_RWProductDefinitionFormationRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionFormationRelationship,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductDefinitionFormationRelationship,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_ProductDefinitionFormationRelationship,
    ) -> None: ...

class RWStepBasic_RWProductDefinitionFormationWithSpecifiedSource:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionFormationWithSpecifiedSource,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductDefinitionFormationWithSpecifiedSource,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_ProductDefinitionFormationWithSpecifiedSource,
    ) -> None: ...

class RWStepBasic_RWProductDefinitionReference:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionReference,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductDefinitionReference, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductDefinitionReference
    ) -> None: ...

class RWStepBasic_RWProductDefinitionReferenceWithLocalRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionReferenceWithLocalRepresentation,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductDefinitionReferenceWithLocalRepresentation,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_ProductDefinitionReferenceWithLocalRepresentation,
    ) -> None: ...

class RWStepBasic_RWProductDefinitionRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionRelationship,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductDefinitionRelationship,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductDefinitionRelationship
    ) -> None: ...

class RWStepBasic_RWProductDefinitionWithAssociatedDocuments:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductDefinitionWithAssociatedDocuments,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductDefinitionWithAssociatedDocuments,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_ProductDefinitionWithAssociatedDocuments,
    ) -> None: ...

class RWStepBasic_RWProductRelatedProductCategory:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductRelatedProductCategory,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ProductRelatedProductCategory,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductRelatedProductCategory
    ) -> None: ...

class RWStepBasic_RWProductType:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ProductType,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_ProductType, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ProductType
    ) -> None: ...

class RWStepBasic_RWRatioMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_RatioMeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_RatioMeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_RatioMeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWRoleAssociation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_RoleAssociation,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_RoleAssociation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_RoleAssociation
    ) -> None: ...

class RWStepBasic_RWSecurityClassification:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SecurityClassification,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_SecurityClassification, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SecurityClassification
    ) -> None: ...

class RWStepBasic_RWSecurityClassificationLevel:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SecurityClassificationLevel,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SecurityClassificationLevel
    ) -> None: ...

class RWStepBasic_RWSiUnit:
    def __init__(self) -> None: ...
    def DecodeName(self, aName: StepBasic_SiUnitName, text: str) -> bool: ...
    def DecodePrefix(self, aPrefix: StepBasic_SiPrefix, text: str) -> bool: ...
    def EncodeName(self, aName: StepBasic_SiUnitName) -> str: ...
    def EncodePrefix(self, aPrefix: StepBasic_SiPrefix) -> str: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnit,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepBasic_SiUnit) -> None: ...

class RWStepBasic_RWSiUnitAndAreaUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndAreaUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndAreaUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndLengthUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndLengthUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndLengthUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndMassUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndMassUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndMassUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndPlaneAngleUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndPlaneAngleUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndPlaneAngleUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndRatioUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndRatioUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndRatioUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndSolidAngleUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndSolidAngleUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndSolidAngleUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndThermodynamicTemperatureUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndThermodynamicTemperatureUnit,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepBasic_SiUnitAndThermodynamicTemperatureUnit,
    ) -> None: ...

class RWStepBasic_RWSiUnitAndTimeUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndTimeUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndTimeUnit
    ) -> None: ...

class RWStepBasic_RWSiUnitAndVolumeUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SiUnitAndVolumeUnit,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SiUnitAndVolumeUnit
    ) -> None: ...

class RWStepBasic_RWSolidAngleMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SolidAngleMeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_SolidAngleMeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SolidAngleMeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWSolidAngleUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_SolidAngleUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_SolidAngleUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_SolidAngleUnit
    ) -> None: ...

class RWStepBasic_RWThermodynamicTemperatureUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_ThermodynamicTemperatureUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepBasic_ThermodynamicTemperatureUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_ThermodynamicTemperatureUnit
    ) -> None: ...

class RWStepBasic_RWUncertaintyMeasureWithUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_UncertaintyMeasureWithUnit,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_UncertaintyMeasureWithUnit, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_UncertaintyMeasureWithUnit
    ) -> None: ...

class RWStepBasic_RWVersionedActionRequest:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_VersionedActionRequest,
    ) -> None: ...
    def Share(
        self, ent: StepBasic_VersionedActionRequest, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_VersionedActionRequest
    ) -> None: ...

class RWStepBasic_RWWeekOfYearAndDayDate:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepBasic_WeekOfYearAndDayDate,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepBasic_WeekOfYearAndDayDate
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
