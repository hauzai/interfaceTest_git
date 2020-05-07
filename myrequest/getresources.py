from myrequest import myrequests
from myrequest.myerror import ResponseError


class GetResources(myrequests.myrequests):
    #home分支提交代码
    def __init__(self, resourcesCode, **kwargs):
        self.params = {"allocationTag": "0", "dictName": "data_group", "resourcesCode": resourcesCode}
        self.resourcesCode = resourcesCode
        self.url = "http://192.168.1.96:8092/code/systemPropertyResources/resourcesCode"
        self.kwargs = kwargs
        self.kwargs["params"] = self.params
        # data为查询到data数组
        self.data = None
        # response为调用run（）之后返回的response
        self.response = None

        super().__init__(url=self.url, **self.kwargs)



    def getresponse(self):
        return self.response.json()

    def getcustomName(self):
        # self.data = self.response.json()["data"]
        for i in self.data:
            print(i["id"]+" : "+i["customName"]+" : "+i["resource"])

    def search_sourceItem(self, **kwargs):
        if "id" in kwargs.keys():
            for i in self.data:
                if i["id"] == kwargs["id"]:
                    print(str(i))
        elif "customName" in kwargs.keys():
            for i in self.data:
                if i["customName"] == kwargs["customName"]:
                    print(str(i))
        else:
            print("输入错误")

    def run(self):
        super().run()
        if self.response:
            self.data = self.response.json()





if __name__ == "__main__":
    test = GetResources(resourcesCode="issuedPlanDN", headers={"token": "2100000000000000"})
    #print(test.getresponse())
    #print(test.getcustomName())
    #test.search_sourceItem(test="配属单位")
    #print(test.run())
    #test.getcustomName()
    #test.search_sourceItem(customName="公里标")
    print(test)
    test.run()
    print(test.data)