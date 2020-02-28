-- E-R模型中学生  教师   课程表的建立
create table stu(
id int primary key auto_increment,
姓名 varchar(30),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table teacher(
id int primary key auto_increment,
姓名 varchar(30),
职称 varchar(30),
年龄 tinyint
);

create table course(
id int primary key auto_increment,
名称 varchar(30),
学分 float,
tid int,
constraint  t_fk foreign  key (tid)references teacher(id)
);

create table course_stu(
cid int,
sid int,
score float,
primary key(cid,sid),
constraint  c_fk foreign  key (cid)references course(id),
constraint  s_fk foreign  key (sid)references stu(id)
);


关联查询练习 使用cls 和 interest
1 学生对应的爱好和兴趣班的价格
select cls.name,interest.hobby,interest.price from  cls inner join interest on cls.name=interest.name;

2 查询所有班级学生信息，同时标注出哪些同学有什么样的兴趣爱好
select c.name,c.sex,i.hobby from cls as c left join interest as i on c.name=i.name;

3 查看所有兴趣爱的信息，并且标注与其对应的同学
select i.hobby,i.price,c.name from cls as c right join interest as i on c.name=i.name;

函数操作:

注意: 1. 函数内的select语句要么return 要么 赋值给变量
     2. 函数最终return 一个值 而不是一堆值
     3. 函数里如果有写操作语句则每次调用都会执行，所以慎用
     4. 一个数据库中函数不能重名

delimiter $$
create function st() returns int
begin
return (select score from cls order by score desc limit 1);
end $$
delimiter ;

delimiter $$
create function querNameById(uid int) returns varchar(30)
begin
return (select name from cls where id = uid);
end $$
delimiter ;

delimiter $$
create function st4() returns int
begin
declare a int;
declare b int;
set a=(select score from cls where name='Lucy');
select score from cls where name = 'Lily' into b;
return a-b;
end $$
delimiter ;

存储过程：
delimiter $$
create procedure st()
begin
select name,age from cls;
update cls set sex='o' where sex is null;
select name,sex,score from cls order by score desc;
end $$
delimiter ;





create table `出版社` (
id int primary key auto_increment,
名称 varchar(64),
创刊日期 date,
地址 text,
电话 char(16)
);

create table `作家`(
id int primary key auto_increment,
姓名 varchar(32),
性别 char,
出生日期 date,
住址 text,
风格 text
);

create table `图书`(
id int primary key auto_increment,
书名 varchar(30),
出版日期 date,
定价 decimal(5,2),
a_id int,
p_id int,
constraint a_fk foreign key(a_id) references 作家(id),
constraint p_fk foreign key(p_id) references 出版社(id)
);

-- 出版社--作家关系
create table publication_author(
author_id int not null,
publication_id int not null,
签约时间 datetime default now(),
primary  key(author_id,publication_id),
constraint a_fk2 foreign key(author_id) references 作家(id),
constraint p_fk2 foreign key(publication_id) references 出版社(id)
);









