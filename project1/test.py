from bookReviewCtr import Controller
from Book import Book
def testBookReviewCtr():
    driver = Controller()
    driver.registrate("user4","ps4")
def testLogin():
    driver = Controller()
    print(driver.login("user4","ps4"))
    print(driver.user.userName)


def testLogout():
    driver = Controller()
    print(driver.login("user4","ps4"))
    print(driver.user.userName)
    driver.logout()
    print(driver.user)

def testReview():
    driver = Controller()
    assert(driver.login("user4","ps4"))
    book = Book(title = "The art of readable code",isbn = 1632168146, author="Boswell & Foucher", year=2012)
    driver.addReview("A very useful handbook",book)
def testAddBook():
    driver = Controller()
    assert(driver.login("user4","ps4"))
    book = Book(title = "The art of readable code",isbn = 1632168146, author="Boswell & Foucher", year=2012)
    driver.addBook(book)

def testSearch():
    driver = Controller()
    assert(driver.login("user4","ps4"))
    driver.search(isbn = 1632168)
    driver.search(title = "readable code")
    driver.search(author = "Boswell")
    pass
def testGoodReadAPI():
    driver = Controller()
    assert(driver.login("user4","ps4"))
    book = Book(title = "Krondor: The Betrayal", isbn = "380795272", author = "Raymond E. Feist", year = 1998)
    book2 = Book(title = "The Dark Is Rising",isbn = "1416949658",author = "Susan Cooper",year = 2000 ) 
    book3 = Book(title = "",isbn = "1632168146",author = "",year = 2000 ) 
    driver.searchFromGoodReads(book)
    driver.searchFromGoodReads(book2)
    driver.searchFromGoodReads(book3)
try:
   #testAddBook()
   #testSearch()
   testGoodReadAPI()
except RuntimeError:
    print("rasied an excpetion")