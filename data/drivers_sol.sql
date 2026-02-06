WITH r AS (
SELECT month(requested_at) M , ride_distance , ride_duration FROM rides r ,  
acceptedrides a WHERE a.ride_id=r.ride_id AND requested_at >= '2020-01-01' AND requested_at <= '2020-12-31' )
,rp AS (SELECT FLOOR((M-1)/3) AS P, M, ride_distance, ride_duration FROM r ORDER BY M),
mon AS (SELECT 1 AS mm UNION SELECT 2  UNION SELECT 3 UNION
SELECT 4 UNION SELECT 5  UNION SELECT 6 UNION
SELECT 7 UNION SELECT 8  UNION SELECT 9 UNION
SELECT 10 UNION SELECT 11  UNION SELECT 12 ),
outerjoin AS (SELECT * FROM mon LEFT OUTER JOIN rp ON mon.mm=rp.M),
computed AS ( SELECT mm,  SUM(ride_distance) AS month_distance, SUM(ride_duration) AS month_duration  FROM outerjoin GROUP BY mm)

SELECT mm, ROUND((AVG(month_distance) OVER w) /3,2),  ROUND((AVG(month_duration) OVER w) /3,2)  FROM computed 
window w AS (ORDER BY mm ROWS BETWEEN CURRENT ROW AND  2 FOLLOWING)






