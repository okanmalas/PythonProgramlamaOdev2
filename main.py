#region Imports
import os
#endregion

#region Classes
class Book:
    def __init__(self, name, page_count, author, is_available=True):
        self.name = name
        self.page_count = page_count
        self.author = author
        self.is_available = is_available
    @staticmethod
    def add_book():
        pass

class EBook(Book):
    def __init__(self, name, page_count, author, size, is_available=True):
        super().__init__(name, page_count, author, is_available)
        self.size = size
    @staticmethod
    def add_book():
        print("Kitap ismi > ")
        name = input()
        print("Sayfa sayısı > ")
        page_count = input()
        print("Yazar > ")
        author = input()
        print("Boyut (Byte cinsinden) > ")
        size = input()
        return EBook(name, page_count, author, size)

class PhysicalBook(Book):
    def __init__(self, name, page_count, author, inventory_count, is_available=True):
        super().__init__(name, page_count, author, is_available)
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
    @staticmethod
    def add_book():
        print("Kitap ismi > ")
        name = input()
        print("Sayfa sayısı > ")
        page_count = input()
        print("Yazar > ")
        author = input()
        print("Adet > ")
        inventory_count = input()
        return PhysicalBook(name, page_count, author, inventory_count)

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    @staticmethod
    def add_user():
        print("isminiz > ")
        isim = input()
        print("emailiniz > ")
        email = input()
        print("şifreniz > ")
        sifre = input()
        return User(isim, email, sifre)

class Library:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.books = []
    def add_user(self):
        self.users.append(User.add_user())
    def add_physical_book(self):
        self.books.append(PhysicalBook.add_book())
    def add_ebook(self):
        self.books.append(EBook.add_book())
    def list_books(self):
        if not self.books:
            print("Kütüphanede kayıtlı kitap yok.")
        else:
            print("Kütüphane Kitapları:")
            for book in self.books:
                if isinstance(book, PhysicalBook):
                    print(f"- {book.name} ({book.author}) - {book.inventory_count} adet")
                else:
                    print(f"- {book.name} ({book.author}) - {book.size} byte")
    def list_users(self):
        if not self.users:
            print("Kayıtlı kullanıcı yok.")
        else:
            print("Kütüphane Kullanıcıları:")
            for user in self.users:
                print(f"- {user.name} ({user.email})")
#endregion

#region Static Methods
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    #yapay zeka tarafından oluşturulan bir fonksiyon
def main_menu():
    clear_screen()
    print(f"{library.name} kütüphanesine hoşgeldiniz")
    print("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    print("1. Kullanıcı Ekle")
    print("2. Kitap Ekle")
    print("3. Kitapları Listele")
    print("4. Kitap Ödünç Al")
    print("5. Kitap İade Et")
    print("6. Çıkış")
    try:
        result = int(input())
        return result
    except ValueError:
        clear_screen()
        print("Geçersiz Seçim.")
        print("Rastgele Bir Tuşa Basın.")
        input()
        return main_menu()
def ui():
    match main_menu():
        case 1:
            # todo: User ekle
            return True
        case 2:
            # todo: Kitap ekle
            return True
        case 3:
            # todo: Kitap listele
            return True
        case 4:
            # todo: Ödünç al
            return True
        case 5:
            # todo: İade et
            return True
        case 6:
            return False
        case _:
            return True
#endregion

#region Main
if __name__ == "__main__":
    library = Library("Malas")
    while ui():
        pass
    print("Program Kapanıyor...")
    pass
#endregion