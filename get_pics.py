from lib.func import get_imgs
from temp.page_urls import page_urls

cookie_value = 'PHPSESSID=8d7b065aaca254fe76b3e4076c1bdb4d; ba1b8_cloudClientUid=57571005; ba1b8_threadlog=%2C438%2C; ba1b8_jobpop=0; ba1b8_readlog=%2C3184979%2C3183580%2C3184676%2C; ba1b8_cknum=CQ0OUQAKDVAIBzw%2BVFQEV1QLAAFVV1FcUVQBVQcFVARWBVcCDw4BUwEBAwA; ba1b8_winduser=CQEPVAEwDVNcAANWAwEFV1IBDwkFUVFcAQQOAwUDUwYEUFVRW14%2F; ba1b8_ck_info=%2F%09; ba1b8_lastvisit=0%091580038202%09%2Fthread.php%3Ffid-438-page-1.html; ba1b8_lastpos=F438; ba1b8_ol_offset=10282; ba1b8_ci=thread%091580038202%09%09438'
# print(page_urls[12])
for url in page_urls[12:]:
    get_imgs(url, cookie_value)
    print(f'程序执行到第"{page_urls.index(url)+1}"处！---------')
