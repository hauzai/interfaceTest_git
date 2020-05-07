import requests
from myrequest.myerror import ResponseError

class myrequests:

    def __init__(self, method="GET", url="", **kwargs):
        self.url = url
        self.kwargs = kwargs
        self.method = method
        self.response = None

    def __str__(self):
        return "url:"+self.url+"\nmethod:"+self.method+"\nkwargs:"+str(self.kwargs)

    def set_url(self, url):
        self.url = url

    def set_method(self, method):
        self.method = str(method).upper()

    def set_headers(self, headers):
        if "headers" in self.kwargs.keys():
            #self.kwargs["headers"] = headers
            self.add_headers(headers)
        else:
            self.kwargs["headers"] = headers

    def add_headers(self, dict_headers):
        if "headers" in self.kwargs.keys():
            for name in dict_headers.keys():
                if name in self.kwargs["headers"]:
                    print("header中值重复")
                    continue
                else:
                    self.kwargs["headers"][name] = dict_headers[name]
        else:
            self.set_headers(dict_headers)

    def run(self):
        try:
            response = requests.request(self.method, self.url, **self.kwargs)
            if response.status_code != 200:
                message = response.json()['msg']
                raise ResponseError(message=message, statusCode=response.status_code)
            else:
                self.response = response
        except ResponseError as e:
            print(e)




if __name__ == "__main__":
    test = myrequests(url="http://192.168.1.96:8092/comp/subject/lists?authCode=LOOK_SUBJECT_MANAGEMENT&parentId=0", headers = {"token": "2100000000000000"})
    test.set_headers({"token": "1"})
    test.run()