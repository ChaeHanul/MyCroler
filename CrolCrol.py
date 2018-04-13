import requests
from bs4 import BeautifulSoup

##전역으로 다룸
Malware_Type_Dictionary = {}
Malware_Name_list  = []
Malware_Type_list  = []
dict_Malware_Info_Page = {}

ahnlab_URL = 'http://www.ahnlab.com/kr/site/securityinfo/asec/asecCodeList.do?'


##악성코드 분석 정보 페이지 데이터 긁어옴
def get_Malware_Info_Page(dict_Malware_Info_Page,pageNum):
    req = requests.get(ahnlab_URL+'curPage='+pageNum)
    req_HTML = req.text
    dict_Malware_Info_Page[pageNum] = req_HTML
    
##악성코드 분석 정보에 있는 것 중 진단명만
def get_Malware_Name_list(Malware_Name_list,pageNum) :
    BS = BeautifulSoup(dict_Malware_Info_Page[pageNum],"html.parser")
    fProd_list = BS.select('[class~=fProd]')
    for item in fProd_list :
        item_split_list = item.string.split()
        try:
            Malware_Name_list.append(item.string.split()[0])
        except Exception as e:
            print(e)
            print("------------------------------")
            print("item is {0}".format(item.string))
            print("------------------------------")
            print("pageNum is {0}".format(pageNum))
    return len(fProd_list)

##악성코드 분석 정보에 있는 것 중 유형만
def get_Malware_Type_list(Malware_Type_list,pageNum) :
    BS = BeautifulSoup(dict_Malware_Info_Page[pageNum],"html.parser")
    bbsList = BS.select('[class~=bbsList]')
    tbody = bbsList.find('tbody')
    tr_list = tbody.find_all('tr')
    for tr_item in tr_list :
        try:
            Malware_Type_list.append(tr_item.get_text().split()[2])
            if item in Malware_Type_Dictionary is True :
                Malware_Type_Dictionary[item] += 1
            else :
                Malware_Type_Dictionary[item] = 1

        except Exception as e:
            print(e)
            print("------------------------------")
            print("item is {0}".format(item.string))
            print("------------------------------")
            print("pageNum is {0}".format(pageNum))
    return len(tr_list)
            

## Main 임
## 딕셔너리 값으로 들어가는 유형별 개수는 악성코드 실제 총 개수와 비교했을 때 덜 들어간게 있는가 파악하기 위한 용도로 씀
def Croler() :
    ###Malware_Type_Dictionary = {}
    Total_number_of_Malware_Type_item = 0
    ###dict_Malware_Info_Page 에 req.text 전부 저장
    print("starting load page to dict")
    for pageNum in range(1,3416):
        get_Malware_Info_Page(dict_Malware_Info_Page,pageNum)
    print("finishing")
    
    #for pageNum in range(1,3416):
        #get_Malware_Name_list(Malware_Name_list,str(pageNum))
    #   get_Malware_Type_list(Malware_Type_list,str(pageNum))
    #print("the number of Malware_Type_list is {0}".format(str(Total_number_of_Malware_Type_item)))
    #print("the number of Malwrae_Type_Dictionary is {0}".format(str(sum(Malware_Type_Dictionary.values()))))

if __name__ == "__main__" :
    Croler()
