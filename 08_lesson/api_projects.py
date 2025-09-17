import requests

class ProjectsApi:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, payload):
        """Создание проекта"""
        return requests.post(f"{self.base_url}/projects", headers=self.headers, json=payload)

    def get_project(self, project_id):
        """Получение проекта по ID"""
        return requests.get(f"{self.base_url}/projects/{project_id}", headers=self.headers)

    def update_project(self, project_id, payload):
        """Обновление проекта по ID"""
        return requests.put(f"{self.base_url}/projects/{project_id}", headers=self.headers, json=payload)
