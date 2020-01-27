from lib.func import del_file, get_imgs_urls

# 获取所有页面图片链接的url,总共有38页
cookie_value = 'PHPSESSID=8d7b065aaca254fe76b3e4076c1bdb4d; ba1b8_cloudClientUid=57571005; ba1b8_threadlog=%2C438%2C; ba1b8_jobpop=0; ba1b8_readlog=%2C3184979%2C3183580%2C3184676%2C; ba1b8_cknum=CQ0OUQAKDVAIBzw%2BVFQEV1QLAAFVV1FcUVQBVQcFVARWBVcCDw4BUwEBAwA; ba1b8_winduser=CQEPVAEwDVNcAANWAwEFV1IBDwkFUVFcAQQOAwUDUwYEUFVRW14%2F; ba1b8_ck_info=%2F%09; ba1b8_lastvisit=0%091580038202%09%2Fthread.php%3Ffid-438-page-1.html; ba1b8_lastpos=F438; ba1b8_ol_offset=10282; ba1b8_ci=thread%091580038202%09%09438'
page_urls = []
for i in range(11, 39):
    url = f'http://www.jvcxp.org/thread-htm-fid-438-page-{i}.html'
    img_urls = get_imgs_urls(url, cookie_value)
    print(f'已经获取了第{i}页')
    page_urls = page_urls + img_urls
# 删除原有网址记录
path = 'temp/page_urls.py'
del_file(path)
# 写入网址
with open(path, 'a+', encoding="utf-8") as f:
    f.write('page_urls=[')
    for i in page_urls:
        f.write(f'\'{i}\',' + '\n')
    f.write(']')

print(page_urls)
