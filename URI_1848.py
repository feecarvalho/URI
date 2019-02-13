while True:
    try:
        total = 0
        str1 = input().strip()
        while str1 != 'caw caw':
            if str1 == '--*':
                total += 1
            elif str1 == '-*-':
                total += 2
            elif str1 == '*--':
                total += 4
            elif str1 == '-**':
                total += 3
            elif str1 == '***':
                total += 7
            elif str1 == '**-':
                total += 6
            elif str1 == '*-*':
                total += 5
            str1 = input().strip()
        if str1 == 'caw caw':
            print(total)
    except EOFError:
        break
