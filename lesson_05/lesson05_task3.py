from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        driver = webdriver.Firefox()
        driver.get("http://the-internet.herokuapp.com/inputs")
        input_field = driver.find_element(By.TAG_NAME, "input")
        input_field.send_keys("Sky")
        input_field.clear()
        input_field.send_keys("Pro")
        print("Упражнение 3 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
