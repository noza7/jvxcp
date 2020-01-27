import os, random, re, time, requests


def create_dir(foldername):
    '''
    创建目录----- 判断当前文件夹下文件名是否存在，如果不存在就创建‘foldername’文件夹
    :param foldername:
    :return:
    '''
    if not os.path.exists(str(foldername)):
        os.mkdir(str(foldername))


def down_page(url):
    # 这个请求头是从网上搜来的，用于破解防盗链，测试没有问题！
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': 'http://www.jvcxp.org/index.php'
    }
    response = requests.get(url=url, headers=headers)
    data = response.content
    return data


def del_file(path):
    '''
    # 删除已有文件
    :param path: 文件路径
    :return:
    '''
    my_file = 'temp/paper_id.py'  # 文件路径
    if os.path.exists(path):
        os.remove(path)


def get_imgs_urls(url, cookie_value):
    '''
    获取图片链接
    :param url: 网址
    :param cookie_value: cookie值
    :return: 图片地址
    '''
    # 构造请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookie_value,
        'Host': 'www.jvcxp.org',
        'Referer': 'http://www.jvcxp.org/login.php?',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }

    # 打开1页
    r = requests.get(url, headers=headers)  # 发送请求
    r.encoding = r.apparent_encoding  # 设置编码格式为获取到的编码格式，这样不仅省去了猜测编码的环节，而且不会出错
    # 打印1页网页内容
    # print(r.text)
    # 利用正则表达式获取一页的所有链接
    img_link_re = '<a href="(.*?)" name="readlink" id="a_ajax_'
    img_urls = re.findall(img_link_re, r.text)
    # 统一加前缀获取完整网址
    img_urls = ['http://www.jvcxp.org/' + x for x in img_urls]
    # print(img_urls)
    return img_urls


def get_imgs(url, cookie_value):
    '''
    获取图片
    :param url: 网址
    :param cookie_value: cookie值
    :return:
    '''
    # 构造请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookie_value,
        'Host': 'www.jvcxp.org',
        'Referer': 'http://www.jvcxp.org/login.php?',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }

    # 打开1页
    r = requests.get(url, headers=headers)  # 发送请求
    r.encoding = r.apparent_encoding  # 设置编码格式为获取到的编码格式，这样不仅省去了猜测编码的环节，而且不会出错
    # 打印1页网页内容
    # print(r.text)
    # 利用正则表达式获取该页的文件名
    dir_name_re = '<title>(.*?)\|模拍私房 - 武当休闲山庄 - 稳定,和谐,人性化的中文社区</title>'
    dir_name = re.findall(dir_name_re, r.text)
    # 创建文件夹
    try:
        # 尝试创建目录
        foldername = f'pics/{dir_name}'
        create_dir(foldername=foldername)
    except Exception as e:
        # 如果创建目录失败，说明有特殊字符，用函数替换掉
        print(e)
        dir_name = replace_not_name_str(dir_name[0])
        foldername = f'pics/{dir_name}'
        create_dir(foldername=foldername)

    # 获取图片网址
    img_urls_re = '<img src="(.*?)" border="0" onclick="if'
    img_urls = re.findall(img_urls_re, r.text)
    # print(img_urls)
    # 保存文件
    for index, value in enumerate(img_urls):
        try:
            get_img = down_page(value)
        except Exception as e:
            print(e)
            with open('log.txt', 'a+', encoding="utf-8") as f:
                f.write(img_urls[index] + '\n')
            print('图片未下载！')
            continue
        with open(f'{foldername}/{index + 1}.jpg', 'wb') as fp:
            fp.write(get_img)
            print(f'正在下载<---{dir_name}图片--->第{index + 1}张')
        time.sleep(random.randint(1, 5))
    print(f'{url}---{dir_name}下载完毕！---------------------------------------')


def replace_not_name_str(dir_name):
    '''
    替换不能命名文件夹的特殊字符串
    :param dir_name: 文件夹名
    :return: 替换后的文件夹名
    '''
    not_name_str = '/\:*"<>|?'
    for i in dir_name:
        if i in not_name_str:
            dir_name_ = dir_name.replace(i, '-')

    return dir_name_
