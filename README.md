# cnbing-wallpaper
下载https://cn.bing.com/  每日壁纸..壁纸每天下载,且备份到本地,可以设置每天早上自动更换.
## 要求
 python3.5 (系统环境变量要配置), windows
## 使用
clone本项目到本地

### 手动执行(适用于单纯下载一次,或者测试下载)：
    点击run.bat可以直接执行。生成壁纸目录cnBingImage，以及备份目录
    
### 定时执行(完整的姿势)：
- 1 请严格将本程序clone到D盘根目录
- 2 点击task_install.bat，安装定时器
- 3 设置windows壁纸自动切换,壁纸路径指向D:\cnbing-wallpaper\cnBingImage

## 备注
 其实一直想用windows的包管理工具。终于此项目需要安装python3，于是在曾经失败尝试基础上再次尝试。终于上了Chocolatey 的车。
 
 [Chocolatey安装](https://chocolatey.org/install) 非常简单
 
 [Chocolatey配置关键点](https://www.cnblogs.com/ys-wuhan/p/6395417.html) 非常ok
 
 安装python3就这么简单  choco install python3
