from api import site_connector
import mysql.connector
import json
# second_stop_id = "S0113"
# a = second_stop_id[0:1]
# print(a)
# sql3 = "SELECT * FROM `path_relationship` WHERE from_id = '" + \
#     second_stop_id + "' ORDER BY d_edge DESC LIMIT 1"
# print(sql3)
# while True:
#     option = eval(input("1.優缺點   2.路徑  3.收藏 4.退出：\n"))
#     if(option == 1):
#         print("進入優缺點 site=台北101")
#     #     input1 = "台北101"
#     #     getInfo = site_connector(input1)
#     #     p, n = getInfo.getEval()
#     #     print(p)
#     #     print(n)
#     elif(option == 2):
#         print("進入路徑 site=台北101")
#         input1 = "台北101"
#         getInfo = site_connector(input1)
#         p= getInfo.getPath()
#         print(p)
#     elif(option == 3):
#         print("進入收藏 site=台北101")
#     elif(option == 4):
#         print("結束")
#         break
#     else:
#         break

#優缺點
# input1 = "台北101"
# getInfo = site_connector(input1)
# a,b = getInfo.getEval()
# print(a)
# print(b)
#路徑

#收藏

# {"events": [{"type": "message", "replyToken": "941dedd2fd774a0c88cadad3e835ea9d", "source": {"userId": "Udb39262bc44f3276e08be729bac4de38", "type": "user"}, "timestamp": 1597391341045, "mode": "active", "message": {"type": "text", "id": "12497771467378", "text": "優缺點查詢"}}], "destination": "U4df685a8291b0a4391f65840609d2fe2"} V8jED70esyMgYNRGv9nO2/teuleTHIiQ5oHuA5Bm+y8 =


# def getRound(uID):
#     cnx = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="123456789",
#         database='linebot'
#     )
#     cursor = cnx.cursor(buffered=True)
#     #SQL
#     sql = "SELECT round FROM `user_log` WHERE user_id = '" + uID + "'"
#     cursor.execute(sql)
#     entry = cursor.fetchone()
#     rnd = ""
#     if entry is None:
#         return "None"
#     else:
#         rnd = 0
#         for res in entry:
#             rnd = res
#         return rnd


# a = getRound("Udb39262bc44f3276e08be729bac4de38")
# print(a)

# reply_text1 = "a b c"
# reply_text2 = "d e f"
# reply_text = "優點："+reply_text1 + "\n" + "缺點："+reply_text2
# print(reply_text)


arrow = "➡️"

print(arrow)
















# # site = "台北101"
# # sql = "SELECT id FROM `site_data` WHERE name = "' + site + '""
# # print(sql)
# # site_id = "S10000"
# # sql = "SELECT * FROM `segment_data` WHERE site_id = '" + site_id + "' AND evaluation = 'P' ORDER BY weight DESC"
# # print(sql)

# # cnx = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     passwd="12345678",
# #     database='test4'
# # )
# # cursor2 = cnx.cursor(buffered=True)
# # site_id = "S0113"
# # sql2 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
# #     site_id + "' AND evaluation = 'P' ORDER BY weight DESC LIMIT 3"
# # print(sql2)
# # cursor2.execute(sql2)
# # advantages = []

# # for each in cursor2:
# #     print(each[0])
# #     print("~~~~~")
# {
#     "size": {
#         "width": 2500,
#         "height": 843
#     },
#     "selected": true,
#     "name": "圖文選單 1",
#     "chatBarText": "優缺點查詢",
#     "areas": [
#         {
#             "bounds": {
#                 "x": 0,
#                 "y": 0,
#                 "width": 2500,
#                 "height": 843
#             },
#             "action": {
#         }
#         {
#             "bounds": {
#                 "x": 0,
#                 "y": 843,
#                 "width": 833,
#                 "height": 843
#             },
#             "action": {
#                 "type": "postback",
#                 "text": "優缺點查詢",
#             }
#         },
#         {
#             "bounds": {
#                 "x": 833,
#                 "y": 843,
#                 "width": 833,
#                 "height": 843
#             },
#             "action": {
#                 "type": "postback",
#                 "text": "路徑查詢",
#             }
#         },
#         {
#             "bounds": {
#                 "x": 1666,
#                 "y": 843,
#                 "width": 834,
#                 "height": 843
#             },
#             "action": {
#                 "action": {
#                     "type": "postback",
#                     "text": "優我的收藏路線",
#                 }
#         }
#     ]
# }



