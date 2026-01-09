import pytest
import requests
from config import BASE_URL, USER_ID, HEADERS


@pytest.fixture(scope="module")
def create_project():
    url = f"{BASE_URL}/projects"

    payload = {
        "title": "Тестовый проект для автотестов",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201, (
        f"Создание проекта: ожидался 201, получен {response.status_code}"
    )
    data = response.json()
    project_id = data["id"]
    yield project_id


def test_post_create_project_positive(create_project):
    project_id = create_project
    assert project_id is not None, "Проект не создан"


def test_post_create_project_negative():
    url = f"{BASE_URL}/projects"
    payload = {
        "title": "",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 400, (
        f"Ожидался 400, получен {response.status_code}"
    )


def test_put_update_project_positive(create_project):
    project_id = create_project
    url = f"{BASE_URL}/projects/{project_id}"
    payload = {
        "title": "Обновлённый тест-проект",
        "users": {
            USER_ID: "admin"
        }
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}"
    )
    data = response.json()
    assert data["id"] == project_id, "ID изменился после обновления"


def test_put_update_project_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    url = f"{BASE_URL}/projects/{fake_id}"
    payload = {
        "title": "Несуществующий проект"
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    assert response.status_code == 404, (
        f"Ожидался 404, получен {response.status_code}"
    )


def test_get_project_positive(create_project):
    project_id = create_project
    url = f"{BASE_URL}/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, (
        f"Ожидался 200, получен {response.status_code}"
    )
    data = response.json()
    assert data["id"] == project_id, "Неверный ID в ответе"
    assert "title" in data, "Нет поля title в ответе"


def test_get_project_negative():
    fake_id = "11111111-1111-1111-1111-111111111111"
    url = f"{BASE_URL}/projects/{fake_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 404, (
        f"Ожидался 404, получен {response.status_code}"
    )
