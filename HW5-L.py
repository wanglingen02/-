m = int(input())

# 初始化總硬幣數量變數為 0
coin_count = 0

# 使用 while 迴圈，當金額 m 大於 0 時，每次「逐枚」挑選最大面額扣除
while m > 0:
    if m >= 50:
        m -= 50
    elif m >= 10:
        m -= 10
    elif m >= 5:
        m -= 5
    else:
        m -= 1
    
    # 每扣除一枚硬幣，硬幣總數加 1
    coin_count += 1

# 輸出最少硬幣數
print(coin_count)