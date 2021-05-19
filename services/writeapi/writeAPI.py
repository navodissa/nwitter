# sqlite3, haslib modules are already ported with Python3
import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
from datetime import datetime
#from flask_jsonpify import jsonify


class WriteAPI():

    def __init__(self) -> None:
        pass
    
    def read_db_config(filename='nwitter/services/config/config.ini', section='mysql'):
        """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
        """
        # create parser and read ini configuration file
        parser = ConfigParser()
        parser.read(filename)

        # get section, default to mysql
        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception('{0} not found in the {1} file'.format(section, filename))

        return db


    def connect(self):
        """ Connect to MySQL database """
        db_config = self.read_db_config()
        conn = None
        try:
            conn = mysql.connector.MySQLConnection(**db_config)
            if conn.is_connected():
                print('Connected to MySQL database')

        except Error as e:
            print(e)

            
    def createDB(self):
        # Create table
        self.conn.execute('''CREATE TABLE pastes
                    ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')''')


    def writeDataAPI(self, params):
        try:
            self.connect()
            # Getting the current time
            timeNow = str(datetime.now())

            # Insert a row of data
            self.conn.execute(
                "INSERT INTO Nweet_data ('UserID', 'Status', 'MediaID', 'NweetID', 'CreatedAT')VALUES ( ?, ?, ?, ?, ?)", (params['user_id'], params['message'], params['media_ids'], 1001, timeNow))

            # Save (commit) the changes
            self.conn.commit()
            self.conn.close()
            return "Success"
            #return jsonify({'status' : '1'})
        except Exception as e:
            print (e)
            return "Failed"
            #return jsonify({'status' : '0'})





    # def writeData(self, params):
    #     try:

            
    #         # Getting the current time
    #         timeNow = str(datetime.now())

    #         # Insert a row of data
    #         self.conn.execute(
    #             "INSERT INTO pastes ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')VALUES ( ?, 0, ?, ?)", (new_Url, timeNow, url))

    #         # Save (commit) the changes
    #         self.conn.commit()
    #         self.conn.close()
    #         return new_Url
    #     except Exception as e:
    #         print (e)
    #         return "Your request got failed"


    def closeConn(self):
    #     # We can also close the connection if we are done with it.
    #     # Just be sure any changes have been committed or they will be lost.
        self.conn.close()