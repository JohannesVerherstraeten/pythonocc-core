from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepDimTol import *

class RWStepDimTol_RWAngularityTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_AngularityTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_AngularityTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_AngularityTolerance
    ) -> None: ...

class RWStepDimTol_RWCircularRunoutTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_CircularRunoutTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_CircularRunoutTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_CircularRunoutTolerance
    ) -> None: ...

class RWStepDimTol_RWCoaxialityTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_CoaxialityTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_CoaxialityTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_CoaxialityTolerance
    ) -> None: ...

class RWStepDimTol_RWCommonDatum:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_CommonDatum,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_CommonDatum, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_CommonDatum
    ) -> None: ...

class RWStepDimTol_RWConcentricityTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ConcentricityTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_ConcentricityTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ConcentricityTolerance
    ) -> None: ...

class RWStepDimTol_RWCylindricityTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_CylindricityTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_CylindricityTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_CylindricityTolerance
    ) -> None: ...

class RWStepDimTol_RWDatum:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_Datum,
    ) -> None: ...
    def Share(self, ent: StepDimTol_Datum, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepDimTol_Datum) -> None: ...

class RWStepDimTol_RWDatumFeature:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumFeature,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_DatumFeature, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumFeature
    ) -> None: ...

class RWStepDimTol_RWDatumReference:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumReference,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_DatumReference, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumReference
    ) -> None: ...

class RWStepDimTol_RWDatumReferenceCompartment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumReferenceCompartment,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_DatumReferenceCompartment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumReferenceCompartment
    ) -> None: ...

class RWStepDimTol_RWDatumReferenceElement:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumReferenceElement,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_DatumReferenceElement, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumReferenceElement
    ) -> None: ...

class RWStepDimTol_RWDatumReferenceModifierWithValue:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumReferenceModifierWithValue,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumReferenceModifierWithValue
    ) -> None: ...

class RWStepDimTol_RWDatumSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumSystem,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_DatumSystem, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumSystem
    ) -> None: ...

class RWStepDimTol_RWDatumTarget:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_DatumTarget,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_DatumTarget, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_DatumTarget
    ) -> None: ...

class RWStepDimTol_RWFlatnessTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_FlatnessTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_FlatnessTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_FlatnessTolerance
    ) -> None: ...

class RWStepDimTol_RWGeneralDatumReference:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeneralDatumReference,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_GeneralDatumReference, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeneralDatumReference
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthDatRef:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRef,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_GeoTolAndGeoTolWthDatRef, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeoTolAndGeoTolWthDatRef
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMaxTol,
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndGeoTolWthMod:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndGeoTolWthMod,
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndModGeoTolAndPosTol,
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthDatRefAndUneqDisGeoTol:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeoTolAndGeoTolWthDatRefAndUneqDisGeoTol,
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthMaxTol:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthMaxTol,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_GeoTolAndGeoTolWthMaxTol, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeoTolAndGeoTolWthMaxTol
    ) -> None: ...

class RWStepDimTol_RWGeoTolAndGeoTolWthMod:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeoTolAndGeoTolWthMod,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_GeoTolAndGeoTolWthMod, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeoTolAndGeoTolWthMod
    ) -> None: ...

class RWStepDimTol_RWGeometricTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_GeometricTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeometricTolerance
    ) -> None: ...

class RWStepDimTol_RWGeometricToleranceRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricToleranceRelationship,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeometricToleranceRelationship,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeometricToleranceRelationship
    ) -> None: ...

class RWStepDimTol_RWGeometricToleranceWithDatumReference:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricToleranceWithDatumReference,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeometricToleranceWithDatumReference,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeometricToleranceWithDatumReference,
    ) -> None: ...

class RWStepDimTol_RWGeometricToleranceWithDefinedAreaUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricToleranceWithDefinedAreaUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeometricToleranceWithDefinedAreaUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeometricToleranceWithDefinedAreaUnit,
    ) -> None: ...

