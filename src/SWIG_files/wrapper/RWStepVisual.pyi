from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepVisual import *

class RWStepVisual_RWAnnotationCurveOccurrence:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AnnotationCurveOccurrence,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_AnnotationCurveOccurrence, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_AnnotationCurveOccurrence
    ) -> None: ...

class RWStepVisual_RWAnnotationCurveOccurrenceAndGeomReprItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AnnotationCurveOccurrenceAndGeomReprItem,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_AnnotationCurveOccurrenceAndGeomReprItem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_AnnotationCurveOccurrenceAndGeomReprItem,
    ) -> None: ...

class RWStepVisual_RWAnnotationFillArea:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AnnotationFillArea,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_AnnotationFillArea, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_AnnotationFillArea
    ) -> None: ...

class RWStepVisual_RWAnnotationFillAreaOccurrence:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AnnotationFillAreaOccurrence,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_AnnotationFillAreaOccurrence,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_AnnotationFillAreaOccurrence
    ) -> None: ...

class RWStepVisual_RWAnnotationOccurrence:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AnnotationOccurrence,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_AnnotationOccurrence, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_AnnotationOccurrence
    ) -> None: ...

class RWStepVisual_RWAnnotationPlane:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AnnotationPlane,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_AnnotationPlane, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_AnnotationPlane
    ) -> None: ...

class RWStepVisual_RWAreaInSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_AreaInSet,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_AreaInSet, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepVisual_AreaInSet) -> None: ...

class RWStepVisual_RWBackgroundColour:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_BackgroundColour,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_BackgroundColour, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_BackgroundColour
    ) -> None: ...

class RWStepVisual_RWCameraImage:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraImage,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CameraImage, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraImage
    ) -> None: ...

class RWStepVisual_RWCameraModel:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraModel,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraModel
    ) -> None: ...

class RWStepVisual_RWCameraModelD2:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraModelD2,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CameraModelD2, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraModelD2
    ) -> None: ...

class RWStepVisual_RWCameraModelD3:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraModelD3,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CameraModelD3, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraModelD3
    ) -> None: ...

class RWStepVisual_RWCameraModelD3MultiClipping:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraModelD3MultiClipping,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CameraModelD3MultiClipping, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraModelD3MultiClipping
    ) -> None: ...

class RWStepVisual_RWCameraModelD3MultiClippingIntersection:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraModelD3MultiClippingIntersection,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_CameraModelD3MultiClippingIntersection,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_CameraModelD3MultiClippingIntersection,
    ) -> None: ...

class RWStepVisual_RWCameraModelD3MultiClippingUnion:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraModelD3MultiClippingUnion,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_CameraModelD3MultiClippingUnion,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraModelD3MultiClippingUnion
    ) -> None: ...

class RWStepVisual_RWCameraUsage:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CameraUsage,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CameraUsage, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CameraUsage
    ) -> None: ...

class RWStepVisual_RWCharacterizedObjAndRepresentationAndDraughtingModel:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_CharacterizedObjAndRepresentationAndDraughtingModel,
    ) -> None: ...

class RWStepVisual_RWColour:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_Colour,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepVisual_Colour) -> None: ...

class RWStepVisual_RWColourRgb:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_ColourRgb,
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepVisual_ColourRgb) -> None: ...

class RWStepVisual_RWColourSpecification:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_ColourSpecification,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_ColourSpecification
    ) -> None: ...

class RWStepVisual_RWComplexTriangulatedFace:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_ComplexTriangulatedFace,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_ComplexTriangulatedFace,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_ComplexTriangulatedFace
    ) -> None: ...

class RWStepVisual_RWComplexTriangulatedSurfaceSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_ComplexTriangulatedSurfaceSet,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_ComplexTriangulatedSurfaceSet,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        theSW: StepData_StepWriter,
        theEnt: StepVisual_ComplexTriangulatedSurfaceSet,
    ) -> None: ...

class RWStepVisual_RWCompositeText:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CompositeText,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CompositeText, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CompositeText
    ) -> None: ...

class RWStepVisual_RWCompositeTextWithExtent:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CompositeTextWithExtent,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CompositeTextWithExtent, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CompositeTextWithExtent
    ) -> None: ...

