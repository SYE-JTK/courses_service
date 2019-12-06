import psycopg2
import gc


def all_stud():
    try:
        conn = psycopg2.connect(
            dbname="jbpeek16_university",
            user="jbpeek16",
            host="cs-linuxlab-02.stlawu.local",
            password="Vnr7mr86"
        )
        gc.collect()
        print("Successfully connected to database")
    except psycopg2.Error:
        print("Cannot connect to database")
        exit()

    cmd = "SELECT * FROM student WHERE dept_name = 'Comp. Sci.';"

    # every query needs a cursor, a cursor is a reference to the result
    # of a query
    cur = conn.cursor()
    cur.execute(cmd)

    output = ""
    for each in cur:
        output += "<div>" + str(each) + "</div>"
    return output


def courses():
    try:
        conn = psycopg2.connect(
            dbname="jbpeek16_university",
            user="jbpeek16",
            host="cs-linuxlab-02.stlawu.local",
            password="Vnr7mr86"
        )
        gc.collect()
        print("Successfully connected to database")
    except psycopg2.Error:
        print("Cannot connect to database")
        exit()

    cmd = "SELECT title, dept_name FROM course ORDER BY dept_name;"

    # every query needs a cursor, a cursor is a reference to the result
    # of a query
    cur = conn.cursor()
    cur.execute(cmd)

    output = ""
    for each in cur:
        output += "<div>" + str(each[0]) + "</div><div>Dept: " + str(each[1]) + "</div><br/>"
    return output


def depts():
    try:
        conn = psycopg2.connect(
            dbname="jbpeek16_university",
            user="jbpeek16",
            host="cs-linuxlab-02.stlawu.local",
            password="Vnr7mr86"
        )
        gc.collect()
        print("Successfully connected to database")
    except psycopg2.Error:
        print("Cannot connect to database")
        exit()

    cmd = "SELECT * FROM department;"

    # every query needs a cursor, a cursor is a reference to the result
    # of a query
    cur = conn.cursor()
    cur.execute(cmd)

    output = ""
    for each in cur:
        output += "<div>" + str(each[0]) + "</div>"
    return output
