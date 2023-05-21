import libs


def main():
    libs.iFace.menuHead()
    print('Enter the number of option: ')
    print('')
    print('1. Bad URL')
    print('2. Injection UNION')
    print('3. Injection GetUser')
    print('4. Injection LOADFILE')
    print('0. Exit')
    print('')

    reqNum = input('>> ')
    print('')
    menuInput(reqNum)


def menuInput(num):
    if num == '1':
        libs.iFace.entURL()
        libs.Atk.badURL()
        libs.iFace.keyExit()
        main()
    elif num == '2':
        libs.iFace.entURL()
        libs.Atk.injUnion()
        libs.iFace.keyExit()
        main()
    elif num == '3':
        libs.iFace.entURL()
        libs.Atk.injGetUser()
        libs.iFace.keyExit()
        main()
    elif num == '4':
        libs.iFace.entURL()
        libs.Atk.injLoadFile()
        libs.iFace.keyExit()
        main()
    elif num == '0':
        exit
    else:
        libs.iFace.wrongNum()
        libs.iFace.keyBack()
        main()
