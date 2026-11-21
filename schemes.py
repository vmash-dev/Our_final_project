from pydantic import BaseModel, Field
from datetime import datetime


class TourPriceImageSchema(BaseModel):
    price: float = Field(ge=1)
    hotel_view: str = Field(examples=['hotel_view'])


class TourCreateSchema(TourPriceImageSchema):
    tour_name: str = Field(examples=['tour_name'])
    tour_description: str = Field(examples=['tour_description'])


class TourSavedSchema(TourCreateSchema):
    id: str
    created_at: datetime = Field(default_factory=datetime.now)