import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

my_database = mysql.connector.connect(
        host=os.getenv("db_server"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        database=os.getenv("db_name")
    )
orders_table = "tbl_orders"
users_table = "tbl_users"
user_balance_table = "tbl_user_balance"


class Database():

    # @staticmethod
    # def create_db():
    #     my_cursor = mydb.cursor()
    #     my_cursor.execute("show databases")
    #     my_result = my_cursor.fetchall()
    #     for x in my_result:
    #         if config.db_name == x:
    #             my_cursor.execute(f"CREATE DATABASE {config.db_name}")
    #             config.SETUP_DB = 1
    #             Database.create_table()
    #     else:
    #         return True

    @staticmethod
    def create_table():
        cur = my_database.cursor()
        cur.execute("CREATE TABLE tbl_users (id int(11) NOT NULL AUTO_INCREMENT,"
                    "nick_name varchar(20) DEFAULT NULL,"
                    "full_name varchar(25) NOT NULL,"
                    "phone_number varchar(50) NOT NULL,"
                    "email_address varchar(50) NOT NULL,"
                    "password varchar(50) NOT NULL,"
                    "password_hash varchar(75) NOT NULL,"
                    "designation varchar(100) DEFAULT NULL,"
                    "role_id int(11) DEFAULT NULL,"
                    "is_login tinyint(1) NOT NULL DEFAULT 1,"
                    "PRIMARY KEY (id)"
                    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci")
        cur.execute("CREATE TABLE tbl_orders (id int(11) NOT NULL AUTO_INCREMENT,"
                    "symbol varchar(20) DEFAULT NULL,"
                    "amount decimal(15,2) DEFAULT 0,"
                    "price decimal(15,2) DEFAULT 0,"
                    "side varchar(100) DEFAULT NULL,"
                    "quantity int(11) DEFAULT 0,"
                    "profit decimal(15,2) DEFAULT 0,"
                    "time_date varchar(100) DEFAULT NULL,"
                    "PRIMARY KEY (id)"
                    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci")
        cur.execute("CREATE TABLE tbl_user_balance (id int(11) NOT NULL AUTO_INCREMENT,"
                    "user_id int(11) DEFAULT NULL,"
                    "balance decimal(15,2) NOT NULL,"
                    "account_number varchar(50) NOT NULL,"
                    "account_name varchar(50) NOT NULL,"
                    "created_date varchar(100) DEFAULT NULL,"
                    "updated_date varchar(100) DEFAULT NULL,"
                    "PRIMARY KEY (id)"
                    ") ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci")
        my_database.commit()
        return True

    @staticmethod
    def write_orders(data):
        cur = my_database.cursor()
        cur.execute('''INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
        my_database.commit()

    @staticmethod
    def get_orders(data):
        cur = my_database.cursor()
        cur.execute('''INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)''', data)
        my_database.commit()
