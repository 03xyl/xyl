from pathlib import Path


SETTINGS_DATA = {
    'FIND_ALL_DATA_URL' : "https://affiliate-us.tiktok.com/connection/creator-management?shop_region=US",
    # 'DETAIL_DATA_URL' : 'https://affiliate.tiktokglobalshop.com/connection/creator/detail?cid={}',
    # 'File_name' : 'request_data',
    'Time_out' : 20,
    'EMAIL' : 'shop10302@woworldtech.com',
    'PASSWORD' : '123456.q',
    'edge_driver_path': r'D:\edge_driver\msedgedriver.exe',
    'USER_FILE_PATH': str(Path(__file__).parent.parent.parent) + r'\edge_user_data',
    'COLLECT_TOTAL_DATA': 12
}