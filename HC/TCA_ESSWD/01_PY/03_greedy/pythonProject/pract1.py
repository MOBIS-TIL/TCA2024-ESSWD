n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse = True)

first = data[0]
second = data[1]

cnt = 0
result = 0

for i in range(m) :
    if cnt == k :
        result += second
        cnt = 0
    else :
        cnt += 1
        result += first

print(result)
