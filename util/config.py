import configparser
#  生成config文件解析器
# cf = configparser.ConfigParser()
#  读取config文件，此处使用相对路径
# cf.read(r"..\config.ini")
#  展示配置文件中的所有section
# print(cf.sections())
#  get方法使用 sectionname，key 获取 value
# print(cf.get('96', 'ip'))

def get_url(section):
    cf = configparser.ConfigParser()
    cf.read(r"..\config.ini")
    return r"http://"+cf.get(section,"ip")+":"+cf.get(section,"port")

if __name__ == '__main__':
    print(get_url('96'))