class RWStepVisual_RWContextDependentInvisibility:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_ContextDependentInvisibility,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_ContextDependentInvisibility,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_ContextDependentInvisibility
    ) -> None: ...

class RWStepVisual_RWContextDependentOverRidingStyledItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_ContextDependentOverRidingStyledItem,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_ContextDependentOverRidingStyledItem,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_ContextDependentOverRidingStyledItem,
    ) -> None: ...

class RWStepVisual_RWCoordinatesList:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CoordinatesList,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CoordinatesList
    ) -> None: ...

class RWStepVisual_RWCubicBezierTessellatedEdge:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_CubicBezierTessellatedEdge,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_CubicBezierTessellatedEdge,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_CubicBezierTessellatedEdge
    ) -> None: ...

class RWStepVisual_RWCubicBezierTriangulatedFace:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_CubicBezierTriangulatedFace,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_CubicBezierTriangulatedFace,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_CubicBezierTriangulatedFace
    ) -> None: ...

class RWStepVisual_RWCurveStyle:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CurveStyle,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CurveStyle, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CurveStyle
    ) -> None: ...

class RWStepVisual_RWCurveStyleFont:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CurveStyleFont,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_CurveStyleFont, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CurveStyleFont
    ) -> None: ...

class RWStepVisual_RWCurveStyleFontPattern:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_CurveStyleFontPattern,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_CurveStyleFontPattern
    ) -> None: ...

class RWStepVisual_RWDraughtingCallout:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_DraughtingCallout,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_DraughtingCallout, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_DraughtingCallout
    ) -> None: ...

class RWStepVisual_RWDraughtingModel:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_DraughtingModel,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_DraughtingModel, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_DraughtingModel
    ) -> None: ...

class RWStepVisual_RWDraughtingPreDefinedColour:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_DraughtingPreDefinedColour,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_DraughtingPreDefinedColour
    ) -> None: ...

class RWStepVisual_RWDraughtingPreDefinedCurveFont:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_DraughtingPreDefinedCurveFont,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_DraughtingPreDefinedCurveFont
    ) -> None: ...

class RWStepVisual_RWExternallyDefinedCurveFont:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_ExternallyDefinedCurveFont,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_ExternallyDefinedCurveFont, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_ExternallyDefinedCurveFont
    ) -> None: ...

class RWStepVisual_RWFillAreaStyle:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_FillAreaStyle,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_FillAreaStyle, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_FillAreaStyle
    ) -> None: ...

class RWStepVisual_RWFillAreaStyleColour:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_FillAreaStyleColour,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_FillAreaStyleColour, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_FillAreaStyleColour
    ) -> None: ...

class RWStepVisual_RWInvisibility:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_Invisibility,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_Invisibility, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_Invisibility
    ) -> None: ...

class RWStepVisual_RWMechanicalDesignGeometricPresentationArea:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_MechanicalDesignGeometricPresentationArea,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_MechanicalDesignGeometricPresentationArea,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_MechanicalDesignGeometricPresentationArea,
    ) -> None: ...

class RWStepVisual_RWMechanicalDesignGeometricPresentationRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_MechanicalDesignGeometricPresentationRepresentation,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_MechanicalDesignGeometricPresentationRepresentation,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_MechanicalDesignGeometricPresentationRepresentation,
    ) -> None: ...

class RWStepVisual_RWOverRidingStyledItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_OverRidingStyledItem,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_OverRidingStyledItem, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_OverRidingStyledItem
    ) -> None: ...

class RWStepVisual_RWPlanarBox:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PlanarBox,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PlanarBox, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepVisual_PlanarBox) -> None: ...

class RWStepVisual_RWPlanarExtent:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PlanarExtent,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PlanarExtent
    ) -> None: ...

class RWStepVisual_RWPointStyle:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PointStyle,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PointStyle, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PointStyle
    ) -> None: ...

class RWStepVisual_RWPreDefinedColour:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PreDefinedColour,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PreDefinedColour
    ) -> None: ...

class RWStepVisual_RWPreDefinedCurveFont:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PreDefinedCurveFont,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PreDefinedCurveFont
    ) -> None: ...

