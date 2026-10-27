target = int(input())
steps = list(map(int, input().split()))

# 1. 計算總步數
total_steps = sum(steps)

# 2. 計算達標天數 與 3. 找出最高步數出現的所有日期
achieve_count = 0
max_steps = max(steps)
max_days = []

for i in range(7):
    # 判斷達標天數（日期為第 1 至第 7 天，索引為 i + 1）
    if steps[i] >= target:
        achieve_count += 1
    
    # 判斷是否為最高步數日期
    if steps[i] == max_steps:
        max_days.append(str(i + 1))

# 4. 計算最長連續達標天數（連續記錄只計本週，不把第 7 天與第 1 天接起來）
max_continuous = 0
current_continuous = 0

for i in range(7):
    if steps[i] >= target:
        current_continuous += 1
        if current_continuous > max_continuous:
            max_continuous = current_continuous
    else:
        current_continuous = 0