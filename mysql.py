import pymysql
from config.config import auConfigs


def mysql(sql):
    config = auConfigs()
    db = pymysql.connect(host=config.sql_address, port=3306, user=config.sql_username,
                         password=config.sql_password, db=config.sql_dbname, charset='utf8')
    try:
        db.connect()
    except:
        return 0
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
    except:
        db.rollback()
        db.close()
        return 0

    db.close()
    if not results:
        return 1

    return results








if __name__ == '__main__':
    sql = """
    CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )
    """
    print(mysql(sql))