### Running Database Migrations
* Make sure to run database migrations everytime you make a change to any model.
* Use the following commands.
cd StockTwitterWeb/Apps
python3 manage.py makemigrations - responsbile for creating new migrations based on the changes you have made to your models.
python3 manage.py migrate - responsible for applying and unapplying migrations.
python3 manage.py showmigrations - lists a project migrations and their status
python3 manage.py sqlmigrate - displays the sql statements for a migration.

## Creating a superuser
cd StockTwitterWeb/Apps
python3 manage.py createsuperuser


Pick up from here -https://adiramadhan17.medium.com/build-django-required-login-apps-with-custom-login-logout-page-ec6b6d722f21