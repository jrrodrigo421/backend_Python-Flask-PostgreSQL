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


def executeQuery(query):
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                            password=db_pw, host=db_host)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def addTask(name, date):
    executeQuery(
        'INSERT INTO public."TaskList"(task_name, due_date) values(\'%s\', \'%s\')' % (name, date))


def updateTask(name, id):
    executeQuery(
        'UPDATE public."TaskList" SET task_name=\'% s\' WHERE id=%s;' % (name, id))


def deleteTask(id):
    executeQuery('DELETE FROM public."TaskList" WHERE id=%s;' % (id))
