import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np

# 打开浏览器，并最小化
driver = webdriver.Chrome()
driver.minimize_window()
# 隐性等待
# driver.implicitly_wait(300)
# 打开鉴定磁性拓扑网页
driver.get("https://www.cryst.ehu.es/cgi-bin/cryst/programs/magnetictopo.pl?tipog=gmag")
# 读取所有的trace.txt文件名
alltxtname = np.loadtxt(r'C:\Users\cz7989\Desktop\code\mfiles\topoU\2Dmatpedia\zxcal\fm001\alltxtname',dtype=np.str_,encoding='utf-8')
# trace.txt所在目录
tracedirname = r"C:\Users\cz7989\Desktop\code\mfiles\topoU\2Dmatpedia\zxcal\fm001\trace_honeycomb_fm001\trace_col"
fanxie = "\\"
# 下载文件夹所在目录
downloaddir = r"C:\Users\cz7989\Downloads"

for ztxtname in alltxtname:
    zfenge = ztxtname.split(".")
    if os.path.exists(downloaddir+fanxie+zfenge[0]+".tar.gz"):
        continue
    # 通过name找到"选择文件"按钮，上传本地trace.txt文件
    upload_box = driver.find_element('name','bandfile')
    upload_box.send_keys(tracedirname+fanxie+ztxtname)
    # 等待2秒，确保上传完毕
    time.sleep(2)
    # 通过name找到"show"按钮，点击提交
    show_button = driver.find_element('name','submit')
    show_button.click()
    # 待运行完毕后点击下载链接
    try:
        download_button = driver.find_element(by=By.PARTIAL_LINK_TEXT, value='files')
        download_button.click()
    except:
        pass
    # 返回上一页
    driver.back()

# 关闭整个浏览器，并且关闭驱动chromedriver
# driver.quit()
