s, d, t = map(int, input().split())

# 初始化經過天數為 0
days = 0

# 使用 while 迴圈，當目前存款 s 還沒達到目標金額 t 時就持續執行
while s < t:
    s += d      # 存款每天增加 d 元
    days += 1   # 天數增加 1 天

# 輸出最少天數
print(days)