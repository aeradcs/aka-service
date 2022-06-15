# aka-service install


1. 
        git clone https://gitlab.ssd.sscc.ru/e.nalepova/aka-service.git

2. 
        cd aka-service/

3. 
        python3 -m venv venv

4. 
        source venv/bin/activate

5. 
        pip install -r requirements.txt


6. Если не работает pip install -r requirements.txt, то выполнить:

        pip install Django djangorestframework PyYAML uritemplate django-rest-swagger

7. 
        cd service/

8. Запустить django проект в текущей ssh сессии:

        python manage.py runserver 0.0.0.0:7710

   Вместо **7710** может быть любой свободный порт.

   Проверить, что сервис отвечает:

        открыть в браузере страницу по ссылке http://84.237.87.18:7710/docs/ 

9. Запустить django проект в фоновом режиме:

        nohup python manage.py runserver 0.0.0.0:7710 > out.txt 2> err.txt &

_______________________________________________________________________________

10. Настроить автоперезапуск сервера в случае падения (**если вы настроили сервер по шагу 9, то сначала его необходимо отключить** -- kill <pid_num>):

- В каталоге /aka-service/service лежит 2 файла – cron.sh и run.sh.

   В cron.sh нужно поменять путь в строке

        cd /home/nalepova/aka-service/service 

   на тот, по которому у вас лежит каталог aka-service/service.

- В run.sh нужно поменять команду

        . ../venv/bin/activate

   на ту, по которой у вас запускается виртуальная python-среда.

   . – source
        
   venv – название каталога виртуальной среды

   **Если структура проекта при клонировании не была изменена, то эту строку менять не нужно.**

- APP_NAME="python3 manage.py runserver 0.0.0.0:7710"

        7710 – нужно поменять на любой свободный порт.

- Добавить права:

        chmod u+x run.sh

- Запуск сервера:

        ./run.sh start

- Проверка работы сервера:

        ./run.sh status

   Если все настроено правильно, то команда выдаст:

        python3 manage.py runserver 0.0.0.0:<your_port> is running with PID: <your_pid_num>

- Остановка сервера:

        ./run.sh stop


_______________________________________________________________________________

# примеры запросов к сервису
1. Создать переменную filename со значением D_Nov_042_fon1:
        
        POST http://127.0.0.1:8000/jobs/0/vars/
        body: {
        "varname":"filename", 
        "varvalue":"D_Nov_042_fon1"
        }

2. Получить список названий сохраненных переменных:
        
        GET http://127.0.0.1:8000/jobs/0/vars/

3. Удалить все переменные:
        
        DELETE http://127.0.0.1:8000/jobs/0/vars/

4. Получить значение переменной filename:
        
        GET http://127.0.0.1:8000/jobs/0/vars/filename/

5. Удалить переменную filename:
        
        DELETE http://127.0.0.1:8000/jobs/0/vars/filename/

6. Поставить задачу на кластере:
        
        POST http://127.0.0.1:8000/jobs/ 

7. Получить значения -- результат выполнения задачи:
        
        GET http://127.0.0.1:8000/jobs/0/

8. _Служебный запрос_: получить словарь файлов и дат обработки:
        
        GET http://127.0.0.1:8000/paths/
        пример ответа --> {'Европеоиды/первый год/11/Fon1/Co_011_v1_fon1.set': 'Jun 12 12:33', ...}

9. _Служебный запрос_: получить изображение .png, сохраненное при выполнении задачи на кластере:
        
        GET http://127.0.0.1:8000/images/<name.png>
