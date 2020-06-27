from bookReviewCtr import Controller
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
try:
   testLogout()
except RuntimeError:
    print("rasied an excpetion")