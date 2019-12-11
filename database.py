from configparser import ConfigParser

from mysql.connector import MySQLConnection,Error

class Database:
    
    def __init__(self,table_name=None,fields=None,filename='config.ini',section='mysql'):
        """
        Initialize the connection with the database and make the required table.
        :param table_name: name of the table to be inserted
        :param fields: a dictionary of field_name and their_type to be inserted in the table table_name
        :optional param filename: name of the configuration file
        :optional param section: section of database configuration
        """
        self.table_name = table_name 
        db_config = self.read_db_config(filename,section)
         
        try :
            self.conn = MySQLConnection(**db_config)
        except Error as error:
            print(error)
            return

        self.cursor = self.conn.cursor()
        
        if table_name is not None and fields is not None:
            self.cursor.execute(f"show tables like '{self.table_name}'") 
            output = self.cursor.fetchone()
            #if no such table exits create one
            if output is None:
                fields_list = [f'{x} {fields[x]}' for x in fields.keys()]            
                self.cursor.execute(f"CREATE TABLE {self.table_name}({','.join(fields_list)})")
                print('Table successfully created')
                self.conn.commit()
            

    def insert(self,data):
        """
        This function is used to insert data into the table.
        :param data: dictonary contain the pair wise data {field_name:value}
        """
       
        values = [data[x] for x in data.keys()]
        s = ('%s,'*len(data))[:-1]
        insert_statement = f"INSERT INTO {self.table_name} values({s})"
        self.cursor.execute(insert_statement,values) 
        self.conn.commit()  

    def read_db_config(self,filename,section):
        """
        Read database configuration from the file and return dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
        """

        parser = ConfigParser()
        parser.read(filename)

        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception(f'{section} not found in the {filename} file')

        return db

    def __del__(self):
        self.cursor.close()
        self.conn.close()
