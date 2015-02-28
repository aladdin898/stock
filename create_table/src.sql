drop table if exists src_price_day;

create table src_price_day (
    id int,
    date int,
    open float,
    high float,
    low float,
    close float,
    volume int,
    adj_close float,
    primary key(id, date)
);
