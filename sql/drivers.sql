CREATE TABLE drivers (driver_id INT, join_date DATE);
CREATE TABLE rides (ride_id INT, user_id INT, requested_at DATE);
CREATE TABLE acceptedrides (ride_id INT, driver_id INT, ride_distance INT, ride_duration INT);

INSERT INTO drivers VALUES ( 10, '2019-12-10');
INSERT INTO drivers VALUES ( 5, '2019-12-10');
INSERT INTO drivers VALUES ( 7, '2019-12-10');
INSERT INTO drivers VALUES ( 4, '2019-12-10');
INSERT INTO drivers VALUES ( 1, '2019-12-10');
INSERT INTO drivers VALUES ( 6, '2019-12-10');

INSERT INTO rides VALUES( 6       , 75      , '2019-12-9'    );
INSERT INTO rides VALUES( 1       , 54      , '2020-2-9'     );
INSERT INTO rides VALUES( 10      , 63      , '2020-3-4'     );
INSERT INTO rides VALUES( 19      , 39      , '2020-4-6'     );
INSERT INTO rides VALUES( 3       , 41      , '2020-6-3'     );
INSERT INTO rides VALUES( 13      , 52      , '2020-6-22'    );
INSERT INTO rides VALUES( 7       , 69      , '2020-7-16'    );
INSERT INTO rides VALUES( 17      , 70      , '2020-8-25'    );
INSERT INTO rides VALUES( 20      , 81      , '2020-11-2'    );
INSERT INTO rides VALUES( 5       , 57      , '2020-11-9'    );
INSERT INTO rides VALUES( 2       , 42      , '2020-12-9'    );
INSERT INTO rides VALUES( 11      , 68      , '2021-1-11'    );
INSERT INTO rides VALUES( 15      , 32      , '2021-1-17'    );
INSERT INTO rides VALUES( 12      , 11      , '2021-1-19'    );
INSERT INTO rides VALUES( 14      , 18      , '2021-1-27'    );

INSERT INTO acceptedrides VALUES( 10      , 10 ,        63,             38  );
 INSERT INTO acceptedrides VALUES(13      , 10,         73        ,     96     );       
 INSERT INTO acceptedrides VALUES(7       , 8  ,        100      ,      28       );     
 INSERT INTO acceptedrides VALUES(17      , 7   ,       119     ,       68         );   
 INSERT INTO acceptedrides VALUES(20     ,  1    ,      121    ,        92            );
 INSERT INTO acceptedrides VALUES(5     ,   7       ,   42         ,    101          ); 
 INSERT INTO acceptedrides VALUES(2    ,    4     ,     6     ,         38            );
 INSERT INTO acceptedrides VALUES(11  ,     8      ,    37   ,          43            );
 INSERT INTO acceptedrides VALUES(15 ,      8       ,   108 ,           82            );
 INSERT INTO acceptedrides VALUES(12   ,    8         , 38  ,           34            );
 INSERT INTO acceptedrides VALUES(14,       1         , 90,             74            );
