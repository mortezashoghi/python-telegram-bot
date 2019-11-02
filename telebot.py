import os
import json
# import socks
# import socket
from urllib.request import urlopen
import time
import requests
from urllib.parse import quote,unquote
class telegram:
    
    def __init__(self,connectionStr):
        self.token=connectionStr["token"]
        self.url=connectionStr["url"]+self.token+"/"
        self.command=connectionStr["command"]
        self.text=""
        self.http_proxy =connectionStr["proxy"]
    
           
    def testmytoken(self):
        test_cmd="getme"
        #for use proxy uncomment below two lines
        # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
        # socket.socket = socks.socksocket
        response=urlopen(self.url+self.command).read()
        result=self.decode_utf(response)
        result=json.loads(result)
        if result['ok']:
            return True
        else:
            return False
    def connectotlg(self):
        pass
        
    def sendmessage(self,chat_id,text,upid):
        self.command='sendmessage'
        response=urlopen(self.url+self.command+'?chat_id={}&text={}'.format(chat_id,text))
        dec_msg=self.decode_utf(response)
        dec_msg=json.loads(dec_msg)
        if dec_msg['ok']:
            # self.getupdates(upid)
            return True
        else:
            # self.getupdates(upid)
            return False
    
    def getupdates(self,updateid=""):
        if updateid!="":
            urlopen(self.url+"getupdates"+'?offset={}'.format(updateid+1))
        updated_cmd=""
        self.command='getupdates'
        response=urlopen(self.url+self.command)
        dec_msg=self.decode_utf(response)
        updated_cmd=json.loads(dec_msg)
          
        if len(updated_cmd['result']) > 0 :
            print(str(updated_cmd["result"][0]['message']["from"]))
            msg=updated_cmd['result'][0]['message']
            update_id=updated_cmd['result'][0]['update_id']
            chat_id=str(msg['chat']['id'])
            if 'text' in msg:
                userreq=quote(str(msg['text']).encode('utf-8'))
                reqinfo={
                   "chat_id":chat_id,
                   "text":userreq,
                   "upid":update_id
                    }
                return reqinfo
    def casesend(self,chatid,text):
        self.command='sendmessage'
        response=urlopen(self.url+self.command+'?chat_id={}&text={}'.format(chatid,text))
        dec_msg=self.decode_utf(response)
        dec_msg=json.loads(dec_msg)
        if dec_msg["ok"]:
            return True
    def decode_utf(self,texttodec=""):
        decoded_text=''
        if texttodec!="":
            for line in texttodec:
                decoded_text+=line.decode('utf-8')
            return decoded_text
        else:
            for line in self.text:
                decoded_text+=line.decode('utf-8')
            return decoded_text
            
        
    def savelog(self):
        #TODO: save all actions in app
        pass
    def savetodb(self,data):
        #TODO:  check user exist or no if not , call saveAscontact() and save it
        pass
    def saveAscontact(self):
        #TODO: save new joined users info (user id , username , first name , .... all info from telegram getupdate command)  
        pass
    def __str__(self):
        pass