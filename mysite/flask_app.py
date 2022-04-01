#----------------------------------------------------------------------------#
# For adding additional feature. It is simple to add more routes i.e more
# call back methods of which each one is associated with either a GET or POST
# request to share data to the Web UI.
#----------------------------------------------------------------------------#



#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import pandas as pd
import sqlite3

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
tableName = 'programs'

def getConn():
    """ Method to initiate a sqlite db connection """
    conn = sqlite3.connect('/home/gshkr/mysite/database.db')
    cur = conn.cursor()
    return conn, cur

@app.route("/")
def show_tables(value=None):
    conn, cur = getConn()
    df = pd.read_sql_query("SELECT * FROM '{0}'".format(tableName), conn)
    conn.close()
    cities = df['Viewer Hometown'].unique()
    if value == 1:
        return df
    return render_template('views.html',tables=[df.to_html(classes='females')], titles = ['Popular Shows'], cities=cities)

@app.route("/getSelectData/<string:city>", methods=['GET'])
def getSelectData(city):
    conn, cur = getConn()
    colName = 'Viewer Hometown'
    df = pd.read_sql_query("SELECT * FROM '{0}' where '{1}' = '{2}'".format(tableName, colName, city), conn)
    conn.close()
    df = show_tables(1)
    df = df.loc[(df[colName] == city)]
    return render_template('views_selected.html',tables=[df.to_html(classes='females')], titles = ['Selected City Data'])

@app.route("/getDataByViewerCount/<int:value>", methods=['GET'])
def getDataByViewerCount(count):
    return []


@app.route("/getDataByViewerCount/<string:value>", methods=['GET'])
def getDataByProgramGenre(genre):
    return []

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

