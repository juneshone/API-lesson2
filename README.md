# Обрезка ссылок с помощью Битли

Создана консольная утилита, которая делает запрос к API сервиса Bitly на сокращение ссылки и считает переходы по сокращенным ссылкам

### Как установить

Зарегистрируйтесь на сервисе Bitly и сгенерируйте токен типа GENERIC ACCESS TOKEN. Создайте файл .env и пропишите в нем токен 

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).