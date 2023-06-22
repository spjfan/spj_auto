from Utils import reqUtils

class TestGetApi:

    def test_get_baidu(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method = "get", url = url)
        print(res.text)

    def test_get_baidu(self):
        url = "http://www.baidu.com"
        res = reqUtils.ReqUtils().all_request(method = "get", url = url)
        assert "123" == "456"