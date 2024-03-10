class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)

    def contracts(self):
        """Returns a list of contracts associated with the book"""
        return [contract for contract in Contract.all_contracts if contract.book == self]


class Author:
    all_authors = []
    contracts = []  # Optional list to store author's contracts

    def __init__(self, name):
        self.name = name
        self.all_authors.append(self)

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        contract = Contract(self, book, date, royalties)
        # Optionally, add the contract to the author's list
        self.contracts.append(contract)
        return contract

    def contracts(self):
        """Returns a list of contracts associated with the author"""
        return self.contracts  # Use the list if maintained by Author

    def books(self):
        """Returns a list of books associated with the author through contracts"""
        return [contract.book for contract in self.contracts()]

    def total_royalties(self):
        """Calculates total royalties earned by the author across all contracts"""
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts signed on a specific date"""
        return [contract for contract in cls.all_contracts if contract.date == date]


# Test Suite (using pytest)
def test_book_init():
    book = Book("Title")
    assert book.title == "Title"


def test_author_init():
    author = Author("Name")
    assert author.name == "Name"


def test_contract_init():
    author = Author("Name")
    book = Book("Title")
    contract = Contract(author, book, "01/01/2001", 50000)
    assert contract.author == author
    assert contract.book == book
    assert contract.date == "01/01/2001"
    assert contract.royalties == 50000


def test_contract_raises_error_for_non_author():
    book = Book("Title")
    with pytest.raises(Exception) as e:
        Contract("Invalid Author", book, "01/01/2001", 50000)
    assert str(e.value) == "Author must be an instance of the Author class"


def test_contract_raises_error_for_non_book():
    author = Author("Name")
    with pytest.raises(Exception) as e:
        Contract(author, "Invalid Book", "01/01/2001", 50000)
    assert str(e.value) == "Book must be an instance of the Book class"


def test_contract_raises_error_for_non_string_date():
    author = Author("Name")
    book = Book("Title")
    with pytest.raises(Exception) as e:
        Contract(author, book, 2021, 50000)
    assert str(e.value) == "Date must be a string"