#     {
#         "size": {
#             "width": 2500,
#             "height": 1686
#         },
#         "selected": false,
#         "name": "Controller",
#         "chatBarText": "Controller",
#         "areas": [
#             {
#                 "bounds": {
#                     "x": 0,
#                     "y": 0,
#                     "width": 2500,
#                     "height": 843
#                 },
#                 "action": {
#                     "type": "message",
#                     "text": "Back"
#                 }
#             },
#             {
#                 "bounds": {
#                     "x": 0,
#                     "y": 843,
#                     "width": 1250,
#                     "height": 843
#                 },
#                 "action": {
#                     "type": "message",
#                     "text": "B1"
#                 }
#             },
#             {
#                 "bounds": {
#                     "x": 1250,
#                     "y": 843,
#                     "width": 1250,
#                     "height": 843
#                 },
#                 "action": {
#                     "type": "message",
#                     "text": "B2"
#                 }
#             }

#         ]
#     }'


# {
#     "size": {
#         "width": 2500,
#         "height": 1686
#     },
#     "selected": true,
#     "name": "圖文選單 1",
#     "chatBarText": "查看更多資訊",
#     "areas": [
#         {
#             "bounds": {
#                 "x": 8,
#                 "y": 80,
#                 "width": 539,
#                 "height": 686
#             },
#             "action": {
#                 "type": "postback",
#                 "text": "查看訂單",
#                 "data": "action=getOrders"
#             }
#         },
#         {
#             "bounds": {
#                 "x": 652,
#                 "y": 81,
#                 "width": 560,
#                 "height": 682
#             },
#             "action": {
#                 "type": "uri",
#                 "uri": "line://ti/p/@dml3676y"
#             }
#         },
#         {
#             "bounds": {
#                 "x": 1302,
#                 "y": 76,
#                 "width": 520,
#                 "height": 682
#             },
#             "action": {
#                 "type": "postback",
#                 "text": "會員資料",
#                 "data": "action=getMemberInfo"
#             }
#         },
#         {
#             "bounds": {
#                 "x": 1902,
#                 "y": 81,
#                 "width": 556,
#                 "height": 673
#             },
#             "action": {
#                 "type": "postback",
#                 "text": "商品資訊",
#                 "data": "action=getProducts"
#             }
#         }
#     ]
# }


# contents = {
#     "type": "bubble",
#     "size": "mega",
#     "hero": {
#         "type": "image",
#         "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
#         "size": "full",
#         "aspectMode": "cover",
#         "aspectRatio": "20:10"
#     },
#     "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#             {
#                 "type": "text",
#                 "text": "景點名稱",
#                 "weight": "regular",
#                 "decoration": "none",
#                 "align": "center",
#                 "wrap": "false",
#                 "style": "normal",
#                 "size": "xs"
#             },
#             {
#                 "type": "text",
#                 "text": "台北101",
#                 "size": "xl",
#                 "margin": "md",
#                 "align": "center",
#                 "weight": "bold"
#             },
#             {
#                 "type": "separator",
#                 "margin": "xl",
#                 "color": "#000000"
#             },
#             {
#                 "type": "text",
#                 "text": "優點",
#                 "margin": "lg",
#                 "size": "sm",
#                 "color": "#888888",
#                 "weight": "bold"
#             },
#             {
#                 "type": "text",
#                 "text": "1.美食好吃 2.餐廳多 3.景色美",
#                 "margin": "sm",
#                 "size": "sm",
#                 "align": "center",
#                 "weight": "bold"
#             },
#             {
#                 "type": "text",
#                 "text": "缺點",
#                 "size": "sm",
#                 "margin": "lg",
#                 "color": "#888888",
#                 "weight": "bold"
#             },
#             {
#                 "type": "text",
#                 "text": "1.美食好吃 2.餐廳多 3.景色美",
#                 "margin": "sm",
#                 "size": "sm",
#                 "align": "center",
#                 "maxLines": 20,
#                 "weight": "bold"
#             },
#             {
#                 "type": "separator",
#                 "margin": "xl",
#                 "color": "#000000"
#             }
#         ]
#     },
#     "styles": {
#         "footer": {
#             "separator": "false"
#         }
#     }
# }
# jsonStr = json.dumps(contents, sort_keys=True, indent=1)
# print(jsonStr)

