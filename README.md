# Skychimp 2.0 Сервис по управлению рассылками .

 Нужно было разработать сервис управления рассылками, администрирования и получения статистики.
 


### Build & Launch

```bash

source env/bin/activate 
pip install -r requirement.txt

```

После этого необходимо в config/settings.py изменить индивидуальные настройки 
Пример и перечень переменных лежит в файле .env_example

```bash

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

```

После проделанных команд проект будет доступен по адресу http://127.0.0.1:8000/

Скрипт рассылки, работает как из командой строки, так и по расписанию.
Для запуска рассылки командой используйте :

```bash

python3 manage.py sendmail

```

