from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage

import configparser
import json
import random
from api import site_connector
import mysql.connector
app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456789",
        database='linebot'
    )
    #非本機端

    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        print("=====first round====")
        u_id = event.source.user_id
        print("user :" + u_id)
        rnd = getRound(cnx, u_id)
        print("取得round.....", rnd)
        # print("選擇功能")
        # choice = event.message.text
        # print("text :" + choice)
        if rnd == 0:
            print("選擇功能")
            choice = event.message.text
            print("text :" + choice)
        elif rnd == 1:
            choice = getChoice(cnx, u_id)
            new_choice = event.message.text
            form = ['優缺點查詢', '路徑查詢','問題中心']
            if(new_choice in form):
                choice = new_choice
                addRound(cnx, u_id, 0)
            else:
                print("選擇地點")
        else:
            rnd = 0
            choice = "錯誤輸入"
                
        #取得user_id ,text
        # first round 表單選擇
        rnd = getRound(cnx, u_id)
        if(rnd == 0 and(choice == "優缺點查詢" or choice == "路徑查詢" or choice == "問題中心")):
            if(choice == "優缺點查詢"):
                print("進入優缺點")
                message = "歡迎使用優缺點查詢功能!!\n請輸入查詢景點名稱：(ex：台北101)"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            elif(choice == "路徑查詢"):
                print("路徑查詢")
                message = "歡迎使用路徑查詢功能!!\n請輸入查詢景點名稱：(ex：台北101)"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            elif(choice == "問題中心"):
                print("問題中心")
                message = "歡迎使用問題中心功能!!\n請輸入相關指令：\n!about 系統說明\n!how 操作說明\n!connect 聯絡方式"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            saveChoice(cnx, u_id, choice)
            addRound(cnx, u_id, 1)
            print("結束第一輪")
            print("=====first round end !====")
            
        elif(rnd == 1):
            print("=====second round====")
            #地點輸入
            site = event.message.text
            print("輸入的地點 :" + site)
            saveText(cnx, u_id, site)
            # print("選擇地點")
            # choice = getChoice(cnx, u_id)
            # site = event.message.text
            # u_id = event.source.user_id
            # print("輸入的地點 :" + site)
            print("rnd ",rnd," choice ", choice," site ",site)
            if(choice == "優缺點查詢" or choice == "路徑查詢"):
                replyer(event,choice,site)
            else:
                replyer2(event, choice, site)
            print("=====second round end !====")
            # addRound(cnx,u_id, 2)
            print("結束第二輪")
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="請先在選單選擇功能!!")
            )


def replyer2(event, choice, site):
    order = ''.join(site.split())
    if order == "!about":
        message = "SightSeeing是一個可以節省你大量爬文時間的旅程規劃系統。透過系統分析資料，讓你輕鬆的找到想要的旅遊景點或飯店並讓你安排屬於自己的旅程!"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message)
        )
    elif order == "!how":
        message = "SightSeeing聊天機器人主要提供兩種功能（1.優缺點查詢  2.路徑查詢）\n使用者請先在選單中選擇功能\n1.當您選擇'優缺點查詢'時，請輸入一個景點，系統將會分析出該景點前三被提及到的優點與缺點!\n2.當您選擇'路徑查詢'時，請輸入一個景點，系統將會分析出去完該景點後還可以去哪些地方!"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message)
        )
    elif order == "!connect":
        message = "如需與我們聯繫，聯絡方式為以下\nemail：sightseeing@gmail.com"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="請輸入正確指令!!\n若有其他問題，請洽 email：sightseeing@gmail.com")
        )

            
        

def replyer(event,choice,site):
    if(choice == "優缺點查詢"):
        print("優缺點查詢")
        getInfo = site_connector(site)
        status,site_name,positive,negative = getInfo.getEval()
        print("status = ",status)
        if status == 1:
            #回覆無資料
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="查無此景點!!")
            )
        elif status == -1:
            #回覆分析資料數不足
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="您輸入的景點分析資料數不足，故無分析結果!!")
            )
        elif status == 0 or status == 2:
            reply_text1 = ""
            for i in positive:
                reply_text1 += i
                reply_text1 += " "

            reply_text2 = ""
            for i in negative:
                reply_text2 += i
                reply_text2 += " "
            #flex message
            reply_text = "優點："+reply_text1 + "\n" + "缺點："+ reply_text2
            if status == 0:
                contents = get_flex_content_eval(site,reply_text1,reply_text2)
            else:
                site = "您在找? " + site_name
                contents = get_flex_content_eval(
                    site, reply_text1, reply_text2)

            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text="回覆分析結果", contents=contents)
            )

        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text=reply_text)
        # )
 
    elif(choice == "路徑查詢"):
        print("路徑查詢")
        site = event.message.text
        print(site)
        getInfo = site_connector(site)
        status, site_name, result = getInfo.getPath()
        print("status = ", status)
        reply_text = ""
        pt = 1
        if status == 1:
            #回覆無資料
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="查無此景點!!")
            )
        elif status == -1:
            #回覆分析資料數不足
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="您輸入的景點分析資料數不足，故無分析結果!!")
            )
        elif status == 0 or status == 2:
            for i in result:
                reply_text += i
                if (pt <= 2):
                    reply_text += " \n➡️ "
                    pt += 1
            if status == 0:
                contents = get_flex_content_path(site, reply_text)
            else:
                site = "您在找? " + site_name
                contents = get_flex_content_path(site, reply_text)
                
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text="回覆分析結果", contents=contents)
            )




        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text=reply_text)
        # )


