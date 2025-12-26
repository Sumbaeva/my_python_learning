from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    try:
        driver = webdriver.Chrome()
        driver.get("http://uitestingplayground.com/dynamicid")
        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        blue_button.click()
        print("Упражнение 2 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
