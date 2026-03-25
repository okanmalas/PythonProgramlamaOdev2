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
        return EBook(name, int(page_count), author, int(size))

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
        return PhysicalBook(name, int(page_count), author, int(inventory_count))

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.borrowed_books = []

    @staticmethod
    def add_user():
        print("isminiz > ")
        isim = input()
        print("emailiniz > ")
        email = input()
        print("şifreniz > ")
        sifre = input()
        return User(isim, email, sifre)

    @staticmethod
    def login(users):
        print("Email > ")
        email = input()
        print("Şifre > ")
        password = input()
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None

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
    print("4. Kullanıcı Girişi (Ödünç Al/İade Et)")
    print("5. Çıkış")
    try:
        result = int(input())
        return result
    except ValueError:
        clear_screen()
        print("Geçersiz Seçim.")
        print("Rastgele Bir Tuşa Basın.")
        input()
        return main_menu()
def user_menu(user):
    while True:
        clear_screen()
        print(f"Hoşgeldiniz, {user.name}")
        print("1. Kitap Ödünç Al")
        print("2. Kitap İade Et")
        print("3. Emanet Aldığım Kitaplar")
        print("4. Çıkış")
        choice = input("Seçiminiz > ")
        match choice:
            case "1":
                clear_screen()
                library.list_books()
                book_name = input("Ödünç almak istediğiniz kitabın ismini girin: ")
                found = False
                for book in library.books:
                    if book.name == book_name:
                        found = True
                        if isinstance(book, PhysicalBook):
                            if book.borrow_book():
                                user.borrowed_books.append(book)
                                print(f"{book_name} ödünç alındı.")
                            else:
                                print(f"{book_name} şu an mevcut değil.")
                        else:
                            print("E-Kitaplar ödünç alınamaz, her zaman indirilebilir.")
                        break
                if not found:
                    print(f"{book_name} kütüphanede bulunamadı.")
                input("Devam etmek için bir tuşa basın...")
            case "2":
                clear_screen()
                if not user.borrowed_books:
                    print("Emanet aldığınız kitap bulunmamaktadır.")
                else:
                    print("Emanet Aldığınız Kitaplar:")
                    for i, book in enumerate(user.borrowed_books):
                        print(f"{i+1}. {book.name}")
                    book_name = input("İade etmek istediğiniz kitabın ismini girin: ")
                    found_in_user = False
                    for book in user.borrowed_books:
                        if book.name == book_name:
                            found_in_user = True
                            book.deposit_book()
                            user.borrowed_books.remove(book)
                            print(f"{book_name} iade edildi.")
                            break
                    if not found_in_user:
                        print(f"{book_name} emanet listenizde bulunamadı.")
                input("Devam etmek için bir tuşa basın...")
            case "3":
                clear_screen()
                if not user.borrowed_books:
                    print("Emanet aldığınız kitap bulunmamaktadır.")
                else:
                    print("Emanet Aldığınız Kitaplar:")
                    for book in user.borrowed_books:
                        print(f"- {book.name} ({book.author})")
                input("Devam etmek için bir tuşa basın...")
            case "4":
                break
            case _:
                print("Geçersiz seçim.")
                input("Devam etmek için bir tuşa basın...")
def ui():
    match main_menu():
        case 1:
            clear_screen()
            library.add_user()
            print("Kullanıcı eklendi. Devam etmek için bir tuşa basın.")
            input()
            return True
        case 2:
            clear_screen()
            print("1. Fiziksel Kitap")
            print("2. E-Kitap")
            choice = input("Seçiminiz > ")
            if choice == "1":
                library.add_physical_book()
            elif choice == "2":
                library.add_ebook()
            else:
                print("Geçersiz seçim.")
            print("Kitap eklendi. Devam etmek için bir tuşa basın.")
            input()
            return True
        case 3:
            clear_screen()
            library.list_books()
            print("\nDevam etmek için bir tuşa basın.")
            input()
            return True
        case 4:
            clear_screen()
            print("--- Kullanıcı Girişi ---")
            user = User.login(library.users)
            if user:
                user_menu(user)
            else:
                print("Giriş başarısız. Email veya şifre hatalı.")
                input("Devam etmek için bir tuşa basın...")
            return True
        case 5:
            return False
        case _:
            clear_screen()
            print("Geçersiz Seçim.")
            print("Devam Etmek için bir tuşa basın...")
            input()
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