def saveChoice(cnx,uID,text):
    #SQL
    cursor = cnx.cursor(buffered=True)
    #user :Udb39262bc44f3276e08be729bac4de38,text: 優缺點查詢
    if checkIfExist(cnx,uID):
        #update
        update_data = ("UPDATE user_log"
                       " SET choice=%s"
                    " WHERE user_id=%s")
        data = (text, uID)
        cursor.execute(update_data, data)
        cnx.commit()
    else:
        #insert
        add_data = ("INSERT INTO user_log"
                    "(user_id,choice) "
                    "VALUES (%s,%s)")
        data = (uID, text)
        cursor.execute(add_data, data)
        cnx.commit()


def saveText(cnx, uID, text):
    #SQL
    cursor = cnx.cursor(buffered=True)
    #user :Udb39262bc44f3276e08be729bac4de38,text: 優缺點查詢
    #update
    update_data = ("UPDATE user_log"
                " SET text=%s"
                " WHERE user_id=%s")
    data = (text, uID)
    cursor.execute(update_data, data)
    cnx.commit()


def getChoice(cnx, uID):
    cursor = cnx.cursor(buffered=True)
    #SQL
    sql = "SELECT choice FROM `user_log` WHERE user_id = '" + uID + "'"
    cursor.execute(sql)
    choice = ""
    for res in cursor:
        choice = res[0]
    return choice


def getText(cnx, uID):
    cursor = cnx.cursor(buffered=True)
    #SQL
    sql = "SELECT text FROM `user_log` WHERE user_id = '" + uID + "'"
    cursor.execute(sql)
    text = ""
    for res in cursor:
        text = res[0]
    return text


def checkIfExist(cnx, uID):
    cursor = cnx.cursor(buffered=True)
    sql = "SELECT * FROM `user_log` WHERE user_id = '" + uID + "'"
    cursor.execute(sql)
    entry = cursor.fetchone()
    if entry is None:
        return False
    else:
        return True


def addRound(cnx, uID, rnd):
    cursor = cnx.cursor(buffered=True)
    update_data = ("UPDATE user_log"
                   " SET round=%s"
                   " WHERE user_id=%s")
    data = (rnd, uID)
    cursor.execute(update_data, data)
    cnx.commit()


def getRound(cnx, uID):
    cursor = cnx.cursor(buffered=True)
    #SQL
    sql = "SELECT round FROM `user_log` WHERE user_id = '" + uID + "'"
    cursor.execute(sql)
    entry = cursor.fetchone()
    rnd = 0
    if entry is None:
        return rnd
    else:
        for res in entry:
            rnd = res
        return rnd

def get_flex_content_eval(site,pros,cons):
    contents = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "20:10"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "景點名稱",
                    "weight": "regular",
                    "decoration": "none",
                    "align": "center",
                    "style": "normal",
                    "size": "xs"
                },
                {
                    "type": "text",
                    "text": site,
                    "size": "xl",
                    "margin": "md",
                    "align": "center",
                    "weight": "bold"
                },
                {
                    "type": "separator",
                    "margin": "xl",
                    "color": "#000000"
                },
                {
                    "type": "text",
                    "text": "優點",
                    "margin": "lg",
                    "size": "sm",
                    "color": "#888888",
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": pros,
                    "margin": "sm",
                    "size": "sm",
                    "align": "center",
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": "缺點",
                    "size": "sm",
                    "margin": "lg",
                    "color": "#888888",
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": cons,
                    "margin": "sm",
                    "size": "sm",
                    "align": "center",
                    "maxLines": 20,
                    "weight": "bold"
                },
                {
                    "type": "separator",
                    "margin": "xl",
                    "color": "#000000"
                }
            ]
        },
        "styles": {
            "footer": {
            }
        }
    }
    return contents


def get_flex_content_path(site, path):
    contents = {
        "type": "bubble",
        "size": "mega",
        "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "20:10"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "景點名稱",
                    "weight": "regular",
                    "decoration": "none",
                    "align": "center",
                    "style": "normal",
                    "size": "xs"
                },
                {
                    "type": "text",
                    "text": site,
                    "size": "xl",
                    "margin": "md",
                    "align": "center",
                    "weight": "bold"
                },
                {
                    "type": "separator",
                    "margin": "xl",
                    "color": "#000000"
                },
                {
                    "type": "text",
                    "text": "推薦路徑",
                    "margin": "lg",
                    "size": "sm",
                    "color": "#888888",
                    "weight": "bold"
                },
                {
                    "type": "text",
                    "text": path,
                    "margin": "sm",
                    "size": "sm",
                    "align": "center",
                    "weight": "bold"
                },
                {
                    "type": "separator",
                    "margin": "xl",
                    "color": "#000000"
                }
            ]
        },
        "styles": {
            "footer": {
            }
        }
    }
    return contents

if __name__ == "__main__":
    app.run()