class RWStepDimTol_RWGeometricToleranceWithDefinedUnit:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricToleranceWithDefinedUnit,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeometricToleranceWithDefinedUnit,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeometricToleranceWithDefinedUnit
    ) -> None: ...

class RWStepDimTol_RWGeometricToleranceWithMaximumTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricToleranceWithMaximumTolerance,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeometricToleranceWithMaximumTolerance,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_GeometricToleranceWithMaximumTolerance,
    ) -> None: ...

class RWStepDimTol_RWGeometricToleranceWithModifiers:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_GeometricToleranceWithModifiers,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_GeometricToleranceWithModifiers,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_GeometricToleranceWithModifiers
    ) -> None: ...

class RWStepDimTol_RWLineProfileTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_LineProfileTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_LineProfileTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_LineProfileTolerance
    ) -> None: ...

class RWStepDimTol_RWModifiedGeometricTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ModifiedGeometricTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_ModifiedGeometricTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ModifiedGeometricTolerance
    ) -> None: ...

class RWStepDimTol_RWNonUniformZoneDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_NonUniformZoneDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_NonUniformZoneDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_NonUniformZoneDefinition
    ) -> None: ...

class RWStepDimTol_RWParallelismTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ParallelismTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_ParallelismTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ParallelismTolerance
    ) -> None: ...

class RWStepDimTol_RWPerpendicularityTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_PerpendicularityTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_PerpendicularityTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_PerpendicularityTolerance
    ) -> None: ...

class RWStepDimTol_RWPlacedDatumTargetFeature:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_PlacedDatumTargetFeature,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_PlacedDatumTargetFeature, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_PlacedDatumTargetFeature
    ) -> None: ...

class RWStepDimTol_RWPositionTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_PositionTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_PositionTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_PositionTolerance
    ) -> None: ...

class RWStepDimTol_RWProjectedZoneDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ProjectedZoneDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_ProjectedZoneDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ProjectedZoneDefinition
    ) -> None: ...

class RWStepDimTol_RWRoundnessTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_RoundnessTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_RoundnessTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_RoundnessTolerance
    ) -> None: ...

class RWStepDimTol_RWRunoutZoneDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_RunoutZoneDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_RunoutZoneDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_RunoutZoneDefinition
    ) -> None: ...

class RWStepDimTol_RWRunoutZoneOrientation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_RunoutZoneOrientation,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_RunoutZoneOrientation
    ) -> None: ...

class RWStepDimTol_RWStraightnessTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_StraightnessTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_StraightnessTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_StraightnessTolerance
    ) -> None: ...

class RWStepDimTol_RWSurfaceProfileTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_SurfaceProfileTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_SurfaceProfileTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_SurfaceProfileTolerance
    ) -> None: ...

class RWStepDimTol_RWSymmetryTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_SymmetryTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_SymmetryTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_SymmetryTolerance
    ) -> None: ...

class RWStepDimTol_RWToleranceZone:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ToleranceZone,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_ToleranceZone, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ToleranceZone
    ) -> None: ...

class RWStepDimTol_RWToleranceZoneDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ToleranceZoneDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_ToleranceZoneDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ToleranceZoneDefinition
    ) -> None: ...

class RWStepDimTol_RWToleranceZoneForm:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_ToleranceZoneForm,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_ToleranceZoneForm
    ) -> None: ...

class RWStepDimTol_RWTotalRunoutTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_TotalRunoutTolerance,
    ) -> None: ...
    def Share(
        self, ent: StepDimTol_TotalRunoutTolerance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepDimTol_TotalRunoutTolerance
    ) -> None: ...

class RWStepDimTol_RWUnequallyDisposedGeometricTolerance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepDimTol_UnequallyDisposedGeometricTolerance,
    ) -> None: ...
    def Share(
        self,
        ent: StepDimTol_UnequallyDisposedGeometricTolerance,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepDimTol_UnequallyDisposedGeometricTolerance,
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
