from datetime import datetime
import time
from pymongo import MongoClient
import hashlib

def translate(post):
    words = post.split('&')
    dici= {}
    for word in words:
        w = word.split('=')
        dici[w[0]] = w[1]
    return dici

def check_login(username, password):
    client = MongoClient()
    db = client.admin
    res = db.admin_user.find_one({'username':username, 'password':password})
    if(res):
        return True
    else:
        return False

def save_token(username, token):
    client = MongoClient()
    db = client.admin
    res = db.login_token.insert({'username':username, 'token':token, 'time':time.time()})

def load_token(token):
    client = MongoClient()
    db = client.admin
    res = db.login_token.find_one({'token':token})
    if(res):
        clock = float(res['time'])
        if (time.time() - clock) < 3600:
            return True
        else:
            return False
    else:
        return False

def hash_str(string):

   timestamp = str(datetime.now().year) + str(datetime.now().month) + \
               str(datetime.now().day) + str(datetime.now().hour) + \
               str(datetime.now().minute) + str(datetime.now().second) + \
               str(datetime.now().microsecond)    
   sha1 = hashlib.sha1()
   sha1.update(string.encode('utf-8'))
   sha1.update(timestamp.encode('utf-8'))
   hashd = sha1.hexdigest()
   return hashd