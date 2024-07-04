import requests


class CKAN:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_record(self, dataset_id):
        url = f"{self.base_url}/api/3/action/package_show?id={dataset_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
