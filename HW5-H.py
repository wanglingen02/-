n = int(input())

# 初始化各位數總和變數為 0
digit_sum = 0

# 如果輸入剛好是 0，因為不進入 while 迴圈，最後會直接正確輸出 0
# 使用 while 迴圈，當 n 大於 0 時持續拆解
while n > 0:
    digit_sum += n % 10  # 用 % 10 取出當前的個位數並累加
    n = n // 10          # 用 // 10 去掉當前的個位數，將數字右移一位

# 輸出最終各位數總和
print(digit_sum)