import psycopg2

username = 'postgres'
password = '123'
database = 'postgres'
host = 'localhost'
port = '5432'
query_1 = '''
select driverRef, sum(r.laps) from drivers d
left join results r on r.driverId = d.driverId
GROUP by r.driverId
order by sum(r.laps) desc
limit 50;
'''
query_2 = '''
select driverRef, count(r.position) from drivers d
left join results r on r.driverId = d.driverId
where r.position = 1
GROUP by r.driverId
order by count(r.laps) desc
limit 50;
'''
query_3 = '''
select age(to_date(d."dob",'DD/MM/YYYY')) , max(CAST(r."fastestLapSpeed" as decimal)) from drivers d
left join results r on r."driverId" = d."driverId"
where r."fastestLapSpeed" != 0
GROUP by d."dob" 
order by max(CAST(r."fastestLapSpeed" as decimal)) desc
limit 50;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
  print ("Database opened successfully");

  print("Query 1")
  cur1 = conn.cursor()
  cur1.execute(query_1)
  print("круги по водіям")
  for row in cur1:
    print(row)

  print("Query 2")
  cur2 = conn.cursor()
  cur2.execute(query_2)
  driver_name = []
  sum1 = []

  for row in cur2:
    driver_name.append(row[0])
    sum1.append(row[1])

  print("SUM  driver_name")
  for i in range(len(driver_name)):
    print(driver_name[i], sum1[i])

  print("Query 3")
  cur3 = conn.cursor()
  cur3.execute(query_3)
  driver_name = []
  max_speed = []

  for row in cur3:
    driver_name .append(row[0])
    max_speed.append(row[1])