class Publication: 

    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def info(self):
        return f"Title: {self._title}\nAuthor: {self._author}"

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @author.setter
    def author(self, new_author):
        self._author = new_author

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self._number_of_pages = number_of_pages

    @property
    def number_of_pages(self):
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, new_number_of_pages):
        if new_number_of_pages > 0:
            self._number_of_pages = new_number_of_pages
        else:
            print("Number of pages must be positive.")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self._issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, new_issue_number):
        if new_issue_number > 0:
            self._issue_number = new_issue_number
        else:
            print("Issue number must be positive.")

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
print(pub1.info)

print("\nBook Information:")
book1.number_of_pages = -310
print(book1.info)
print(book1.number_of_pages)

print("\nMagazine Information:")
print(mag1.info)
print(mag1.issue_number)