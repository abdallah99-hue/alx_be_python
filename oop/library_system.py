# library_system.py

# الفئة الأساسية
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# الفئات المشتقة
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # استدعاء المنشئ الأساسي
        self.file_size = file_size  # سمة إضافية

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # استدعاء المنشئ الأساسي
        self.page_count = page_count  # سمة إضافية

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# فئة المكتبة باستخدام التكوين
class Library:
    def __init__(self):
        self.books = []  # قائمة لتخزين كل أنواع الكتب

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
