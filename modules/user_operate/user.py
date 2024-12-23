import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

from components.get_webdriver import  driver
from config.settings import SETTINGS_DATA
from modules.user_operate.user_utils import  input_or_click_element
from selenium.webdriver.support import expected_conditions as EC

# 批量上傳
def upload_files():
    driver.get(SETTINGS_DATA.get('my_url'))
    # 点击达人标签
    input_or_click_element((By.CSS_SELECTOR, '.arco-select-view-with-prefix'), 'click')
    # 点击标签管理
    # a = input_or_click_element((By.CSS_SELECTOR, '.arco-trigger div div div'), choose=2)
    # a[-1].click()
    # time.sleep(5)
    input_or_click_element((By.CSS_SELECTOR, 'body > div:nth-child(14) div.text-neutral-text2.cursor-pointer.flex.p-8.items-center'), 'click')
    # 获得最新标签的名字
    tags = input_or_click_element((By.CSS_SELECTOR, 'table tbody'), choose=2)[-1]
    tag_text = input_or_click_element((By.CSS_SELECTOR, 'tr span div div'), element=tags).text
    print(tag_text)
    # 点击添加标签
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="9eb870c0-e14a-ff51"]'), 'click')

    # 添加标签 .find_elements(By.CSS_SELECTOR, 'tr')[-1]
    tr_add = input_or_click_element((By.CSS_SELECTOR, 'table tbody'), choose=2)[-1]
    # 获得最页面新生产的tr标签
    tr_add = input_or_click_element((By.CSS_SELECTOR, 'tr'), choose=2, element=tr_add)[-1]
    # 输入标签名
    input_or_click_element((By.CSS_SELECTOR, 'input'), 'input',element=tr_add ,input_value=str(int(tag_text) + 1))
    # 点击确认
    input_or_click_element((By.CSS_SELECTOR, 'button'), 'click', element=tr_add)
    time.sleep(2)
    # 关闭标签管理
    input_or_click_element((By.XPATH, '/html/body/div[5]/div[2]/div/span/div/span'), 'click')

    # 点击批量上传
    input_or_click_element((By.CSS_SELECTOR, '[data-e2e="acdc5222-9c95-bf6f"]'), 'click')
    # 显示input[type=file]
    driver.execute_script("document.querySelector('input[type=file]').style.display='block';")
    # 选择文件
    input_or_click_element((By.CSS_SELECTOR, 'input[type="file"]'), 'input',
                           input_value=r'D:\Project\get_tiktok_data\modules\user_operate\creator_template.xlsx')
    # 上传完成在等待2秒
    time.sleep(2)
    # 点击添加标签
    icon_tag = input_or_click_element((By.CSS_SELECTOR, 'span.arco-select-suffix-icon'), choose=2)[-2]
    icon_tag.click()
    # 选择标签
    # input_or_click_element((By.CSS_SELECTOR, '[trigger-placement="bottom"] li label'), 'click')
    driver.execute_script("document.querySelector('[trigger-placement=bottom] li label').click()")
    # 点击添加按钮
    input_or_click_element((By.XPATH, '/html/body/div[7]/div[2]/div/span/div/div[3]/div/div[2]/button[2]'), 'click')

def delete_tag(_tag: str) -> bool:
    driver.get(SETTINGS_DATA.get('my_url'))
    if _tag == '0': return False
    # 点击达人标签
    input_or_click_element((By.CSS_SELECTOR, '.arco-select-view-with-prefix'), 'click')
    # 点击标签管理
    input_or_click_element((By.CSS_SELECTOR, 'body > div:nth-child(14) div.text-neutral-text2.cursor-pointer.flex.p-8.items-center'), 'click')
    # 获得最新标签的名字
    get_tags = input_or_click_element((By.CSS_SELECTOR, 'table tbody'), choose=2)[-1]
    get_tags = input_or_click_element((By.CSS_SELECTOR, 'tr'), choose=2, element=get_tags)
    for tag in get_tags:
        tds = input_or_click_element((By.CSS_SELECTOR, 'td'), 'click',choose=2 ,element=tag)
        tag_name = input_or_click_element((By.CSS_SELECTOR, 'div span div div'), element=tds[0])
        if tag_name.text == _tag:
            input_or_click_element((By.CSS_SELECTOR, 'div span div svg.alliance-icon.alliance-icon-Delete2'), 'click', element=tds[-1])
            input_or_click_element((By.CSS_SELECTOR, '[role="dialog"] button:nth-child(3)'), 'click')
            break
    time.sleep(2)
    input_or_click_element((By.XPATH, '/html/body/div[4]/div[2]/div/span/div/span'), 'click')
    return True


# 主程序
# def main():
#     # 打开链接
#
#     upload_files()
#     # delete_tag('1')

# if __name__ == '__main__':
#     main()
#     input()
