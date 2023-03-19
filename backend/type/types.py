from datetime import date
from pydantic import BaseModel, validator
from typing import Optional

class Period(BaseModel):
    DepartureDate: date
    ReturnDate: date

    # https://pydantic-docs.helpmanual.io/usage/validators/
    # ReturnDate must be after DepartureDate
    @validator('ReturnDate')
    def check_return_date(cls, v, values):
        if 'DepartureDate' in values and v <= values['DepartureDate']:
            raise ValueError('Return date must be after departure date')
        return v
    
class InsuranceInformation(BaseModel):
    Period: Period
    Plan: int
    CovidAddOn: Optional[bool] = False
    StampDuty: Optional[int] = None
    SST: Optional[bool] = False