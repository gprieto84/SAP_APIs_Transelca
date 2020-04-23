from config import Config
import pandas as pd

def clean_list(sap_list, split_value):
    return_list = []
    for value in sap_list:
        clean_value = [i.strip(' ') for i in value['WA'].split(split_value)]
        return_list.append(clean_value)
    return return_list

def sap_get_table(table, fields, options, rows=1000000, delimeter='ɷ'):
    result = Config.sap_conn.call('RFC_READ_TABLE', \
        QUERY_TABLE = table, \
        FIELDS = fields, \
        OPTIONS = [{ 'TEXT': options}], \
        ROWCOUNT = rows, DELIMITER=delimeter)    
    cleaned_list = clean_list(result["DATA"], delimeter)
    return pd.DataFrame(cleaned_list, columns=fields)