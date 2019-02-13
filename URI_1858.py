cases = int(input())
al = input().split()
al = list(map(int, al))
print(al.index(min(al)) + 1)