# data = json.loads(jsonStr)
# print(data)

# print(type(data))
# print(type(jsonStr))



# def getEval(site):
#     cnx = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="123456789",
#         database='test1'
#     )
#     cursor = cnx.cursor(buffered=True)
#     site = site
#     #0 資料存在,1 無資料 ,-1 無分析資料, 2 模糊搜尋
#     status = 0
#     #確認id是否存在
#     sql = "SELECT id,name FROM `site_data` WHERE name LIKE '%" + site + "%'"
#     cursor.execute(sql)
#     entry = cursor.fetchone()
#     site_id = ""
#     advantages = []
#     disadvantages = []

#     if entry is None:
#         #找不到 staus = 1
#         status = 1
#     else:
#         #找到 staus = 0,給site_id
#         status = status
#         entry = list(entry)
#         site_id = entry[0]
#         site_name = entry[1]
#         if site_name != site:
#             status = 2
#         #確認該id有無分析資料
#     if status == 0 or status == 2:
#         sql4 = "SELECT * FROM `segment_data` WHERE site_id = '" + site_id + "'"
#         cursor4 = cnx.cursor(buffered=True)
#         cursor.execute(sql4)
#         entry = cursor.fetchone()
#         if entry is None:
#             status = -1
#         else:
#             print("entry：",entry)
#             status = status
#             #找前三優點
#             cursor2 = cnx.cursor(buffered=True)
#             sql2 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
#                 site_id + "' AND evaluation = 'P' ORDER BY degree DESC LIMIT 3"
#             cursor2.execute(sql2)

#             for each in cursor2:
#                 advantages.append(each[0])

#             #找前三缺點
#             cursor3 = cnx.cursor(buffered=True)
#             sql3 = "SELECT segment FROM `segment_data` WHERE site_id = '" + \
#                 site_id + "' AND evaluation = 'N' ORDER BY degree DESC LIMIT 3"
#             cursor3.execute(sql3)

#             for each in cursor3:
#                 disadvantages.append(each[0])

#     #優缺點回傳
#     return status,advantages, disadvantages


# a, b, c = getEval("汽車")
# print(a)
# print(b)
# print(c)

# site_id = 's0101'
# sql4 = "SELECT * FROM `path_relationship` WHERE from_id = '" + \
#     site_id + "' OR to_id = '" + site_id + "'"
# print(sql4)

# aa = "SightSeeing聊天機器人主要提供兩種功能（1.優缺點查詢  2.路徑查詢）\n使用者請先在選單中選擇功能\n1.當您選擇'優缺點查詢'時，請輸入一個景點，系統將會分析出該景點前三被提及到的優點與缺點!\n2.當您選擇'路徑查詢'時，請輸入一個景點，系統將會分析出去玩該景點還可以去哪些地方!"
# print(aa)

a = "! a"
b = " !a"
c = "!a "
d = " !a "
print(a)
print(b)
print(c)
print(d)
a = ''.join(a.split())
b = ''.join(b.split())
c = ''.join(c.split())
d = ''.join(d.split())
print(a)
print(b)
print(c)
print(d)
