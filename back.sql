-- 创建数据库
create database stu_DBMS;
use stu_DBMS;

----------------------------- 创建系表 -----------------------------
CREATE TABLE Department(
    Dno INT         AUTO_INCREMENT,
    Dname CHAR(20)  NOT NULL UNIQUE,
    Dnum INT        NOT NULL CHECK(Dnum >= 0),
    Dloc CHAR(50)   NOT NULL,
    Dorm INT        NOT NULL CHECK(Dorm >= 0),
    PRIMARY KEY(Dno)
);
## 系表插入数据
INSERT INTO department VALUES (1,'通信工程系',667,'主楼二区通院办公室',12);
INSERT INTO department VALUES (2,'电子工程系',682,'办公楼二层西侧',12);
INSERT INTO department VALUES (3,'计算机系',865,'主楼Ⅳ213-218',11);
INSERT INTO department VALUES (4,'机电系',514,'主楼III区',11);
-- INSERT INTO department VALUES (6,'机电系',333,'主楼II区',11);
INSERT INTO department VALUES (20,'人工智能系',311,'南校区',13);

----------------------------- 创建专业表 -----------------------------
CREATE TABLE Major(
    Mno INT         AUTO_INCREMENT,
    Mname CHAR(20)  NOT NULL UNIQUE,
    Dno INT         NOT NULL,
    PRIMARY KEY(Mno),
    FOREIGN KEY(Dno) REFERENCES Department(Dno)
);
## 专业表插入数据
INSERT INTO major VALUES 
(1,'通信工程',1),
(2,'信息工程',1),
(3,'电子工程',2),
(4,'电磁波和电磁场',2),
(5,'计算机科学与技术',3),
(6,'软件工程',3),
(7,'机械',4),
(8,'自动化',4),
(9,'人工智能',20),
(10,'智能科学与技术',20);

----------------------------- 创建班级表 -----------------------------
CREATE TABLE Class(
    Cno INT AUTO_INCREMENT,
    Mno INT NOT NULL,
    Cnum INT CHECK(Cnum>0),
    Cyear YEAR CHECK(Cyear>1949 AND Cyear <=2021),  
    PRIMARY KEY(Cno),
    FOREIGN KEY(Mno) REFERENCES Major(Mno)
);
## 班级表插入数据
INSERT INTO Class VALUES
(1601011,1,80,2016),
(1501012,2,75,2015),
(1702015,3,150,2017),
(1903013,5,120,2019),
(1905045,6,120,2019),
(1904006,8,40,2019),
(1820011,9,25,2018);

----------------------------- 创建学生表 -----------------------------
CREATE TABLE Student(
    Sno INT AUTO_INCREMENT,
    Sname Char(20) NOT NULL,
    Sex CHAR(8) CHECK(Sex in('男','女')),
    Age INT CHECK(Age>=7 AND Age <= 100),
    Cno INT NOT NULL,
    PRIMARY KEY(Sno),
    FOREIGN KEY(Cno) REFERENCES Class(Cno)
);
## 学生表插入数据
INSERT INTO student VALUES
(19030001,'赵宇盛','男',20,1903013),
(16010001,'李华','男',23,1601011),
(17020010,'丽丽','女',22,1702015),
(19030002,'小明','男',20,1903013),
(19030003,'Amy','女',20,1903013),
(19050001,'老王','男',20,1905045),
(18200145,'黑夜男爵','男',21,1820011);

----------------------------- 创建学会表 -----------------------------
CREATE Table Conference(
    Confno INT AUTO_INCREMENT,
    Confname CHAR(20) NOT NULL UNIQUE,
    Esyear YEAR NOT NULL CHECK(Esyear>1949 AND Esyear<2021),
    Confloc CHAR(50) NOT NULL,
    PRIMARY KEY(Confno)
);
## 学会表插入数据
INSERT INTO conference VALUES 
(1,'数学学会',1990,'数学中心'),
(2,'计算机学会',1985,'计算机楼'),
(3,'校园动植物学会',2014,'百草园'),
(4,'反内卷学会',2019,'书院3楼'),
(5,'内卷卷内学会',2019,'书院3楼对面');

