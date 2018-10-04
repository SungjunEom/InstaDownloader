import os
import time
import urllib.request
import queue as Queue
from selenium import webdriver


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating Directory.' + directory)

#입력
user = input('계정 이름을 입력하세요:')
base = 'https://www.instagram.com'
url = base + '/' + user
downloaded_directory = './downloaded/' + user + '/'

createFolder(downloaded_directory)

driver = webdriver.Chrome(r'./dev/chromedriver.exe')
driver.set_window_position(-10000,0)

driver.get(url)
driver.implicitly_wait(7)
before = time.time()

position = driver.execute_script("return window.pageYOffset;")
temp = list()
list_del = list()
while True:
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    if time.time() - before > 0.2:
        ###
        posts = driver.find_elements_by_tag_name('a')

        #링크 정리
        #temp = list()
        #list_del = list()

        for post in posts:
            try:
                temp.append(post.get_attribute('href'))
            except:
                pass
        
        
        ###

    if time.time() - before > 3.5:
        if position == driver.execute_script("return window.pageYOffset;"):
            break
        else:
            position = driver.execute_script("return window.pageYOffset;")
            before = time.time()

driver.execute_script('window.scrollTo(0,0);')

temp = list(set(temp))



#링크 정리
iter = 0
for i in temp:
    if not '/p/' in i:
        list_del.append(iter)
    iter += 1
for i in reversed(list_del):
        del temp[i]




#저장
file_order = 0
file_name = '.jpg'
for i in temp:
    driver.get(i)
    #driver.implicitly_wait(0.5)
    imgs_temp = driver.find_elements_by_tag_name('img')
    for img_temp in imgs_temp:
        if '/s150x150' in img_temp.get_attribute('src'):
            continue
        urllib.request.urlretrieve(img_temp.get_attribute('src'),downloaded_directory + str(file_order) + file_name)
        file_order += 1

driver.quit()

if file_order == 0:
    print('계정이 없거나 비공개된 계정입니다.')