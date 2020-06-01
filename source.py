import sqlite3
from datetime import datetime

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('data\Logical.db')
        self.cursor = self.conn.cursor()
        self.conn.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Book_ID TEXT, Book_Title TEXT, Author TEXT,Book_STD TEXT,Book_Price TEXT,Date TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS STUDENT_RECORD(id INTEGER PRIMARY KEY, Member_Type TEXT, StudentID TEXT, Name TEXT, Class TEXT, Section TEXT, Issue_Date TEXT, Return_Date TEXT, BookID TEXT, Book_Title TEXT, Author TEXT, Book_STD TEXT, Book_Price TEXT, Date TEXT)")
        self.conn.commit()
        

    def __del__(self):
        self.conn.close()
#--------------------------------------------------------------------------------------books-----------
    def books(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return rows
    
    def insert1(self, Book_ID, Book_Title, Author, Book_STD, Book_Price, Date):
        self.cursor.execute("INSERT INTO books VALUES (NULL,?,?,?,?,?,?)", (Book_ID, Book_Title, Author, Book_STD, Book_Price, Date))
        self.conn.commit()

    def search1(self, Book_STD=" "):
        self.cursor.execute("SELECT * FROM books WHERE Book_STD = ?",(Book_STD))
        found_rows = self.cursor.fetchall()
        return found_rows
    
    def update1(self, id, Book_ID, Book_Title, Author, Book_STD, Book_Price, Date):
        self.cursor.execute("UPDATE books SET Book_ID=?, Book_Title=?, Author=?, Book_STD=?, Book_Price=?, Date=? WHERE id=?",
                            (Book_ID, Book_Title, Author, Book_STD, Book_Price, Date,id))
        self.conn.commit()

    def delete1(self, id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()
#----------------------------------------STUDENT_RECORD------------------------------------------
    def STUDENT_RECORD(self):
        self.cursor.execute("SELECT * FROM STUDENT_RECORD")
        rows = self.cursor.fetchall()
        return rows

    def insert2(self, Member_Type,StudentID, Name, Class, Section, Issue_Date, Return_Date, BookID, Book_Title, Author, Book_STD, Book_Price, Date):
        self.cursor.execute("INSERT INTO STUDENT_RECORD VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", (Member_Type,StudentID, Name, Class, Section, Issue_Date, Return_Date, BookID, Book_Title, Author, Book_STD, Book_Price, Date))
        self.conn.commit()

    def update2(self, id, Date):
        self.cursor.execute("UPDATE STUDENT_RECORD SET Date=? WHERE id=?",(Date,id))
        self.conn.commit()

    def search2(self,id, Date=""):
        self.cursor.execute("SELECT *FROM STUDENT_RECORD SET Date=? WHERE id=?",(Date,id))
        found_rows = self.cursor.fetchall()
        return found_rows