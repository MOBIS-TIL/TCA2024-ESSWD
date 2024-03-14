n, m = map(int, input().split())

result = 0

for i in range(n) :
    data = list(map(int, input().split()))
    dmin = min(data)
    if dmin > result :
        result = dmin

print(result)
