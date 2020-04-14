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

## 第3次提交
1. 新建一个lists app: `python .\manage.py startapp lists`
2. 编写lists/tests.py，写一个单元测试
3. 运行`python .\manage.py test`，查看单元测试是否成功
4. git commit

## 第4次提交
1. 关于Django的MVC：
    1. Django中MVC的概念与一般认为的MVC不一样，Django中的Model就是M，但Django中用View代表C，用Template代表V
    2. 所以Django中的是：MTV设计模式
2. 更改lists/tests.py，并运行单元测试`python .\manage.py test`
3. 编写 lists/views.py，增加home_page变量，代表view
4. 编写superlists/urls.py，增加从"/"到lists.views.home_page的映射
5. 更改lists/views.py，将变量home_page改为函数home_page，真正代表view
6. git commit -am "First unit test and url mapping, dummy view"

## 第5次提交
1. 编写lists/tests.py，增加测试，判断访问主页是否返回了正确的html，运行测试，预料的失败
2. 为了使测试通过，更改 lists/views.py 中 home_page 方法，再次运行测试，成功
3. 运行 python manage.py runserver，此时打开 http://127.0.0.1:8000/ 可以看到主页
4. git commit -am "简单的网页"

## 第6次提交
1. 编写 functional_test.py ，增加一些用户故事
2. git commit -am "增加功能测：可以输入 to-do item"

## 第7次提交
1. 单元测不测内容，要测逻辑，控制流，配置信息
2. 新建 lists\templates\home.html 模版文件，编写
3. 更改 lists\views.py ，返回编写好的模版
4. 编写 superlists\settings.py ，向 Django 注册 lists app
5. 更改 lists\tests.py ，用 Django Test Client 改进单元测
6. 重构的过程不能添加新的功能
7. 提交 使用模版重构主页