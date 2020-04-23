from flask import Blueprint, request
from database.notification_model import Notification, noti_col, Type, type_cols
from utils import sap_util, noti_util
from app import db
import pandas as pd
from datetime import date
import time

notifications = Blueprint('notifications', __name__)

@notifications.route('/notifications', methods=['POST'])
def load_notifications():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        df_notification = sap_util.sap_get_table('VIQMEL',['QMNUM','IWERK','QMART','AUFNR','EQUNR','QMTXT','STRMN','LTRMN','ERDAT','PRIOK','ERNAM','TPLNR','ARBPL', 'OBJNR'],\
                                                "IWERK EQ 'TR01' AND ERDAT >= '" + start_date + "' and ERDAT <= '"+end_date+"'")
        df_notification.rename(columns=noti_col,inplace=True)
        noti_util.delsert_table(df_notification,Notification,db,'n_number')
        return f'Notification Process completed for {df_notification.shape}'
    except Exception as e:
        return  f'Error loading notifications: {str(e)}'

@notifications.route('/notifications_type', methods=['POST'])
def load_types():
    try:
        df_type = sap_util.sap_get_table('TQ80', ['QMART','STSMA'], "MANDT EQ '020'")
        df_type.rename(columns=type_cols,inplace=True)
        noti_util.delsert_table(df_type,Type,db,'type_n')
        return f'Notification Type completed for {df_type.shape}'
    except Exception as e:
        return  f'Error loading type: {str(e)}'