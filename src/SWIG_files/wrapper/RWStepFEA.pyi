from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepFEA import *

class RWStepFEA_RWAlignedCurve3dElementCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_AlignedCurve3dElementCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_AlignedCurve3dElementCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_AlignedCurve3dElementCoordinateSystem,
    ) -> None: ...

class RWStepFEA_RWAlignedSurface3dElementCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_AlignedSurface3dElementCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_AlignedSurface3dElementCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_AlignedSurface3dElementCoordinateSystem,
    ) -> None: ...

class RWStepFEA_RWArbitraryVolume3dElementCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ArbitraryVolume3dElementCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_ArbitraryVolume3dElementCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_ArbitraryVolume3dElementCoordinateSystem,
    ) -> None: ...

class RWStepFEA_RWConstantSurface3dElementCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ConstantSurface3dElementCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_ConstantSurface3dElementCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_ConstantSurface3dElementCoordinateSystem,
    ) -> None: ...

class RWStepFEA_RWCurve3dElementProperty:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_Curve3dElementProperty,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_Curve3dElementProperty, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_Curve3dElementProperty
    ) -> None: ...

class RWStepFEA_RWCurve3dElementRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_Curve3dElementRepresentation,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_Curve3dElementRepresentation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_Curve3dElementRepresentation
    ) -> None: ...

class RWStepFEA_RWCurveElementEndOffset:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_CurveElementEndOffset,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_CurveElementEndOffset, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_CurveElementEndOffset
    ) -> None: ...

class RWStepFEA_RWCurveElementEndRelease:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_CurveElementEndRelease,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_CurveElementEndRelease, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_CurveElementEndRelease
    ) -> None: ...

class RWStepFEA_RWCurveElementInterval:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_CurveElementInterval,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_CurveElementInterval, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_CurveElementInterval
    ) -> None: ...

class RWStepFEA_RWCurveElementIntervalConstant:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_CurveElementIntervalConstant,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_CurveElementIntervalConstant, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_CurveElementIntervalConstant
    ) -> None: ...

class RWStepFEA_RWCurveElementIntervalLinearlyVarying:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_CurveElementIntervalLinearlyVarying,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_CurveElementIntervalLinearlyVarying,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_CurveElementIntervalLinearlyVarying
    ) -> None: ...

class RWStepFEA_RWCurveElementLocation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_CurveElementLocation,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_CurveElementLocation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_CurveElementLocation
    ) -> None: ...

class RWStepFEA_RWDummyNode:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_DummyNode,
    ) -> None: ...
    def Share(self, ent: StepFEA_DummyNode, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_DummyNode) -> None: ...

class RWStepFEA_RWElementGeometricRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ElementGeometricRelationship,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_ElementGeometricRelationship, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_ElementGeometricRelationship
    ) -> None: ...

class RWStepFEA_RWElementGroup:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ElementGroup,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_ElementGroup, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_ElementGroup) -> None: ...

class RWStepFEA_RWElementRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ElementRepresentation,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_ElementRepresentation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_ElementRepresentation
    ) -> None: ...

class RWStepFEA_RWFeaAreaDensity:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaAreaDensity,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaAreaDensity, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaAreaDensity
    ) -> None: ...

class RWStepFEA_RWFeaAxis2Placement3d:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaAxis2Placement3d,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaAxis2Placement3d, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaAxis2Placement3d
    ) -> None: ...

class RWStepFEA_RWFeaCurveSectionGeometricRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaCurveSectionGeometricRelationship,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaCurveSectionGeometricRelationship,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaCurveSectionGeometricRelationship
    ) -> None: ...

class RWStepFEA_RWFeaGroup:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaGroup,
    ) -> None: ...
    def Share(self, ent: StepFEA_FeaGroup, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_FeaGroup) -> None: ...

class RWStepFEA_RWFeaLinearElasticity:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaLinearElasticity,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaLinearElasticity, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaLinearElasticity
    ) -> None: ...

class RWStepFEA_RWFeaMassDensity:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaMassDensity,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaMassDensity, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaMassDensity
    ) -> None: ...

class RWStepFEA_RWFeaMaterialPropertyRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaMaterialPropertyRepresentation,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaMaterialPropertyRepresentation,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaMaterialPropertyRepresentation
    ) -> None: ...

class RWStepFEA_RWFeaMaterialPropertyRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaMaterialPropertyRepresentationItem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaMaterialPropertyRepresentationItem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_FeaMaterialPropertyRepresentationItem,
    ) -> None: ...

class RWStepFEA_RWFeaModel:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaModel,
    ) -> None: ...
    def Share(self, ent: StepFEA_FeaModel, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_FeaModel) -> None: ...

class RWStepFEA_RWFeaModel3d:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaModel3d,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaModel3d, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_FeaModel3d) -> None: ...

class RWStepFEA_RWFeaModelDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaModelDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaModelDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaModelDefinition
    ) -> None: ...

