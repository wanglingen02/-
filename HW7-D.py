def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 2. 定義簡化配方函式
def simplify_recipe(tea, milk, syrup):
    # 透過兩兩求 GCD，推導出三個數的最大公因數
    g = gcd(tea, gcd(milk, syrup))
    
    # 三個材料分別除以最大公因數，得到最簡整數比
    # 使用整數除法 // 確保輸出為整數
    return tea // g, milk // g, syrup // g

# 主程式
# 讀取配方數 N
n = int(input())

# 迴圈讀取並處理每一行配方
for _ in range(n):
    t, m, s = map(int, input().split())
    # 呼叫簡化函式
    ans_t, ans_m, ans_s = simplify_recipe(t, m, s)
    # 格式化輸出最簡比例
    print(f"{ans_t} {ans_m} {ans_s}")