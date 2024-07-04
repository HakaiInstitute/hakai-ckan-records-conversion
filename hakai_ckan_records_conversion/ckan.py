import requests
from loguru import logger


class CKAN:
    def __init__(self, base_url:str):
        self.base_url = base_url

    def get_record(self, dataset_id:str) -> dict:
        url = f"{self.base_url}/api/3/action/package_show?id={dataset_id}"
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
        if result["success"]:
            return result["result"]
        logger.error(f"Error retrieving dataset {dataset_id}")
