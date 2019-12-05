import psycopg2
import gc


# connect to the database
def select_all():
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

    # issue query
    major = input('Enter a major: ')

    cmd = "SELECT * FROM student WHERE dept_name = %s"

    # every query needs a cursor, a cursor is a reference to the result
    # of a query
    cur = conn.cursor()
    cur.execute(cmd, (major,))

    return cur

