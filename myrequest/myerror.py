class MyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "自定义错误："+str(self.message)


class ResponseError(MyError):
    def __init__(self, message, statusCode):
        self.message = message
        self.statusCode = statusCode

    def __str__(self):
        return "提示信息："+str(self.message)+"\nstatuscode："+str(self.statusCode)