----------------------------- 参会表 -----------------------------
CREATE TABLE Attend(
    Sno INT NOT NULL CHECK(Sno>0),
    Confno INT NOT NULL CHECK(Confno>0),
    ATime DATE NOT NULL,
    PRIMARY KEY(Sno,Confno)
);
## 参会表插入数据
INSERT INTO Attend VALUES
(19030001,1,'2019-12-1'),
(19030001,2,'2019-11-1'),
(19030001,5,'2021-12-1'),
(16010001,2,'2018-7-4'),
(16010001,3,'2019-11-4'),
(19030003,4,'2020-5-10'),
(19030003,1,'2020-5-8'),
(19030003,2,'2020-5-6');

-------------------------------------------------------------------

----------------------------- 视图 -----------------------------
## 班级视图
CREATE VIEW ClassView(Cno,Dname,Mname,Cyear,Cnum) AS
SELECT  Class.Cno,Department.Dname,Major.Mname,Class.Cyear,Class.Cnum
FROM    Department, Major, Class
WHERE   Class.Mno = Major.Mno AND Major.Dno = Department.Dno;
## 学生视图
CREATE VIEW studentView(Sno,Sname,Age,Dname,Cno,Dorm) AS
SELECT  Student.Sno,Student.Sname,Student.Age,Department.Dname,Class.Cno,Department.Dorm
FROM    Student, Department, Class, Major
WHERE   Student.Cno = Class.Cno AND Class.Mno = Major.Mno AND Major.Dno = Department.Dno;
## 系视图
CREATE VIEW departmentView(Dno,Dname,Dloc,Dnum) AS
SELECT Department.Dno,Department.Dname,Department.Dloc,Department.Dnum
FROM Department;
## 学会视图
## 1.创建视图显示学会号、学会名和学生数
CREATE VIEW conferenceView(Confno,Confname,Confnum) AS
SELECT Conference.Confno,Conference.Confname,COUNT(Attend.Sno)
FROM Conference INNER JOIN Attend 
ON Conference.Confno = Attend.Confno
GROUP BY Conference.Confno
ORDER BY Confno;

----------------------------- 触发器 -----------------------------
## 插入触发器
DROP TRIGGER IF EXISTS stuInsert;
CREATE TRIGGER stuInsert
AFTER INSERT ON Student
FOR EACH ROW BEGIN
    ## 更新班级表
    UPDATE  Class SET Class.Cnum = Class.Cnum + 1 WHERE Class.Cno = NEW.Cno;
    ## 更新系表
    UPDATE  Department
    SET     Department.Dnum = Department.Dnum + 1
    WHERE   Department.Dno = (
        SELECT  Major.Dno FROM Major WHERE Major.Mno = (
            SELECT  Class.Mno FROM Class WHERE Class.Cno = NEW.Cno
        )
    );
END;
----------------------------- 测试用例stuInsert
INSERT INTO student VALUES (18200255,'明日香','女',21,1820011);
----------------------------------------------------------
## 删除触发器
DROP TRIGGER IF EXISTS stuDelete;
CREATE TRIGGER stuDelete
BEFORE DELETE ON Student
FOR EACH ROW BEGIN
    -- 更新班级表
    UPDATE Class SET Class.Cnum = Class.Cnum - 1 WHERE Class.Cno = OLD.Cno;
    --更新系表
    UPDATE department
    SET Department.Dnum = Department.Dnum - 1
    WHERE   Department.Dno = (
        SELECT Major.Dno FROM Major WHERE Major.Mno = (
            SELECT Class.Mno FROM Class WHERE Class.Cno = OLD.Cno
        )
    );
END;

