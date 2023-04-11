import psycopg2

# db_name = "TaskListDB"
# db_user = "tasklist_user"
# db_pw = "root"
# db_host = "localhost"


db_name = "d4e9vv9rf1ck4t"
db_user = "lyphsfaebehbbi"
db_pw = "b41eab2ba62a80d0156e8e2996b2bc47bb53ac7a1dccdeee56aeeae59694a024"
db_host = "ec2-52-54-200-216.compute-1.amazonaws.com"
db_port = 5432


def getTaskList():
    conn = psycopg2.connect(dbname=db_name, user=db_user,
                            password=db_pw, host=db_host, port=db_port)
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
