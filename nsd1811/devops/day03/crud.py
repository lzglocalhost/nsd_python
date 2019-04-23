from dbconn import Departments, Employees, Salary, Session

session = Session()
#############################
# hr = Departments(dep_id=1, dep_name='人事部')
# session.add(hr)
#############################
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# finance = Departments(dep_id=5, dep_name='财务部')
# ui = Departments(dep_id=6, dep_name='设计部')
# session.add_all([ops, dev, qa, finance, ui])
#############################
# yc = Employees(
#     emp_id=1,
#     emp_name='杨晨',
#     email='yc@163.com',
#     dep_id=2
# )
# zyp = Employees(
#     emp_id=2,
#     emp_name='郑云鹏',
#     email='zyp@163.com',
#     dep_id=2
# )
# lzj = Employees(
#     emp_id=3,
#     emp_name='李注江',
#     email='lzj@163.com',
#     dep_id=2
# )
# cyj = Employees(
#     emp_id=4,
#     emp_name='陈益建',
#     email='cyj@qq.com',
#     dep_id=1
# )
# hqp = Employees(
#     emp_id=5,
#     emp_name='黄勤品',
#     email='hqp@tarena.com',
#     dep_id=3
# )
# zds = Employees(
#     emp_id=6,
#     emp_name='赵东升',
#     email='zds@.tedu.cn',
#     dep_id=3
# )
# cd = Employees(
#     emp_id=7,
#     emp_name='陈栋',
#     email='cd@tedu.cn',
#     dep_id=4
# )
# session.add_all([yc, zyp, lzj, cyj, hqp, zds, cd])
#############################
query1 = session.query(Departments)  # 将class作为参数，返回实例
# print(query1)  # query1只是个sql语句
# deps = query1.all()  # 取出查询的全部结果
# print(deps)   # deps是由 数据库表每行记录生成的实例 构成的列表
# for dep in query1:
#     print(dep.dep_id, dep.dep_name)
#############################
query2 = session.query(Employees)
# for emp in query2:
#     print(emp.emp_id, emp.emp_name, emp.email)
#############################
# 将类变量作为参数，返回值是元组
query3 = session.query(Employees.emp_name, Employees.email)
# print(query3)
# print(query3.all())
# for name, email in query3:
#     print(name, email)
#############################
query4 = session.query(Employees).order_by(Employees.emp_id)
# print(query4)
# for emp in query4:
#     print(emp.emp_id, emp.emp_name, emp.email)
#############################
# 取切片时，涉及到了取值，所以query5不再是sql语句，而是实例构成的列表
query5 = session.query(Departments).order_by(Departments.dep_id)[2:5]
# print(query5)
for dep in query5:
    print(dep.dep_id, dep.dep_name)
#############################
session.commit()
session.close()
