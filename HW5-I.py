n = int(input())

# 初始化反轉後的數字變數為 0
reversed_num = 0

# 如果輸入剛好是 0，因為不進入 while 迴圈，最後會直接正確輸出 0
# 使用 while 迴圈，當 n 大於 0 時持續進行反轉建立
while n > 0:
    remainder = n % 10                # 取出目前的個位數
    reversed_num = reversed_num * 10 + remainder  # 原本的數字乘以 10 再加上新數字，達成平移效果
    n = n // 10                       # 去掉目前的個位數

# 輸出最終反轉後的整數（純數值運算會自動去除前導零）
print(reversed_num)