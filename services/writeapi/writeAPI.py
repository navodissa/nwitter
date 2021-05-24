import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'notification' )
sys.path.append( mymodule_dir )

# sqlite3, haslib modules are already ported with Python3
import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser
from datetime import datetime
import ConfigReader
import sendEmail as email
from flask_jsonpify import jsonify


class WriteAPI():
    
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


    def writeDataAPI(self, params):
        try:
            self.connect()
            timeNow = str(datetime.now())
            with self.conn.cursor() as cus:
            # Insert a row of data
                cus.execute("INSERT INTO Nweet_data (UserID, Status, MediaID, NweetID, CreatedAT)VALUES ( %s, %s, %s, %s, %s)", (params["user_id"], params["message"], params["media_ids"], 1002, timeNow))
                self.conn.commit()
            # Save (commit) the changes
            email.SendEmail().sendMail(params["user_id"])
            self.conn.close()
            #return "Success"
            return jsonify({'status' : '1'})
        except Exception as e:
            print (e)
            #return "Failed"
            return jsonify({'status' : '0'})


    def closeConn(self):
    #     # We can also close the connection if we are done with it.
    #     # Just be sure any changes have been committed or they will be lost.
        self.conn.close()