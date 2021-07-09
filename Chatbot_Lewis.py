#简易聊天机器人2020.8
__author__ = 'Liuyichuan'

import requests
import json
import csv

flag=True
print("-----------简易聊天机器人Lewis开启-----------")
print("输入语句按回车后得到回复，输入“再见”或“拜拜”退出")

while flag:
    print("我：",end='')
    enty='entity='
    enty_num=0
    message=input()
    backwords=[]
    print("Chatbot：",end='')
   
    #常见套路式对话
    if message[0:2]=='你好':
        print("你好");continue
    if len(message)==3 and message[2]=='好':#应对早上好、晚上好等
        print(message);continue
    if message[0:4]=='你吃了吗':
        print("我不用吃饭的呀");continue
    if message[0:3]=='你是谁':
        print("我是聊天机器人Lewis");continue
    if message[0:6]=='你叫什么名字':
        print("我叫Lewis");continue
    if message[0:6]=='你是机器人吗':
        print("是的，我是聊天机器人Lewis");continue
    if message[0:4]=='你是人吗':
        print("不是，我是聊天机器人Lewis");continue
    if message[0:6]=='你有女朋友吗' or message[0:6]=='你有男朋友吗':
        print("你帮我找个嘛");continue
    if message[0:7].lower()=='lewis是谁':#忽略大小写
        print("是我呀");continue
    if message[0:3]=='你真傻':
        print("我自我感觉很好呀");continue
    if message[0:3]=='你太笨':
        print("我不笨，我生气了");continue
    if message[0:6]=='你是谁开发的':
        print("我是LYC开发的");continue
    if message[0:3]=='你累吗':
        print("不累，我是不知疲倦的");continue
    if message[0:3]=='你真棒' or message[0:3]=='你很好' or message[0:3]=='你很棒' or message[0:4]=='你真不错' :
        print("谢谢，我会再接再厉的");continue
    if message[0:3]=='你几岁' or message[0:3]=='你多大' or message[0:2]=='几岁' :
        print("我2个月大，哈哈~没想到吧");continue
    if message[0:4]=='天气真好' or message[0:6]=='今天天气真好' or message[0:5]=='今天天气好':
        print("是啊，可以出去玩了");continue
    if message[0:2]=='谢谢' or message[0:2]=='感谢':
        print("不客气啦");continue
    if message[0:2]=='晚安' or message[0:2]=='睡觉':
        print("晚安");continue
    if message[0:10]=='今天中午我吃了红烧肉' :
        print("那你一定很开心吧，我喜欢回锅肉")

    if message[0:2]=='再见' or message[0:2]=='拜拜':
        print("再见")
        flag=False#通过输入“再见”或“拜拜”退出循环
        continue

    #回答模板式问题
    if message[0:3]=='你知道':#回答“你知道XX吗”
        for word in message[3:]:#提取关键词
            if word!='吗':
                enty=enty+word
                enty_num+=1
            else:
                break      
        r = requests.get("https://api.ownthink.com/kg/knowledge",params=enty)#调用知识图谱
        backsentence=r.text
        #print(r.json())
        backwords=''
        for word in backsentence[62+enty_num:]:
            if word!=']':
                backwords=backwords+word
            else:
                break
        if backwords=='':
            print("不好意思，我不知道，换个问题吧");continue
        else:
            print("是的，"+backwords);continue

    if message[-2:]=='是谁' or message[-3:]=='是谁？' or message[-4:]=='是什么？' or message[-3:]=='是什么':#回答“XX是谁（？）”和“XX是什么（？）”
        for word in message:
            if word!='是':
                enty=enty+word
                enty_num+=1
            else:
                break      
        r = requests.get("https://api.ownthink.com/kg/knowledge",params=enty)
        backsentence=r.text
        backwords=''
        for word in backsentence[62+enty_num:]:
            if word!=']':
                backwords=backwords+word
            else:
                break
        if backwords=='':
            print("不好意思，我不知道，换个问题吧");continue
        else:
            print(backwords);continue

    print("不好意思，我有点不明白，换个话题吧");continue#以上所有都无法分析时的情况

    #回复一般性的语句
    #score=SnowNLP(message)#情感倾向数值（0-1，数字越大越积极）
    #if score>0.8:
      #  print('那你一定很开心吧，',end='')
    #if score<0.2:
      #  print('别难过了，',end='')

    # keywords_textrank = jieba.analyse.textrank(message)
    # for keyword in keywords_textrank:
    #     enty=enty+keyword
    #     r = requests.get("https://api.ownthink.com/kg/knowledge",params=enty)#调用知识图谱
    #     keywords2_textrank = jieba.analyse.textrank(r.text)#再次提取关键词
    #     enty='entity='+keywords2_textrank[0]#选第一个关键词
    #     if enty=='entity=':#提取关键词失败了
    #         break
    #     else:
    #         r = requests.get("http://ip:8888/top_sim",params=enty)#调用词向量
    #         dictword=dict(r.text)
    #         print("我也喜欢"+dictword['top_similar_words'][0][0])
        

#print(r.json())


