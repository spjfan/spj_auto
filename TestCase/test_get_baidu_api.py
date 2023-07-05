import pytest

from Utils import reqUtils,mysqlUtil

class TestGetApi:

    def test_get_baidu(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method = "get", url = url)
        print(url,res.status_code)

    def test_get_baidu_false(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method = "get", url = url)
        assert "123" == "456"

    @pytest.mark.smoke
    def test_get_from_database(self):
        data = mysqlUtil.MysqlUtil().get_requests_form_database("test_case","method","url", 2)
        print(data)
        # for i in data:
        #     res = reqUtils.ReqUtils().all_request(method = i[0],url = i[1])
        #     print(i[1],"-----------------------",res.status_code)
        #     assert res.status_code == 200

    # @pytest.mark.parametrize("id,method,url,n",mysqlUtil.MysqlUtil().get_data("test_case", 2))
    # def test_DDT(self):
    #     res = reqUtils.ReqUtils().all_request(method=method, url=url)
    #     print(i[1], "-----------------------", res.status_code)
    #     assert res.status_code == 200
