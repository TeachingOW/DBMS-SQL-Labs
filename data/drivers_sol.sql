with r as (
select month(requested_at) M , ride_distance , ride_duration from rides r ,  
acceptedrides a where a.ride_id=r.ride_id and requested_at >= '2020-01-01' and requested_at <= '2020-12-31' )
,rp as (select floor((M-1)/3) as P, M, ride_distance, ride_duration from r order by M),
mon as (select 1 as mm union select 2  union select 3 union
select 4 union select 5  union select 6 union
select 7 union select 8  union select 9 union
select 10 union select 11  union select 12 ),
outerjoin as (select * from mon left outer join rp on mon.mm=rp.M),
computed as ( select mm,  sum(ride_distance) as month_distance, sum(ride_duration) as month_duration  from outerjoin group by mm)

select mm, round((avg(month_distance) over w) /3,2),  round((avg(month_duration) over w) /3,2)  from computed 
window w as (order by mm rows between current row and  2 following)






