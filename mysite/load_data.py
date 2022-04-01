import pandas as pd
import sqlite3

tableName = 'programs'

def getConn():
    """ Method to initiate a sqlite db connection """
    conn = sqlite3.connect('/home/gshkr/database.db')
    cur = conn.cursor()
    return conn, cur


def loadData():
    """ Method to load a large data file in chunks
    for ideal memory processing. This method only reads a portion
    of the entire file by a given chunk size """
    print("Loading data from file in chunks")
    filename = '/home/gshkr/data.csv'
    chunksize = 10
    #This is where we are reading the file per chunk size at a time
    #and this way the condition where a file of size > memory can be handled
    #effeciently
    for chunk in pd.read_csv(filename, chunksize=chunksize, iterator=True):
        insertToDB(chunk)

def insertToDB(df):
    """ Method to insert the data into sqlite table """
    try:
        sqliteConnection, cursor = getConn()
        print("Inserting dataframe chunk into '{}' table".format(tableName))

        #Here we are using pandas builtin function to_sql to insert df data
        #directly to sqlite tables.
        df.to_sql(tableName, sqliteConnection, if_exists='append', index=False)

        print("Records inserted successfully into '{}' table".format(tableName))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite '{}' table".format(tableName), error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def deleteRecords():
    """ Method to delete all the records from programs table """
    conn, cur = getConn()
    cur.execute('delete from "{0}"'.format(tableName))
    conn.commit()
    conn.close()

def readRecords():
    """ Method to retrieve all data from programs sqlite table """
    conn, cur = getConn()
    df = pd.read_sql_query("SELECT * FROM '{0}'".format(tableName), conn)
    print(df)
    conn.close()

if __name__ == '__main__':
    deleteRecords()
    loadData()
    readRecords()