import psycopg2

db_name = "TaskListDB"
db_user = "tasklist_user"
db_pw = "root"
db_host = "localhost"


def getTaskList():
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                            password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute('SELECT id, task_name, is_done FROM public. "TaskList"')
    tasklist = cur.fetchall()
    cur.close
    conn.close

    return tasklist


def addTask(name, date):
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                            password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO public."TaskList"(task_name, due_date) values(\'%s\', \'%s\')' % (name, date))
    conn.commit()
    cur.close()
    conn.close()


def updateTask(name, id):
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                            password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute(
        'UPDATE public."TaskList" SET task_name=\'% s\' WHERE id=%s;' % (name, id))
    conn.commit()
    cur.close()
    conn.close()


def deleteTask(id):
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                            password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute(
        'DELETE FROM public."TaskList" WHERE id=%s;' % (id))
    conn.commit()
    cur.close()
    conn.close()
