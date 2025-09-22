# multiplication_table.py
# Generate and print the multiplication table for a given number

# طلب رقم من المستخدم
number = int(input("Enter a number to see its multiplication table: "))

# توليد جدول الضرب باستخدام حلقة for
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")

