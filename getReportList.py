# encoding:utf-8
import time
import os
import sys
import zipfile
from main.SQlitDB import connect_db

reportPath = 'G:/reportServer/'             # 测试报告HTML存放位置
reportNum = 0                               # 当前目录下的测试报告总数
tmpNum = 0                                  # 测试报告临时总数，用来判断当前获取到的报告数量
strHttpServer = "192.168.22.171"            # 环境配置，服务器
ServerPort = "8080"                         # 环境配置，服务器
htmlFileName = "test_report.html"           # 测试报告的入口HTML文件：http://192.168.22.171:8080/XX/test_report.html
DownLoadFilePath = "download/"              # 下载的路径：http://192.168.22.171:8080/download/XX.zip
ShowFilePath = "show/"                      # 下载的路径：http://192.168.22.171:8080/download/XX.zip
conn = connect_db()                         # 初始化数据库连接
ReportSaveDays = 30                         # 报告保存时间，30会主动删除30天前的数据库报告

# 每次运行该程序，将会先从数据库读取一次库里的报告信息
# 用来避免已经存在的报告重复加入数据库。
reportAll = conn.selectfromtable("reportList", "reportName")
reportAllListTmp = reportAll.fetchall()
# 取出来的是元组，转换成string
reportAllList = []
for re in reportAllListTmp:
    reportAllList.append(re[0])

# print reportAllList
# print reportAllList[1]
# print type(reportAllList[1])
# sys.exit()


# 查询指定目录下的文件，并且排序
def get_file_list(file_path, need='.zip'):
    dir_list = []
    tmp_dir_list = os.listdir(file_path)
    # print tmp_dir_list
    if not tmp_dir_list:
        return dir_list
    else:
        # 去除非*.zip的
        for iDirList in tmp_dir_list:
            if need not in iDirList:
                continue
            else:
                dir_list.append(iDirList.split('.')[0])
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x + ".zip")))
        print dir_list
        return dir_list

while 1:
    lis = get_file_list(reportPath + DownLoadFilePath)
    tmpNum = len(lis)
    if tmpNum > reportNum:
        print '- find some new files'
        chaNum = tmpNum - reportNum
        try:
            for i in range(chaNum):
                # 如果已经存在的话，那么不写入
                tmpName = lis[tmpNum - 1 - i]
                if tmpName in reportAllList:
                    print tmpName, ' Already in db, continue.'
                    continue
                else:
                    # 写入“报告名称，入库当前时间，服务器IP 端口号”
                    value = "'" + tmpName + "','" + str(time.strftime("%Y-%m-%d %H:%M:%S")) + "','" +\
                            "http://" + strHttpServer + ":" + ServerPort + "'"
                    addFlag = conn.Addtotable('reportList', value, 'reportId')
                    if addFlag:
                        print "Successe add file to db end, Now we'll unzip it"
                        zipfilePath = reportPath + DownLoadFilePath + tmpName + ".zip"
                        f = zipfile.ZipFile(zipfilePath, 'r')
                        for fileTmp in f.namelist():
                            f.extract(fileTmp, reportPath + ShowFilePath)
                    else:
                        tmpStr = "Failed while adding the report " + tmpName + ".zip Info. into the db"
                        raise Exception(tmpStr)
        except Exception, e:
            print e
            break
        reportNum = tmpNum
        time.sleep(3)
        # break
    else:
        print '- not have new files'
        time.sleep(3)

