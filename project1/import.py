import csv
from Book import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
url = "postgres://gcztxtbtaigjma:c24730296b530720e4f729653533f73e373084ce256f965ff007f13013bf2f7b@ec2-54-236-169-55.compute-1.amazonaws.com:5432/d3kqjb70c0l7tc"
def importBook(fileName):
    engine=create_engine(url)
    db = scoped_session(sessionmaker(bind=engine))
    f = open(fileName)
    count = 0
    if f is not None:
        reader = csv.reader(f)
        for isbn, title, author, year in reader:
            try:
                db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn":isbn,"title":title,"author":author,"year":year})
                db.commit()    
                count += 1
                print("imported %s books"%str(count))
            except Exception:
                db.commit()
                print("can't imoport %s"%title)
    print("imported %s books in total"%str(count))

def main():
    importBook("books.csv")

if __name__ == "__main__":
    main()