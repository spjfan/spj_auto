from Utils import reqUtils,mysqlUtil

class TestGetApi:

    def test_get_baidu(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method = "get", url = url)
        print(res.text)

    def test_get_baidu_false(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method = "get", url = url)
        assert "123" == "456"

    def test_get_from_database(self):
        data = mysqlUtil.MysqlUtil().get_data("test_case", 3)

        for i in data:
            res = reqUtils.ReqUtils().all_request(method = i[2],url = i[1])
            print(i[1],"-----------------------")