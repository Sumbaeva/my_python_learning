# Домашняя работа №11: Отчётность в Allure

Это проект с тестами на основе PageObject (калькулятор и магазин SauceDemo)  
с добавленной отчётностью через библиотеку **Allure**.

## О проекте

- Используется **pytest** + **Selenium** + **PageObject**
- Тесты: калькулятор с задержкой и полный цикл покупки в магазине
- Добавлена интеграция с **Allure** для красивых отчётов с шагами и скриншотами

## Требования к запуску

Установите зависимости:

```bash
pip install selenium pytest allure-pytest allure-python-commons webdriver-manager
```

## Как запустить тесты и сформировать отчёт Allure

1. Запустите тесты с сохранением результатов в папку `allure-results`:

   ```bash
   pytest lesson_10 --alluredir=allure-results
   ```

   После выполнения появится папка `allure-results` с сырыми данными.

2. Сгенерируйте красивый HTML-отчёт:

   ```bash
   allure generate allure-results -o allure-report --clean
   ```

   - Параметр `--clean` очищает предыдущую версию отчёта (если была)
   - Появится папка `allure-report`

3. Откройте готовый отчёт в браузере:

   ```bash
   allure open allure-report
   ```

   Браузер автоматически откроется с красивым интерактивным отчётом.

## Важно

- Папки `allure-results` и `allure-report` **не пушатся** в репозиторий  
  (они добавлены в `.gitignore`)
- В репозитории оставлена пустая папка `allure-results/` — для удобства
- Для запуска отчёта Allure должен быть установлен глобально  
  (инструкция: https://github.com/allure-framework/allure2/releases)
