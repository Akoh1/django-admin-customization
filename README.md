# task-manager
A web app to manage tasks for technical teams, You can open a workspace for your organizations
 and users can sign up to that workspace, create tasks, assign it milestones, change tasks milestones.
 This web app also provides RESTFUL API which would be consumed by my front-end project which would be implemented by vuejs later on. 

**Technology Used:** Django 2.1.5 (Python 3)

 **Database:** SQLite 3 (SQLite is used because it can be safely assumed that it would not be a very busy site and enterprise level database can be avoided)



## Installation
## clone from branch samuel 

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

    
 
 
