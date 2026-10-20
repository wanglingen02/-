total_sum = 0

# 先讀取第一筆整數
num = int(input())

# 使用 while 迴圈，當讀到的數字不等於 0 時就持續執行
while num != 0:
    total_sum += num    # 將數值累加到總和中
    num = int(input())  # 繼續讀取下一行整數

# 輸出最終總和
print(total_sum)