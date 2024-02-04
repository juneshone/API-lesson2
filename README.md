# Обрезка ссылок с помощью Битли

Создана консольная утилита, которая делает запрос к API сервиса Bitly на сокращение ссылки и считает переходы по сокращенным ссылкам

### Как установить

Зарегистрируйтесь на сервисе Bitly:
```
https://bitly.com/a/sign_in?rd=/settings/integrations
```
Сгенерируйте токен типа `GENERIC ACCESS TOKEN`. Создайте файл .env и присвойте значение переменной окружения `BITLY_TOKEN`. 

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Пример запуска скрипта

Убедитесь, что в терминале находитесь в директории `API-lesson2` и запустите скрипт командой
```
python main.py
```

Введите в консоль адрес сайта в интернете, который будете сокращать. На выходе получите сокращенную ссылку.
```
https://dzen.ru/?yredirect=true&clid=2270456&win=539
```

_Пример:_

![Битлинк](https://github.com/juneshone/API-lesson2/assets/122731315/72434214-d386-4b2e-98e5-f6228a882729)

Для получения кликов по ссылке введите в консоль сокращенную ссылку.
```
https://bit.ly/42reuxz
```

_Пример:_

![Клики](https://github.com/juneshone/API-lesson2/assets/122731315/9f67ee8e-6f88-47ea-99de-16d6338517b5)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).