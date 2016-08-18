import re
import urllib.request
import os
import time


def get_html(url):
    #print("开始获取页面源代码...")

    # 隐藏python
    request = urllib.request.Request(url)
    request.add_header = [('user-Agent',
                           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36")]

    # 读取源代码
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")

    #print("源代码获取成功...")
    return html


def get_imglist(html):
    #print("开始获取图片地址...")

    r_img = r'((?:http)[^,]*cn\.bing\.net[^,]*1080[^,]*.(?:jpg|png))'  # 正则表达式
    p_img = re.compile(r_img)  # 正则编译

    imglist = p_img.findall(html)
    #for img in imglist:
        #print(img)
    #print("图片地址获取成功")
    return imglist


def save_pic(imglist):
    script_path = os.getcwd()
    path = script_path + "\\cnBingImage\\"
    bak_path = script_path + "\\cnBingImage_bak\\"
    name = path + "1.jpg"
    if not os.path.exists(path):
        #print("创建目录..." + path)
        os.makedirs(path)
    #print("开始下载图片...")
    for img in imglist:
        conn = urllib.request.urlopen(img)
        f = open(name, 'wb')
        f.write(conn.read())
        f.flush()
        f.close()
    copy_file(name, bak_path)
    #print("图片下载完成...")


def copy_file(name, todir):
    #print("备份文件开始...")
    old_file = open(name, 'rb')
    if not os.path.exists(todir):
        #print("创建目录..." + todir)
        os.makedirs(todir)
    new_file_name = today_date_str() + os.path.splitext(name)[1]
    new_file = open(todir + new_file_name, 'wb')
    new_file.write(old_file.read())
    old_file.flush()
    old_file.close()
    new_file.close()
    #print("备份文件结束..." + new_file_name)


def today_date_str():
    localtime = time.localtime(time.time())
    year = str(localtime[0])
    month = localtime[1]
    day = localtime[2]
    return year + ("" if (month / 10 > 1) else "0") + str(month) + ("" if (day / 10 > 1) else "0") + str(day)


def get_content():
    url = "http://cn.bing.com"
    html = get_html(url)
    # #print(html)
    image_urls = get_imglist(html)
    save_pic(image_urls)


if __name__ == "__main__":
    get_content()
