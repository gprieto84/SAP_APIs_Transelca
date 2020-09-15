from flask import request
from app.resources import bp
from utils import sap_util, noti_util
from app.models.notification_model import Notification, noti_col
from datetime import date, timedelta

@bp.route('/')
@bp.route('/index')
def index():
    return "Hello, World!"

@bp.route('/notifications')
def load_notifications():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        start_date = date(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
        end_date = date(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
        delta = timedelta(days=45)
        while start_date <= end_date:
            new_end = start_date + delta
            print (f'{start_date.strftime("%Y%m%d")} -  {new_end.strftime("%Y%m%d")}')
            df = sap_util.sap_get_table('VIQMEL',['QMNUM','IWERK','QMART','AUFNR','EQUNR','QMTXT','STRMN','LTRMN','ERDAT','PRIOK','ERNAM','TPLNR','ARBPL', 'OBJNR'],\
                                                "IWERK EQ 'TR01' AND ERDAT >= '" + start_date.strftime("%Y%m%d") + "' and ERDAT <= '"+new_end.strftime("%Y%m%d")+"'")
            print(f'Shape: {df.shape}')
            df.rename(columns=noti_col,inplace=True)
            noti_util.delsert_table(df,Notification,'n_number')
            start_date += delta + timedelta(days=1)
        return "Notification loaded completed"
    except Exception as e:
        return  f'Error loading notifications: {str(e)}'