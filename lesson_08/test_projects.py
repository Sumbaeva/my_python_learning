import pytest
import requests
from config import API_KEY, BASE_URL


HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

created_project_id = None


def test_post_create_project_positive():
    url = f"{BASE_URL}/projects"
    payload = {
        "title": "Тестовый проект от автотеста",
        "users": {
            "80e55b40-b6af-4f50-91b8-0df7141e909c": "admin"
        }
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 201, (
        f"Ожидался статус 201, получен {response.status_code}"
    )
    data = response.json()
    assert "id" in data, "В ответе нет поля 'id'"
    print(f"Проект успешно создан с ID: {data['id']}")
    global created_project_id
    created_project_id = data["id"]
    print("Позитивный тест создания проекта пройден")


def test_post_create_project_negative():
    url = f"{BASE_URL}/projects"
    payload = {
        "title": "",
        "users": {
            "80e55b40-b6af-4f50-91b8-0df7141e909c": "admin"
        }
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    assert response.status_code == 400, (
        f"Ожидался статус 400, получен {response.status_code}"
    )
    print("Негативный тест создания проекта пройден")


def test_put_update_project_positive():
    if created_project_id is None:
        pytest.skip("Нет ID проекта — запустите сначала тест создания")
    url = f"{BASE_URL}/projects/{created_project_id}"
    payload = {
        "title": "Обновлённый тестовый проект",
        "users": {
            "80e55b40-b6af-4f50-91b8-0df7141e909c": "admin"
        }
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}"
    )
    data = response.json()
    assert data["id"] == created_project_id
    print(f"Проект {created_project_id} успешно обновлён!")


def test_put_update_project_negative():
    fake_id = "00000000-0000-0000-0000-000000000000"
    url = f"{BASE_URL}/projects/{fake_id}"
    payload = {
        "title": "Несуществующий",
        "users": {
            "80e55b40-b6af-4f50-91b8-0df7141e909c": "admin"
        }
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    assert response.status_code == 404, (
        f"Ожидался статус 404, получен {response.status_code}"
    )
    print("Негативный тест обновления пройден")


def test_get_project_positive():
    if created_project_id is None:
        pytest.skip("Нет ID проекта — запустите сначала тест создания")
    url = f"{BASE_URL}/projects/{created_project_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 200, (
        f"Ожидался статус 200, получен {response.status_code}"
    )
    data = response.json()
    assert data["id"] == created_project_id
    assert "title" in data
    print(f"Проект {created_project_id} успешно получен")
    print(f"Название: {data.get('title', 'Без названия')}")


def test_get_project_negative():
    fake_id = "11111111-1111-1111-1111-111111111111"
    url = f"{BASE_URL}/projects/{fake_id}"
    response = requests.get(url, headers=HEADERS)
    assert response.status_code == 404, (
        f"Ожидался статус 404, получен {response.status_code}"
    )
    print("Негативный тест получения пройден")
