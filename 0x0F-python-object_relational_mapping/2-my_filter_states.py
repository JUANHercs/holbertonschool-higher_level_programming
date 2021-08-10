#!/usr/bin/python3
"""
Display all values in the states table of database hbtn_0e_0_usa
where name matches
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ the file is not executed when imported"""

    #Connect with database
    db = MySQLdb.connect(host = 'localhost',
                         user = sys.argv[1],
                         passwd = sys.argv[2],
                         database = sys.argv[3])
    #create cursor
    cursor = db.cursor()
    #execute the query
    cursor.execute("SELECT * FROM states"
                   "WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    #Selecting the information
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    #closing cursor and database
    cursor.close()
    db.close()
