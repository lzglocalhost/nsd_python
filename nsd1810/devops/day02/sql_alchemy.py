from dbconn import Departments, Employees, Session

session = Session()  # 创建会话类的实例
# hr = Departments(dep_id=1, dep_name='人事部')
# session.add(hr)
# dev = Departments(dep_id=2, dep_name='开发部')
# ops = Departments(dep_id=3, dep_name='运维部')
# market = Departments(dep_id=4, dep_name='市场部')
# finance = Departments(dep_id=5, dep_name='财务部')
# session.add_all([dev, ops, market, finance])
####################################
# dzh = Employees(
#     emp_id=1,
#     emp_name='董志华',
#     birth_date='1993-9-4',
#     email='dzh@qq.com',
#     dep_id=2
# )
# zc = Employees(
#     emp_id=2,
#     emp_name='郑聪',
#     birth_date='1992-4-10',
#     email='zc@qq.com',
#     dep_id=2
# )
# fxq = Employees(
#     emp_id=3,
#     emp_name='方兴清',
#     birth_date='1995-8-22',
#     email='fxq@163.com',
#     dep_id=3
# )
# mca = Employees(
#     emp_id=4,
#     emp_name='莫成安',
#     birth_date='1990-6-29',
#     email='mca@qq.com',
#     dep_id=1
# )
# rwj = Employees(
#     emp_id=5,
#     emp_name='任武杰',
#     birth_date='1995-1-12',
#     email='rwj@126.com',
#     dep_id=2
# )
# session.add_all([dzh, zc, fxq, mca, rwj])
#############################################
# qset1 = session.query(Departments)
# print(qset1) # 此时qset1只是一条sql语句，向qset1取值时，才真正的查询数据库
# print(qset1.all())  # 返回departments表中所有记录组成的对象集合
# for dep in qset1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#############################################
# qset2 = session.query(Departments).order_by(Departments.dep_id)
# print(qset2)
# for dep in qset2:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#############################################
# qset3 = session.query(Employees.emp_name, Employees.email)
# print(qset3)
# for item in qset3:
#     print(item)  # 查询指定字段，返回的是元组
# for name, email in qset3:
#     print('%s: %s' % (name, email))
#############################################
# qset4 = session.query(Departments.dep_name.label('部门'))
# for dep in qset4:
#     print(dep.部门)
#############################################
# qset5 = session.query(Departments).order_by(Departments.dep_id)[2:4]
# print(qset5)
# for dep in qset5:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#############################################
qset6 = session.query(Departments).filter(Departments.dep_id==1)
print(qset6)
for dep in qset6:
    print('%s: %s' % (dep.dep_id, dep.dep_name))

session.commit()
session.close()
