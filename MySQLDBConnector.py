import mysql.connector
from mysql.connector import Error

import pandas as pd

from Table import Table

class DBConnector():
    def __init__(self, address, login, password, db_name):
        self.address = address
        self.login = login
        self.db_name = db_name

        self.connection = None
        try:

            self.connection = mysql.connector.connect(
                host=address,
                user=login,
                passwd=password,
                database=db_name
            )

            self.cursor = self.connection.cursor()

        except Error as e:
            print(f"The error '{e}' occurred")
    
    def create_table(self, table_name, columns):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                        (id INT AUTO_INCREMENT,
                        {' TEXT ,'.join(columns)} TEXT,
                        PRIMARY KEY (id))''')

        self.connection.commit()

    def read(self, table_name, volume=0):
        if volume == 0:
            res_df = pd.read_sql_query(f"select * from {table_name};", self.connection)
        else:
            res_df = pd.read_sql_query(f"select * from {table_name} order by id desc limit {volume};", self.connection)

        return Table(table_name, res_df)

    def write_from_df(self, table, method = 'replace'):
        """
        :param df:
        :param table_name:
        :param method: 'replace'/'append' or 'replace last

        :return:
        """
        df = table.get_data()
        df['id'] = pd.Series([None for i in range(len(df))])

        if method == 'replace last':
            # Если этот метод будет необходим, стоит попробовать переписать на запрос UPDATE
            data = self.read(table.get_name()).get_data()
            len_df = len(df)

            data = data.iloc[:-len_df, :]
            data = pd.concat([data, df], axis=0)
            data.to_sql(table.get_name(), self.connection, index=False, if_exists='replace')
        else:
            df.to_sql(table.get_name(), self.connection, index=False, if_exists = method)        
    
    def _add_user(self, name):
        data = self.read('users').get_data()
        if name not in data['login']:
            series = pd.Series([None, name])
            self.write_from_df(Table('users', series), 'append')
        else:
            print('Warning: User already exists!')

    def _create_settings_table(self, table_name, columns, dep_table, foreign_key='id'):
        query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT, 
            {' TEXT ,'.join(columns)} TEXT,
            user_id INTEGER NOT NULL, 
            FOREIGN KEY fk_user_id (user_id) REFERENCES {dep_table}({foreign_key}), 
            PRIMARY KEY (id)
            ) ENGINE = InnoDB
            """
        print(query)
        self.cursor.execute(query)

        self.connection.commit()

    def _on_startup(self):
        self.create_table

        settings_cols = ['algo', 'volume', 'alphas', 'thr']

        db._create_settings_table(self, 'BaseSettings', settings_cols, 'users', foreign_key='id')


def _on_system_startup(address, login, password, db_name):
    connection = mysql.connector.connect(
            host=address,
            user=login,
            passwd=password,
            
        )
    
    query = f"CREATE DATABASE IF NOT EXISTS {db_name}"

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred on creating db")

    db = DBConnector(address, login, password, db_name)

    db.create_table('users', ['name'])

    settings_cols = ['algo', 'volume', 'alphas', 'thr']
    db._create_settings_table('BaseSettings', settings_cols, 'users', foreign_key='id')

    dictionary_cols = ['lexem', 'x_1', 'x_2', 'x_3']
    db.create_table('BaseDictionary', dictionary_cols)


if __name__=='__main__':
    password = input()
    _on_system_startup('localhost', "root", password, 'BaseDB')
    db = DBConnector('localhost', "root", password, 'BaseDB')


    '''
    if FIRST_TEST:
        connection = create_connection("localhost", "root", "")

        create_database_query = "CREATE DATABASE sm_app"
        create_database(connection, create_database_query)
    
    connection = create_connection("localhost", "root", "", "Settings")

    create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT, 
        name TEXT NOT NULL, 
        age INT, 
        gender TEXT, 
        nationality TEXT, 
        PRIMARY KEY (id)
        ) ENGINE = InnoDB
        """
    execute_query(connection, create_users_table)

    create_posts_table = """
        CREATE TABLE IF NOT EXISTS posts (
        id INT AUTO_INCREMENT, 
        title TEXT NOT NULL, 
        description TEXT NOT NULL, 
        user_id INTEGER NOT NULL, 
        FOREIGN KEY fk_user_id (user_id) REFERENCES users(id), 
        PRIMARY KEY (id)
        ) ENGINE = InnoDB
        """
    execute_query(connection, create_posts_table)

    ###

    sql = "INSERT INTO likes ( user_id, post_id ) VALUES ( %s, %s )"
    val = [(4, 5), (3, 4)]

    cursor = connection.cursor()
    cursor.executemany(sql, val)
    connection.commit()

    select_users = "SELECT * FROM users"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)


    ###

    update_post_description = """
    UPDATE
    posts
    SET
    description = "The weather has become pleasant now"
    WHERE
    id = 2
    """

    execute_query(connection,  update_post_description)

    ###
    delete_comment = "DELETE FROM comments WHERE id = 5"
    execute_query(connection, delete_comment)
    ###
    def create_table(self, table_name, columns):
    self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                    ({','.join(columns)})""")

    '''