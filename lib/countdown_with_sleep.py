

import time


def countdown_with_sleep():
    number = 10
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)
        number -= 1

    print("HAPPY NEW YEAR!") 