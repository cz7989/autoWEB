import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np

# 打开特定config的浏览器：
# 在终端执行指令 chrome.exe --remote-debugging-port=1688 --user-data-dir="D:\chrome4py"
# 进入网站人工登录到指定页面

# 启动的浏览器地址
# 将浏览器配置信息进行添加
options = Options()
options.debugger_address ='127.0.0.1:1688'
driver = webdriver.Chrome( chrome_options=options)

# 隐性等待
# driver.implicitly_wait(20)
# 需要保证打开的浏览器在前台
time.sleep(5)
driver.maximize_window()

# 读取要填的数据
allinfo = np.loadtxt(r'C:\Users\cz7989\Desktop\lesson_info',dtype=np.str_,encoding='utf-8')


# 循环填写数据
for ihang in range(allinfo.shape[0]):
    zinfo=allinfo[ihang][:]
    # 点击新增
    # time.sleep(5)
    newbutton = driver.find_element(by=By.XPATH, value='//input[@value="新 增"]')
    newbutton.click()
    # 开始填表
    hdmc_box = driver.find_element(by=By.XPATH, value='//input[@class="exerciseName"]')
    hdmc_box.click()
    hdmc_box.clear()
    hdmc_box.send_keys(zinfo[0])
    hdmc_box = driver.find_element(by=By.XPATH, value='//input[@id="j_idt43:j_idt49:date"]')
    hdmc_box.click()
    hdmc_box.clear()
    hdmc_box.send_keys(zinfo[1])
    hdmc_box = driver.find_element(by=By.XPATH, value='//input[@class="lessons"]')
    hdmc_box.click()
    hdmc_box.clear()
    hdmc_box.send_keys(zinfo[2])
    hdmc_box = driver.find_element(by=By.XPATH, value='//input[@class="teacherName"]')
    hdmc_box.click()
    hdmc_box.clear()
    hdmc_box.send_keys(zinfo[3])
    hdmc_box = driver.find_element(by=By.XPATH, value='//input[@class="studentClasses"]')
    hdmc_box.click()
    hdmc_box.clear()
    hdmc_box.send_keys(zinfo[4])
    hdmc_box = driver.find_element(by=By.XPATH, value='//textarea[@class="summary"]')
    hdmc_box.click()
    hdmc_box.clear()
    hdmc_box.send_keys(zinfo[5])
    # 点击保存
    hdmc_box = driver.find_element(by=By.XPATH, value='//input[@value="保 存"]')
    hdmc_box.click()
