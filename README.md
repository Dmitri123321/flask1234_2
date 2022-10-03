# API на фреймворке Flask.


    API предоставляет возможность добавлять данные в базу (postgresql) из файла с помощью get-запроса и
    получать данные из базы post-запросом:
        - /get_data - эндпойнт для получения данных из базы.
    Формат запроса на получение данных из базы:
        POST Host: https://127.0.0.1/get_data
        Request Body schema: 
            {
                "date_before": '2014-10-29', # не указывается, если нужна выборка строго меньше выбранной даты (date_after)
                "date_after": '2014-10-21' # не указывается, если нужна выборка строго меньше выбранной даты (date_before)
            }
    


проект представлен в виде контейнеров. Для работы проекта на компьютере должны быть установленны:

    - docker
    - docker-compose

## Запуск проекта.
    
    - Создайте дирректорию с названием проекта (в любом удобном месте)*
    - В консоли перейдите в созданную дирректорию
    - наберите в консоли команду "docker pull dmitry123123/flask_api"
    - Наберите команду "docker run dmitry123123/flask_api"
    - Для создания базы данных наберите команду "docker compose exec api python manage.py create_db"
    - Для заполнения базы данных наберите команду "docker compose exec api python manage.py seed_db"
    - Теперь можно забирать данные с помощью POST-запроса к ендпоинту /get_data


* к моему сожалению я потратил очень много времени на docker-compose, так как я не очень его знаю, недавно приступил к изучению, и планирую разобраться в обозримом будущем. 
* Возможно я не все сделал как надо потому как на одной машине удалось запустить а на другой удалось запустить только после скачивания всего проекта из репозитория в папку
* ссылка на репозиторий