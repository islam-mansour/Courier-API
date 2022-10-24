# Courier Managment System
### Simple api for managing your courier system

<br><br>

## Installation guide

### - start application
```bash
docker-compose up -d --build
```

### - make and apply db migrations
```bash
docker exec -ti WEB python manage.py makemigrations
docker exec -ti WEB python manage.py migrate --run-syncdb
```

### you can enrich the database with sample data using the admin ui at ```localhost:8000/admin```

<br><br>

## Notes
``` queuing system (kafka or rabbitmq) can be used for scalability reasons, enqueuing the creation of waybills/shipment should be enqueued and background workers will execute the needed database insert operations ``` 