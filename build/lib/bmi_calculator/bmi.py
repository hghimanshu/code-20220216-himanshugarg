import json
from typing import Dict, List, Text, Tuple, Union

from bmi_calculator.utils import BMICategories, HealthRisk


class calculateBMI:
    def __init__(self, file_path: Text) -> None:
        self.__file_path = file_path
        self.__bmi_file = None
        self.overweight_counter = 0

    @property
    def get_bmi_file(self) -> List[Dict]:
        if not self.__bmi_file:
            with open(self.__file_path) as f:
                self.__bmi_file = json.load(f)
        return self.__bmi_file

    def get_bmi(self, height: int, weight: int) -> float:
        height /= 100
        return round(weight / (height * height), 3)

    def get_category_and_risk(
        self, bmi: float
    ) -> Union[Tuple[BMICategories, HealthRisk], None]:
        response = None
        if bmi <= 18.4:
            response = (
                BMICategories.UNDER_WEIGHT.value.text,
                HealthRisk.MALNUTRITION_RISK.value.text,
            )
        elif bmi >= 18.5 and bmi <= 24.9:
            response = (
                BMICategories.NORMAL_WEIGHT.value.text,
                HealthRisk.LOW_RISK.value.text,
            )
        elif bmi >= 25 and bmi <= 29.9:
            response = (
                BMICategories.OVER_WEIGHT.value.text,
                HealthRisk.ENHANCED_RISK.value.text,
            )
            self.overweight_counter += 1
        elif bmi >= 30 and bmi <= 34.9:
            response = (
                BMICategories.MODERATELY_OBESE.value.text,
                HealthRisk.MEDIUM_RISK.value.text,
            )
        elif bmi >= 35 and bmi <= 39.9:
            response = (
                BMICategories.SEVERELY_OBESE.value.text,
                HealthRisk.HIGH_RISK.value.text,
            )
        elif bmi >= 40:
            response = (
                BMICategories.VERY_SEVERELY_OBESE.value.text,
                HealthRisk.VERY_HIGH_RISK.value.text,
            )
        return response

    def get_bmi_related_info(
        self, height: int, weight: int
    ) -> Union[Tuple[int, BMICategories, HealthRisk], None]:
        bmi = self.get_bmi(height, weight)
        bmi_category, health_risk = self.get_category_and_risk(bmi)
        return bmi, bmi_category, health_risk

    def get_user_response(self) -> List[Dict]:
        for idx, doc in enumerate(self.get_bmi_file):
            (
                self.__bmi_file[idx]["BMI"],
                self.__bmi_file[idx]["BMI-Category"],
                self.__bmi_file[idx]["Health-Risk"],
            ) = self.get_bmi_related_info(doc["HeightCm"], doc["WeightKg"])
        return self.__bmi_file
    
    def get_overweight_persons(self) -> int:
        if self.__bmi_file is None:
            _= self.get_user_response()
        return self.overweight_counter
