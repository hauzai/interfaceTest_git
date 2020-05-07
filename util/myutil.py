import urllib.parse as pa

a = pa.urlparse("http://192.168.1.96:8092/jcw/produce/issuedPlan/issuedPlan/pages?orderBy=task_name+asc&pageSize=50&pageNo=1&authCode=LOOK_JCW_PLANMANAGE_TCDWRJH&planType=3&lineDegree=1" ,scheme="http")
print(a.query)
b = pa.parse_qs(a.query)
print(b["orderBy2"])