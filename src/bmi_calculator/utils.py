from enum import Enum
import os
from pathlib import Path
from typing import Text

from pydantic.main import BaseModel


EXCPETION_CODE = 500

__DATA_FILE_PATH = None
DATA_FILE_PATH = "DATA_FILE_PATH"

def get_data_file_path() -> Path:
    global __DATA_FILE_PATH
    if DATA_FILE_PATH in os.environ:
        __DATA_FILE_PATH = Path(os.environ[DATA_FILE_PATH])
    else:
        __DATA_FILE_PATH = Path("configs/inputData.json")
    return __DATA_FILE_PATH


class category(BaseModel):
    text: Text


class BMICategories(Enum):
    UNDER_WEIGHT: category = category(text="Underweight")
    NORMAL_WEIGHT: category = category(text="Normal weight")
    OVER_WEIGHT: category = category(text="Overweight")
    MODERATELY_OBESE: category = category(text="Moderately obese")
    SEVERELY_OBESE: category = category(text="Severely obese")
    VERY_SEVERELY_OBESE: category = category(text="Very severely obese")


class risk(BaseModel):
    text: Text


class HealthRisk(Enum):
    MALNUTRITION_RISK: risk = risk(text="Malnutrition risk")
    LOW_RISK: risk = risk(text="Low risk")
    ENHANCED_RISK: risk = risk(text="Enhanced risk")
    MEDIUM_RISK: risk = risk(text="Medium risk")
    HIGH_RISK: risk = risk(text="High risk")
    VERY_HIGH_RISK: risk = risk(text="Very high risk")
