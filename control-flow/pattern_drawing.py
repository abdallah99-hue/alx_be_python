# pattern_drawing.py
# Draw a square pattern of asterisks using nested loops

# طلب حجم النمط من المستخدم
size = int(input("Enter the size of the pattern: "))

# التحقق من أن الرقم موجب
if size <= 0:
    print("Please enter a positive integer.")
else:
    # العدادات
    row = 0
    while row < size:
        # حلقة لطباعة الأعمدة في الصف الحالي
        for col in range(size):
            print("*", end="")
        print()  # الانتقال للسطر التالي بعد كل صف
        row += 1
