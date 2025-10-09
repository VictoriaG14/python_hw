Для запуска автотестов требуется:
- браузеры Google Chrome и Firefox
- библиотека Allure ("pip install allure-pytest") в нужной папке с тестами
- запустить тесты с помощью команды "pytest --alluredir=allure-result" --> результаты прогона сохранятся в папке allure-result
Для генерации отчета Allure требуется:
- ввести в терминале команду "allure serve allure-result" --> отчет сформируется в браузере
