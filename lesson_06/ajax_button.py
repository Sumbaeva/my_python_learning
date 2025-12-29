from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ajax_button_test():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/ajax")
        blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
        blue_button.click()
        wait = WebDriverWait(driver, 20)
        success_alert = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".bg-success")
            )
        )
        alert_text = success_alert.text
        print(f"Текст из зеленой плашки: '{alert_text}'")
        print("Упражнение 1 выполнено успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    ajax_button_test()
