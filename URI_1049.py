a = input()
b = input()
c = input()

if a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        if c == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")
else:
    if b == 'ave':
        if c == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if c == 'onivoro':
            print("homem")
        else:
            print("vaca")
