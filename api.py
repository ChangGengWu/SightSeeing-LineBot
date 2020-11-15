import mysql.connector


class site_connector:
    site = ""
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456789",
        database='test1'
    )

    def __init__(self,new_site):
        self.site = new_site

    def __str__(self):
        return self.site

    def getEval(self):
        cursor = self.cnx.cursor(buffered=True)
        site = self.site
        status = 0
        site_id = ""
        site_name = ""
        advantages = []
        disadvantages = []
        #確認id是否存在
        sql = "SELECT id,name FROM `site_data` WHERE name LIKE '%" + site + "%'"
        cursor.execute(sql)
        entry = cursor.fetchone()
        #0 資料存在,1 無資料 ,-1 無分析資料, 2 模糊搜尋
        if entry is None:
            #找不到 staus = 1
            status = 1
        else:
            #找到 staus = 0,給site_id
            status = status
            entry = list(entry)
            site_id = entry[0]
            site_name = entry[1]
            if site_name != site:
                status = 2
            #確認該id有無分析資料
        if status == 0 or status == 2:
            sql4 = "SELECT * FROM `segment_data` WHERE site_id = '" + site_id + "'"
            cursor4 = self.cnx.cursor(buffered=True)
            cursor.execute(sql4)
            entry = cursor.fetchone()
            if entry is None:
                status = -1
            else:
                status = status
                #找前三優點
                cursor2 = self.cnx.cursor(buffered=True)
                sql2 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
                    site_id + "' AND evaluation = 'P' ORDER BY degree DESC LIMIT 3"
                cursor2.execute(sql2)

                for each in cursor2:
                    advantages.append(each[0])

                #找前三缺點
                cursor3 = self.cnx.cursor(buffered=True)
                sql3 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
                    site_id + "' AND evaluation = 'N' ORDER BY degree DESC LIMIT 3"
                cursor3.execute(sql3)

                for each in cursor3:
                    disadvantages.append(each[0])

        #優缺點回傳
        return status, site_name, advantages, disadvantages

    
    def getPath(self):
        cursor = self.cnx.cursor(buffered=True)
        site = self.site
        site_id = ""
        site_name = ""
        path = []
        status = 0
        sql = "SELECT id,name FROM `site_data` WHERE name LIKE '%" + site + "%'"
        cursor.execute(sql)
        entry = cursor.fetchone()
        if entry is None:
            #找不到 staus = 1
            status = 1
        else:
            #找到 staus = 0,給site_id
            status = status
            entry = list(entry)
            site_id = entry[0]
            site_name = entry[1]
            if site_name != site:
                status = 2
            #確認該id有無分析資料
        if status == 0 or status == 2:
            sql4 = "SELECT * FROM `path_relationship` WHERE from_id = '" + site_id + "' OR to_id = '" + site_id + "'"
            cursor4 = self.cnx.cursor(buffered=True)
            cursor.execute(sql4)
            entry = cursor.fetchone()
            #無分析資料 回傳-1
            if entry is None:
                status = -1
            else:
                cursor2 = self.cnx.cursor(buffered=True)
                sql2 = "SELECT to_id FROM `path_relationship` WHERE from_id = '" + site_id + "' ORDER BY d_edge DESC LIMIT 1"
                cursor2.execute(sql2)
                second_stop_id = ""
                for each in cursor2:
                    second_stop_id = each[0]
                cursor3 = self.cnx.cursor(buffered=True)
                sql3 = "SELECT to_id FROM `path_relationship` WHERE from_id = '" + \
                    second_stop_id + "' ORDER BY d_edge DESC LIMIT 1"
                cursor3.execute(sql3)
                third_stop_id = ""
                for each in cursor3:
                    third_stop_id = each[0]
                raw_path = []
                raw_path.append(site_id)
                raw_path.append(second_stop_id)
                raw_path.append(third_stop_id)

                for stopId in raw_path:
                    identity = stopId[0:1]
                    cursor4 = self.cnx.cursor(buffered=True)
                    if identity == "S":
                        #to site database
                        sql4 = "SELECT name FROM `site_data` WHERE id = '" + \
                            stopId + "'"
                        cursor4.execute(sql4)
                        for each in cursor4:
                            path.append(each[0])
                    elif identity == "H":
                        #to hotel database
                        sql4 = "SELECT name FROM `hotel_data` WHERE id = '" + \
                            stopId + "'"
                        cursor4.execute(sql4)
                        for each in cursor4:
                            path.append(each[0])
                    elif identity == "R":
                        #to restaurant database
                        sql4 = "SELECT name FROM `resta_data` WHERE id = '" + \
                            stopId + "'"
                        cursor4.execute(sql4)
                        for each in cursor4:
                            path.append(each[0])

        return status, site_name, path


# def getEval(self):
    #     cursor = self.cnx.cursor(buffered=True)
    #     site = self.site
    #     #0 資料存在,1 無資料 ,-1 無分析資料
    #     status = 0
    #     #找id
    #     sql = "SELECT id FROM `site_data` WHERE name LIKE '%" + site + "%'"
    #     cursor.execute(sql)
    #     entry = cursor.fetchone()
    #     site_id = ""
    #     if entry is None:
    #         status = 1
    #     else:
    #         status = status
    #         for res in entry:
    #         site_id = res

    #     #找前三優點
    #     cursor2 = self.cnx.cursor(buffered=True)
    #     sql2 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
    #         site_id + "' AND evaluation = 'P' ORDER BY degree DESC LIMIT 3"
    #     cursor2.execute(sql2)
    #     advantages = []

    #     for each in cursor2:
    #         advantages.append(each[0])

    #     #找前三缺點
    #     cursor3 = self.cnx.cursor(buffered=True)
    #     sql3 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
    #         site_id + "' AND evaluation = 'N' ORDER BY degree DESC LIMIT 3"
    #     cursor3.execute(sql3)

    #     disadvantages = []
    #     for each in cursor3:
    #         disadvantages.append(each[0])

    #     #優缺點回傳
    #     return advantages,disadvantages
