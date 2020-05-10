def warpper_method(methoed):
    '''
    传入函数名，创建内置函数warpper,在warpper函数中调用传入的方法，并添加其他拓展操作
    :param methoed:
    :return:
    '''
    def warpper(*args, **kwargs):
        '''
        内置函数，执行传入的方法发并添加拓展操作
        :param args: 被拓展函数的参数
        :param kwargs: 被拓展函数的参数
        :return: 内置函数名
        '''
        print("包装方法")
        print(methoed.__name__)
        return methoed(*args, **kwargs)

    return warpper


@warpper_method
def func():
    print("原方法\n")


@warpper_method
def addfunc(x, y):
    '''
    @warpper_method装饰器的作用：
        warpper_method(method)方法，传入函数名，对函数进行拓展
    :param x:
    :param y:
    :return:
    '''
    return x + y


if __name__ == '__main__':
    func()
    print(addfunc(1, 2))
