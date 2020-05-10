import configparser


def get_dictitem4config(dictname, code: str):
    cf = configparser.ConfigParser()
    cf.read(r"..\dictconfig.ini", encoding="utf-8")
    try:
        return cf.get(section=dictname, option=code)
    except Exception as e:
        print(e)
        return code


if __name__ == '__main__':
    # print(configparser.ConfigParser().read(r"..\dictconfig.ini",encoding="utf-8"))
    print(get_dictitem4config('newStatus',"1"))