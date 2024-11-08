import time
from datetime import datetime, timedelta

from selenium.webdriver.common.devtools.v85.dom import get_attributes

from components.get_webdriver import driver, wait
from config.settings import SETTINGS_DATA
from modules.user_operate.user import upload_files, delete_tag

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# driver.get('https://affiliate-us.tiktok.com/connection/creator-management?shop_region=US')

def _wait(a, b):
    try:
        wait.until(EC.presence_of_element_located((a, b)))
    except Exception as e:
        print(e)


def is_element(_by, css):
    try:
        return driver.find_element(_by, css).click()
    except Exception as e:
        print(e)
tag = None

def selector_tag():
    upload_files()
    time.sleep(5)
    # selecet tag
    _wait(By.XPATH, '//input[@autocomplete="off"][1]')
    is_element(By.XPATH, '//input[@autocomplete="off"][1]')
    # 默认选最上面的tag
    element = driver.find_element(By.CSS_SELECTOR, '[data-e2e="75c1cb63-9d93-c8f6"]')
    global tag
    tag = element.text
    is_element(By.CSS_SELECTOR, '[data-e2e="75c1cb63-9d93-c8f6"]')
    return tag


def run():
    # 添加标签
    selector_tag()
    # batch invite
    _wait(By.ID, 'crm_batch_invite')
    is_element(By.ID, 'crm_batch_invite')
    # SELECT ALL
    _wait(By.CSS_SELECTOR, 'table thead .arco-checkbox-mask')
    is_element(By.CSS_SELECTOR, 'table thead .arco-checkbox-mask')
    #select one
    # time.sleep(1)
    # driver.find_elements(By.CSS_SELECTOR,'table > tbody td.arco-table-td.arco-table-operation.arco-table-checkbox  span.arco-icon-hover.arco-checkbox-icon-hover.arco-checkbox-mask-wrapper > div')[11].click()#second


    # invite to collaborate
    _wait(By.CSS_SELECTOR, '[data-e2e="20c84e8e-6e2b-893c"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="20c84e8e-6e2b-893c"]')

    # #wait four regins
    # wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-e2e="1adf7b37-5743-0a73"]')))
    # #block four regions
    # driver.execute_script("Array.from(document.querySelectorAll('[role=region]')).forEach(item => item.style.display = 'block')")

    # ------------------------------------1.creat invitation------------------------
    # click create invitation
    _wait(By.CSS_SELECTOR, '[data-e2e="500724e9-9450-8cd5"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="500724e9-9450-8cd5"]')
    # invitation name
    time.sleep(1)
    _wait(By.CSS_SELECTOR, '[data-e2e="feafd809-5fe4-3adf"]')
    driver.find_element(By.CSS_SELECTOR, '[data-e2e="feafd809-5fe4-3adf"]').send_keys('1')

    # valid unit
    # 获取当天的日期
    today = datetime.today().date()
    # 加上30天
    future_date = today + timedelta(days=30)
    # 有效日期格式化后的结果为邀请日期
    invite_date = future_date.strftime("%m/%d/%Y")

    # 自动填写有效期
    _wait(By.CSS_SELECTOR, '[data-tid="m4b_date_picker"] .arco-picker-start-time')
    driver.find_element(By.CSS_SELECTOR, '[data-tid="m4b_date_picker"] .arco-picker-start-time').send_keys(
        '1' + invite_date)
    is_element(By.CSS_SELECTOR, '.arco-picker-cell-selected')

    # email address
    _wait(By.CSS_SELECTOR, '#target_complete_details_contacts_7_input')
    is_element(By.CSS_SELECTOR, '[data-e2e="4b47def3-3477-eebf"]')
    # d1.send_keys('ENVIPRO@WOWORLDTECH.COM')
    time.sleep(1)
    driver.execute_script("document.querySelector('#target_complete_details_contacts_7_input').value=''")
    driver.find_element(By.CSS_SELECTOR, '[data-e2e="4b47def3-3477-eebf"]').send_keys('ENVIPRO@WOWORLDTECH.COM')
    # driver.execute_script('document.querySelector("#target_complete_details_contacts_7_input").value = " "')
    # inster
    _wait(By.ID, 'target_complete_details_message_input')
    is_element(By.ID, 'target_complete_details_message_input')
    time.sleep(1)
    # driver.find_element(By.ID,'target_complete_details_message_input').clear()
    driver.execute_script("document.querySelector('#target_complete_details_message_input').value=''")
    driver.find_element(By.ID, 'target_complete_details_message_input').send_keys('hello')
    # driver.execute_script("document.querySelector("#target_complete_details_message_input").value=''")
    # # driver.execute_script('document.querySelector("#target_complete_details_message_input").value="hello"')
    # driver.execute_script('console.log("--------------------------------------------------------------")')
    # driver.execute_script('console.log(document.querySelector("#target_complete_details_message_input").value)')
    # driver.execute_script('console.log("--------------------------------------------------------------")')
    # -----------------------------------2.choose product---------------------------------
    # click product
    _wait(By.CSS_SELECTOR, '[data-e2e="2db00f21-e6e3-0eda"]')
    driver.find_elements(By.CSS_SELECTOR, '[data-e2e="2db00f21-e6e3-0eda"]')[1].click()
    # Add product
    time.sleep(1)
    _wait(By.CSS_SELECTOR, '[data-e2e="05f9b037-2b9d-d20b"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="05f9b037-2b9d-d20b"]')
    # 全选 product
    time.sleep(1)
    _wait(By.CSS_SELECTOR, '[data-tid="m4b_image"]')
    # driver.find_elements(By.CSS_SELECTOR,'table thead')[-1].find_element(By.CSS_SELECTOR,'span')
    driver.find_elements(By.CSS_SELECTOR, 'table thead span')[10].click()
    # Add
    _wait(By.CSS_SELECTOR, '[data-e2e="6453523e-5b3f-f3a9"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="6453523e-5b3f-f3a9"]')
    # send20
    _wait(By.CSS_SELECTOR, '[data-e2e="3a1bf7cf-465b-f541"]')
    driver.find_element(By.CSS_SELECTOR, '[data-e2e="3a1bf7cf-465b-f541"]').send_keys('20')

    # -----------------------------------3.set up free sample--------------
    # click
    driver.find_elements(By.CSS_SELECTOR, '[data-tid="m4b_collapse_item"]')[2].click()
    # Manually review requests
    driver.find_elements(By.CSS_SELECTOR, '[data-e2e="2bef7fda-3f0c-80f4"] span')[-1].click()


    # -----------------------------------4.choose creators-----------------
    # click choose creators
    driver.find_elements(By.CSS_SELECTOR, '[data-e2e="1adf7b37-5743-0a73"]')[-1].click()
    # creators
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, 'table thead tr th div')[-5].click()
    # send
    time.sleep(1)
    _wait(By.CSS_SELECTOR, '[data-e2e="140f8059-efa6-4618"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="140f8059-efa6-4618"]')


    # print(bool_)
    # 打开一个新标签页
    time.sleep(5)
    driver.execute_script(f"window.open('{SETTINGS_DATA.get('my_url')}');")

    # 切换到新打开的标签页
    driver.switch_to.window(driver.window_handles[-1])

    bool_ = delete_tag(tag)
    print(bool_)
run()
input()