#todo: add_book fonksiyonu düzenlenecek
class Book:
    def __init__(self, name, page_count, book_type, author, is_available=True):
        self.name = name
        self.page_count = page_count
        self.book_type = book_type
        self.author = author
        self.is_available = is_available

    def add_book(self, library):
        pass
class EBook(Book):
    def __init__(self, name, page_count, book_type, author, size, is_available=True):
        super().__init__(name, page_count, book_type, author, is_available)
        self.size = size
    def add_book(self,library):
        pass
class PhysicalBook(Book):
    def __init__(self, name, page_count, book_type, author, inventory_count, is_available=True):
        super().__init__(name, page_count, book_type, author, is_available)
        self.inventory_count = inventory_count

    def deposit_book(self):
        self.inventory_count += 1
        self.is_available = True

    def borrow_book(self):
        if self.inventory_count > 0:
            self.inventory_count -= 1
            if self.inventory_count == 0:
                self.is_available = False
            return True
        return False

    def add_book(self,library):
        pass
#endtodo

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
class Library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_user(self, user):
        if isinstance(user, User):
            self.users.append(user)
            print(f"Kullanıcı {user.name} başarıyla eklendi.")
        else:
            print("Geçersiz kullanıcı.")

    # todo: düzenlenecek
    def add_physical_book(self, book):
        if isinstance(book, PhysicalBook):
            self.books.append(book)
            print(f"Kitap '{book.name}' başarıyla eklendi.")
        else:
            print("Geçersiz kitap.")
    def add_ebook(self, book):
        if isinstance(book, EBook):
            self.books.append(book)
            print(f"Kitap '{book.name}' başarıyla eklendi.")
        else:
            print("Geçersiz kitap.")
    def list_books(self):
        if not self.books:
            print("Kütüphanede kayıtlı kitap yok.")
        else:
            print("Kütüphane Kitapları:")
            for book in self.books:
                status = "Mevcut" if book.is_available else "Mevcut Değil"
                print(f"- {book.name}, Yazar: {book.author} ({book.book_type}) - {status}")
    # endtodo

    def list_users(self):
        if not self.users:
            print("Kayıtlı kullanıcı yok.")
        else:
            print("Kütüphane Kullanıcıları:")
            for user in self.users:
                print(f"- {user.name} ({user.email})")

if __name__ == "__main__":
    #todo: main fonksiyonu yazılacak
    pass

