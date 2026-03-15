import math

from flask import Flask, request, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskDB"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)


class Users(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), nullable=False, unique=True)
  age = db.Column(db.Integer, nullable=True)
  email = db.Column(db.String(120), unique=True)
  phone = db.Column(db.String(11), unique=True)
  # python3 Run.py db init
  # python3 Run.py db migrate
  # python3 Run.py db upgrade


class Students(db.Model):
  __tablename__ = 'student'
  id = db.Column(db.Integer, primary_key=True)
  sname = db.Column(db.String(30), nullable=False)
  sage = db.Column(db.Integer, nullable=True)
  isActive = db.Column(db.Boolean, default=True)
  #对Student 和 Course的影响
  #在Student类中 增加属性courses表示对当前学生的所有课程的查询
  #在Course类中 增加属性students表示对学习当前课程的所有学员的查询
  #增加关联属性和反向引用关系属性 表示与Course的多对多关系
  courses = db.relationship(
      #指定多对多的另一个类
      'Course',
      #指定第三张关联表的名称
      secondary='student_course',
      backref=db.backref(
          #要加到Course中的
          #表示course对student的引用的属性名
          'students',
          lazy='dynamic',
      ),
      lazy='dynamic',
  )

# "多的实体类"
class Teacher(db.Model):
  __tablename__ = 'teacher'
  id = db.Column(db.Integer, primary_key=True)
  tname = db.Column(db.String(30), nullable=False)
  tage = db.Column(db.Integer, nullable=True)
  course_id = db.Column(
    db.Integer,
    db.ForeignKey('course.id')
  )
  # 增加一个关联属性 表示要引用的wife的信息
  #关联属性在Teacher中要增加哪个属性 用来表示对Wife的引用
  #反向引用关系属性 在Teacher中设置 但是要添加到Wife中的属性 表示在Wife中要增加哪个属性表示对Teacher的引用
  wife = db.relationship(
    "Wife",
    backref='teacher',
    uselist = False
  )

# "一的实体类"
class Course(db.Model):
  __tablename__ = 'course'
  id = db.Column(db.Integer, primary_key=True)
  cname = db.Column(db.String(30), nullable=False)
  # 增加对Teacher的关联属性和反向引用关系属性
  teachers = db.relationship(
    "Teacher",
    backref='course',
    lazy='dynamic'
    )

#创建类 StudentCourse
class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    id = db.Column(db.Integer,primary_key=True)
    #外键 student_id 引用student表的主键
    student_id = db.Column(
      db.Integer,
      db.ForeignKey('student.id')
    )
    # 外键 course_id 引用course表的主键
    course_id = db.Column(
      db.Integer,
      db.ForeignKey('course.id')
    )





class Wife(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  wname = db.Column(db.String(30), unique=True)
  teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), unique=True)

@app.route('/01-add')
def add_view():
  # 创建实体类对象
  user = Users()
  # 对对象属性赋值
  user.username = 'WWC'
  user.age = 30
  user.email = 'wwc@tedu.cn'
  user.phone = '13012345678'
  # 将User对象保存到数据库
  db.session.add(user)
  db.session.commit()
  return '添加数据成功'

@app.route('/02-reg', methods=['GET', 'POST'])
def reg_view():
  if request.method == 'GET':
    return render_template('register.html')
  elif request.method == 'POST':
    user = Users()
    user.username = request.form.get('uname')
    user.age = int(request.form.get('age'))
    user.email = request.form.get('email')
    user.phone = request.form.get('phone')
    db.session.add(user)
    db.session.commit()
    return '注册用户成功!'

@app.route('/03-query')
def query_view():
  # 查询Users实体类中的id和username
  # query = db.session.query(Users.id,Users.username)
  # print(query)
  # print('type',type(query))

  # 查询用户表中的所有数据
  # users = db.session.query(Users).all()
  # print(users)
  # for u in users:
  #     print('id:%s,用户名:%s,年龄:%d,邮箱:%s,手机:%s' % (u.id,u.username,u.age,u.email,u.phone))

  # user = db.session.query(Users).first()
  # print(user)
  # print(type(user))
  # print('id:%s,用户名:%s,年龄:%d,邮箱:%s,手机:%s' % (user.id, user.username, user.age, user.email, user.phone))
  # student = db.session.query(Students).first()

  # first_or_404() 使用方式 同first
  # 如果没有查询到数据 响应404
  # student = db.session.query(Students).first_or_404()
  # print(student)

  # count = db.session.query(Users).count()
  # print('共有%d条数据' % count)
  return '查询成功'

