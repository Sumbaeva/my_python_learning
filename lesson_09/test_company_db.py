"""
Автотесты для проверки работы с таблицей employee в базе x_clients
Используем SQLAlchemy + pytest
Каждый тест создаёт → проверяет → удаляет свои данные
"""

import uuid
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import DB_CONNECTION_STRING

engine = create_engine(DB_CONNECTION_STRING, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def generate_test_prefix(prefix="Test"):
    """
    Генерируем уникальный префикс, чтобы
    имена/телефоны не пересекались при повторных запусках
    """
    return f"{prefix}{str(uuid.uuid4())[:3]}"


@pytest.fixture
def db_session():
    """Фикстура: сессия с автоматическим откатом при ошибке и закрытием"""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def test_create_employee(db_session):
    """
    Создание нового сотрудника
    Обязательные поля: first_name, last_name
    """
    prefix = generate_test_prefix("c")
    first_name = f"{prefix}Иван"
    last_name = f"{prefix}Петров"
    phone = "+79990000000"
    company_id = 1
    query = text("""
            INSERT INTO employee (
                first_name,
                last_name,
                is_active,
                phone,
                company_id
            )
            VALUES (:first_name, :last_name, true, :phone, :company_id)
            RETURNING id, first_name, last_name, is_active, phone, company_id
        """)
    result = db_session.execute(query, {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "company_id": company_id
    })
    emp = result.fetchone()
    assert emp is not None, "Сотрудник не создался"
    assert emp.first_name == first_name
    assert emp.last_name == last_name
    assert emp.is_active is True
    assert emp.phone == phone
    assert emp.company_id == company_id
    print(
        f"Создан: {first_name} {last_name}, "
        f"компания {emp.company_id} "
        f"(id={emp.id})"
    )
    db_session.execute(
        text("DELETE FROM employee WHERE id = :id"),
        {"id": emp.id}
    )


def test_update_employee(db_session):
    """
    Создание → обновление имени + добавление телефона → проверка
    """
    prefix = generate_test_prefix("Update")
    first_name_orig = f"{prefix}Анна"
    last_name = f"{prefix}Сидорова"
    phone_orig = "+79991112233"
    company_id = 1
    result = db_session.execute(
        text("""
            INSERT INTO employee (
                first_name,
                last_name,
                is_active,
                phone,
                company_id
            )
            VALUES (:fn, :ln, true, :phone, :company_id)
            RETURNING id
        """),
        {
            "fn": first_name_orig,
            "ln": last_name,
            "phone": phone_orig,
            "company_id": company_id,
        }
    )
    emp_id = result.fetchone()[0]
    new_first = f"{prefix}АннаNEW"
    new_phone = "+79994445566"
    db_session.execute(
        text("""
            UPDATE employee
               SET first_name = :new_fn,
                   phone = :new_phone
             WHERE id = :id
        """),
        {"new_fn": new_first, "new_phone": new_phone, "id": emp_id}
    )
    result = db_session.execute(
        text("SELECT first_name, phone FROM employee WHERE id = :id"),
        {"id": emp_id}
    )
    updated = result.fetchone()
    assert updated.first_name == new_first
    assert updated.phone == new_phone
    print(f"Обновлено: {new_first}, телефон {new_phone}")
    db_session.execute(
        text("DELETE FROM employee WHERE id = :id"),
        {"id": emp_id}
    )


def test_delete_employee(db_session):
    """
    Создание → удаление → проверка, что запись исчезла
    """
    prefix = generate_test_prefix("Delete")
    first_name = f"{prefix}Олег"
    last_name = "Козлов"
    phone = "+79997778899"
    company_id = 1
    result = db_session.execute(
        text("""
            INSERT INTO employee (
                first_name,
                last_name,
                is_active,
                phone,
                company_id
            )
            VALUES (:fn, :ln, true, :phone, :company_id)
            RETURNING id
        """),
        {
            "fn": first_name,
            "ln": last_name,
            "phone": phone,
            "company_id": company_id,
        }
    )
    emp_id = result.fetchone()[0]
    db_session.execute(
        text("DELETE FROM employee WHERE id = :id"),
        {"id": emp_id}
    )
    result = db_session.execute(
        text("SELECT id FROM employee WHERE id = :id"),
        {"id": emp_id}
    )
    assert result.fetchone() is None, "Сотрудник не удалился!"
    print(f"Сотрудник с id {emp_id} успешно удалён")
