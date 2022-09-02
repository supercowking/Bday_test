# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 22:18:54 2022

@author: super_000
"""


from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio import start_server

# create a flask app

app = Flask(__name__)


def quiz():
    q1 = radio("這位客官，請問您是？",["低哥","沈鴻宇","Dylan"])

    if q1 == "低哥":
        q2 = radio("你好沈鴻宇，聽説 Dylan 要生日了，你知道他生日是那一天嗎",["9/5","9/6","5/9"])
        
        if q2 == "9/5":
            put_text("好棒棒，你竟然沒記錯！ 既然這樣，恭喜你，你可以去換取禮物了")
            put_button('點我！！',onclick=lambda: toast("你以爲你以爲的就是你以爲的嗎，請點'不要點我...'"))
            put_button('不要點我...',onclick=lambda: toast("恭喜你得到了'金斧頭一把'，不過第一次就答對了，會不會有點無聊...要不要去試試別的選項，説不定有驚喜喔"))
            put_button('請最後再點我',onclick=lambda: toast("其實這個按鍵沒做完...請退出再按 QR code or refresh the page即可重新開始"))
            #put_image('sticker_1.png').onclick(lambda: toast('不要亂點...'))
        elif q2 == "9/6":
            q3 = radio("好棒棒喔，你怎麽對得起 Dylan! 再給你一次機會好了！ Dylan的生日到底是哪一天？",["9/5","5/9"])           
            if q3 == "9/5":
                put_text("嗯，這次猜對了，那我勉爲其難讓你去換取禮物吧")
                put_button('點這裏',onclick=lambda: toast("恭喜你得到了'銀斧頭一把'，確定不去試試別的選項了嗎？"))
                put_button('再點這裏',onclick=lambda: toast("這是一個沒有用的按鍵...請退出再按 QR code or refresh the page即可重新開始"))
            else:
                put_text("恭喜你，兩次都選錯，這也算是天選之子了，再給你一次機會顯得有點沒有必要了，你去換取禮物吧...")
                put_button('勉爲其難得讓你點一下這裏',onclick=lambda: toast("恭喜你得到了'不知名的斧頭一把'"))
        else:
            q4 = radio("這位客官，這差的有點遠了...我看您需要的是...",["記憶麵包","左右不分的超能力","再來一次的機會"])
            if q4 == "記憶麵包":
                put_text("對不起，大雄說他剛吃完最後一片耶...請退出再按 QR code or refresh the page 重新開始")
            elif q4 == "左右不分的超能力":  
                put_text("不好意思，這個賬戶的餘額剛被一位女俠取完了...下次請早")
                put_text("請退出再按 QR code or refresh the page重新開始")
            else:
                q5 = radio("Dylan的生日到底是哪一天？...",["9/5","9/6"])
                if q5 == "9/5":
                   put_text("這還差不多，您差點就要和禮物擦肩而過了") 
                   put_button('沒有擦肩而過的禮物在這裏',onclick=lambda: toast("恭喜你得到了'不知名的斧頭一把'"))
                else:
                   put_text("左右不分的超能力也救不了你了")  
                   put_text("請退出再按 QR code or refresh the page重新開始")
                   
    elif q1 == "沈鴻宇":
        q6 = radio("你好 Dylan，聽説低哥要生日了，你知道他生日是那一天嗎",["9/5","9/6","5/9"])
        
        if q6 == "9/5":
            put_text("好棒棒，你竟然沒記錯！ 既然這樣，恭喜你，你可以去換取禮物了")
            put_button('點我！！',onclick=lambda: toast("你以爲你以爲的就是你以爲的嗎，請點'不要點我...'"))
            put_button('不要點我...',onclick=lambda: toast("恭喜你得到了'金斧頭一把'，不過第一次就答對了，會不會有點無聊...要不要去試試別的選項，説不定有驚喜喔"))
            put_button('請最後再點我',onclick=lambda: toast("其實這個按鍵沒做完...如果不介意的話退出再按 QR code or refresh the page即可重新開始"))
            
        elif q6 == "9/6":
            q7 = radio("好棒棒喔，你怎麽對得起低哥! 再給你一次機會好了！ 低哥的生日到底是哪一天？",["9/5","5/9"])           
            if q7 == "9/5":
                put_text("看來二選一比較容易猜對，那我勉爲其難讓你去換取禮物吧")
                put_button('先點這裏',onclick=lambda: toast("恭喜你得到了'銀斧頭一把'，確定不去試試別的選項了嗎？"))
                put_button('才能點這裏',onclick=lambda: toast("這是一個沒有用的按鍵...請退出再按 QR code or refresh the page即可重新開始"))
            else:
                put_text("恭喜你，兩次都選錯，這也有點故意了，再給你一次機會顯得有點沒有必要了，你去換取禮物吧...")
                put_button('勉爲其難得讓你點一下這裏',onclick=lambda: toast("恭喜你得到了'不知名的斧頭一把'"))
        else:
            q8 = radio("這位客官，這差的有點遠了...我看您需要的是...",["咪嗦C夢","左右不分的超能力","再來一次的機會"])
            if q8 == "咪嗦C夢":
                put_text("對不起，咪嗦C夢說他哥才有記憶麵包...請退出再按 QR code or refresh the page重新開始")
            elif q8 == "左右不分的超能力":  
                put_text("這個超能力很難後天習得...這是屬於出廠時的隱藏技能...所以...")
                put_text("請退出再按 QR code or refresh the page重新開始")
            else:
                q9 = radio("低哥的生日到底是哪一天？...",["9/5","9/6"])
                if q9 == "9/5":
                   put_text("這還差不多，您差點就要和禮物擦肩而過了") 
                   put_button('差點擦肩而過的禮物在這裏',onclick=lambda: toast("恭喜你得到了'不知名的斧頭一把'"))
                else:
                   put_text("左右不分的超能力也救不了你了") 
                   put_text("請退出再按 QR code or refresh the page重新開始")
        
    else:
        q10 = radio("你好低哥，聽説沈鴻宇要生日了，你知道他生日是那一天嗎",["9/5","9/6","5/9"])
        
        if q10 == "9/5":
            put_text("好棒棒，你竟然沒記錯！ 既然這樣，恭喜你，你可以去換取禮物了")
            put_button('點我！！',onclick=lambda: toast("你以爲你以爲的就是你以爲的嗎，請點'不要點我...'"))
            put_button('不要點我...',onclick=lambda: toast("恭喜你得到了'金斧頭一把'，不過第一次就答對了，會不會有點無聊...要不要去試試別的選項，説不定有驚喜喔"))
            put_button('請最後再點我',onclick=lambda: toast("其實這個按鍵沒做完...如果不介意的話退出再按 QR code or refresh the page即可重新開始"))
        elif q10 == "9/6":
            q11 = radio("好棒棒喔，你怎麽對得起沈鴻宇! 再給你一次機會好了！ 沈鴻宇的生日到底是哪一天？",["9/5","5/9"])           
            if q11 == "9/5":
                put_text("嗯，這次猜對了，那我勉爲其難讓你去換取禮物吧")
                put_button('點這裏',onclick=lambda: toast("恭喜你得到了'銀斧頭一把'，確定不去試試別的選項了嗎？"))
                put_button('還是這裏呢？',onclick=lambda: toast("這是一個沒有用的按鍵...請退出再按 QR code or refresh the page即可重新開始"))
            else:
                put_text("恭喜你，兩次都選錯，這也算是天選之子了，再給你一次機會顯得有點沒有必要了，你去換取禮物吧...")
                put_button('勉爲其難得讓你點一下這裏',onclick=lambda: toast("恭喜你得到了'不知名的斧頭一把'"))
        else:
            q12 = radio("這位客官，這差的有點遠了...我看您需要的是...",["記憶果實","左右不分的超能力","再來一次的機會"])
            if q12 == "記憶果實":
                put_text("記憶果實嗎？想要的話可以全部給你，去找吧，我全部都放在那裏...找不到的話請退出再按 QR code or refresh the page重新開始")
            elif q12 == "左右不分的超能力":  
                put_text("這個可能需要天賦異稟的人才能得到...下次教你...")
                put_text("請退出再按 QR code or refresh the page重新開始")
            else:
                q13 = radio("沈鴻宇的生日到底是哪一天？...",["9/5","9/6"])
                if q13 == "9/5":
                   put_text("這還差不多，您差點就要和禮物擦肩而過了") 
                   put_button('差點擦肩而過的禮物在這裏',onclick=lambda: toast("恭喜你得到了'不知名的斧頭一把'"))
                else:
                   put_text("左右不分的超能力也救不了你了")
                   put_text("請退出再按 QR code or refresh the page重新開始")     
        
        
    
        
app.add_url_rule('/','webio_view',webio_view(quiz),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    
    start_server(quiz, port=args.port)

#app.run(host='localhost', port=5000)