import os, sys
import json
import bottle
from bottle import route, run, template, default_app, request, post, response, auth_basic, static_file
from json import dumps
from utils import translate, load_token, check_login, save_token, hash_str

index_html = '''{{ results }}'''

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/index.html')
@enable_cors
def server_static():
    return static_file('index.html', root='../frontend')

@route('/<dire>/<filename>')
@enable_cors
def acess(dire, filename):
    valida = load_token(request.cookies.get('token','0'))

    if(dire in ['csslogin','jslogin']):
        return static_file(filename, root='../frontend/'+ dire)
    if(dire in ['css','js']):
        if(valida):
            return static_file(filename, root='../frontend/'+ dire)
        else:
            return '<b>Acess Denied, go to <a href="http://127.0.0.1:8080/index.html">Login</a></b>!'

@route('/<filename>')
@enable_cors
def send_css(filename):
    token = request.cookies.get('token','0')
    if load_token(token):
        return static_file(filename, root='../frontend')
    else:
        return '<b>Acess Denied, go to <a href="http://127.0.0.1:8080/index.html">Login</a></b>!'

@post('/login')
@enable_cors
def do_login():
    
    postdata = request.body.read()
    dici = translate(postdata)

    res = check_login(dici['user'], dici['pass'])

    if res != False:
        token = hash_str(dici['user'])
        response.set_cookie("token", token)
        save_token(dici['user'],token)
        return "true"
    else:
        return "false"

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, reload=True, workers=4, debug=False)
