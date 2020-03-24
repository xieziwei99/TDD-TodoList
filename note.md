## 准备环境
1. 下载firefox浏览器
2. 下载 geckodriver（仅有一个exe文件），将此文件放在(python安装目录)\Scripts目录下
    查看是否安装成功：`geckodriver --version`
3. 安装 virtualenv：运行命令`pip install virtualenvwrapper-win`
    如果网络不好，可以用国内镜像源：例如运行命令：
    `pip install virtualenvwrapper-win -i https://mirrors.aliyun.com/pypi/simple/`
    国内源：
    阿里云 https://mirrors.aliyun.com/pypi/simple/
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    豆瓣(douban) http://pypi.douban.com/simple/
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
4. 安装 Django，运行：`pip install "django < 1.12" -i https://mirrors.aliyun.com/pypi/simple/`
5. 安装 selenium（用作功能测），运行：`pip install "selenium < 4" -i https://mirrors.aliyun.com/pypi/simple/`

## 首次提交
1. 新建functional_test.py文件
2. 运行`django-admin startproject superlists`，新建项目
3. 进入目录运行`python manage.py runserver`，启动项目
4. 将functional_test.py移入superlists文件夹，运行`git init`命令
5. 新建.gitignore，将一些不必要的文件ignore
6. 运行`git add .`，运行`git status`查看
7. 运行`git rm -r --cached .\superlists\__pycache__`，移除一些不必要提交的，并将__pycache__和*.pyc加入gitignore（--cached表示不要删除源文件）
8. `git add .`, `git status`, `git commit`

## 第2次提交
1. 编写functional_test.py，更新一些代码