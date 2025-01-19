#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#from nltk.corpus import stopwords
#EngStopWords = set(stopwords.words('english'))#這裡設定稍後取用 English 的停用詞語料庫
#text = "There is an apple on the table."
#for word in text.split():
    #if word in EngStopWords:
        #pass #如果詞彙是個英文的停用詞的話，就略過不處理。
    #else:
        #print(word) #如果詞彙不是英文的停用詞的話，呈現在畫面上。


from ArticutAPI import Articut

text = "在這個數位娛樂盛行的時代，線上捕魚遊戲已經成為了眾多玩家心目中的首選娛樂方式啦！這款遊戲不僅擁有超高品質的視覺效果和逼真的聲音體驗，還提供了豐富的獎勵機制，讓你在享受遊戲樂趣的同時，還能賺取真實的金錢！

線上捕魚遊戲的玩法簡單有趣，遊戲中還有各種特效和道具，讓你的捕魚之旅更加精彩。無論是休閒娛樂還是挑戰高額獎勵，線上捕魚遊戲都能滿足你的需求。現在就讓我們加入這個充滿樂趣和挑戰的世界，體驗捕魚遊戲的無限魅力吧！"

articut = Articut(username="", apikey="")
result = articut.parse(text)

contentWordLIST = articut.getContentWordLIST(result)
for sentence in contentWordLIST:
    for word in sentence:
        print(word[-1])
