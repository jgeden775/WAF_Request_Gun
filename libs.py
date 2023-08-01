import os
import requests
import json


class iFace:
    def menuHead():
        os.system('cls || clear')
        print('WAF Request Gun v 0.1.9')
        print('-----------------------')
        print('')

    def entURL():
        print('Enter the target URL in the format: "http(s)://example.com"')
        print('')

    def entFile():
        print('Enter the target file in the format: "/dir/file"')
        print('')

    def wrongNum():
        print('')
        print('Wrong number!')

    def keyExit():
        print('')
        input('Press any key to exit')

    def keyBack():
        print('')
        input('Press any key to back')


class URL:
    def headers():
        with open('headers.json', 'r') as hfile:
            headers = json.load(hfile)

        return headers
    
    def body():
        with open('body.json', 'r') as bfile:
            body = json.load(bfile)

        return body

    def urlInput(url):
        if url == '':
            url = input('>> URL: ')
        return url

    def fileInput(file):
        if file == '':
            print('')
            iFace.entFile()
            file = input('>> FILE: ')
        return file

    def urlSet(url, method, path, headers, params, body):

        if method == 'get':
            response = requests.get(
                f'{url}{path}', headers = headers, params = params, json = body)
        elif method == 'post':
            response = requests.post(
                f'{url}{path}', headers = headers, params = params, json = body)

        return response

    def respCode(req):
        print('')
        print(f'>> Response code is: {req.status_code}')


class Atk:
    def injUnion():
        path = '/index.php'
        params = '\'union'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), params, URL.body())
        URL.respCode(req)

    def injGetUser():
        path = '/index.php'
        params = '\'select%20user%20from%20mysql.user'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), params, URL.body())
        URL.respCode(req)

    def injOutFile():
        path = '/index.php'
        params = '\'into%20outfile'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), params, URL.body())
        URL.respCode(req)

    def injLoadFile():
        path = '/index.php'
        params = '\'load_file()'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), params, URL.body())
        URL.respCode(req)

    def fileAccess():
        path = '/index.php'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), URL.fileInput(''), URL.body())
        URL.respCode(req)

    def injBWHTML():
        path = '/bWAPP/htmli_get.php'
        params = 'firstname=<a%20href=http://www.google.com>&lastname=click</a>'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), params, URL.body())
        URL.respCode(req)

    def injBWphp():
        path = '/bWAPP/phpi.php'
        params = 'message=%27FIX%20ME!%27'
        req = URL.urlSet(URL.urlInput(''), 'get', path, URL.headers(), params, URL.body())
        URL.respCode(req)