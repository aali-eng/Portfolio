# Write your code here
print("Earned amount:")
print("""
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
""")
print("Income: 5405")
staff_expenses = int(input("Staff expenses: "))
other_expenses = int(input("Other expenses: "))
print(f"Net income ${5405 - staff_expenses - other_expenses}")