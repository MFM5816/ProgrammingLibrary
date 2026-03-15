from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/01-setcookie')
def setcookie():
    #构建响应对象
    resp = make_response('构建响应对象成功')
    #保存用户名密码到cookie
    resp.set_cookie('uname','laotao',60*60*24)
    resp.set_cookie('upwd','123456',60*60*24)
    return resp

@app.route('/02-getcookie')
def getcookie():
    if 'uname' in request.cookies:
        uname = request.cookies['uname']
    else:
        uname = '用户名不存在'
    upwd = request.cookies.get('upwd','密码为空')
    return '用户名:%s,密码%s' % (uname,upwd)

@app.route('/03-delcookie')
def delcookie():
    resp = make_response('删除cookie成功')
    if 'uname' in request.cookies:
         resp.delete_cookie('uname')
    return resp

@app.route('/04-login',methods=['GET','POST'])
def login_view():
    if request.method == 'GET':
        #判断 如果cookie中有uname
        if 'uname' in request.cookies:
        #判断 如果uname是admin
            uname = request.cookies.get('uname')
            if uname == 'admin':
            #响应字符串 '欢迎%s登录,<a href="#">退出</a>' % uname
                return '欢迎%s登录,<a href="/05-logout">退出</a>' % uname
        return render_template('04-login.html')
    elif request.method == 'POST':
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        if uname == 'admin' and upwd == 'tarena':
            resp = make_response('欢迎%s登录,<a href="/05-logout">退出</a>' % uname )
            if 'isSaved' in request.form:
                resp.set_cookie('uname',uname,60*60*24*31*3)
            return resp
        else:
            return '<script>alert("登录失败");location.href="/04-login";</script>'

@app.route('/05-logout')
def logout_view():
    if 'uname' in request.cookies:
        #创建响应对象
        resp = make_response('退出成功')
        #通过响应对象删除 uname的cookie
        resp.delete_cookie('uname')
        #返回响应对象
        return resp
    return '没有有效的用户'



if __name__ == '__main__':
    app.run(debug=True)