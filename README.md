# django-tree
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

## Screenshots
[![Screenshot-from-2023-02-22-18-17-44.png](https://i.postimg.cc/cJhnX806/Screenshot-from-2023-02-22-18-17-44.png)](https://postimg.cc/VSSvNvSc)
[![Screenshot-from-2023-02-22-18-22-36.png](https://i.postimg.cc/8zBJzrFw/Screenshot-from-2023-02-22-18-22-36.png)](https://postimg.cc/w1MTWMQs)
[![Screenshot-from-2023-02-22-18-23-00.png](https://i.postimg.cc/VkB4MRZC/Screenshot-from-2023-02-22-18-23-00.png)](https://postimg.cc/tsJhGhjq)
[![Screenshot-from-2023-02-22-18-23-29.png](https://i.postimg.cc/bJdR7jyx/Screenshot-from-2023-02-22-18-23-29.png)](https://postimg.cc/qhVnKSCq)
[![Screenshot-from-2023-02-22-18-24-14.png](https://i.postimg.cc/SQC9JKvX/Screenshot-from-2023-02-22-18-24-14.png)](https://postimg.cc/CdM52wYY)

## Конфигурация
`git clone https://github.com/aliquews/django-tree.git`
##
`docker-compose up --build -d`
## 
`docker-compose exec web python website/manage.py migrate`
### Админка Django
`docker-compose exec web python website/manage.py createsuperuser --username=<your_username> --email=<your_email>`

## Важно подметить
По стандарту данное веб-приложение работает на хосте 0.0.0.0 и порт у него 8080, тк такой хост я задал в settings.py и порт который пробрасывается на локальный хост в docker-compose. Это значит что к нему(веб-приложению) можно обратиться http://0.0.0.0:8080<br>
Также, при запуске контейнера список меню будет будет пуст, его нужно добавлять в Django админке. Но т.к я нахардкодил, я просто добавил
некоторые "эндпоинты" в website/menuapp/urls.py, там их можно посмореть, это значит если добавить пункт меню, url которого будет относиться к данному приложению, ответ будет 404. Список доступных эндпоинтов можно посмтреть в urls.py о котором я говорил.
Но при этом если в списке меню добавить пункт с ссылкой на внешний сайт, то работать все будет нормально.