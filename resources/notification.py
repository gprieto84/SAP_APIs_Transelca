from flask import Blueprint, request
# from database.notification_model import Notification, noti_col, Type, type_col, Text, text_col, Activity,acti_col, Activity_H, acth_col, \
#     Noti_System_Status, sys_stat_col
from utils import sap_util, noti_util
# import pandas as pd
from datetime import date, timedelta

notifications = Blueprint('notifications', __name__)

@notifications.route('/notifications', methods=['GET'])
def load_notifications():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        start_date = date(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
        end_date = date(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
        delta = timedelta(days=45)
        df_notification = sap_util.sap_get_table('VIQMEL',['QMNUM','IWERK','QMART','AUFNR','EQUNR','QMTXT','STRMN','LTRMN','ERDAT','PRIOK','ERNAM','TPLNR','ARBPL', 'OBJNR'],\
                                                 "IWERK EQ 'TR01' AND ERDAT >= '" + start_date.strftime("%Y%m%d") + "' and ERDAT <= '"+new_end.strftime("%Y%m%d")+"'")
                #     df_notification.rename(columns=noti_col,inplace=True)
        #     noti_util.delsert_table(df_notification,Notification,'n_number')
        # while start_date <= end_date:
        #     new_end = start_date + delta
        #     print (f'{start_date.strftime("%Y%m%d")} -  {new_end.strftime("%Y%m%d")}')
        #     df_notification = sap_util.sap_get_table('VIQMEL',['QMNUM','IWERK','QMART','AUFNR','EQUNR','QMTXT','STRMN','LTRMN','ERDAT','PRIOK','ERNAM','TPLNR','ARBPL', 'OBJNR'],\
        #                                         "IWERK EQ 'TR01' AND ERDAT >= '" + start_date.strftime("%Y%m%d") + "' and ERDAT <= '"+new_end.strftime("%Y%m%d")+"'")
        #     print(f'Shape: {df_notification.shape}')
        #     df_notification.rename(columns=noti_col,inplace=True)
        #     noti_util.delsert_table(df_notification,Notification,'n_number')
        #     start_date += delta + timedelta(days=1)
        return f'Notification Process completed '
    except Exception as e:
        return  f'Error loading notifications: {str(e)}'

# @notifications.route('/notifications_type', methods=['GET'])
# def load_types():
#     try:
#         df_type = sap_util.sap_get_table('TQ80', ['QMART','STSMA'], "MANDT EQ '020'")
#         df_type.rename(columns=type_col,inplace=True)
#         noti_util.delsert_table(df_type,Type,'type_n')
#         return f'Notification Type completed for {df_type.shape}'
#     except Exception as e:
#         return  f'Error loading type: {str(e)}'

# @notifications.route('/notifications_text', methods=['GET'])
# def load_text():
#     try:
#         start_date = request.args.get('start_date')
#         end_date = request.args.get('end_date')
#         start_date = date(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
#         end_date = date(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
#         delta = timedelta(days=30)
#         #noti_util.del_index(Text,db)
#         while start_date <= end_date:
#             new_end = start_date + delta
#             print (f'{start_date.strftime("%Y%m%d")} -  {new_end.strftime("%Y%m%d")}')
#             df_text = sap_util.sap_get_table('QMFE', ['QMNUM','FETXT'],
#                         "FETXT NE '' AND ERDAT >= '" + start_date.strftime("%Y%m%d") + "' and ERDAT <= '"+new_end.strftime("%Y%m%d")+"'")
#             df_text.rename(columns=text_col,inplace=True)
#             print(f'Shape: {df_text.shape}')
#             noti_util.insert(df_text,Text)
#             start_date += delta + timedelta(days=1)
#         return f'Notification Text completed for {df_text.shape}'
#     except Exception as e:
#         return  f'Error loading Text: {str(e)}'

# @notifications.route('/notifications_activities', methods=['GET'])
# def load_activities():
#     try:
#         start_date = request.args.get('start_date')
#         end_date = request.args.get('end_date')
#         start_date = date(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
#         end_date = date(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
#         delta = timedelta(days=30)
#         #noti_util.del_index(Activity, db)
#         while start_date <= end_date:
#             new_end = start_date + delta
#             print (f'{start_date.strftime("%Y%m%d")} -  {new_end.strftime("%Y%m%d")}')
#             df_activity = sap_util.sap_get_table('QMMA',['MANDT','QMNUM','MATXT','MNGRP','MNCOD','MNKAT'],
#                                             "MANDT EQ '020' AND ERDAT >= '" + start_date.strftime("%Y%m%d") + "' and ERDAT <= '"+new_end.strftime("%Y%m%d")+"'")
#             df_activity.rename(columns=noti_col,inplace=True)
#             print(f'Shape: {df_activity.shape}')
#             #noti_util.insert(df_activity,Activity,db)
#             start_date += delta + timedelta(days=1)
#         return f'Notification Type completed for {df_activity.shape}'
#     except Exception as e:
#         return  f'Error loading type: {str(e)}'

# @notifications.route('/notifications_activities_h', methods=['GET'])
# def load_activities_h():
#     try:
#         df_type = sap_util.sap_get_table('TQ80', ['QMART','STSMA'], "MANDT EQ '020'")
#         df_type.rename(columns=type_col,inplace=True)
#         #noti_util.delsert_table(df_type,Type,db,'type_n')
#         return f'Notification Type completed for {df_type.shape}'
#     except Exception as e:
#         return  f'Error loading type: {str(e)}'
##SAP_process_table('QPCT', ['MANDT','CODEGRUPPE','CODE','KURZTEXT','KATALOGART'], "MANDT EQ '020' AND INAKTIV EQ ''", notification_activity_header_columns, Notification_Activity_Header)
#SAP_process_table('TQ15T', ['MANDT','KATALOGART','KATALOGTXT'], "MANDT EQ '020' AND SPRACHE EQ 'S'", notification_catalog_columns, Notification_Catalog)

#@notifications.route('/notifications_catalog', methods=['GET'])
#@notifications.route('/notifications_catalog', methods=['GET'])
#def load_causes():
#    open_obj=Noti_System_Status.query.filter(Noti_System_Status.status_id == 'I0072').\
#        filter(Noti_System_Status.disabled == '').with_entities(Noti_System_Status.obj_nr)
#    open_noti = Notification.query.filter(~Notification.obj_nr.in_(open_obj))

