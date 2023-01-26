create table employees (
  employee_id serial primary key,
  first_name text not null,
  last_name text not null,
  salary numeric not null,
  description text
);

insert into employees(first_name,last_name,salary,description) values ('Jan','Kowalski',10000,'Opisa Jana Kowalskiego, bardzo długi bo będziemy tego potrzebować w aplikacji webowej');
insert into employees(first_name,last_name,salary,description) values ('Stefan','Męczypupa',5000,'Opisa Stefana Meczypupy, bardzo długi bo będziemy tego potrzebować w aplikacji webowej');
insert into employees(first_name,last_name,salary,description) values ('Krzysztof','Testowy',8000,'Opisa Krzysztofa Testowego, bardzo długi bo będziemy tego potrzebować w aplikacji webowej');


create table products(
	product_id serial primary key,
	product_name text not null,
	price numeric not null default 0,
	description text,
	stock integer default 0
);


insert into products(product_name,price,description,stock) values ('Bulbulator',100,'Urządzenie które robi bul bul',32);
insert into products(product_name,price,description,stock) values ('Półoś do Jelcza',1500,'Takie coś z takim czymś bez takiego czegoś',2);
insert into products(product_name,price,description,stock) values ('Wihajster',300,'Z dzyndzlem albo bez',0);

select * from employees;
select * from products;


create table players (
	player_id integer primary key,
	first_name text not null,
	last_name text not null,
	height numeric not null,
	weight numeric not null
);