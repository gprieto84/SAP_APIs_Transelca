from flask import request
from app.resources import bp
from utils import sap_util, noti_util
from app.models.notification_model import Notification, noti_col

@bp.route('/')
@bp.route('/index')
def index():
    return "Hello, World!"

@bp.route('/notifications')
def load_notifications():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        df = sap_util.sap_get_table('VIQMEL',['QMNUM','IWERK','QMART','AUFNR','EQUNR','QMTXT','STRMN','LTRMN','ERDAT','PRIOK','ERNAM','TPLNR','ARBPL', 'OBJNR'],\
                                                 "IWERK EQ 'TR01' AND ERDAT >= '" + start_date + "' and ERDAT <= '"+end_date+"'")
        df.rename(columns=noti_col,inplace=True)
        noti_util.delsert_table(df,Notification,'n_number')
        return "The size of notifications is {}".format(str(df.shape[0]))
    except Exception as e:
        return  f'Error loading notifications: {str(e)}'