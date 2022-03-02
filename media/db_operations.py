import pymysql
from pymysql.err import OperationalError, ProgrammingError

# b6_data


def get_database_conn(database_name):
    try:
        db_conn = pymysql.connect(host="localhost", user="root", password="root", database=database_name)  # risky code
        # print("Connected Successfully..!")
        return db_conn
    except OperationalError:
        return f"{database_name} doesn't exists in your database..!"


# print(get_database_conn("b6_data"))

def get_dbs_list():
    conn = get_database_conn("b6_data")
    query = "show databases"
    com_channel = conn.cursor()   # communication channel
    com_channel.execute(query)
    resultset = com_channel.fetchall()   # fetchall()   , fetchone(), fetchmany()
    # db_list = list(map(lambda x: x[0], resultset))
    print(resultset)
    
# get_dbs_list()

def show_tables():
    conn = get_database_conn("b6_data")
    query = "show tables"
    com_channel = conn.cursor()   # communication channel
    com_channel.execute(query)
    resultset = com_channel.fetchall()
    if resultset:
        print(resultset)
    else:
        print("No any table found in db.")

# show_tables()


def create_table_in_db(tb_name):
    conn = get_database_conn("b6_data")
    create_table_query = f"create table {tb_name} (eid int AUTO_INCREMENT, name varchar(100), salary float, primary key(eid))"
    com_channel = conn.cursor()   # communication channel
    com_channel.execute(create_table_query)
    print("Table created successfully..!")

# create_table_in_db("emp_data")

def insert_data_in_table():
    conn = get_database_conn("b6_data")
    insert_query = "insert into emp_data (name, salary) values ('Deepti', 64247), ('Girish', 69847), ('Omkar', 87457)"
    com_channel = conn.cursor()   
    com_channel.execute(insert_query)
    print("Data inserted successfully...!")
    conn.commit()


# insert_data_in_table()


def read_from_db():
    conn = get_database_conn("b6_data")
    read_query = "select * from emp_data"  # f"update emp_data set name='{}' where eid={}"  - commit -- 
    com_channel = conn.cursor()   
    com_channel.execute(read_query)
    data = com_channel.fetchall()
    for emp in data:
        print(f""" ------ Emp ID:- {emp[0]} ------
Emp Name:- {emp[1]}
Emp Salary:- {emp[2]}
        """)


# read_from_db()


# Assignment:- 6
# -- Product Class -- pid, name, cat, price, qty

# class DBOperattion:  # modular code
# methods

# generate_product -- cat -- ["Ele", "Wood"]   - random choice -- cat

# table -  create ---- 
# prod_list =-- for i in ----- f"{}"


# f"insert into emp_data (name, salary) values ('{prod.prodname}', {prod.price})"

# update -- price update
# read -- emp object create -- return list --

# main method --- 

# select * from table where id={} --- get_all_data-- 
# read single -- 
# exception handling --- 
# resultset -- no data -- print()


# 13 th January -- 