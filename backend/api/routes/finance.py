from fastapi import APIRouter

from backend.finance.controller import run_finance_controller


router = APIRouter(
    prefix="/finance",
    tags=["finance"],
)


@router.post("/reconcile")
def reconcile_finance():

    result = run_finance_controller()

    return result