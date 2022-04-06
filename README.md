# Куда пойти — Москва

Сайт о самых интересных местах в Москве - интерактивная карта с интересными местами в Москве.
Нажав на отмеченное на карте место вы получите информацию о данном месте.



## Как установить

* Python3 должен быть установлен
* Скопировать репозиторий на свой компьютер:
```
https://github.com/clownkill/yandex_afisha
```
* Установите зависимости:
```python
pip install -r requirements.txt
```

## Переменные окружения
```
SECRET_KEY=секретный_код_проекта
DEBUG=включить(True)/выключить(False) режим отладки
```

## Как запустить
* Выполните миграции:
```
python manage.py migrate
```
* Запустите сервер:
```
python manage.py runserver
```
* Перейдите в браузере по адресу:
```
http://127.0.0.1:8000
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
