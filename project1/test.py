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

try:
   #testAddBook()
   testSearch()
except RuntimeError:
    print("rasied an excpetion")