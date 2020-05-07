from myrequest import myrequests


class GetResources(myrequests.myrequests):

    def __init__(self, url, method="GET", **kwargs):
        super().__init__(method=method, url=url, **kwargs)
        self.data = None
        self.response = super().run()

    def getresponse(self):
        return self.response.json()

    def getcustomName(self):
        self.data = self.response.json()["data"]
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

if __name__ == "__main__":
    test = GetResources(url="http://192.168.1.96:8092/code/systemPropertyResources/resourcesCode?resourcesCode=issuedPlanDN&allocationTag=0&dictName=data_group", headers={"token": "2100000000000000"})
    #print(test.getresponse())
    #print(test.getcustomName())
    #test.search_sourceItem(test="配属单位")
    print(test.run())
    test.getcustomName()
    test.search_sourceItem(customName="公里标")