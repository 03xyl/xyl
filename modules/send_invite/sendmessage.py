import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SET import SETTINGS_DATA
from selenium.webdriver.support.ui import WebDriverWait

#创建文件
os.path.exists(SETTINGS_DATA.get('USER_FILE_PATH')) or os.mkdir(SETTINGS_DATA.get('USER_FILE_PATH'))

option = Options()
# # 爬虫反屏蔽
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument(f'--user-data-dir={SETTINGS_DATA.get("USER_FILE_PATH")}')
driver = webdriver.Edge(service=Service(r'D:\edg_driver\msedgedriver.exe'), options=option)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get:()=>undefined})'
})


driver.get('https://affiliate-us.tiktok.com/connection/creator-management?shop_region=US')

#显式等待
wait=WebDriverWait(driver,20)
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
if __name__ == '__main__':

    #点击Batch message
    _wait(By.ID, 'crm_batch_im')
    is_element(By.ID, 'crm_batch_im')
    #全选达人
    _wait(By.CSS_SELECTOR, 'table thead .arco-checkbox-mask')
    is_element(By.CSS_SELECTOR, 'table thead .arco-checkbox-mask')
    #点击Batch message
    _wait(By.CSS_SELECTOR, '[data-e2e="837e365f-24f2-d052"]')
    is_element(By.CSS_SELECTOR,'[data-e2e="837e365f-24f2-d052"]')
    #输入邀请
    wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '#title_input')))
    driver.find_element(By.CSS_SELECTOR,'#title_input').send_keys('1')
    driver.find_element(By.CSS_SELECTOR,'#content_input').send_keys('1')


    # add_1
    _wait(By.CSS_SELECTOR, '[data-e2e="5b7c3496-6daf-d90c"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="5b7c3496-6daf-d90c"]')
    #
    _wait(By.CSS_SELECTOR, 'table tbody tr td span')
    is_element(By.CSS_SELECTOR, 'table tbody tr td span')
    # add_2
    _wait(By.CSS_SELECTOR, '[data-e2e="db5b7284-f1d3-db50"]')
    is_element(By.CSS_SELECTOR, '[data-e2e="db5b7284-f1d3-db50"]')
    #send message
    _wait(By.CSS_SELECTOR,'[data-e2e="7c807b3b-fcf4-6c97"]')
    is_element(By.CSS_SELECTOR,'[data-e2e="7c807b3b-fcf4-6c97"]')
    #send
    _wait(By.CSS_SELECTOR,'[data-focus-lock-disabled="false"] .arco-btn-primary')
    is_element(By.CSS_SELECTOR,'[data-focus-lock-disabled="false"] .arco-btn-primary')

    input()