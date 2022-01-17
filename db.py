import sqlite3
class Database():

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor();
        self.cur.execute("create table if not exists Items(id integer primary key,Item text,customer text,vendor text,price integer)")
        self.conn.commit();

    def fetch(self):
        self.cur.execute("select * from Items;")
        rows=self.cur.fetchall()
        return rows

    def insert(self,Item,customer,vendor,price):
        self.cur.execute("insert into Items values(NULL,?,?,?,?)",(Item,customer,vendor,price))
        self.conn.commit()

    def remove(self,id):
        self.cur.execute("DELETE from Items where id=?;",(id,))
        self.conn.commit()

    def update(self,id,Item,customer,vendor,price):
        self.cur.execute("UPDATE Itemss SET Item=?,customer=?,vendor=?,price=? where id=?",(Item,customer,vendor,price,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
        
db= Database("Stock.db")
