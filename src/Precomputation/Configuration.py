hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'imsoumya'
port_id = 5432

# ! databasetype://username:password@hostname:port/database
db_connection_string = 'postgresql://' + username + ':' + pwd + '@' + hostname + ':' + str(port_id) + '/' + database
