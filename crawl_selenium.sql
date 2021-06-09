
drop table web_crawl.item_link;

create table web_crawl.list_kw(
	keywordId int not null auto_increment primary key,
	keywordName varchar(255)
);

insert into web_crawl.list_kw(keywordName)
values
	("stock"),
	("sports"),
	("foods"),
	("animals"),
	("fashion");


create table web_crawl.item_link(
	itemId int not null auto_increment primary key,
	keywordId int,
	itemLink text default '-',
	timeCrawled datetime,
	foreign key (keywordId) references web_crawl.list_kw(keywordId)
);

select *
from web_crawl.item_link il ;