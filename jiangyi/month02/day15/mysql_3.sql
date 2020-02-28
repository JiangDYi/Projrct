练习1： 使用book表完成

1. 统计每位作家写的图书的平均价格

select author,avg(price) from book group by author;

2. 统计每个出版社出版图书的数量
select publication,count(*) from book group by puclication;

3. 查看总共有多少个出版社
select count(distinct publication) from book;

4. 筛选出 那些出版过超过50的图书的出版社，并按照图书最高价格排序
select publication,max(price)
from book
group by publication
having max(price) > 50
order by max(price) desc;

5. 统计相同出版时间的图书的平均价格
select publication_time,avg(price) from book group by publication_time;


索引示例

create table index_test
(id int primary key auto_increment,name varchar(20),
index name_index(name));


insert into dept values
(1,'技术部'),
(2,'财务部'),
(3,'销售部'),
(4,'行政部'),
(5,'市场部');


insert into person values
(1,'Lily',29,'w',20000,'2017-4-3',2),
(2,'Tom',27,'w',22300,'2018-11-20',1),
(3,'Joy',30,'m',17800,'2019-5-6',1),
(4,'Emma',25,'m',21000,'2017-6-6',4),
(5,'Baron',32,'w',12300,'2019-8-8',5),
(6,'Abby',31,'m',20330,'2018-4-19',3),
(7,'Jack',23,'w',19700,'2020-1-24',3);

练习：  完成朋友圈表的建设
用户信息   朋友圈内容  点赞评论内容


create table user(
id int primary key,
name varchar(30),
passwd char(64)
);


create table pyq(
id int primary key,
content text,
time datetime,
address text,
u_id int,
constraint u_fk1 foreign key (u_id) references user (id));

create table user_pyq(
id int primary key,
uid int,
pid int,
lk bit,
comment text,
constraint u_fk2 foreign key (uid) references user(id),
constraint p_fk1 foreign key (pid) references pyq(id)
);

ER作业:

create table student(
id int primary key,
name varchar(30) not null,
age int not null,
sex enum ('w','m'),
native_place varchar(90) not null
);

create table teacher(
id int primary key,
name varchar(30) not null,
age int not null,
rank varchar(30) not null
);

create table curriculum(
id int primary key,
name varchar(60) not null,
credit float not null,
constraint t_fk primary key (tid) references teacher (id),
);

create table grade(
id int primary key,
sid int ,
cid int ,
score float not null,
constraint s_fk primary key (sid) references student (id),
constraint c_fk primary key (cid) references curriculum (id)
);















