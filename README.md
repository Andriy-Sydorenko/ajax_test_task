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

Pytest in terminal:

Log file example:



### Possible improvements
- Replace [driver.reset()](tests/login/test_login.py) method in as it'll be deprecated in future updates.

    Possible sollution - use `driver.activate_app()` and `driver.terminate_app()`
- Replace `desired_capabilities` for webdriver with `Options object with options kwarg` as it'll be also deprecated.
- Maybe separate login test into 2 functions(one with invalid inputs, and ne with valid), but since they have the same algorithm, I decided to write only 1 function.