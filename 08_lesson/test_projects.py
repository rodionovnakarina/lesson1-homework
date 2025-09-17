import pytest
import uuid

from api_projects import ProjectsApi


def test_create_project_positive(api):
    """Позитивный тест: успешное создание проекта"""
    payload = {"title": f"Test Project {uuid.uuid4()}"}
    response = api.create_project(payload)
    assert response.status_code == 201

    project_id = response.json()["id"]

    # Делаем GET, чтобы проверить название
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["title"] == payload["title"]


def test_create_project_negative_no_title(api):
    """Негативный тест: создание проекта без title"""
    payload = {}
    response = api.create_project(payload)
    assert response.status_code == 400


def test_get_project_positive(api):
    """Позитивный тест: получение существующего проекта"""
    payload = {"title": f"Project {uuid.uuid4()}"}
    project = api.create_project(payload).json()
    project_id = project["id"]

    response = api.get_project(project_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == payload["title"]


def test_update_project_positive(api):
    """Позитивный тест: обновление проекта"""
    payload = {"title": f"Project {uuid.uuid4()}"}
    project = api.create_project(payload).json()
    project_id = project["id"]

    new_payload = {"title": f"Updated {uuid.uuid4()}"}
    response = api.update_project(project_id, new_payload)
    assert response.status_code == 200

    # Делаем GET, чтобы проверить обновлённое название
    get_resp = api.get_project(project_id)
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["title"] == new_payload["title"]


def test_update_project_negative_invalid_id(api):
    """Негативный тест: обновление проекта с невалидным ID"""
    new_payload = {"title": "Invalid update"}
    response = api.update_project("invalid-id", new_payload)
    assert response.status_code == 404
