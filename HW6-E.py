m = int(input())
menu_names = []
menu_prices = []
menu_counts = [] # 用來統計全班該飲料的總杯數

for _ in range(m):
    drink, price_str = input().split()
    menu_names.append(drink)
    menu_prices.append(int(price_str))
    menu_counts.append(0) # 預設總杯數為 0

# 2. 讀取訂單資料
n = int(input())
order_students = []
order_drinks = []
order_quantities = []

# 用來記錄有哪些不重複的學生，以及他們在訂單首出現的順序
student_names = []
student_totals = []

for _ in range(n):
    student, drink, qty_str = input().split()
    qty = int(qty_str)
    
    order_students.append(student)
    order_drinks.append(drink)
    order_quantities.append(qty)
    
    # 累加該飲料的全班總杯數
    drink_idx = menu_names.index(drink)
    menu_counts[drink_idx] += qty
    
    # 記錄學生出現的順序
    if student not in student_names:
        student_names.append(student)
        student_totals.append(0)

# 3. 根據全班總杯數是否滿 10 杯，動態調整菜單單價
for i in range(m):
    if menu_counts[i] >= 10:
        menu_prices[i] -= 5

# 4. 計算每位學生的應付總額
for i in range(n):
    student = order_students[i]
    drink = order_drinks[i]
    qty = order_quantities[i]
    
    drink_idx = menu_names.index(drink)
    price = menu_prices[drink_idx]
    
    stu_idx = student_names.index(student)
    student_totals[stu_idx] += price * qty

# 5. 格式化輸出結果
# (1) 先輸出 M 行飲料杯數統計（依菜單順序）
for i in range(m):
    print(f"DRINK {menu_names[i]} {menu_counts[i]}")

# (2) 再輸出每個學生的應付金額（依訂單首出現順序）
for i in range(len(student_names)):
    print(f"STUDENT {student_names[i]} {student_totals[i]}")

# (3) 最後輸出一行 TOTAL 全班總額
print(f"TOTAL {sum(student_totals)}")