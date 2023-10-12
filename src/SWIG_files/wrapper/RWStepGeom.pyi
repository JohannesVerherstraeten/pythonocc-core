from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepGeom import *

class RWStepGeom_RWAxis1Placement:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Axis1Placement,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_Axis1Placement, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_Axis1Placement
    ) -> None: ...

class RWStepGeom_RWAxis2Placement2d:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Axis2Placement2d,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_Axis2Placement2d, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_Axis2Placement2d
    ) -> None: ...

class RWStepGeom_RWAxis2Placement3d:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Axis2Placement3d,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_Axis2Placement3d, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_Axis2Placement3d
    ) -> None: ...

class RWStepGeom_RWBSplineCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BSplineCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BSplineCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BSplineCurve
    ) -> None: ...

class RWStepGeom_RWBSplineCurveWithKnots:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_BSplineCurveWithKnots,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BSplineCurveWithKnots,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BSplineCurveWithKnots, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BSplineCurveWithKnots
    ) -> None: ...

class RWStepGeom_RWBSplineCurveWithKnotsAndRationalBSplineCurve:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_BSplineCurveWithKnotsAndRationalBSplineCurve,
    ) -> None: ...

class RWStepGeom_RWBSplineSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BSplineSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BSplineSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BSplineSurface
    ) -> None: ...

class RWStepGeom_RWBSplineSurfaceWithKnots:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_BSplineSurfaceWithKnots,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BSplineSurfaceWithKnots,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BSplineSurfaceWithKnots, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BSplineSurfaceWithKnots
    ) -> None: ...

class RWStepGeom_RWBSplineSurfaceWithKnotsAndRationalBSplineSurface:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_BSplineSurfaceWithKnotsAndRationalBSplineSurface,
    ) -> None: ...

class RWStepGeom_RWBezierCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BezierCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BezierCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_BezierCurve) -> None: ...

class RWStepGeom_RWBezierCurveAndRationalBSplineCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BezierCurveAndRationalBSplineCurve,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_BezierCurveAndRationalBSplineCurve,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BezierCurveAndRationalBSplineCurve
    ) -> None: ...

class RWStepGeom_RWBezierSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BezierSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BezierSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BezierSurface
    ) -> None: ...

class RWStepGeom_RWBezierSurfaceAndRationalBSplineSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BezierSurfaceAndRationalBSplineSurface,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_BezierSurfaceAndRationalBSplineSurface,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_BezierSurfaceAndRationalBSplineSurface,
    ) -> None: ...

class RWStepGeom_RWBoundaryCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BoundaryCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_BoundaryCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BoundaryCurve
    ) -> None: ...

class RWStepGeom_RWBoundedCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BoundedCurve,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BoundedCurve
    ) -> None: ...

class RWStepGeom_RWBoundedSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_BoundedSurface,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_BoundedSurface
    ) -> None: ...

class RWStepGeom_RWCartesianPoint:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CartesianPoint,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CartesianPoint
    ) -> None: ...

class RWStepGeom_RWCartesianTransformationOperator:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CartesianTransformationOperator,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_CartesianTransformationOperator,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CartesianTransformationOperator
    ) -> None: ...

class RWStepGeom_RWCartesianTransformationOperator3d:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CartesianTransformationOperator3d,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_CartesianTransformationOperator3d,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CartesianTransformationOperator3d
    ) -> None: ...

class RWStepGeom_RWCircle:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Circle,
    ) -> None: ...
    def Share(self, ent: StepGeom_Circle, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Circle) -> None: ...

class RWStepGeom_RWCompositeCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CompositeCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_CompositeCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CompositeCurve
    ) -> None: ...

class RWStepGeom_RWCompositeCurveOnSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CompositeCurveOnSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_CompositeCurveOnSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CompositeCurveOnSurface
    ) -> None: ...

class RWStepGeom_RWCompositeCurveSegment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CompositeCurveSegment,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_CompositeCurveSegment, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CompositeCurveSegment
    ) -> None: ...

class RWStepGeom_RWConic:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Conic,
    ) -> None: ...
    def Share(self, ent: StepGeom_Conic, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Conic) -> None: ...

class RWStepGeom_RWConicalSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_ConicalSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_ConicalSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_ConicalSurface
    ) -> None: ...

class RWStepGeom_RWCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Curve,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Curve) -> None: ...

class RWStepGeom_RWCurveBoundedSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CurveBoundedSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_CurveBoundedSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CurveBoundedSurface
    ) -> None: ...

class RWStepGeom_RWCurveReplica:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CurveReplica,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_CurveReplica, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CurveReplica
    ) -> None: ...

class RWStepGeom_RWCylindricalSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_CylindricalSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_CylindricalSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_CylindricalSurface
    ) -> None: ...

