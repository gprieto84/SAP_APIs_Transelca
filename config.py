import os
import urllib
from pyrfc import Connection
from configparser import ConfigParser

class Config(object):
    # Build the MSSQL ULR for SqlAlchemy
    params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=Cobartram016\TRABDSP10;DATABASE=BDVIAJE2;UID=tra-sap;PWD=12345.TS;')
    mssql_url = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_DATABASE_URI = mssql_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Getting SAP config parameters
    config = ConfigParser()
    config.read(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'sap_config', 'sapnwrfc.cfg')))
    params_connection = config._sections['connection']
    # Stablishing the SAP connection
    sap_conn = Connection(**params_connection)