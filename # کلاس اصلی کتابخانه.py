class Library:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def list_items(self):
        for item in self.items:
            print(item)
    def borrow_item(self, title):
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                print(f"{title} amanat gerefte shod.")
                return
        print(f"{title}  mojood nemebashd.")


    def add_new_item(self):
        print("Noe item ra vared konid (ketab/majale/payan-name): ")
        item_type = input().strip().lower()
        print("Onvan ra vared konid: ")
        title = input().strip()
        print("Nevisande ra vared konid: ")
        nevisande = input().strip()
        print("Sal enteshar ra vared konid: ")
        year = input().strip()

        if item_type == "ketab":
            print("Shomare ketab ra vared konid: ")
            isbn = input().strip()
            new_item = ketab(title, nevisande, year, isbn)
        elif item_type == "majale":
            print("Shomare majale ra vared konid: ")
            issue_number = input().strip()
            new_item = majale(title, nevisande, year, issue_number)
        elif item_type == "payan-name":
            print("Nam payan_name ra vared konid: ")
            university = input().strip()
            new_item = payan_name(title, nevisande, year, university)
        else:
            print("Noe item ghalat.")
            return

        self.add_item(new_item)
        print(f"{title} be ketabkhane ezafe shod.")

    def remove_item(self):
        print("Onvane itemi ke mikhahid amanat bardarid ra vared konid:(ketab/majale/payan-name) ")
        title = input().strip()
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                print(f"{title} az ketabkhane hazf shod.")
                return
        print(f"{title} dar ketabkhane mojood nist.")

    def manage_library(self):
        print("Aya mikhahid item gharar dahid ya  bardarid? (gh(gharar dadan)/b(bardashtan)): ")
        action = input().strip().lower()
        if action == "gh":
            self.add_new_item()
        elif action == "b":
            self.remove_item()
        else:
            print("dobare talash konid")

#در اینجا کلاس مربوط به کتابخانه را گفتیم 
class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} tavasote {self.author}, {self.year}"
# در اینجا کلاس مربوط به کتاب
class ketab(LibraryItem):
    def __init__(self, title, author, year, shomare):
        super().__init__(title, author, year)
        self.shomare = shomare

# کلاس مجله
class majale(LibraryItem):
    def __init__(self, title, author, year, number):
        super().__init__(title, author, year)
        self.number = number
# کلاس پایان‌نامه
class payan_name(LibraryItem):
    def __init__(self, title, author, year, university):
        super().__init__(title, author, year)
        self.university = university


library = Library()
# از طریق ترمینال بتونیم دستور بدیم
library.manage_library()
# اخرین وضعیت نشون میده
library.list_items()
