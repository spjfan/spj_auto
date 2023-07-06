import os

from Utils import reqUtils, mysqlUtil
from xToolkit import xfile


class TestGetApi:

    def test_get_baidu(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method="get", url=url)
        print(url, res.status_code)

    def test_get_excel_data(self):
        caseList = xfile.read(os.getcwd()+"/Data/excTestCase.xls").excel_to_dict()
        print(caseList)
        for t in caseList:
            resp = reqUtils.ReqUtils().all_request(url=t["url"], method=t["method"])
            print(t["url"], "+++++++++++++++++++++++++-----------------------", resp.status_code)
            assert resp.status_code == 200

    def test_get_baidu_false(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method="get", url=url)
        assert res.status_code == "456"

    # @pytest.mark.smoke
    def test_get_from_database(self):
        data = mysqlUtil.MysqlUtil().get_requests_form_database("test_case", "method", "url", 2)
        print(data)
        for i in data:
            res = reqUtils.ReqUtils().all_request(method=i[0], url=i[1])
            print(i[1], "-----------------------", res.status_code)
            assert res.status_code == 200



    # @pytest.mark.parametrize("id,method,url,n",mysqlUtil.MysqlUtil().get_data("test_case", 2))
    # def test_DDT(self):
    #     res = reqUtils.ReqUtils().all_request(method=method, url=url)
    #     print(i[1], "-----------------------", res.status_code)
    #     assert res.status_code == 200
