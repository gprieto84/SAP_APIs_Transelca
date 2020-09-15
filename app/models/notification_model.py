from app import db

noti_col = {'QMNUM':'n_number', 'IWERK':'plant','QMART':'type_n','AUFNR':'order','EQUNR':'equipment','QMTXT':'description', \
    'STRMN':'required_start_date','LTRMN':'required_end_date','ERDAT':'creation_date','PRIOK':'priority','ERNAM':'created_by', \
    'TPLNR':'func_location', 'ARBPL':'work_center', 'OBJNR':'obj_nr' }
class Notification(db.Model): #VIQMEL
    __tablename__ = 'SAP_notifications'

    n_number = db.Column(db.String(20), primary_key=True) #QMNUM
    plant =  db.Column(db.String) #IWERK
    type_n = db.Column(db.String, nullable= False) #QMART
    order = db.Column(db.String) #AUFNR
    equipment = db.Column(db.String, nullable= False) #EQUNR
    description = db.Column(db.String) #QMTXT
    required_start_date = db.Column(db.DateTime) #STRMN
    required_end_date = db.Column(db.DateTime) #LTRMN
    creation_date = db.Column(db.DateTime, nullable=False) #ERDAT
    priority = db.Column(db.String) #PRIOK
    created_by = db.Column(db.String, nullable = False) #ERNAM
    func_location = db.Column(db.String) #TPLNR
    work_center = db.Column(db.Integer) #ARBPL
    obj_nr = db.Column(db.String,nullable = False) #OBJNR

type_col = {'QMART':'type_n', 'STSMA':'status_schema'}
class Type(db.Model): #TQ80
    __tablename__ = 'SAP_notification_type'
    
    type_n =  db.Column(db.String(20), primary_key=True) #QMART
    status_schema =  db.Column(db.String(20)) #STSMA

text_col = {'QMNUM':'n_number', 'FETXT':'short_text'}
class Text(db.Model): #QMFE
    __tablename__ = 'SAP_notification_text'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #ID
    n_number = db.Column(db.String(20), nullable= False) #QMNUM
    short_text = db.Column(db.String) #FETXT

acti_col = {'QMNUM':'n_number', 'MATXT':'activity_text','MNGRP':'group','MNCOD':'code', 'MNKAT':'catalog'}
class Activity(db.Model): #QMMA
    __tablename__ = 'SAP_notification_activities'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #ID
    n_number = db.Column(db.String(20), nullable= False) #QMNUM
    group = db.Column(db.String(30), nullable= False) #MNGRP
    code = db.Column(db.String(20)) #MNCOD
    activity_text = db.Column(db.String) #MATXT
    catalog = db.Column(db.String) #MNKAT

acth_col = {'CODEGRUPPE':'group', 'CODE':'code', 'KURZTEXT':'description', 'KATALOGART':'catalog'}
class Activity_H(db.Model): #QPCT
    __tablename__ = 'SAP_notification_activities_header'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #ID
    group = db.Column(db.String(30), nullable= False) #CODEGRUPPE
    code = db.Column(db.String(20)) #CODE
    description = db.Column(db.String) #KURZTEXT
    catalog = db.Column(db.String) #KATALOGART

notification_catalog_columns = {'KATALOGART':'catalog', 'KATALOGTXT':'description'}
class Notification_Catalog(db.Model): #TQ15T
    __tablename__ = 'SAP_notification_catalog'
    
    catalog = db.Column(db.String(10),primary_key=True ) #KATALOGART
    description = db.Column(db.String(100), nullable= False) #KATALOGTXT


notification_cause_columns = {'QMNUM':'n_number', 'URTXT':'cause'}
class Notification_Cause(db.Model): #QMUR
    __tablename__ = 'SAP_notification_causes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #ID
    n_number = db.Column(db.String(20), nullable= False) #QMNUM
    cause = db.Column(db.String) #URTXT

equipment_columns = {'EQUNR':'equipment', 'EQART':'type_e','HERST':'manufacturer', 'TYPBZ':'model'}
class Equipment(db.Model): #EQUI
    __tablename__ = 'SAP_equipments'

    equipment = db.Column(db.String(20), primary_key=True) #EQUNR
    type_e = db.Column(db.String, nullable= False) #EQART
    manufacturer = db.Column(db.String) #HERST
    model = db.Column(db.String) #TYPBZ

