from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def wait_images_test():
    driver = webdriver.Chrome()
    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "loading-images.html"
        )
        selector = "#image-container img"
        wait = WebDriverWait(driver, 40)
        wait.until(
            lambda d: (
                len(d.find_elements(By.CSS_SELECTOR, selector)) == 4
                and all(
                    d.execute_script(
                        "return arguments[0].complete && "
                        "arguments[0].naturalWidth > 0",
                        img
                    )
                    for img in d.find_elements(
                        By.CSS_SELECTOR, "#image-container img"
                    )
                )
            )
        )
        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        if len(images) >= 3:
            third_image = images[2]
            third_image_src = third_image.get_attribute("src")
            third_image_alt = third_image.get_attribute("alt")
            print(f"Третье изображение: {third_image_alt}")
            print("Атрибут src 3-й картинки:")
            print(f"   {third_image_src}")
            if third_image_src and any(
                ext in third_image_src.lower()
                for ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg']
            ):
                print("Упражнение 3 выполнено успешно!")
            else:
                print("Возможно, это не изображение или путь некорректный")
        else:
            print("Не все изображения загрузились")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    wait_images_test()
