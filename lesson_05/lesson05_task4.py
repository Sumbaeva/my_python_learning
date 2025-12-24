from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        driver = webdriver.Firefox()
        driver.get("http://the-internet.herokuapp.com/login")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR,
                                           "button[type='submit']")
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()
        success_message_element = driver.find_element(By.CLASS_NAME,
                                                      "flash.success")
        success_text = success_message_element.text
        clean_text = success_text.split("\n")[0]
        clean_text = clean_text.replace("×", "").strip()
        print(f"Текст с зеленой плашки: '{clean_text}'")
        print("Упражнение 4 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