equipment_text_columns = {'EQUNR':'equipment', 'EQKTX':'description'}
class Equipment_Text(db.Model):#EQKT
    __tablename__ = 'SAP_equipment_text'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    equipment = db.Column(db.String, nullable= False) #EQUNR
    description = db.Column(db.String, nullable= False) #EQKTX

work_center_columns = {'OBJID':'work_center', 'ARBPL':'description', 'KTEXT':'information'}
class Work_Center(db.Model): #CRHD
    __tablename__ = 'SAP_work_center'

    work_center = db.Column(db.String(20), primary_key=True) #OBJID
    description = db.Column(db.String) #ARBPL
    information = db.Column(db.String) #KTEXT

func_location_columns =  {'TPLNR':'func_location', 'STRNO':'description', 'ACTVS':'active','TPLKZ':'indicator','ERDAT':'creation_date',\
    'VERSN':'version', 'ERNAM':'created_by' }
class Functional_Location(db.Model): #IFLOS
    __tablename__ = 'SAP_functional_location'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    func_location = db.Column(db.String(50), primary_key=True) #TPLNR
    description = db.Column(db.String) #STRNO
    active = db.Column(db.String(5)) #ACTVS
    indicator = db.Column(db.String(20)) #TPLKZ
    creation_date = db.Column(db.String(20)) #ERDAT
    version = db.Column(db.String(5)) #VERSN
    created_by = db.Column(db.String(20)) #ERNAM
    

system_columns = {'ISTAT':'status_id', 'TXT04':'code','TXT30':'description'}
class System_Status(db.Model):#TJ02
    __tablename__ = 'SAP_system_status'

    status_id = db.Column(db.String(20), primary_key=True) #ISTAT
    code = db.Column(db.String(20),nullable = False) #TXT04
    description = db.Column(db.String,nullable = False) #TXT30

user_columns = {'STSMA':'status_schema','ESTAT':'status_id','TXT04':'code','TXT30':'description'}
class User_Status(db.Model):#TJ30T
    __tablename__ = 'SAP_user_status'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    status_schema = db.Column(db.String(20)) #STSMA
    status_id = db.Column(db.String,nullable = False) #ESTAT
    code = db.Column(db.String(20),nullable = False) #TXT04
    description = db.Column(db.String,nullable = False) #TXT30

status_col = {'OBJNR':'obj_nr', 'STAT':'status_id','INACT':'disabled'}
sys_stat_col = {'OBJNR':'obj_nr', 'STAT':'status_id','INACT':'disabled'}
class Noti_System_Status(db.Model):
    __tablename__ = 'SAP_notification_system_status'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    obj_nr = db.Column(db.String,nullable = False) #OBJNR
    status_id = db.Column(db.String,nullable = False) #STAT
    disabled = db.Column(db.String(3)) #INACT

user_status_columns = {'OBJNR':'obj_nr', 'STSMA':'status_schema','STAT':'status_id','INACT':'disabled'}
class Notification_User_Status(db.Model):
    __tablename__ = 'SAP_notification_user_status'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    obj_nr = db.Column(db.String,nullable = False) #OBJNR
    status_schema = db.Column(db.String(20)) #STSMA
    status_id = db.Column(db.String,nullable = False) #STAT
    disabled = db.Column(db.String(3)) #INACT

log_columns = {'OBJNR':'obj_nr', 'STAT':'status_id','USNAM':'changed_by','UDATE':'change_date','UTIME':'changed_time','INACT':'inactive','CHIND':'change_indicator'}
class Notification_Log_System(db.Model):
    __tablename__ = 'SAP_status_log_system'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obj_nr = db.Column(db.String,nullable = False) #OBJNR
    status_id = db.Column(db.String,nullable = False) #STAT
    changed_by = db.Column(db.String,nullable = False) #USNAM
    change_date = db.Column(db.String,nullable = False) #UDATE
    changed_time = db.Column(db.String,nullable = False) #UTIME
    inactive = db.Column(db.String) #INACT
    change_indicator = db.Column(db.String) #CHIND

class Notification_Log_User(db.Model):
    __tablename__ = 'SAP_status_log_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    obj_nr = db.Column(db.String,nullable = False) #OBJNR
    status_id = db.Column(db.String,nullable = False) #STAT
    changed_by = db.Column(db.String,nullable = False) #USNAM
    change_date = db.Column(db.String,nullable = False) #UDATE
    changed_time = db.Column(db.String,nullable = False) #UTIME
    inactive = db.Column(db.String) #INACT
    change_indicator = db.Column(db.String) #CHIND
    status_schema = db.Column(db.String(20)) #STSMA