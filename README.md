# Skychimp 2.0 Сервис по управлению рассылками .

 Нужно было разработать сервис управления рассылками, администрирования и получения статистики.
 


### Build & Launch

```bash

docker-compose up -d --build

```

Чтобы закрыть:

```bash

docker-compose down

После проделанных команд проект будет доступен по адресу http://127.0.0.1:8000/

Скрипт рассылки, работает как из командой строки, так и по расписанию.
Для запуска рассылки командой используйте :

```bash

python3 manage.py sendmail

```

