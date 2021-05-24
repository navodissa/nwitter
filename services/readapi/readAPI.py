# sqlite3, haslib modules are already ported with Python3
import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
from datetime import datetime
import ConfigReader
from flask_jsonpify import jsonify


class ReadAPI():
    
    def connect(self):
        """ Connect to MySQL database """
        db_config = ConfigReader.read_db_config()
        self.conn = None
        try:
            self.conn = mysql.connector.MySQLConnection(**db_config)
            if self.conn.is_connected():
                print('Connected to MySQL database')

        except Error as e:
            print(e)

            
    def createDB(self):
        # Create table
        self.conn.execute('''CREATE TABLE pastes
                    ('shortlink', 'expiration_length_in_minutes', 'created_at', 'paste_path')''')


    def readDataAPI(self, user):
        try:
            self.connect()
            cus = self.conn.cursor()
            # Insert a row of data
            cus.execute("SELECT * FROM Nweet_data WHERE UserID = (%s)" % user)
                #self.conn.commit()
            # Save (commit) the changes
            results = cus.fetchall()
            param = ['UserID', 'Status', 'MediaID', 'NweetID', 'CreatedAT']
            returnJson = {}
            fullJson = []
            for row in results:
                for col in range(0,len(row)):
                    returnJson[param[col]] = row[col]
                fullJson.append(returnJson)
                returnJson = {}
            self.conn.close()
            return jsonify(fullJson)
            #return jsonify({'status' : '1'})
        except Exception as e:
            print (e)
            #return "Failed"
            return jsonify({'status' : '0'})


    def closeConn(self):
    #     # We can also close the connection if we are done with it.
    #     # Just be sure any changes have been committed or they will be lost.
        self.conn.close()