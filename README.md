### AppStore

#### Your marketplace for buying and selling apps

#### To run locally
- Python version: `3.11.0`

```commandline
make setup
make migrate
make runserver
```

#### Create superuser
```commandline
python manage.py createsuperuser
```


#### Docs
- http://localhost:8000/swagger/
- http://localhost:8000/redoc/


#### HowTo: Implement a Dashboard service
- Add a Logtable. This table would keep track of every transaction 
(creation of apps, buying and selling, buyer, seller, the cost, the app ID...)
- Create a `Dashboard` application. 
- We'd use Django here to build the FrontEnd. We can have Views that queries
the Logtable and returns the data in a paginated format.
- Different endpoints can be tied to different views, returning data in specified
format. We can have services the views would call to perform various SQL operations
to properly format the database data.