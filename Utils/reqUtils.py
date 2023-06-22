import requests

class ReqUtils:
    mySession = requests.session()

    def  all_request(self,**kwargs):
        res = ReqUtils.mySession.request(**kwargs)
        return res