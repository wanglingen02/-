def best_total(prices, index, remaining):
    # 基礎條件（Base Case）：當所有商品都考慮完了，無法再獲得任何價值，回傳 0
    if index == len(prices):
        return 0
        
    # 分支一：不選目前商品
    skip_current = best_total(prices, index + 1, remaining)
    
    # 分支二：如果剩餘預算買得起目前商品，則嘗試選目前商品
    take_current = 0
    if remaining >= prices[index]:
        take_current = prices[index] + best_total(prices, index + 1, remaining - prices[index])
        
    # 回傳兩種決策中的最大購物總額
    return max(skip_current, take_current)

# 主程式
# 讀取商品件數 N 與總預算 B
n, b = map(int, input().split())

# 讀取 N 個商品的價格
item_prices = list(map(int, input().split()))

# 主程式呼叫題目指定的起始參數並輸出結果
ans = best_total(item_prices, 0, b)
print(ans)