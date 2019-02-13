num = int(input())
roman = []

while num != 0:
    if num >= 1000:
        roman.append('M')
        num -= 1000
    elif num >= 500:
        if num >= 900:
            roman.append('CM')
            num -= 900
        else:
            roman.append('D')
            num -= 500
    elif num >= 100:
        if num >= 400:
            roman.append('CD')
            num -= 400
        else:
            roman.append('C')
            num -= 100
    elif num >= 50:
        if num >= 90:
            roman.append('XC')
            num -= 90
        else:
            roman.append('L')
            num -= 50
    elif num >= 10:
        if num >= 40:
            roman.append('XL')
            num -= 40
        else:
            roman.append('X')
            num -= 10
    elif num >= 5:
        if num == 9:
            roman.append('IX')
            num -= 9
        else:
            roman.append('V')
            num -= 5
    elif num >= 1:
        if num == 4:
            roman.append('IV')
            num -= 4
        else:
            roman.append('I')
            num -= 1
print(*roman, sep='')
