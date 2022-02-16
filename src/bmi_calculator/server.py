from fastapi import FastAPI, HTTPException

from bmi_calculator.bmi import calculateBMI
from bmi_calculator.utils import EXCPETION_CODE, get_data_file_path

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.bmi_calculator = calculateBMI(get_data_file_path())


@app.get("/get-bmi-data")
async def get_bmi_data():
    try:
        return app.bmi_calculator.get_user_response()
    except (ConnectionError, BrokenPipeError, ConnectionRefusedError) as e:
        raise HTTPException(status_code=EXCPETION_CODE, detail=str(e))


@app.get("/get-overweight-persons")
async def get_overweight_persons():
    try:
        return app.bmi_calculator.get_overweight_persons()
    except (
        ConnectionError,
        BrokenPipeError,
        ConnectionRefusedError,
    ) as e:
        raise HTTPException(status_code=EXCPETION_CODE, detail=str(e))


@app.get("/health")
async def health():
    try:
        return {"message": "Everything is working fine !!"}
    except (ConnectionError, BrokenPipeError, ConnectionRefusedError) as e:
        raise HTTPException(status_code=EXCPETION_CODE, detail=str(e))
