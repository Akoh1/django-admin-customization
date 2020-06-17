# A project for Savevest test


**Technology Used:** Django 3.0 (Python 3)

 **Database:** SQLite 3 (SQLite is used because it can be safely assumed that it would not be a very busy site and enterprise level database can be avoided)



## Installation

- Clone repository

    ```bash
    git clone https://github.com/Akoh1/django-admin-customization.git
    ```
- You'll need to have virtual enviroment installed on your machine  

    ```python
  pip3 install virtualenv
  
    ```


- Setup virtual environment

    ```markdown
    virtualenv -p python3 .virtualenv
    
    ```

    

- Activate virtual environment

    ```markdown
    source .virtualenv/bin/activate
    
    ```

    
    

   - Install requirements
    
        ```bash
        pip install -r requirements.txt
        ```


### Run migrations before starting the django-server

```python
   python manage.py migrate
```

- Start Django server
```python
   python manage.py runserver
```
### Visit localhost/admin and login with crediantials username: root and password: password

### To view emails being sent start the Debugging smtpd email server

```python
    python -m smtpd -n -c DebuggingServer localhost:1025
```

    
 
 
