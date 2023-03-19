from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from type import InsuranceInformation

from helper import calculate_insurance_price, calculate_covid_addon_price

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/pricing-calculator")
def pricing_calculator(info: InsuranceInformation):
    period_days = (info.Period.ReturnDate - info.Period.DepartureDate).days

    price = calculate_insurance_price(period_days, info.Plan)

    if info.CovidAddOn:
        price += calculate_covid_addon_price(period_days, info.Plan)

            
    if info.StampDuty and price >= 150:
        price += info.StampDuty

    if info.SST:
        price *= 1.06

    return {"price": price}

    
    

