# LoginWithCookies
Login with cookies verification, using bottle and mongo

- pypy:
    
    Create a virtualenv with python 2.7 and: 
    
    `pip install -r requirements.txt`
    
- Requirements:
    
    Install MongoDB
    
- Now you insert an user in mongo:
    
    ```
    mongo admin
    db.admin_user.insert({'username':'toninho', 'password':'123123'})
    ```
    
- Initiate the app in server directory:
    
    ``python app.py``
    
- Acess 127.0.0.1:8080/index.html


The generated tolken longs by 1 hour


CSS from: https://codepen.io/Lewitje/pen/BNNJjo