class RWStepGeom_RWDegeneratePcurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_DegeneratePcurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_DegeneratePcurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_DegeneratePcurve
    ) -> None: ...

class RWStepGeom_RWDegenerateToroidalSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_DegenerateToroidalSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_DegenerateToroidalSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_DegenerateToroidalSurface
    ) -> None: ...

class RWStepGeom_RWDirection:
    def __init__(self) -> None: ...
    def Check(
        self, ent: StepGeom_Direction, shares: Interface_ShareTool, ach: Interface_Check
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Direction,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Direction) -> None: ...

class RWStepGeom_RWElementarySurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_ElementarySurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_ElementarySurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_ElementarySurface
    ) -> None: ...

class RWStepGeom_RWEllipse:
    def __init__(self) -> None: ...
    def Check(
        self, ent: StepGeom_Ellipse, shares: Interface_ShareTool, ach: Interface_Check
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Ellipse,
    ) -> None: ...
    def Share(self, ent: StepGeom_Ellipse, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Ellipse) -> None: ...

class RWStepGeom_RWEvaluatedDegeneratePcurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_EvaluatedDegeneratePcurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_EvaluatedDegeneratePcurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_EvaluatedDegeneratePcurve
    ) -> None: ...

class RWStepGeom_RWGeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_GeomRepContextAndGlobUnitAssCtxAndGlobUncertaintyAssCtx,
    ) -> None: ...

class RWStepGeom_RWGeometricRepresentationContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_GeometricRepresentationContext,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_GeometricRepresentationContext
    ) -> None: ...

class RWStepGeom_RWGeometricRepresentationContextAndGlobalUnitAssignedContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_GeometricRepresentationContextAndGlobalUnitAssignedContext,
    ) -> None: ...

class RWStepGeom_RWGeometricRepresentationContextAndParametricRepresentationContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_GeometricRepresentationContextAndParametricRepresentationContext,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_GeometricRepresentationContextAndParametricRepresentationContext,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_GeometricRepresentationContextAndParametricRepresentationContext,
    ) -> None: ...

class RWStepGeom_RWGeometricRepresentationItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_GeometricRepresentationItem,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_GeometricRepresentationItem
    ) -> None: ...

class RWStepGeom_RWHyperbola:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Hyperbola,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_Hyperbola, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Hyperbola) -> None: ...

class RWStepGeom_RWIntersectionCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_IntersectionCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_IntersectionCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_IntersectionCurve
    ) -> None: ...

class RWStepGeom_RWLine:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Line,
    ) -> None: ...
    def Share(self, ent: StepGeom_Line, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Line) -> None: ...

class RWStepGeom_RWOffsetCurve3d:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_OffsetCurve3d,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_OffsetCurve3d, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_OffsetCurve3d
    ) -> None: ...

class RWStepGeom_RWOffsetSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_OffsetSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_OffsetSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_OffsetSurface
    ) -> None: ...

class RWStepGeom_RWOrientedSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_OrientedSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_OrientedSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_OrientedSurface
    ) -> None: ...

class RWStepGeom_RWOuterBoundaryCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_OuterBoundaryCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_OuterBoundaryCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_OuterBoundaryCurve
    ) -> None: ...

class RWStepGeom_RWParabola:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Parabola,
    ) -> None: ...
    def Share(self, ent: StepGeom_Parabola, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Parabola) -> None: ...

class RWStepGeom_RWPcurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Pcurve,
    ) -> None: ...
    def Share(self, ent: StepGeom_Pcurve, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Pcurve) -> None: ...

class RWStepGeom_RWPlacement:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Placement,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_Placement, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Placement) -> None: ...

class RWStepGeom_RWPlane:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Plane,
    ) -> None: ...
    def Share(self, ent: StepGeom_Plane, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Plane) -> None: ...

class RWStepGeom_RWPoint:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Point,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Point) -> None: ...

class RWStepGeom_RWPointOnCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_PointOnCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_PointOnCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_PointOnCurve
    ) -> None: ...

class RWStepGeom_RWPointOnSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_PointOnSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_PointOnSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_PointOnSurface
    ) -> None: ...

class RWStepGeom_RWPointReplica:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_PointReplica,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_PointReplica, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_PointReplica
    ) -> None: ...

class RWStepGeom_RWPolyline:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Polyline,
    ) -> None: ...
    def Share(self, ent: StepGeom_Polyline, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Polyline) -> None: ...

class RWStepGeom_RWQuasiUniformCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_QuasiUniformCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_QuasiUniformCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_QuasiUniformCurve
    ) -> None: ...

class RWStepGeom_RWQuasiUniformCurveAndRationalBSplineCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_QuasiUniformCurveAndRationalBSplineCurve,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_QuasiUniformCurveAndRationalBSplineCurve,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_QuasiUniformCurveAndRationalBSplineCurve,
    ) -> None: ...

