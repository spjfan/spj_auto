import pymysql

class MysqlUtil:
    db = pymysql.connect(host='localhost',
                    port=3307,
                    user='root',
                    password='123456',
                    database='spj_data')

    cursor = db.cursor()


    def get_requests_form_database(self,table_name:str,method:str,url:str,count:int) ->list:
        sql = "select %s,%s from %s limit %d" %(method,url,table_name,count)
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            self.db.rollback()
            print("查询失败")
            print(e)
        finally:
            self.cursor.close()
            self.db.close()