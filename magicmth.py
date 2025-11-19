class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
            and self.pages == other.pages
        )

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, word):
        return word in self.title or word in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            raise KeyError(f"Key {key} not found")


book1 = book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = book("1984", "George Orwell", 328)
print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
print(book1 + book2)
print("Great" in book1)
print(book1["author"])