class RWStepVisual_RWPreDefinedItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PreDefinedItem,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PreDefinedItem
    ) -> None: ...

class RWStepVisual_RWPresentationArea:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationArea,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PresentationArea, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationArea
    ) -> None: ...

class RWStepVisual_RWPresentationLayerAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationLayerAssignment,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_PresentationLayerAssignment,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationLayerAssignment
    ) -> None: ...

class RWStepVisual_RWPresentationLayerUsage:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationLayerUsage,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PresentationLayerUsage, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationLayerUsage
    ) -> None: ...

class RWStepVisual_RWPresentationRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationRepresentation,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PresentationRepresentation, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationRepresentation
    ) -> None: ...

class RWStepVisual_RWPresentationSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationSet,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationSet
    ) -> None: ...

class RWStepVisual_RWPresentationSize:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationSize,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PresentationSize, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationSize
    ) -> None: ...

class RWStepVisual_RWPresentationStyleAssignment:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationStyleAssignment,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_PresentationStyleAssignment,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationStyleAssignment
    ) -> None: ...

class RWStepVisual_RWPresentationStyleByContext:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationStyleByContext,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PresentationStyleByContext, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationStyleByContext
    ) -> None: ...

class RWStepVisual_RWPresentationView:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentationView,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_PresentationView, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentationView
    ) -> None: ...

class RWStepVisual_RWPresentedItemRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_PresentedItemRepresentation,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_PresentedItemRepresentation,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_PresentedItemRepresentation
    ) -> None: ...

class RWStepVisual_RWRepositionedTessellatedGeometricSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theAch: Interface_Check,
        theEnt: StepVisual_RepositionedTessellatedGeometricSet,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_RepositionedTessellatedGeometricSet,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        theSW: StepData_StepWriter,
        theEnt: StepVisual_RepositionedTessellatedGeometricSet,
    ) -> None: ...

class RWStepVisual_RWRepositionedTessellatedItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theAch: Interface_Check,
        theEnt: StepVisual_RepositionedTessellatedItem,
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_RepositionedTessellatedItem
    ) -> None: ...

class RWStepVisual_RWStyledItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_StyledItem,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_StyledItem, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_StyledItem
    ) -> None: ...

class RWStepVisual_RWSurfaceSideStyle:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceSideStyle,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceSideStyle, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceSideStyle
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleBoundary:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleBoundary,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleBoundary, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleBoundary
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleControlGrid:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleControlGrid,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleControlGrid, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleControlGrid
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleFillArea:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleFillArea,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleFillArea, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleFillArea
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleParameterLine:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleParameterLine,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleParameterLine, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleParameterLine
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleReflectanceAmbient:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleReflectanceAmbient,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_SurfaceStyleReflectanceAmbient,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleReflectanceAmbient
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleRendering:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleRendering,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleRendering, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleRendering
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleRenderingWithProperties:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleRenderingWithProperties,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_SurfaceStyleRenderingWithProperties,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        SW: StepData_StepWriter,
        ent: StepVisual_SurfaceStyleRenderingWithProperties,
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleSegmentationCurve:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleSegmentationCurve,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_SurfaceStyleSegmentationCurve,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleSegmentationCurve
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleSilhouette:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleSilhouette,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleSilhouette, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleSilhouette
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleTransparent:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleTransparent,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleTransparent, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleTransparent
    ) -> None: ...

class RWStepVisual_RWSurfaceStyleUsage:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_SurfaceStyleUsage,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_SurfaceStyleUsage, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_SurfaceStyleUsage
    ) -> None: ...

class RWStepVisual_RWTemplate:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_Template,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_Template, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepVisual_Template) -> None: ...

class RWStepVisual_RWTemplateInstance:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TemplateInstance,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_TemplateInstance, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TemplateInstance
    ) -> None: ...

class RWStepVisual_RWTessellatedAnnotationOccurrence:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TessellatedAnnotationOccurrence,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_TessellatedAnnotationOccurrence,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TessellatedAnnotationOccurrence
    ) -> None: ...

