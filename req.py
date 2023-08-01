import libs


def main():
    libs.iFace.menuHead()
    print('Enter the number of option: ')
    print('')
    print('1. Injection UNION')
    print('2. Injection GET USER')
    print('3. Ijection LOAD FILE')
    print('4. Injection OUTFILE')
    print('5. File Access Attempt')
    print('6. Injection HTML Refl. GET (bWAPP)')
    print('7. Injection PHP (bWAPP)')
    print('0. Exit')
    print('')

    reqNum = input('>> ')
    print('')
    menuInput(reqNum)


def menuInput(num):
    if num == '1':
        libs.iFace.entURL()
        libs.Atk.injUnion()
        libs.iFace.keyExit()
        main()
    elif num == '2':
        libs.iFace.entURL()
        libs.Atk.injGetUser()
        libs.iFace.keyExit()
        main()
    elif num == '3':
        libs.iFace.entURL()
        libs.Atk.injLoadFile()
        libs.iFace.keyExit()
        main()
    elif num == '4':
        libs.iFace.entURL()
        libs.Atk.injOutFile()
        libs.iFace.keyExit()
        main()
    elif num == '5':
        libs.iFace.entURL()
        libs.Atk.fileAccess()
        libs.iFace.keyExit()
        main()
    elif num == '6':
        libs.iFace.entURL()
        libs.Atk.injBWHTML()
        libs.iFace.keyExit()
        main()
    elif num == '7':
        libs.iFace.entURL()
        libs.Atk.injBWphp()
        libs.iFace.keyExit()
        main()
    elif num == '0':
        exit
    else:
        libs.iFace.wrongNum()
        libs.iFace.keyBack()
        main()
