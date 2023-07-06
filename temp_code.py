from xToolkit import xfile
from Utils import reqUtils

testCaseList = xfile.read("./Data/excTestCase.xls").excel_to_dict()
print(testCaseList)
for i in testCaseList:
    print(type(i["method"]),i["method"],type(i["url"]),i["url"])
    res = reqUtils.ReqUtils().all_request(url = i["url"],method = i["method"])
    print(res.status_code)