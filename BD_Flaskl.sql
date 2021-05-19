create database FlaskDb;

Use FlaskDb;

create table contacts(
id int NOT NULL AUTO_INCREMENT,
fullname varchar(255),
phone varchar(255),
email varchar(255),
PRIMARY KEY(id)
);