@app.route('/04-filter')
def filter_view():
  # 查询年龄大于25的users信息
  # result = db.session.query(Users).filter(Users.age>25).all()
  # print(result)
  # 查询id为2的users的信息
  # result = db.session.query(Users).filter(Users.id==2).first()
  # result = db.session.query(Users).filter_by(id=2).first()
  # print('id为2的用户是:%s' % result.username)

  # 查询username中包含 王 的用户信息
  # select * from users where username like '%王%'
  # users = db.session.query(Users).filter(Users.username.like('%王%')).all()
  # print(users)
  # 查询email中包含w的Users信息
  # users = db.session.query(Users).filter(Users.email.like('%w%')).all()
  # print(users)

  # 查询查询email中包含w同时年龄小于等于30的users
  # 使用多个filter查询 fiter().filter()
  # users = db.session.query(Users).filter(Users.email.like('%w%')).filter(Users.age<=30).all()
  # print(users)
  # 使用filter(条件1,条件2...)
  # users = db.session.query(Users).filter(
  #   Users.email.like('%w%'),
  #   Users.age <= 30
  # ).all()
  # print(users)

  # 查询年龄小于30 或 邮箱中包含tedu的用户
  # from sqlalchemy import or_
  # 使用or_函数
  # result = db.session.query(Users).filter(
  #   or_(
  #     Users.age<30,
  #     Users.email.like("%tedu%")
  #   )
  # ).all()
  # print(result)

  # 查询年龄是5 或 20 或40 的users
  # 模糊查询 in
  # result = db.session.query(Users).filter(
  #   Users.age.in_([5,20,40])
  # ).all()
  # print(result)

  # 查询年龄在20~40之间的users
  # 模糊查询 between and
  # result = db.session.query(Users).filter(
  #   Users.age.between(20,40)
  # ).all()
  # print(result)

  return '查询成功'

@app.route('/05-users')
def users_view():
  # 获取关键字
  if 'kw' in request.args:
    kw = request.args.get('kw')
    # 通过关键字去 Users表中查询
    # username 或 email 包含关键字的对象
    # users = db.session.query(Users).filter(
    #   or_(
    #     Users.username.like('%' + kw + '%'),
    #     Users.email.like('%' + kw + '%')
    #   )
    # ).all()
    users = Users.query.filter(
      or_(
        Users.username.like('%' + kw + '%'),
        Users.email.like('%' + kw + '%')
      )
    ).all()
  return render_template('users.html', params=locals())

@app.route('/06-limit')
def limit_view():
  users = db.session.query(Users).limit(2).offset(2).all()
  print(users)
  return '查询成功'

@app.route('/07-page')
def page_view():
  # 每页显示的数据数量
  pageSize = 2
  # 当前页数 默认1
  currentPage = int(request.args.get('currentPage', 1))
  # 总数量
  totalCount = db.session.query(Users).count()
  # 最大页数
  lastPage = math.ceil(totalCount / pageSize)
  # 查询当前页的数据
  # 跳过(当前页 - 1) * pageSize条数据
  # 再获取pageSize条数据
  users = db.session.query(Users).offset((currentPage - 1) * pageSize).limit(pageSize).all()

  # 计算上一页的页码
  # 如果当前页大于1 上一页就是当前页-1 否则就是1
  prevPage = 1
  if currentPage > 1:
    prevPage = currentPage - 1

  # 计算下一页的页码
  # 如果当前页不是lastPage 下一页就是当前页+1 否则就是lastPage
  nextPage = lastPage
  if currentPage < lastPage:
    nextPage = currentPage + 1
  return render_template('page.html', params=locals())

@app.route('/08-order')
def order_view():
  # 将所有用户按照年龄降序排序
  result = db.session.query(Users).order_by('id').all()
  print(result)
  return '查询成功'

@app.route('/09-update')
def update_view():
  # 修改id为2的用户名为石博文
  # user = db.session.query(Users).filter_by(id=2).first()
  # user = db.session.query(Users).filter(Users.id==2).first()

  # user = Users.query.filter_by(id=2).first()
  # user.username = '石博文'
  # db.session.add(user)
  # db.session.commit()
  # return '修改成功'
  user = Users.query.filter_by(username='赵金多').first()
  db.session.delete(user)
  db.session.commit()
  return '删除成功'

@app.route('/10-upuser', methods=['GET', 'POST'])
def upuser_view():
  if request.method == 'GET':
    return render_template('upuser.html')
  elif request.method == 'POST':
    id = int(request.form.get('id'))
    user = Users.query.filter_by(id=id).first()
    if user:
      user.username = request.form.get('username')
      user.age = int(request.form.get('age'))
      user.email = request.form.get('email')
      user.phone = request.form.get('phone')
      db.session.add(user)
      db.session.commit()
      return '修改成功'
    else:
      return '修改失败 用户不存在'

