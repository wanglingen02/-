import sys
# 提高遞迴深度上限以防萬一
sys.setrecursionlimit(2000)

# 1. 定義記憶化遞迴函式（禁止使用迴圈與推導式）
def count_ways(step, n, blocked, memo):
    # 邊界條件 1：如果踩到損壞的階梯，或者超出總階數，此路不通
    if step > n or blocked[step]:
        return 0
    
    # 邊界條件 2：剛好安全到達第 N 階，找到 1 種有效走法
    if step == n:
        return 1
        
    # 檢查記憶體：如果這個位置之前已經算過，直接回傳紀錄
    if memo[step] != -1:
        return memo[step]
        
    # 遞迴步驟：走 1 階的走法 + 走 2 階的走法
    ways_1 = count_ways(step + 1, n, blocked, memo)
    ways_2 = count_ways(step + 2, n, blocked, memo)
    
    # 將結果記錄到記憶體中並回傳
    memo[step] = ways_1 + ways_2
    return memo[step]

# 主程式
# 讀取總階數 N 與損壞階數 K
first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])

# 初始化長度為 n + 1 的布林串列，預設皆未損壞
blocked = [False] * (n + 1)

# 如果 K > 0，讀取第二行的損壞階梯編號
if k > 0:
    broken_steps = map(int, input().split())
    for b in broken_steps:
        blocked[b] = True

# 初始化記憶體串列，初值皆為 -1
memo = [-1] * (n + 1)

# 呼叫題目規定的核心主程式並輸出結果
ans = count_ways(0, n, blocked, memo)
print(ans)