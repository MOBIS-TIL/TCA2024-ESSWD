n = 10
coin_types = [500, 100, 50, 10]

cnt = 0

for coin in coin_types :
    while n >= coin :
        n -= coin
        cnt += 1

print(cnt)