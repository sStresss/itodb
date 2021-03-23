from datetime import datetime
import os
import pymysql
import time

SqlHostname = ''
SqlPort = 0
SqlUserName = ''
SqlPwd = ''
SqlDBName = 'itodb'
SqlConCheck = False
SqlConStateTxt = ''
SqlFirstConnectUpdate = False
checkFirstConn = True

specName = ''

# path = str(os.getcwd())
# path = path.replace("\\", "/") + "/"
globalSource = ''
globalSpecSource = ''
globalDocSource = ''
localSpecSource = ''
globalPhotosource = ''
globalTranSource = ''
globalNetConfSource = ''
globalExelDataTableSourse = ''

#флаг для события нажатия дерева для функции генерации контекста
checkTreeClicked = False
treeParentNameByRightClick = ''


#пдф файл спецификации
SpecPath = ''
checkSpeckPath = False
checkSpeckOpenBoxCancel = False
checkOpenSpecFromGlobalStat = False


MesResult = False
MesText = ""

DialogRes = False
DialogText = ""
DialogHeadText = ""

checkThOTableUpdate = False
checkOTblUpdateEvent = False

checkVScrollOTblError = False

AddNewObjResult = False
NewObjName = ''

OTblCurrRow = ""
OTblCurrCol = ""
OTblCurrID = 0
OTblCurrFactObj = ""
OTblCurrTypeObj = ""
OTblCurrModelObj = ""
OTblCurrSerialNumObj = ""
OTblCurrMakerObj = ""
OTblCurrDistributorObj = ""
OTblCurrInputDateObj = ""
OTblCurrTargetObj = ""
OTblCurrTransferDateObj = ""
OTblCurrComment = ""
#групповой режим таблицы ostuff
checkGroupOTbl = False
otbl_selected_lst = []
#групповой режим таблицы kstuff
checkGroupKTbl = False
ktbl_selected_lst = []
#рефреш таблицы по выборке объекта
checkTreeUpdateEvent = False
checkTreeReBuild = False
checkTreeUpdEvOTbl = False
checkTreeUpdEvKTbl = False

#флаги очереди выполнения операций
CHECK_TREE_UPDATE = False
CHECK_OTBL_UPDATE = False
CHECK_KTBL_UPDATE = False

#счетчик потоков
TH_OBJ_COUNTER = 0

checkOTblWasClicked = False
checkTreeFocusInTransfer = False

checkGlobalviewMode = False

checkOStuffReservViewMode = False
checkOTblReservUpdateEvent = False

TreeParentName = ''
pTreeParentName = ''

StopAll = False

checkLoad = False

#-------------------------------------------------

checkThKTableUpdate = False

checkThKTableUpdate = False
checkKTblUpdateEvent = False

checkVScrollOTblError = False

KTblCurrRow = ""
KTblCurrCol = ""
KTblCurrID = 0
KTblCurrFactObj = ""
KTblCurrTypeObj = ""
KTblCurrModelObj = ""
KTblCurrSerialNumObj = ""
KTblCurrMakerObj = ""
KTblCurrDistributorObj = ""
KTblCurrInputDateObj = ""
KTblCurrTargetObj = ""
KTblCurrTransferDateObj = ""
KTblCurrComment = ""

checkKTblWasClicked = False
checkKStuffResrvViewMode = False
treeUpdate = False
checkTreeStatesUpdate = False

#флаг для вызова формы журнала по выделенному оъекту
checkTargetHystory = False
checkWichTblWasClicked = False

#массив для выгрузки статистики
CurrStatArray = []

#тест причины удаления
checkDelComment = False
DelReasonComment = ""

#группы доступа
UserName = ''
AccesGroup = ''

#таблица статистики
checkGlobStatTblUpdateEvent = False
checkStopGlobStatThread = False

#=====================global stat=================================
STblCurrRow = ""
STblCurrCol = ""

STblCurrTypeObj = ""
STblCurrModelObj = ""
STblCurrNumBySpec = ""
STblCurrNumByFact = ""
STblCurrComment = ""


def Hystory(User, Type, Serial, Event):
    now = datetime.now()
    loctime = now.strftime("%d/%m/%Y %H:%M:%S")
    locHostName = str(SqlHostname)
    locPort = int(SqlPort)
    locUserName = str(SqlUserName)
    locPwd = str(SqlPwd)
    locDBName = str(SqlDBName)
    con = pymysql.connect(host=SqlHostname,
                          port=SqlPort,
                          user=SqlUserName,
                          passwd=SqlPwd,
                          db=SqlDBName)
    with con:
        cur = con.cursor()
        cur.execute("SELECT ID FROM hystory")
        rows = cur.fetchall()
        #
        OID = 1
        if (len(rows) != 0):
            for row in reversed(rows):
                try:
                    OID = str(int(row[0]) + 1)
                except:
                    print("OID Error!!!")
                break

        query = (
            "INSERT INTO hystory (ID, DateEvent, userName, TypeObj, SerialNum, EventObj) VALUES (%s, %s, %s, %s, %s, %s )")
        cur.execute(query, (
        OID, loctime, User, Type, Serial, Event))
        con.commit()
    con.close()