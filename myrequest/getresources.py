from typing import Dict, Any, Union

from myrequest import myrequests
from util import config, getdictitem
from myrequest.myerror import ResponseError


class GetResources(myrequests.myrequests):

    # home分支提交代码
    def __init__(self, environment, resourcescode, **kwargs):
        # 固定查询条件
        self.__params = {"allocationTag": "0", "dictName": "data_group", "resourcesCode": resourcescode}
        # 固定接口名称
        self.__interface = "/code/systemPropertyResources/resourcesCode"
        self.resourcesCode = resourcescode
        self.kwargs = kwargs
        self.kwargs["params"] = self.__params
        # DO 使用配置拼接url
        self.url = config.get_url(str(environment)) + self.__interface
        # data为查询到data数组
        self.data = None
        # 调用父类初始化方法
        super().__init__(url=self.url, **self.kwargs)
        self.run()

    def get_response(self):
        return self.response.json()

    # 获取id-自定义名称-名称-资源
    def get_name(self):
        # self.data = self.response.json()["data"]
        for i in self.data:
            print(i["id"] + " - " + i["customName"] + "-" + i["name"] + " - " + i["resource"])

    # 获取各状态字段 new - edit - detail status

    def get_status(self):
        print("id-customName:newStatus-editStatus-detailStatus")
        for i in self.data:
            # DO 使用dict转换此处的数字和dictItem
            print(i['id'] + '-' + i['customName'] + ':' + getdictitem.get_dictitem4config("newStatus",
                                                                                          str(i['newStatus']))
                  + '-' + getdictitem.get_dictitem4config("editStatus",
                                                          str(i["editStatus"])) + '-' + getdictitem.get_dictitem4config(
                "detailStatus", str(i["detailStatus"])))

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
    test = GetResources(environment=96, resourcescode="issuedPlanDN", headers={"token": "2100000000000000"})
  #  test.run()
    test.get_status()
