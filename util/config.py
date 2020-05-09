import configparser
# 生成config文件解析器
cf = configparser.ConfigParser()
# 读取config文件，此处使用绝对path，也可使用相对path
cf.read(r"D:\interfaceTest_git\config.ini")
# 展示配置文件中的所有section
print(cf.sections())
# get方法使用 sectionname，key 获取 value
print(cf.get('test', 'path'))