@app.route('/11-regtea')
def regtea_view():
  # teaTao = Teacher()
  # teaTao.tname = '魏老师'
  # teaTao.tage = 35
  # teaTao.course_id = 1
  # db.session.add(teaTao)

  # course = Course.query.filter_by(cname='Python高级').first()
  # teaLv = Teacher()
  # teaLv.tname = '吕老师'
  # teaLv.tage = 30
  # teaLv.course_id = course.id
  # db.session.add(teaLv)

  course = Course.query.filter_by(cname='Python基础').first()
  teaZhao = Teacher()
  teaZhao.tname = '赵老师'
  teaZhao.tage = 30
  # 底层实际上是将course.id给了teaZhao.course_id属性
  teaZhao.course = course
  db.session.add(teaZhao)
  db.session.commit()
  return '添加成功'

@app.route('/12-otm', methods=['GET', 'POST'])
def otm_view():
  if request.method == 'GET':
    course = Course.query.all()
    return render_template('regtea.html', params=locals())
  elif request.method == 'POST':
    # 接收前端提交的参数
    tname = request.form.get('tname')
    tage = request.form.get('tage')
    cid = request.form.get('cid')
    # 创建对象
    tea = Teacher()
    # 添加属性
    tea.tname = tname
    tea.tage = tage
    tea.course_id = cid
    # 提交到数据库
    db.session.add(tea)
    db.session.commit()
    return '注册成功'

@app.route('/13-otm-query')
def otm_query():
  # 查找课程id为3的所有的老师
  # course = Course.query.filter_by(id=3).first()
  # #通过关联属性
  # teachers = course.teachers.all()
  # # print(teachers)
  # for tea in teachers:
  #     print('姓名:%s,年龄:%d' % (tea.tname,tea.tage))

  # 查找魏老师所授课程
  tea = Teacher.query.filter_by(tname='魏老师').first()
  cour_name = tea.course.cname
  print('魏老师所授课程为:', cour_name)
  return '查询成功'

@app.route('/14-oto')
def oto_view():
    #为王老师添加一个Wife
    wife = Wife()
    wife.wname = '陶夫人'
    laowang = Teacher.query.filter_by(tname='陶老师').first()
    # wife.teacher_id = laowang.id
    wife.teacher = laowang
    db.session.add(wife)
    db.session.commit()
    return '添加成功'
#创建数据库flaskDB 删除migrations
#python3 Run.py db init
#python3 Run.py db migrate
#python3 Run.py db upgrade
#添加课程
# @app.route('16-addcor')
# def addcor():
#     cor = Course()
#     cor.cname = 'python基础'
#     db.session.add(cor)
#     db.session.commit()
#     return '添加成功'
#运行/12-otm添加教师
#运行/14-oto添加wife

@app.route('/15-oto-query')
def oto_query():
    # laotao = Teacher.query.filter_by(tname='陶老师').first()
    # print(laotao.wife.wname)
    all_teachers = Teacher.query.all()
    for t in all_teachers:
        print('%s的妻子是%s' % (t.tname,t.wife.wname))
    return '查询成功'

@app.route('/16-mtm')
def mtm_view():
    # stu1 = Students()
    # stu1.sname = 'HanMeimei'
    # stu1.sage = '20'
    # stu1.isActive = True
    # db.session.add(stu1)
    # db.session.commit()
    # stu1 = Students.query.filter_by(id=2).first()
    # cor1 = Course.query.filter_by(id=2).first()
    # stu1.courses = [cor1]

    #查询
    # stu = Students.query.filter_by(id=3).first()
    # for c in stu.courses:
    #     print('课程名称:',c.cname)

    # cor = Course.query.filter_by(cname='pythonWEB').first()
    # for s in cor.students:
    #     print('学生姓名:',s.sname)

    #删除
    #通过关联属性/反向引用关系属性.remove(对象)
    cor = Course.query.filter_by(cname='pythonWEB').first()
    stu = Students.query.filter_by(id=1).first()
    cor.students.remove(stu)
    db.session.add(cor)
    db.session.commit()

    return '成功'

@app.route('/17-regmtm',methods=['GET','POST'])
def regmtm_view():
    if request.method == 'GET':
        students = Students.query.all()
        courses = Course.query.all()
        return render_template('mtm.html',params=locals())
    elif request.method == 'POST':
        #接受前端提交的数据
        #为学生添加课程
        #如果课程存在的话 提示
        stu_id = request.form.get('stu')
        cor_id = request.form.get('cor')
        student = Students.query.filter_by(id=stu_id).first()
        course = Course.query.filter_by(id=cor_id).first()
        if course not in student.courses:
            # student.courses.append(course)
            # sc = StudentCourse()
            # sc.student_id = stu_id
            # sc.course_id = cor_id
            # db.session.add(sc)
            course.students.append(student)
            db.session.commit()
        else:
            return '已选择过该课程'
        return '课程选择成功'


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()
