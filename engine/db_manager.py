import psycopg2
import re

class DbManager(object):
        def __init__(self):
                self.connections = {}

        def open_connection(self, con_name, user, password, host='localhost', port=5432, database=''):
                con = Connection(user, password, host, port, database)
                self.connections[con_name] = con
                return con

        def close_connection(self, con_name):
                del self.connections[con_name]

        def get_connection(self, con_name):
                return self.connections[con_name]



class Connection(object):
        def __init__(self, user, password, host='localhost', port=5432, database=''):
                self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)

        def __del__(self):
                self.connection.close()

        def execute_query(self, sql, params=None):
                res={'status':False}
                c = self.connection.cursor()
                c.execute(sql, params)
                res['data'] = c.fetchall()
                c.close()
                res['status'] = True
                return res

        def list_databases(self):
                s = "SELECT datname FROM pg_catalog.pg_database WHERE NOT datistemplate"
                return self.execute_query(s)


        
        def list_tables(self):
                s = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
                return self.execute_query(s);



        def create_databases(self, db_name):
                res={'status':False}
                self.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
                c = self.connection.cursor()
                s = "CREATE DATABASE %s" %(db_name)
                c.execute(s, None)
                res={'status':True}
                return res

        def create_table(self, table_name):               
                s = "CREATE TABLE %s" %(table_name)

        


if __name__ == '__main__':
        dbm = DbManager()
        con = dbm.open_connection(con_name='datahub', user='postgres', password='postgres', host='localhost', port=5432, database='datahub')
        print  con.create_databases('test1');
        print  con.list_databases()
        print con.list_tables()