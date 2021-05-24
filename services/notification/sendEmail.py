import smtplib, ssl
import mysql.connector
from mysql.connector import Error
import ConfigReader
import certifi

class SendEmail():

    port = 465  # For SSL
    password = "nQP8tG4xC7H4fq"

    sender_email = "navoda.dev.test@gmail.com"  # Enter your address

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


    def sendMail(self, userid):
        try:
            receiver_email = "navomails@gmail.com"  # Enter receiver address
            message = """\
            Subject: Hi there

            This message is sent from Python.
            """

            # Create a secure SSL context
            context = ssl.create_default_context(cafile=certifi.where())

            with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
                server.login("navoda.dev.test@gmail.com", self.password)
                
                self.connect()
                cus = self.conn.cursor()
                # Insert a row of data
                cus.execute("select email from userDetails where userid IN (SELECT followers FROM follower WHERE userid = (%s))" % userid)
                    #self.conn.commit()
                # Save (commit) the changes
                results = cus.fetchall()
                for row in results:
                    print(row)
                    server.sendmail(self.sender_email, row, message)
                self.conn.close()
        except Exception as e:
            print (e)
