import pymysql

old_query = pymysql.connections.Connection.query
def query_annotation(self, query, *args, **kwargs):
    return old_query(self, f"{query} /* Test */", *args, **kwargs)
pymysql.connections.Connection.query = query_annotation

connection = pymysql.connect(host='localhost')
cursor = connection.cursor()
cursor.execute("select sleep(2)")
