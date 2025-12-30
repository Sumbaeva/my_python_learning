from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "data-types.html"
        )
        driver.maximize_window()
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }
        for name, value in form_data.items():
            field = driver.find_element(By.NAME, name)
            field.clear()
            field.send_keys(value)
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        wait.until(EC.url_contains("data-types-submitted.html"))
        zip_alert = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_alert.get_attribute("class")
        assert zip_alert.text.strip() == "N/A"
        for name, expected in form_data.items():
            alert = driver.find_element(By.ID, name)
            assert "alert-success" in alert.get_attribute("class")
            assert alert.text.strip() == expected
        print("Тест пройден успешно")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_form()
