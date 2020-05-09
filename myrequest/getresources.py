from myrequest import myrequests
from myrequest.myerror import ResponseError


class GetResources(myrequests.myrequests):
    # home分支提交代码
    def __init__(self, resourcesCode, **kwargs):
        # 固定查询条件
        self.__params = {"allocationTag": "0", "dictName": "data_group", "resourcesCode": resourcesCode}
        # 固定接口名称
        self.__interface = "/code/systemPropertyResources/resourcesCode"
        self.resourcesCode = resourcesCode
        self.kwargs = kwargs
        self.kwargs["params"] = self.__params
        # TODO 使用配置拼接url
        self.url = "http://192.168.1.96:8092" + self.__interface
        # data为查询到data数组
        self.data = None
        # 调用父类初始化方法
        super().__init__(url=self.url, **self.kwargs)
    def get_response(self):
        return self.response.json()
    # 获取id-自定义名称-名称-资源
    def get_name(self):
        # self.data = self.response.json()["data"]
        for i in self.data:
            print(i["id"] + " - " + i["customName"] + "-" + i["name"] + " - " + i["resource"])
    # 获取各字段 new - edit - detail status

    def get_status(self):
        print("id-customName:newStatus-editStatus-detailStatus")
        for i in self.data:
            # TODO 使用dict转换此处的数字和dictItem
            print(i['id'] + '-' + i['customName'] + ':' + str(i["newStatus"]) + '-' + str(i["editStatus"]) + '-' + str(i["detailStatus"]))

    def search_sourceItem(self, **kwargs):
        if len(kwargs) != 1:
            print("输入查询方法过多")
            return
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
            self.data = self.response.json()['data']


if __name__ == "__main__":
    test = GetResources(resourcesCode="issuedPlanDN", headers={"token": "2100000000000000"})
    # print(test.getresponse())
    # print(test.getcustomName())
    # test.search_sourceItem(test="配属单位")
    # print(test.run())
    # test.getcustomName()
    # test.search_sourceItem(customName="公里标")
    # print(test)
    test.run()
    # print(test.data)
    # test.search_sourceItem(id="12fdc9787ac445f8b4970b7e67a487ae")
    # test.get_name()
    test.get_status()
