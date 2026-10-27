n = int(input())

# 使用平行串列來儲存商品資料，完全不使用字典與集合
names = []
subtotals = []

# 讀取並計算每種商品的小計
for _ in range(n):
    name, price_str, qty_str = input().split()
    price = int(price_str)
    quantity = int(qty_str)
    
    # 買滿 3 件，其中 1 件免費（例如：買 7 件，有 7 // 3 = 2 件免費，實付 5 件）
    free_items = quantity // 3
    paid_items = quantity - free_items
    subtotal = paid_items * price
    
    # 存入串列
    names.append(name)
    subtotals.append(subtotal)

# 1. 輸出每種商品的名稱及優惠後小計
for i in range(n):
    print(f"{names[i]} {subtotals[i]}")

# 2. 計算並輸出 TOTAL 金額（合計滿 1000 元折 100 元，限折一次）
raw_total = sum(subtotals)
if raw_total >= 1000:
    final_total = raw_total - 100
else:
    final_total = raw_total
print(f"TOTAL {final_total}")

# 3. 找出最高小計的商品（同金額選輸入較早者）
max_val = subtotals[0]
top_idx = 0
for i in range(1, n):
    # 因為要求「同額選輸入較早者」，所以這裡用 > 而不是 >=
    if subtotals[i] > max_val:
        max_val = subtotals[i]
        top_idx = i

print(f"TOP {names[top_idx]}")