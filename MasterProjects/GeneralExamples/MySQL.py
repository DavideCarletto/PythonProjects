import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from decimal import Decimal

DB_NAME = "pySQL"
config = {
            "host":"localhost",
            "user" :"root",
            "password": "",
            "buffered": True
}

tomorrow = datetime.now().date() + timedelta(days=1)

TABLES = {}
#region Tables declaration
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE `salaries` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `salary` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_emp'] = (
    "CREATE TABLE `dept_emp` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_manager'] = (
    "  CREATE TABLE `dept_manager` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`),"
    "  KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['titles'] = (
    "CREATE TABLE `titles` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `title` varchar(50) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date DEFAULT NULL,"
    "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`);w"
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")
#endregion del

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def create_tables(curs):

    '''creazione manuale delle tabelle, successivamente caricate da cmd
    con il comando mysql -u root < employees.sql (prima bisogna recarsi nella cartella dove è contenuto il file)
    '''

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            curs.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

def add_employee(curs):
    add_employees = (
        "INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)")
    data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

    curs.execute(add_employees, data_employee)


def search_between_hiredate(curs):
    query = "SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN %s AND %s ORDER BY last_name LIMIT 5"

    hire_start = date(1999, 1, 1)
    hire_end = date(1999, 1, 2)

    curs.execute(query,(hire_start,hire_end))

    for (first_name, last_name, hire_date) in curs:
        print("{}, {} was hired on {:%d %b %Y}".format(
            last_name, first_name, hire_date))

def raise_salaries(cursA,cursB):
    query = (
        "SELECT s.emp_no, salary, from_date, to_date FROM employees AS e "
        "LEFT JOIN salaries AS s USING (emp_no) "
        "WHERE to_date = DATE('9999-01-01')"
        "AND e.hire_date BETWEEN DATE(%s) AND DATE(%s)")

    update_old_salary = (
        "UPDATE salaries SET to_date = %s "
        "WHERE emp_no = %s AND from_date = %s")
    insert_new_salary = (
        "INSERT INTO salaries (emp_no, from_date, to_date, salary) "
        "VALUES (%s, %s, %s, %s)")

    cursA.execute(query, (date(2000, 1, 1), date(2000, 12, 31)))


    for (emp_no, salary, from_date, to_date) in cursA:
        new_salary = int(round(salary * Decimal('1.15')))
        cursB.execute(update_old_salary, (tomorrow, emp_no, from_date))
        cursB.execute(insert_new_salary,
                     (emp_no, tomorrow, date(9999, 1, 1, ), new_salary))


def main():

    try:
        connection = mysql.connector.connect(**config)
        curs = connection.cursor()
        cursB = connection.cursor()
        curs.execute("USE {}".format(DB_NAME))

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            res = input("Database does not exist, do you want to create one (y/n)?")

            if(res.lower() == "y"):
                create_database(curs)
                print("Database {} created successfully.".format(DB_NAME))
                curs.database = DB_NAME

            elif(res.lower()== "n"):
                print("Closing the process...")

            else:
                print("Wrong input")

        else:
            print(err)

    #create_tables(curs)

    #add_employee(curs)

    #search_between_hiredate(curs)

    #raise_salaries(curs,cursB)
    #connection.commit()

    curs.close()
    connection.close()

if __name__ == "__main__":
    main()