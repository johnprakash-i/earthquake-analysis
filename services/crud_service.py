import pandas as pd
from config.db_config import get_connection


def execute_query(sql: str, fetch=True):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)

    if fetch:
        result = cursor.fetchall()
        df = pd.DataFrame(result)
        cursor.close()
        conn.close()
        return df
    else:
        conn.commit()
        cursor.close()
        conn.close()
        return None
