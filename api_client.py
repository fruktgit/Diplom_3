import requests
from config import BASE_URL

class APIClient:

    @staticmethod
    def post(endpoint, data=None, headers=None):
        return requests.post(f"{BASE_URL}{endpoint}", json=data, headers={'Authorization': f'{headers}'})

    @staticmethod
    def get(endpoint, params=None, headers=None):
        return requests.get(f"{BASE_URL}{endpoint}", params=params, headers={'Authorization': f'{headers}'})

    @staticmethod
    def delete(endpoint, headers=None):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=headers)

    @staticmethod
    def put(endpoint, data=None, headers=None):
        return requests.put(f"{BASE_URL}{endpoint}", json=data, headers={'Authorization': f'{headers}'})

    @staticmethod
    def patch(endpoint, data=None, headers=None):
        return requests.patch(f"{BASE_URL}{endpoint}", json=data, headers={'Authorization': f'{headers}'})