----------------------------- 测试用例 stuDelete
DELETE FROM student WHERE Sno = 19030004;
---------------------------------------------------------------------
## 更新触发器
CREATE TRIGGER stuUpdate
BEFORE UPDATE ON Student
FOR EACH ROW
BEGIN
    ## 更新班级表
    UPDATE Class SET Class.Cnum = Class.Cnum + 1 
    WHERE Class.Cno = NEW.Cno;
    UPDATE Class SET Class.Cnum = Class.Cnum - 1 
    WHERE Class.Cno = OLD.Cno;
    ## 更新系表
    UPDATE Department
    SET Department.Dnum = Department.Dnum + 1
    WHERE Department.Dno = (
        SELECT Major.Dno FROM Major WHERE Major.Mno = (
            SELECT Class.Mno FROM Class WHERE Class.Cno = NEW.Cno));
    UPDATE department
    SET Department.Dnum = Department.Dnum - 1
    WHERE Department.Dno = (
        SELECT Major.Dno FROM Major WHERE Major.Mno = (
            SELECT Class.Mno FROM Class WHERE Class.Cno = OLD.Cno));
END;
----------------------------- 测试 -----------------------------
INSERT INTO student VALUES (19040001,'凌波丽','女',20,1904006);
----------------------------------------------------------


----------------------------- 创建存储过程（班号替换） -----------------------------
DELIMITER //
DROP PROCEDURE IF EXISTS Alter_Cno;
CREATE PROCEDURE Alter_Cno(
    IN New_Cno INT, 
    IN Old_Cno INT,
    OUT num INT
)
BEGIN
    DECLARE Classnum INT DEFAULT 0;
   
    SELECT Cnum FROM Class WHERE Class.Cno = Old_Cno
    INTO Classnum;
    SET FOREIGN_KEY_CHECKS = 0;
    UPDATE Student SET Student.Cno = New_Cno WHERE Student.Cno = Old_Cno ;
    UPDATE Class SET Class.Cno = New_Cno WHERE Class.Cno = Old_Cno ;
    SET FOREIGN_KEY_CHECKS = 1;
    SELECT Classnum INTO num;
END //
DELIMITER ;
## 测试
CALL Alter_Cno(1904031,1904006,@ClassNum) ;
---------------------------------------------------------------------------



----------------------------- 创建存储过程(系号纠正) -----------------------------

## 系真实人数视图
CREATE VIEW Drealnum(Dno,Dname,Drnum) AS
SELECT Department.Dno,Department.Dname,SUM(classView.Cnum)
FROM Department INNER JOIN classView
ON Department.Dname = classView.Dname
GROUP BY Department.Dno
ORDER BY Dno;
-----------------------------------------------------------------------------

## 创建存储过程
DROP PROCEDURE IF EXISTS CheckDnum;
CREATE PROCEDURE CheckDnum(
    IN  aDno INT,
    OUT oDno INT,
    OUT oDname CHAR(20),
    OUT oDoldnum INT,    -- 原人数
    OUT oDnewnum INT     -- 实际人数 
)
BEGIN
    DECLARE done BOOLEAN DEFAULT 0;     #定义结束标识
    DECLARE tDno INT DEFAULT 0;
    DECLARE tDname CHAR(20) DEFAULT "";
    DECLARE tDnum INT DEFAULT 0;
    DECLARE tDrnum INT DEFAULT 0;
    -- 定义游标
    DECLARE Checknum CURSOR 
    FOR SELECT Department.Dno,Department.Dname,Department.Dnum FROM Department;
    
    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET done = 1;
    -- 打开游标
    OPEN Checknum;
        -- 循环遍历，从第一行到最后一行
        REPEAT       
            FETCH Checknum INTO tDno,tDname,tDnum;
        -- 循环结束
        UNTIL ((done = 1) OR (tDno = aDno)) 
        END REPEAT;
    -- 关闭游标
    CLOSE Checknum;
    SELECT Drnum FROM Drealnum WHERE Drealnum.Dno = aDno INTO tDrnum;
    UPDATE Department SET Dnum = tDrnum WHERE Dno = tDno;
    SELECT tDno,tDname,tDnum,tDrnum INTO oDno,oDname,oDoldnum,oDnewnum;
END;
---------------------------------------------------------------------------------------
## 测试
call checkdnum(3,@no ,@name ,@old ,@new );
SELECT  @no ,@name ,@old ,@new ;
## INSERT INTO student VALUES (19050174,'大洋游侠','男',20,1905045);
