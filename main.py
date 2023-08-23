def primenumberf():
    print('From which to which number do you wish to see the prime numbers?')
    while True:
        try:
            limit1 = input('From:')
            limit2 = input('To:')
            limit1 = int(limit1)
            limit2 = int(limit2)
            break
        except:
            print('Unfathomable. Please try again.')
    counter_1 = 2
    counter_2 = 0
    while limit1 < 11 and limit1 <= limit2:
        while (limit1 / 2) >= counter_1:
            if limit1 % counter_1 == 0:
                counter_2 += 1
                break
            counter_1 += 1
        if counter_2 == 0:
            print(limit1)
        limit1 += 1
        counter_1 = 2
        counter_2 = 0
    while limit1 >= 11 and limit1 <= limit2:
        while (limit1 / 4) >= counter_1:
            if limit1 % counter_1 == 0:
                counter_2 += 1
                break
            counter_1 += 1
        if counter_2 == 0:
            print(limit1)
        limit1 += 1
        counter_1 = 2
        counter_2 = 0
    ask = input('Do you wish to use the program again?').lower()
    return ask

loopvar = primenumberf()
while loopvar == 'yes':
    loopvar = primenumberf()