class RWStepVisual_RWTessellatedConnectingEdge:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedConnectingEdge,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_TessellatedConnectingEdge,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedConnectingEdge
    ) -> None: ...

class RWStepVisual_RWTessellatedCurveSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TessellatedCurveSet,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_TessellatedCurveSet, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TessellatedCurveSet
    ) -> None: ...

class RWStepVisual_RWTessellatedEdge:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedEdge,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TessellatedEdge, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedEdge
    ) -> None: ...

class RWStepVisual_RWTessellatedGeometricSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TessellatedGeometricSet,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_TessellatedGeometricSet, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TessellatedGeometricSet
    ) -> None: ...

class RWStepVisual_RWTessellatedItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TessellatedItem,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TessellatedItem
    ) -> None: ...

class RWStepVisual_RWTessellatedPointSet:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedPointSet,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TessellatedPointSet, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedPointSet
    ) -> None: ...

class RWStepVisual_RWTessellatedShapeRepresentation:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedShapeRepresentation,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_TessellatedShapeRepresentation,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        theSW: StepData_StepWriter,
        theEnt: StepVisual_TessellatedShapeRepresentation,
    ) -> None: ...

class RWStepVisual_RWTessellatedShapeRepresentationWithAccuracyParameters:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedShapeRepresentationWithAccuracyParameters,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_TessellatedShapeRepresentationWithAccuracyParameters,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self,
        theSW: StepData_StepWriter,
        theEnt: StepVisual_TessellatedShapeRepresentationWithAccuracyParameters,
    ) -> None: ...

class RWStepVisual_RWTessellatedShell:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedShell,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TessellatedShell, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedShell
    ) -> None: ...

class RWStepVisual_RWTessellatedSolid:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedSolid,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TessellatedSolid, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedSolid
    ) -> None: ...

class RWStepVisual_RWTessellatedStructuredItem:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedStructuredItem,
    ) -> None: ...
    def Share(
        self,
        theEnt: StepVisual_TessellatedStructuredItem,
        theIter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedStructuredItem
    ) -> None: ...

class RWStepVisual_RWTessellatedVertex:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedVertex,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TessellatedVertex, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedVertex
    ) -> None: ...

class RWStepVisual_RWTessellatedWire:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TessellatedWire,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TessellatedWire, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TessellatedWire
    ) -> None: ...

class RWStepVisual_RWTextLiteral:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TextLiteral,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_TextLiteral, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TextLiteral
    ) -> None: ...

class RWStepVisual_RWTextStyle:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TextStyle,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_TextStyle, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(self, SW: StepData_StepWriter, ent: StepVisual_TextStyle) -> None: ...

class RWStepVisual_RWTextStyleForDefinedFont:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TextStyleForDefinedFont,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_TextStyleForDefinedFont, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TextStyleForDefinedFont
    ) -> None: ...

class RWStepVisual_RWTextStyleWithBoxCharacteristics:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_TextStyleWithBoxCharacteristics,
    ) -> None: ...
    def Share(
        self,
        ent: StepVisual_TextStyleWithBoxCharacteristics,
        iter: Interface_EntityIterator,
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_TextStyleWithBoxCharacteristics
    ) -> None: ...

class RWStepVisual_RWTriangulatedFace:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        theData: StepData_StepReaderData,
        theNum: int,
        theCheck: Interface_Check,
        theEnt: StepVisual_TriangulatedFace,
    ) -> None: ...
    def Share(
        self, theEnt: StepVisual_TriangulatedFace, theIter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, theSW: StepData_StepWriter, theEnt: StepVisual_TriangulatedFace
    ) -> None: ...

class RWStepVisual_RWViewVolume:
    def __init__(self) -> None: ...
    def ReadStep(
        self,
        data: StepData_StepReaderData,
        num: int,
        ach: Interface_Check,
        ent: StepVisual_ViewVolume,
    ) -> None: ...
    def Share(
        self, ent: StepVisual_ViewVolume, iter: Interface_EntityIterator
    ) -> None: ...
    def WriteStep(
        self, SW: StepData_StepWriter, ent: StepVisual_ViewVolume
    ) -> None: ...

# harray1 classes
# harray2 classes
# hsequence classes
