import tkinter as tk
from tkinter.messagebox import *
import pymysql

def sql_information(sql):
    connection = pymysql.connect(host='localhost', user='root', password='zys@010717', database="stu_dbms")
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        user_information = cursor.fetchall()
    except Exception as e:
        print(e)
        showerror(message = "查询失败！")
    finally:
        if connection:
            cursor.close()
        if cursor:
            connection.close()
    return user_information

def showStudent(right,width):
    student_information = sql_information('select * from student')
    head_string = ('学号', '姓名', '性别', '年龄', '班号')
    for i in range(len(student_information[0])):
        studentlist = tk.Listbox(right, width=width, height=20, bd=4, relief='flat')
        studentlist.pack(side='left', fill='both')
        studentlist.insert('end', head_string[i])
        for each in student_information:
            studentlist.insert('end', each[i])

def main_page():
    ## window.destroy()
    window_main_page = tk.Tk()
    window_main_page.geometry('950x500')
    window_main_page.title('管理员页面')
    window_main_page.resizable(0,0)

    tk.Label(window_main_page,text='学生管理系统操作页面',bg='grey',font=('华文黑体', 26,"bold")).pack()

    left = tk.LabelFrame(window_main_page,text='学生信息增删改', font=('华文黑体', 16,"bold"), width=200, height=400, padx=10, pady=80)
    left.pack(side='left')
    right = tk.LabelFrame(window_main_page,text='学生信息查询', font=('华文黑体', 16,"bold"), width=700, height=400,padx=10, pady=10)
    right.pack(side='right')

    ## 前后端交互的数据
    deleteNo = tk.IntVar()
    selectNo = tk.IntVar()
    insertNo = tk.IntVar()
    insertName = tk.StringVar()
    insertSex = tk.StringVar()
    insertAge = tk.IntVar()
    insertCno = tk.IntVar()
    updateNo = tk.IntVar()
    updateName = tk.StringVar()
    updateSex = tk.StringVar()
    updateAge = tk.IntVar()



    ## 查询学生信息———输入学号————连接sql后端————前端展示查询结果
    def selectData():
        selNo = selectNo.get()
        sql = """SELECT * FROM Student WHERE Sno = "{selNo}" """.format(selNo=selNo);
        res = sql_information(sql)
        window_select = tk.Toplevel(window_main_page)
        window_select.geometry('400x80')
        window_select.resizable(0,0)
        window_select.title('查询结果')
        head_string = ('学号', '姓名', '性别', '年龄', '班号')
        for i in range(len(res[0])):
            studentlist = tk.Listbox(window_select, width=10, height=3, bd=4, relief='flat')
            studentlist.pack(side='left', fill='both')
            studentlist.insert('end', head_string[i])
            for each in res:
                studentlist.insert('end', each[i])


    ## 打印系表
    def printDepartment():
        sql = """SELECT * FROM Department"""
        res = sql_information(sql)
        window_printDepartment = tk.Toplevel(window_main_page)
        window_printDepartment.geometry('400x80')
        # window_printDepartment.resizable(0, 0)
        window_printDepartment.title('系表查看结果')
        head_string = ('系号', '系名', '系人数', '系地点', '宿舍区')
        for i in range(len(res[0])):
            dlist = tk.Listbox(window_printDepartment, width=10, height=3, bd=4, relief='flat')
            dlist.pack(side='left', fill='both')
            dlist.insert('end', head_string[i])
            for each in res:
                dlist.insert('end', each[i])
    ## 打印班级表
    def printClass():
        sql = """SELECT * FROM Class"""
        res = sql_information(sql)
        window_printClass = tk.Toplevel(window_main_page)
        window_printClass.geometry('400x80')
        # window_printClass.resizable(0, 0)
        window_printClass.title('班级表查看结果')
        head_string = ('班号', '专业号', '班人数', '入学年份')
        for i in range(len(res[0])):
            clist = tk.Listbox(window_printClass, width=10, height=3, bd=4, relief='flat')
            clist.pack(side='left', fill='both')
            clist.insert('end', head_string[i])
            for each in res:
                clist.insert('end', each[i])
    ## 打印学生表
    def printStudent():
        sql = """SELECT * FROM Student"""
        res = sql_information(sql)
        window_printStudent = tk.Toplevel(window_main_page)
        window_printStudent.geometry('400x80')
        # window_printStudent.resizable(0, 0)
        window_printStudent.title('学生表查看结果')
        head_string = ('学号', '姓名', '性别', '年龄', '班号')
        for i in range(len(res[0])):
            clist = tk.Listbox(window_printStudent, width=10, height=3, bd=4, relief='flat')
            clist.pack(side='left', fill='both')
            clist.insert('end', head_string[i])
            for each in res:
                clist.insert('end', each[i])
    ## 打印专业表
    def printmajor():
        sql = """SELECT * FROM Major"""
        res = sql_information(sql)
        window_printStudent = tk.Toplevel(window_main_page)
        window_printStudent.geometry('400x80')
        # window_printStudent.resizable(0, 0)
        window_printStudent.title('学生表查看结果')
        head_string = ('专业号', '专业名', '系号')
        for i in range(len(res[0])):
            clist = tk.Listbox(window_printStudent, width=10, height=3, bd=4, relief='flat')
            clist.pack(side='left', fill='both')
            clist.insert('end', head_string[i])
            for each in res:
                clist.insert('end', each[i])
    ## 打印学会表
    def printconf():
        sql = """SELECT * FROM Conference"""
        res = sql_information(sql)
        window_printStudent = tk.Toplevel(window_main_page)
        window_printStudent.geometry('400x80')
        # window_printStudent.resizable(0, 0)
        window_printStudent.title('学生表查看结果')
        head_string = ('学会号', '学会名', '建立年份','学会地点')
        for i in range(len(res[0])):
            clist = tk.Listbox(window_printStudent, width=10, height=3, bd=4, relief='flat')
            clist.pack(side='left', fill='both')
            clist.insert('end', head_string[i])
            for each in res:
                clist.insert('end', each[i])
    ## 打印参会表
    def printAttend():
        sql = """SELECT * FROM Attend"""
        res = sql_information(sql)
        window_printStudent = tk.Toplevel(window_main_page)
        window_printStudent.geometry('400x80')
        # window_printStudent.resizable(0, 0)
        window_printStudent.title('学生表查看结果')
        head_string = ('学号', '学会号', '入会时间')
        for i in range(len(res[0])):
            clist = tk.Listbox(window_printStudent, width=10, height=3, bd=4, relief='flat')
            clist.pack(side='left', fill='both')
            clist.insert('end', head_string[i])
            for each in res:
                clist.insert('end', each[i])
    ## 打印学会视图
    def printConference():
        sql = """SELECT * FROM ConferenceView """
        res = sql_information(sql)
        window_printConference = tk.Toplevel(window_main_page)
        window_printConference.geometry('400x80')
        #window_printConference.resizable(0, 0)
        window_printConference.title('学会视图查看结果')
        head_string = ('学会号', '学会名', '学会人数')
        for i in range(len(res[0])):
            conflist = tk.Listbox(window_printConference, height=5, bd=4, relief='flat')
            conflist.pack(side='left', fill='both')
            conflist.insert('end', head_string[i])
            for each in res:
                conflist.insert('end', each[i])
    ## 打印班级视图
    def printClassView():
        sql = """SELECT * FROM ClassView """
        res = sql_information(sql)
        window_printClassView = tk.Toplevel(window_main_page)
        window_printClassView.geometry('400x80')
        #window_printClassView.resizable(0, 0)
        window_printClassView.title('班级视图查看结果')
        head_string = ('班级号', '系名', '专业名','入学年份','班级人数')
        for i in range(len(res[0])):
            conflist = tk.Listbox(window_printClassView, height=5, bd=4, relief='flat')
            conflist.pack(side='left', fill='both')
            conflist.insert('end', head_string[i])
            for each in res:
                conflist.insert('end', each[i])
    ## 打印系真实人数
    def printRealDnum():
        sql = """SELECT * FROM dRealnum """
        res = sql_information(sql)
        window_printClassView = tk.Toplevel(window_main_page)
        window_printClassView.geometry('400x80')
        #window_printClassView.resizable(0, 0)
        window_printClassView.title('班级视图查看结果')
        head_string = ('系号', '系名', '系真实人数')
        for i in range(len(res[0])):
            conflist = tk.Listbox(window_printClassView, height=5, bd=4, relief='flat')
            conflist.pack(side='left', fill='both')
            conflist.insert('end', head_string[i])
            for each in res:
                conflist.insert('end', each[i])
    ## 打印学生视图
    def printStudentView():
        sql = """SELECT * FROM StudentView """
        res = sql_information(sql)
        window_StudentView = tk.Toplevel(window_main_page)
        window_StudentView.geometry('400x80')
        #window_StudentView.resizable(0, 0)
        window_StudentView.title('学生视图查看结果')
        head_string = ('学号', '姓名', '年龄', '系名','班号','宿舍区')
        for i in range(len(res[0])):
            conflist = tk.Listbox(window_StudentView, height=5, bd=4, relief='flat')
            conflist.pack(side='left', fill='both')
            conflist.insert('end', head_string[i])
            for each in res:
                conflist.insert('end', each[i])


    def insertPage():
        window_insert = tk.Toplevel(window_main_page)
        window_insert.geometry('400x500')
        window_insert.title('插入学生信息')

        def insertData():
            iSno = insertNo.get()
            iSname = insertName.get()
            iSex = insertSex.get()
            iAge = insertAge.get()
            iCno = insertCno.get()

            try:
                db = pymysql.connect(host='localhost', user='root', password='zys@010717', database="stu_dbms")
                cur = db.cursor()
                sql = """
                INSERT INTO Student VALUES ("{iSno}","{iSname}","{iSex}","{iAge}","{iCno}"); 
                """.format(iSno=iSno, iSname=iSname, iSex=iSex, iAge=iAge, iCno=iCno)
                cur.execute(sql)
                db.commit()
            except Exception as e:
                showerror(message="操作非法，插入失败！")
                print(e)
                db.rollback()
                return
            finally:
                cur.close()
                db.close()
            tk.Label(window_insert, text="插入后学生表如下").pack()
            showStudent(window_insert,10)
            showinfo(message='插入成功！')

        tk.Label(window_insert, text="插入信息填写如下：").pack(side='top')
        tk.Label(window_insert, text="学号：").pack()
        tk.Entry(window_insert, textvariable=insertNo).pack()
        tk.Label(window_insert, text="姓名：").pack()
        tk.Entry(window_insert, textvariable=insertName).pack()
        tk.Label(window_insert, text="性别：").pack()
        tk.Entry(window_insert, textvariable=insertSex).pack()
        tk.Label(window_insert, text="年龄：").pack()
        tk.Entry(window_insert, textvariable=insertAge).pack()
        tk.Label(window_insert, text="班号：").pack()
        tk.Entry(window_insert, textvariable=insertCno).pack()
        tk.Button(window_insert, text="确认插入", command=insertData).pack()


    def deletePage():
        window_delete = tk.Toplevel(window_main_page)
        window_delete.geometry('400x400')
        window_delete.title('删除学生信息')

        def deleteData():
            dSno = deleteNo.get()
            try:
                db = pymysql.connect(host='localhost', user='root', password='zys@010717', database="stu_dbms")
                cur = db.cursor()
                sql = """DELETE FROM Student WHERE Sno = "{dSno}" """.format(dSno=dSno)
                cur.execute(sql)
                db.commit()
            except Exception as e:
                showerror(message="操作非法，删除失败！")
                db.rollback()
                return
            finally:
                cur.close()
                db.close()
            tk.Label(window_delete, text="删除后学生表如下").pack()
            showStudent(window_delete,10)
            showinfo(message='删除成功！')

        tk.Label(window_delete, text="需要删除的学生学号为：").pack()
        tk.Entry(window_delete, textvariable=deleteNo).pack()
        tk.Button(window_delete, text="确认删除", command=deleteData).pack()




    def updatePage():
        window_update = tk.Toplevel(window_main_page)
        window_update.geometry('400x300')
        window_update.title('更新学生信息')

        def updateData():
            uno = updateNo.get()
            uname = updateName.get()
            usex = updateSex.get()
            uage = updateAge.get()
            try:
                db = pymysql.connect(host='localhost', user='root', password='zys@010717', database="stu_dbms")
                cur = db.cursor()
                sql = """
                UPDATE Student SET Sname = "{uname}", Sex = "{usex}", Age = "{uage}"
                WHERE Sno = "{uno}" """.format(uno=uno, uname=uname, usex=usex, uage=uage)
                cur.execute(sql)
                db.commit()
            except Exception as e:
                showerror(message="操作非法，更新失败！")
                db.rollback()
                return
            finally:
                cur.close()
                db.close()
            tk.Label(window_update, text="更新后学生表如下").pack()
            showStudent(window_update, 10)
            showinfo(message='更新成功！')

        tk.Label(window_update, text="需要更新的学生学号为：").pack(side='top')
        tk.Entry(window_update, textvariable=updateNo).pack()
        tk.Label(window_update, text="姓名：").pack()
        tk.Entry(window_update, textvariable=updateName).pack()
        tk.Label(window_update, text="性别：").pack()
        tk.Entry(window_update, textvariable=updateSex).pack()
        tk.Label(window_update, text="年龄：").pack()
        tk.Entry(window_update, textvariable=updateAge).pack()
        tk.Button(window_update, text="确认更新", command=updateData).pack()

    def otherPage():
        otherpage = tk.Toplevel(window_main_page)
        otherpage.geometry('950x500')
        otherpage.title('其他功能操作')
        #otherpage.resizable(0,0)
        #gird12 = tk.Frame(otherpage, width=400, height=500,
        #                    padx=2, pady=2).pack(side="left")
        grid1 = tk.LabelFrame(otherpage, text='查看视图', font=('华文黑体', 16, "bold"),
                             padx=2, pady=2)
        grid1.pack(anchor='nw',fill='both')
        grid2 = tk.LabelFrame(otherpage, text='查看表', font=('华文黑体', 16, "bold"), width=250, height=250,
                              padx=20, pady=2)
        grid2.pack(anchor='sw',fill='both')

        grid3 = tk.LabelFrame(otherpage, text='班号替换', font=('华文黑体', 16, "bold"), width=250, height=250,
                              padx=10, pady=1)
        grid3.pack(anchor='ne',fill='both')
        grid4 = tk.LabelFrame(otherpage, text='系人数矫正', font=('华文黑体', 16, "bold"), width=250, height=250,
                              padx=10, pady=1)
        grid4.pack(anchor='se',fill='both',expand=True)

        oldcno = tk.IntVar()
        newcno = tk.IntVar()
        execdno = tk.IntVar()
        renum = tk.IntVar()
        tablename = tk.StringVar()
        def exchangeClassno():
            ono = oldcno.get()
            nno = newcno.get()
            returnum = renum.get()

            try:
                db = pymysql.connect(host='localhost', user='root', password='zys@010717', database="stu_dbms")
                cur = db.cursor()
                resarg = cur.callproc('Alter_Cno', args=(nno, ono, returnum))
                db.commit()
                res1 = cur.fetchall()
                print(res1)
                print(resarg)
                cur.execute("select @_Alter_Cno_2")

                pvalue = cur.fetchall()
            except Exception as e:
                print(e)
                showerror(message="操作非法，替换失败！")
                db.rollback()
                return
            finally:
                cur.close()
                db.close()
            showinfo(message="替换成功")

        def exchangeDno():
            dno = execdno.get()
            rdno = 0
            rdname = ""
            roldnum = 0
            rnewnum = 0
            try:
                db = pymysql.connect(host='localhost', user='root', password='zys@010717', database="stu_dbms")
                cur = db.cursor()
                resarg = cur.callproc('CheckDnum', args=(dno, rdno, rdname, roldnum, rnewnum))
                db.commit()
                res1 = cur.fetchall()
                print(res1)
                print(resarg)

                pvalue = cur.fetchall()
            except Exception as e:
                print(e)
                showerror(message="操作非法，矫正失败！")
                db.rollback()
                return
            finally:
                cur.close()
                db.close()
            showinfo(message="矫正成功")


        ## 学会视图
        tk.Label(grid1, text="以下查看视图").pack()
        tk.Button(grid1, text='确定查看学会视图', font=('华文黑体', 10, "bold"), height=2, width=15, command=printConference) \
            .pack(side='left')
        tk.Button(grid1, text='确定查看班级视图', font=('华文黑体', 10, "bold"), height=2, width=15, command=printClassView).pack(
            side='left')
        tk.Button(grid1, text='确定查看学生视图', font=('华文黑体', 10, "bold"), height=2, width=15, command=printStudentView).pack(
            side='left')
        tk.Button(grid1, text='确定查看系真实人数视图', font=('华文黑体', 10, "bold"), height=2, width=20, command=printRealDnum).pack(
            side='left')

        ## 触发器 查看表
        tk.Label(grid2, text="以下查看表").pack()
        tk.Button(grid2, text='确定查看系表', font=('华文黑体', 10, "bold"), height=2, width=15, command=printDepartment)\
            .pack(side='left')
        tk.Button(grid2, text='确定查看班级表', font=('华文黑体', 10, "bold"), height=2, width=15, command=printClass).pack(side='left')
        tk.Button(grid2, text='确定查看学生表', font=('华文黑体', 10, "bold"), height=2, width=15, command=printStudent).pack(side='left')
        tk.Button(grid2, text='确定查看专业表', font=('华文黑体', 10, "bold"), height=2, width=15, command=printmajor).pack(
            side='left')
        tk.Button(grid2, text='确定查看学会表', font=('华文黑体', 10, "bold"), height=2, width=15, command=printconf).pack(
            side='left')
        tk.Button(grid2, text='确定查看参会表', font=('华文黑体', 10, "bold"), height=2, width=15, command=printAttend).pack(
            side='left')
        ## 班号替换
        tk.Label(grid3, text="旧班号为").pack()
        tk.Entry(grid3, textvariable=oldcno).pack()
        tk.Label(grid3, text="替换为新班号：").pack()
        tk.Entry(grid3, textvariable=newcno).pack()
        tk.Button(grid3,text='确定替换', font=('华文黑体', 10,"bold"),height=2,width=7,command=exchangeClassno).pack()

        ## 系人数矫正

        tk.Label(grid4, text="系号为").pack()
        tk.Entry(grid4, textvariable=execdno).pack()
        tk.Button(grid4, text='系号修正', font=('华文黑体', 10, "bold"), height=2, width=7, command=exchangeDno).pack()


    insertButton = tk.Button(left,text='插入学生信息', font=('华文黑体', 14,"bold"),height=3,width=12,command=insertPage)
    insertButton.pack(padx=10, pady=5)
    deleteButton = tk.Button(left,text='删除学生信息', font=('华文黑体', 14,"bold"),height=3,width=12,command=deletePage)
    deleteButton.pack(padx=10, pady=5)
    updateButton = tk.Button(left,text='更新学生信息', font=('华文黑体', 14,"bold"),height=3,width=12, command=updatePage)
    updateButton.pack(padx=10, pady=5)
    otherbutton = tk.Button(left, text='其他功能', font=('华文黑体', 14, "bold"), height=3, width=12, command=otherPage)
    otherbutton.pack(padx=10, pady=5)
    label1 = tk.Label(right,text='学生的学号是', font=('华文黑体', 9,"bold"))
    label1.pack()

    entry1 = tk.Entry(right,textvariable=selectNo)
    entry1.pack(padx=10, pady=10)
    selectButton = tk.Button(right,text='查询', font=('华文黑体', 10,"bold"),height=2,width=7,command=selectData)
    selectButton.pack()
    showStudent(right,20)

    window_main_page.mainloop()

main_page()