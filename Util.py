import pymysql
class DBUtil:
    @staticmethod
    def connection():
        con=pymysql.connect(host="localhost", user="root", password="Root", database="db")
        return con