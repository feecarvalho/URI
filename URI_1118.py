def get_input():
    inp = float(input())
    if inp > 10.0 or inp < 0.0:
        print("nota invalida")
        return get_input()
    else:
        return inp


def calculate():
    a = get_input()
    b = get_input()
    media = (float(a) + float(b)) / 2.00
    return media


def redo():
    print("novo calculo (1-sim 2-nao)")
    X = float(input())
    if X < 1 or X > 2:
        redo()
    elif X == 2:
        return False
    elif X == 1:
        return True


while True:
    num = float(calculate())
    print("media = %0.2f" % num)
    x = redo()
    if x == False:
        break
