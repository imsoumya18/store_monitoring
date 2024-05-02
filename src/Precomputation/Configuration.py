"""Configuration file for the application"""

hostname = 'localhost'
database = 'stpre_monitoring.db'
username = 'imsoumya18'
pwd = 'testpswd'
port_id = 5432

# ! databasetype://username:password@hostname:port/database
db_connection_string = 'postgresql://' + username + ':' + pwd + '@' + hostname + ':' + str(port_id) + '/' + database
