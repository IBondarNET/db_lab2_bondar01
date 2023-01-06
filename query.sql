
-- круги по водіям
select driverRef, sum(r.laps) from drivers d
left join results r on r.driverId = d.driverId
GROUP by r.driverId
order by sum(r.laps) desc
limit 50;

-- перші місця
select driverRef, count(r.position) from drivers d
left join results r on r.driverId = d.driverId
where r.position = 1
GROUP by r.driverId
order by count(r.laps) desc
limit 50;

-- найбільша швидкість за віком
select age(to_date(d."dob",'DD/MM/YYYY')) , max(CAST(r."fastestLapSpeed" as decimal)) from drivers d
left join results r on r."driverId" = d."driverId"
where r."fastestLapSpeed" != 0
GROUP by d."dob" 
order by max(CAST(r."fastestLapSpeed" as decimal)) desc
limit 50;