class RWStepFEA_RWFeaMoistureAbsorption:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaMoistureAbsorption,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaMoistureAbsorption, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaMoistureAbsorption
    ) -> None: ...

class RWStepFEA_RWFeaParametricPoint:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaParametricPoint,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaParametricPoint, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaParametricPoint
    ) -> None: ...

class RWStepFEA_RWFeaRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaRepresentationItem,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaRepresentationItem, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaRepresentationItem
    ) -> None: ...

class RWStepFEA_RWFeaSecantCoefficientOfLinearThermalExpansion:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaSecantCoefficientOfLinearThermalExpansion,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaSecantCoefficientOfLinearThermalExpansion,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_FeaSecantCoefficientOfLinearThermalExpansion,
    ) -> None: ...

class RWStepFEA_RWFeaShellBendingStiffness:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaShellBendingStiffness,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaShellBendingStiffness, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaShellBendingStiffness
    ) -> None: ...

class RWStepFEA_RWFeaShellMembraneBendingCouplingStiffness:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaShellMembraneBendingCouplingStiffness,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaShellMembraneBendingCouplingStiffness,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_FeaShellMembraneBendingCouplingStiffness,
    ) -> None: ...

class RWStepFEA_RWFeaShellMembraneStiffness:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaShellMembraneStiffness,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaShellMembraneStiffness, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaShellMembraneStiffness
    ) -> None: ...

class RWStepFEA_RWFeaShellShearStiffness:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaShellShearStiffness,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FeaShellShearStiffness, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FeaShellShearStiffness
    ) -> None: ...

class RWStepFEA_RWFeaSurfaceSectionGeometricRelationship:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaSurfaceSectionGeometricRelationship,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaSurfaceSectionGeometricRelationship,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_FeaSurfaceSectionGeometricRelationship,
    ) -> None: ...

class RWStepFEA_RWFeaTangentialCoefficientOfLinearThermalExpansion:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion,
    ) -> None: ...

class RWStepFEA_RWFreedomAndCoefficient:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FreedomAndCoefficient,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FreedomAndCoefficient, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_FreedomAndCoefficient
    ) -> None: ...

class RWStepFEA_RWFreedomsList:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_FreedomsList,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_FreedomsList, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_FreedomsList) -> None: ...

class RWStepFEA_RWGeometricNode:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_GeometricNode,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_GeometricNode, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_GeometricNode
    ) -> None: ...

class RWStepFEA_RWNode:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_Node,
    ) -> None: ...
    def Share(self, ent: StepFEA_Node, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_Node) -> None: ...

class RWStepFEA_RWNodeDefinition:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_NodeDefinition,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_NodeDefinition, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_NodeDefinition
    ) -> None: ...

class RWStepFEA_RWNodeGroup:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_NodeGroup,
    ) -> None: ...
    def Share(self, ent: StepFEA_NodeGroup, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_NodeGroup) -> None: ...

class RWStepFEA_RWNodeRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_NodeRepresentation,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_NodeRepresentation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_NodeRepresentation
    ) -> None: ...

class RWStepFEA_RWNodeSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_NodeSet,
    ) -> None: ...
    def Share(self, ent: StepFEA_NodeSet, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepFEA_NodeSet) -> None: ...

class RWStepFEA_RWNodeWithSolutionCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_NodeWithSolutionCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_NodeWithSolutionCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_NodeWithSolutionCoordinateSystem
    ) -> None: ...

class RWStepFEA_RWNodeWithVector:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_NodeWithVector,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_NodeWithVector, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_NodeWithVector
    ) -> None: ...

class RWStepFEA_RWParametricCurve3dElementCoordinateDirection:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ParametricCurve3dElementCoordinateDirection,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_ParametricCurve3dElementCoordinateDirection,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_ParametricCurve3dElementCoordinateDirection,
    ) -> None: ...

class RWStepFEA_RWParametricCurve3dElementCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ParametricCurve3dElementCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_ParametricCurve3dElementCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_ParametricCurve3dElementCoordinateSystem,
    ) -> None: ...

class RWStepFEA_RWParametricSurface3dElementCoordinateSystem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_ParametricSurface3dElementCoordinateSystem,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_ParametricSurface3dElementCoordinateSystem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepFEA_ParametricSurface3dElementCoordinateSystem,
    ) -> None: ...

class RWStepFEA_RWSurface3dElementRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_Surface3dElementRepresentation,
    ) -> None: ...
    def Share(
        self,
        ent: StepFEA_Surface3dElementRepresentation,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_Surface3dElementRepresentation
    ) -> None: ...

class RWStepFEA_RWVolume3dElementRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepFEA_Volume3dElementRepresentation,
    ) -> None: ...
    def Share(
        self, ent: StepFEA_Volume3dElementRepresentation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepFEA_Volume3dElementRepresentation
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