class RWStepGeom_RWQuasiUniformSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_QuasiUniformSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_QuasiUniformSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_QuasiUniformSurface
    ) -> None: ...

class RWStepGeom_RWQuasiUniformSurfaceAndRationalBSplineSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_QuasiUniformSurfaceAndRationalBSplineSurface,
    ) -> None: ...

class RWStepGeom_RWRationalBSplineCurve:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_RationalBSplineCurve,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_RationalBSplineCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_RationalBSplineCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_RationalBSplineCurve
    ) -> None: ...

class RWStepGeom_RWRationalBSplineSurface:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_RationalBSplineSurface,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_RationalBSplineSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_RationalBSplineSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_RationalBSplineSurface
    ) -> None: ...

class RWStepGeom_RWRectangularCompositeSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_RectangularCompositeSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_RectangularCompositeSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_RectangularCompositeSurface
    ) -> None: ...

class RWStepGeom_RWRectangularTrimmedSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_RectangularTrimmedSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_RectangularTrimmedSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_RectangularTrimmedSurface
    ) -> None: ...

class RWStepGeom_RWReparametrisedCompositeCurveSegment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_ReparametrisedCompositeCurveSegment,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_ReparametrisedCompositeCurveSegment,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_ReparametrisedCompositeCurveSegment
    ) -> None: ...

class RWStepGeom_RWSeamCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SeamCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SeamCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_SeamCurve) -> None: ...

class RWStepGeom_RWSphericalSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SphericalSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SphericalSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SphericalSurface
    ) -> None: ...

class RWStepGeom_RWSuParameters:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theAch: Interface_Check,
        theEnt: StepGeom_SuParameters,
    ) -> None: ...
    def Share(
        self, theEnt: StepGeom_SuParameters, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepGeom_SuParameters
    ) -> None: ...

class RWStepGeom_RWSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Surface,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Surface) -> None: ...

class RWStepGeom_RWSurfaceCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SurfaceCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SurfaceCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SurfaceCurve
    ) -> None: ...

class RWStepGeom_RWSurfaceCurveAndBoundedCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SurfaceCurveAndBoundedCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SurfaceCurveAndBoundedCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SurfaceCurveAndBoundedCurve
    ) -> None: ...

class RWStepGeom_RWSurfaceOfLinearExtrusion:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SurfaceOfLinearExtrusion,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SurfaceOfLinearExtrusion, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SurfaceOfLinearExtrusion
    ) -> None: ...

class RWStepGeom_RWSurfaceOfRevolution:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SurfaceOfRevolution,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SurfaceOfRevolution, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SurfaceOfRevolution
    ) -> None: ...

class RWStepGeom_RWSurfacePatch:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SurfacePatch,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SurfacePatch, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SurfacePatch
    ) -> None: ...

class RWStepGeom_RWSurfaceReplica:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SurfaceReplica,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SurfaceReplica, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SurfaceReplica
    ) -> None: ...

class RWStepGeom_RWSweptSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_SweptSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_SweptSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_SweptSurface
    ) -> None: ...

class RWStepGeom_RWToroidalSurface:
    def __init__(self) -> None: ...
    def Check(
        self,
        ent: StepGeom_ToroidalSurface,
        shares: Interface_ShareTool,
        ach: Interface_Check,
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_ToroidalSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_ToroidalSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_ToroidalSurface
    ) -> None: ...

class RWStepGeom_RWTrimmedCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_TrimmedCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_TrimmedCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_TrimmedCurve
    ) -> None: ...

class RWStepGeom_RWUniformCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_UniformCurve,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_UniformCurve, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_UniformCurve
    ) -> None: ...

class RWStepGeom_RWUniformCurveAndRationalBSplineCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_UniformCurveAndRationalBSplineCurve,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_UniformCurveAndRationalBSplineCurve,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_UniformCurveAndRationalBSplineCurve
    ) -> None: ...

class RWStepGeom_RWUniformSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_UniformSurface,
    ) -> None: ...
    def Share(
        self, ent: StepGeom_UniformSurface, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepGeom_UniformSurface
    ) -> None: ...

class RWStepGeom_RWUniformSurfaceAndRationalBSplineSurface:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_UniformSurfaceAndRationalBSplineSurface,
    ) -> None: ...
    def Share(
        self,
        ent: StepGeom_UniformSurfaceAndRationalBSplineSurface,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepGeom_UniformSurfaceAndRationalBSplineSurface,
    ) -> None: ...

class RWStepGeom_RWVector:
    def __init__(self) -> None: ...
    def Check(
        self, ent: StepGeom_Vector, shares: Interface_ShareTool, ach: Interface_Check
    ) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepGeom_Vector,
    ) -> None: ...
    def Share(self, ent: StepGeom_Vector, iter: Interface_EntityIterator) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepGeom_Vector) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
