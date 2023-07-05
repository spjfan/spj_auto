import pytest

from Utils import mysqlUtil, reqUtils

@pytest.mark.parametrize('tmethod,turl',list(mysqlUtil.MysqlUtil().get_requests_form_database("test_case","method","url", 2)))
def get_from_database(method,url):
    print(mysqlUtil.MysqlUtil().get_requests_form_database("test_case","method","url", 2))
    res = reqUtils.ReqUtils().all_request(method = method, url = url)
    assert res.status_code == 200

# def get_data():
#     res = mysqlUtil.MysqlUtil().get_requests_form_database("test_case","method","url",4)
#     print(list(res),type(res))

if __name__ == '__main__':
    get_from_database()