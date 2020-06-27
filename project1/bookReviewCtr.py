from Book import Book
from User import User
from Review import Review
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, session
from flask_session import Session
class Controller():
    url = "postgres://gcztxtbtaigjma:c24730296b530720e4f729653533f73e373084ce256f965ff007f13013bf2f7b@ec2-54-236-169-55.compute-1.amazonaws.com:5432/d3kqjb70c0l7tc"
    def __init__(self):
        #All the books
        self.books = []
        #logined user
        self.user = None
        #All the review
        self.reviews = []
       # if not os.getenv("DATABASE_URL"):
          #  raise RuntimeError("DATABASE_URL is not set")
        #self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.engine=create_engine(Controller.url)
        self.db = scoped_session(sessionmaker(bind=self.engine))
       


    


    def registrate(self,userName,ps):
        tmp =  User(userName = userName, password=ps)
        #save to database
        
        self.db.execute("INSERT INTO users (username,password) VALUES(:userName, :password);",
                {"userName":tmp.userName,"password":tmp.password})
        #self.db.execute("INSERT INTO users (username,password) VALUES('user3', 'password3');")
        self.user = tmp
        self.db.commit()

    def login(self,username,password):
        tmp = self.db.execute("SELECT * FROM users WHERE username = :username AND password = :password;",
        {"username":username,"password":password})
        if tmp.rowcount == 0:
            return False
        else:
            tmp = tmp.fetchall()
            self.user= User(tmp[0][1],tmp[0][2])
            return True


    def logout(self):
        self.user = None
        

