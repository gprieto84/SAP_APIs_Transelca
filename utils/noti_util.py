import pandas as pd
from app import db
from datetime import date, timedelta


def test(start_date, end_date):
    start_date = date(int(start_date[0:4]), int(start_date[4:6]), int(start_date[6:8]))
    end_date = date(int(end_date[0:4]), int(end_date[4:6]), int(end_date[6:8]))
    delta = timedelta(days=60)
    while start_date <= end_date:
        new_end = start_date + delta
        print (f'{start_date.strftime("%Y%m%d")} -  {new_end.strftime("%Y%m%d")}')
        start_date += delta + timedelta(days=1)


def delsert_table(df,orm_obj,field):
    df_db = pd.read_sql_table(orm_obj.__tablename__,con=db.engine)
    df_exist = pd.merge(df, df_db[field].drop_duplicates(), how='inner', on=[field])
    orm_obj.query.filter(getattr(orm_obj, field).in_(df_exist[field])).delete(synchronize_session=False)
    db.session.bulk_insert_mappings(orm_obj, df.to_dict(orient="records"))
    db.session.commit()

def del_index(orm_obj):
    orm_obj.query.delete(synchronize_session=False)
    db.session.commit()
    with db.engine.connect() as connection:
        drop_spow = db.DDL(f"DBCC CHECKIDENT ('{orm_obj.__tablename__}', RESEED, 0)")
        connection.execute(drop_spow)
    db.session.commit()

def insert(df, orm_obj):
    db.session.bulk_insert_mappings(orm_obj, df.to_dict(orient="records"))
    db.session.commit()
    
    


