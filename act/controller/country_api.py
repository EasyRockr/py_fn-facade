from fastapi import APIRouter

router = APIRouter(tags=["Countries API"])

@router.get("/country-codes")
def get_country_codes():
    return [
        {"code": "+63", "country": "Philippines"},
        {"code": "+1", "country": "United States"}
    ]
