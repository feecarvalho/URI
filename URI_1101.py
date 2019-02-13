aux = []
soma = 0

values = input().split(' ')
m, n = values
m = int(m)
n = int(n)

while m > 0 and n > 0:
    if n < m:
        for num in range(n, m + 1):
            aux.append(num)
            soma += num
        string = " ".join(map(str, aux))
        print(string, 'Sum=%d' % soma)
        soma = 0
        aux = []
        string = '0'
    elif n > m:
        for num in range(m, n + 1):
            aux.append(num)
            soma += num
        string = " ".join(map(str, aux))
        print(string, 'Sum=%d' % soma)
        soma = 0
        aux = []
        string = '0'
    values = input().split(' ')
    m, n = values
    m = int(m)
    n = int(n)
