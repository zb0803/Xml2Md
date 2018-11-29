#########################################################################
# 该脚本为将html或者xml文件转成md文件。脚本中使用html2text和chardet两个库，使用
# 该脚本时，需要安装以上两个库，库的安装方法：
# 
# Windows下安装脚本html2text:
#     pip install html2text --user
# 
# Windows下安装脚本chardet:
#     pip install chardef --user
# 
# 脚本的执行方法：
#     python Xml2Md.py
#########################################################################

import html2text
import os
import chardet

mdsuffix = ".md"


# 获取xml文件的编码格式
def getEncoding(xmlfile):
    with open(xmlfile, 'rb') as f:
        return chardet.detect(f.read())['encoding']

# Html转换成Markdown文件
def html2md(xmlpath, mdpath):
    encoding = getEncoding(xmlpath)

    html = open(xmlpath, "r", encoding=encoding, errors="ignore")
    
    markdowner = html2text.html2text(html.read())
    open(mdpath, "w", encoding=encoding).write(markdowner)

    print("Convert Successful: " + mdpath)

# 将某一个目录中的所有xml文件转换成md
def htmls2mds(xmldir, mddir):
    if not os.path.exists(mddir):
        os.mkdir(mddir)

    for file in os.listdir(xmldir):
        filepath = os.path.join(xmldir, file)
        
        # 获取文件后缀
        filename = os.path.splitext(file)
        splitext = os.path.splitext(filepath)
        if splitext[1] == '.xml' or splitext[1] == "html":
            mdpath = os.path.join(mddir, filename[0] + mdsuffix)
            html2md(filepath, mdpath)
            

## 执行转换代码
htmls2mds("E:\\0001-Ninebot\\0001-Codes\\8000-MiPlugins\\NewXmPluginSDK\\plugProject\\ninebot_scooter\\src\\main\\assets", "E:\\TestMd")
