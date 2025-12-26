from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def rename_button_example():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/textinput")
        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.clear()
        input_field.send_keys("SkyPro")
        blue_button = driver.find_element(By.ID, "updatingButton")
        blue_button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(
            lambda d: blue_button.text == "SkyPro"
        )
        new_text = blue_button.text
        print(f"Новый текст кнопки: '{new_text}'")
        print("Упражнение 2 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    rename_button_example()
