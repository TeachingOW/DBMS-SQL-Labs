create table drivers (driver_id int, join_date date);
create table rides (ride_id int, user_id int, requested_at date);
create table acceptedrides (ride_id int, driver_id int, ride_distance int, ride_duration int);

insert into drivers values ( 10, '2019-12-10');
insert into drivers values ( 5, '2019-12-10');
insert into drivers values ( 7, '2019-12-10');
insert into drivers values ( 4, '2019-12-10');
insert into drivers values ( 1, '2019-12-10');
insert into drivers values ( 6, '2019-12-10');

insert into rides values( 6       , 75      , '2019-12-9'    );
insert into rides values( 1       , 54      , '2020-2-9'     );
insert into rides values( 10      , 63      , '2020-3-4'     );
insert into rides values( 19      , 39      , '2020-4-6'     );
insert into rides values( 3       , 41      , '2020-6-3'     );
insert into rides values( 13      , 52      , '2020-6-22'    );
insert into rides values( 7       , 69      , '2020-7-16'    );
insert into rides values( 17      , 70      , '2020-8-25'    );
insert into rides values( 20      , 81      , '2020-11-2'    );
insert into rides values( 5       , 57      , '2020-11-9'    );
insert into rides values( 2       , 42      , '2020-12-9'    );
insert into rides values( 11      , 68      , '2021-1-11'    );
insert into rides values( 15      , 32      , '2021-1-17'    );
insert into rides values( 12      , 11      , '2021-1-19'    );
insert into rides values( 14      , 18      , '2021-1-27'    );

insert into acceptedrides values( 10      , 10 ,        63,             38  );
 insert into acceptedrides values(13      , 10,         73        ,     96     );       
 insert into acceptedrides values(7       , 8  ,        100      ,      28       );     
 insert into acceptedrides values(17      , 7   ,       119     ,       68         );   
 insert into acceptedrides values(20     ,  1    ,      121    ,        92            );
 insert into acceptedrides values(5     ,   7       ,   42         ,    101          ); 
 insert into acceptedrides values(2    ,    4     ,     6     ,         38            );
 insert into acceptedrides values(11  ,     8      ,    37   ,          43            );
 insert into acceptedrides values(15 ,      8       ,   108 ,           82            );
 insert into acceptedrides values(12   ,    8         , 38  ,           34            );
 insert into acceptedrides values(14,       1         , 90,             74            );
