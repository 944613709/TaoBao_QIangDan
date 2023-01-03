import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyttsx3
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
times = "2022-05-15 21:00:00"

# 注意此处添加了chrome_options参数
browser = webdriver.Chrome()

engine = pyttsx3.init()
browser.get("https://www.taobao.com")
browser.find_element(by=By.LINK_TEXT, value="亲，请登录").click()
print("请登录")
engine.say("请十五秒内登录")
engine.runAndWait()
time.sleep(15)
browser.get("https://cart.taobao.com/cart.htm")

while True:
    if browser.find_element(by = By.ID,value = "J_SelectAll1"):
        browser.find_element(by = By.ID,value = "J_SelectAll1").click()
        engine.say("抢单功能已开启，到点自动抢单")
        engine.runAndWait()
        break

while True:

    #获取电脑现在的时间,                      year month day
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    print(now)
    #判断是不是到了秒杀时间?
    if now > times:
        # 点击结算按钮
        while True:
            try:
                if browser.find_element(by = By.LINK_TEXT,value = "结 算"):
                    print("here")
                    browser.find_element(by = By.LINK_TEXT,value = "结 算").click()
                    print(f"主人,程序锁定商品,结算成功")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element(by = By.LINK_TEXT,value = '提交订单'):
                    browser.find_element(by = By.LINK_TEXT,value = '提交订单').click()
                    print(f"抢购成功，请尽快付款")
            except:
                engine.say("我已帮你抢到商品啦,您来支付吧")
                engine.runAndWait()
                print(f"主人,我已帮你抢到商品啦,您来支付吧")
                break
        time.sleep(0.01)
