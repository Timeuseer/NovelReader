create database readbooks character set utf8;
use readbooks;
show tables;
show create database readbooks;

drop table admin_info;


create table admin_info(
	admin_id int(3) zerofill primary key auto_increment,
	admin_name	varchar(15),
    admin_pw	varchar(18),
    admin_email	varchar(20),
    admin_ph	char(13)
)auto_increment=1;

create index admin_name on admin_info(admin_name);
create index admin_email on admin_info(admin_email);
create index admin_ph on admin_info(admin_ph);



insert into admin_info values
(0,'张三','zs12345678','zs12345678@qq.com',13345565647),
(0,'张四','zs123456789','zs123456789@qq.com',13445565647),
(0,'张五','zw12345678','zw12345678@qq.com',13545565647),
(0,'张六','zl12345678','zl12345678@qq.com',13645565647);

select * from admin_info;

drop table user_info;

create table user_info(
	user_id int(3) zerofill primary key auto_increment,
	user_name	varchar(15),
    user_pw		varchar(18),
    user_email	varchar(18),
    user_ph		char(11),
    login_tm	timestamp,
    register_tm	timestamp	
)auto_increment=1;

create index user_name on user_info(user_name);
create index user_email on user_info(user_email);
create index user_ph on user_info(user_ph);
desc user_info;

insert into user_info values
(0,'TOM1','tm11234567','tm11234567@qq.com',13112341234,now(),now()),
(0,'TOM2','tm21234567','tm12234567@qq.com',13212341234,now(),now()),
(0,'TOM3','tm31234567','tm13234567@qq.com',13312341234,now(),now()),
(0,'TOM4','tm41234567','tm14234567@qq.com',13412341234,now(),now()),
(0,'TOM5','tm51234567','tm15234567@qq.com',13512341234,now(),now());

select * from user_info;

drop table book_info;

create table book_info(
	book_id int(3) primary key auto_increment,
	book_name varchar(20),
    book_auther varchar(15),
    book_url varchar(1024),
    book_image varchar(1024),
    book_type varchar(20),
    book_dwtm timestamp
)auto_increment=1;

create index book_name on book_info(book_name);
create index book_auther on book_info(book_auther);

insert into book_info values
(0,'紫川','来打我啊','紫川.txt','紫川.jpg','玄幻',now()),
(0,'斗破苍穹','天蚕土豆','斗破苍穹.txt','斗破苍穹.jpg','玄幻',now()),
(0,'武动乾坤','天蚕土豆','武动乾坤.txt','武动乾坤.jpg','玄幻',now()),
(0,'大主宰','天蚕土豆','大主宰.txt','大主宰.jpg','玄幻',now());


update book_info set book_name = '紫川',book_auther='城东' where book_id ='1';
delete from book_info where book_id = 6;
select * from book_info where book_type = '玄幻';
select * from book_info;