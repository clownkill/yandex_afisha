# Куда пойти — Москва

Сайт о самых интересных местах в Москве - интерактивная карта с интересными местами в Москве.
Нажав на отмеченное на карте место вы получите информацию о данном месте. Тестовую реализацию
можно увидеть на [pythonanywhere](https://clownkill.pythonanywhere.com/).

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

## Наполнение базы данных интересных мест

Для пополнения базы данных интересных мест необходимо выполнить следующий скрипт:

```
python manage.py load_place [http-ссылка на json-файл с данными о месте]
```
Примерная структура json-файла:

```json
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
