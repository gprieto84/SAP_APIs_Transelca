import pandas as pd

def delsert_table(df,orm_obj,db,field):
    df_db = pd.read_sql_table(orm_obj.__tablename__,con=db.engine)
    df_exist = pd.merge(df, df_db[field].drop_duplicates(), how='inner', on=[field])
    orm_obj.query.filter(getattr(orm_obj, field).in_(df_exist[field])).delete(synchronize_session=False)
    db.session.bulk_insert_mappings(orm_obj, df_exist.to_dict(orient="records"))
    db.session.commit()