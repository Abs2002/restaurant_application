************************************ Order placing program *********************************

This program is used to place an order and save it to the database and send to the another pc
this program uses socket programming with tkinter. this program accurately shows the amout of 
order placed with options of mode of payment and mode of eating. this is the ready to use
program by anybody. GUI works fine.

NOTE : scoket programming is of same computer by using same port no.
please run these 2 programs in seprate cmds otherwise it will not work

Problems of the program

1. occasional errors of saving of order in mysql
2. scoket programming is not working and order is not transferred to another program
3. program will only work once if we don't use while loop in the client side but program will
   also not work if we use while loop 



Mysql table structure

create database restaurants;
use reataurants;

create table res(
price varchar(5) primary key not null,
payment_mode varchar(20),
mode varchar(20),
date date,
time varchar(10)
);

