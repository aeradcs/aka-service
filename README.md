# aka-service install

    git clone https://gitlab.ssd.sscc.ru/e.nalepova/aka-service.git

    cd aka-service/

    python3 -m venv venv

    source venv/bin/activate

    pip install -r requirements.txt

        // если не работает pip install -r requirements.txt, то выполнить:
        pip install Django djangorestframework PyYAML uritemplate django-rest-swagger

    cd service/

    запустить django проект в текущей ssh сессии:
    python manage.py runserver 0.0.0.0:**7710**

        // вместо 7710 может быть любой свободный порт
        // проверить, что сервис отвечает:
        открыть в браузере страницу по ссылке http://84.237.87.18:7710/docs/ 

    запустить django проект в фоновом режиме:
    nohup python manage.py runserver 0.0.0.0:7710 > out.txt 2> err.txt &

