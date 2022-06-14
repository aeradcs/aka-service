# aka-service install

```
1. git clone https://gitlab.ssd.sscc.ru/e.nalepova/aka-service.git

2. cd aka-service/

3. python3 -m venv venv

4. source venv/bin/activate

5. pip install -r requirements.txt
```

6. если не работает pip install -r requirements.txt, то выполнить:

        pip install Django djangorestframework PyYAML uritemplate django-rest-swagger

7. 
        cd service/

8. запустить django проект в текущей ssh сессии:

        python manage.py runserver 0.0.0.0:7710

            вместо 7710 может быть любой свободный порт

            проверить, что сервис отвечает:

            открыть в браузере страницу по ссылке http://84.237.87.18:7710/docs/ 

9. запустить django проект в фоновом режиме:

        nohup python manage.py runserver 0.0.0.0:7710 > out.txt 2> err.txt &

