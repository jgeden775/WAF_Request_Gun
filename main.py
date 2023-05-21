import libs
import req
import flood
import dos


def main():
    libs.iFace.menuHead()
    print('Enter the number of program:')
    print('')
    print('1. Attack Requests')
    print('2. Flood Gun')
    print('3. DoS Gun')
    print('0. Exit')
    print('')

    mainNum = input('>> ')
    menuInput(mainNum)


def menuInput(num):
    if num == '1':
        req.main()
    elif num == '2':
        flood.floodGun()
    elif num == '3':
        dos.dosGun()
    elif num == '0':
        exit
    else:
        libs.iFace.wrongNum()
        libs.iFace.keyBack()
        main()


if __name__ == "__main__":
    main()
