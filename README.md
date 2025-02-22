# Sprint_6
Чтобы сгенерировать Allure-отчёт, введи в терминале PyCharm:

pytest tests/test_order_page.py --alluredir=allure_results 

Теперь нужно сформировать отчёт в формате веб-страницы. Напиши в терминале PyCharm:

allure serve allure_results 