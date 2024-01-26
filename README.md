### Ajax Systems, Python developer in test for Application team
Для выполнения тестового задания Вам нужно установить приложение Ajax Systems на телефон (если у вас нет реального андроид устройства то вы можете использовать эмулятор).

### Задание
1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд).✔️
2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы).✔️
3) Использовать параметризацию.✔️
4) Закомитить выполненное задание на гитхаб.✔️

### Дополнительное задание (опционально)
1) *Реализовать логирование теста.✔️
2) *Реализовать динамическое определение udid телефона через subprocess.✔️
3) **Написать на проверку элементов SideBar (выезжающее меню слева).✔️

### Полезные ссылки
1) Приложение - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Работа с реальным телефоном - https://developer.android.com/studio/command-line/adb
3) Настройка эмулятора - https://developer.android.com/studio/run/emulator
4) Настройка аппиума - https://appium.io/docs/en/2.0/quickstart/
5) Инспектор приложения - https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/


### Result
Pytest in run:
![image](https://github.com/Andriy-Sydorenko/ajax_test_task/assets/94242534/185f5219-28f9-4d2f-9739-0a71b03ca15e)

Pytest in terminal:
![image](https://github.com/Andriy-Sydorenko/ajax_test_task/assets/94242534/295e662d-8fbc-4ee5-8a20-94667745e38b)

Log file example:
![image](https://github.com/Andriy-Sydorenko/ajax_test_task/assets/94242534/c6a0d00a-25a6-4493-aeea-182fb3b1595b)


### Possible improvements
- Replace [driver.reset()](tests/login/test_login.py#L55) method in as it'll be deprecated in future updates.

    Possible sollution - use `driver.activate_app()` and `driver.terminate_app()`
- Replace `desired_capabilities` for webdriver with `Options object with options kwarg` as it'll be also deprecated.
- Maybe separate login test into 2 functions(one with invalid inputs, and one with valid), but since they have the same algorithm, I decided to write only 1 function.
