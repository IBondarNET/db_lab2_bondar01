import psycopg2
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


username = 'postgres'
password = '123'
database = 'postgres'
host = 'localhost'
port = '5432'

query_1 = '''
select "driverRef", sum(r.laps) from drivers d
left join results r on r."driverId" = d."driverId"
GROUP by d."driverRef"
order by sum(r.laps) desc
limit 50;
'''
query_2 = '''
select "driverRef", count(r.position) from drivers d
left join results r on r."driverId" = d."driverId"
where r.position = 1
GROUP by d."driverRef"
order by count(r.laps) desc
limit 50;
'''
query_3 = '''
select date_part('year', age(to_date(d."dob",'DD/MM/YYYY'))) , max(CAST(r."fastestLapSpeed" as decimal)) from drivers d
left join results r on r."driverId" = d."driverId"
where r."fastestLapSpeed" != 0
GROUP by d."dob" 
order by max(CAST(r."fastestLapSpeed" as decimal)) desc
limit 50;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

with conn:
    cur1 = conn.cursor()
    cur1.execute(query_1)
    orderId = []
    amount = []

    for row in cur1:
        orderId.append(row[0])
        amount.append(row[1])

    plt.bar(orderId, amount)
    plt.title('Кількість кругів по водіям', size=10)
    plt.ylabel('Круги', size=10)
    plt.show()


    cur2 = conn.cursor()
    cur2.execute(query_2)
    driver_name = []
    sum = []

    for row in cur2:
        driver_name.append(row[0])
        sum.append(row[1])

    x, y = plt.subplots()
    plt.title('Топ 50 водіїв по перемогам', size=20)
    y.pie(sum, labels=driver_name, autopct='%1.1f%%')
    plt.show()


    cur3 = conn.cursor()
    cur3.execute(query_3)
    orderId = []
    price = []

    for row in cur3:
        orderId.append(row[1])
        price.append(row[0])


    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator())

    plt.plot(orderId, price)
    plt.xlabel('Максимальна швидкість')
    plt.ylabel('Вік')
    plt.title('Залежність максимальної швидкості від віку', size=10)

    # for qnt, iprice in zip(orderId, price):
    #     plt.annotate(iprice, xy=(qnt, ""+iprice))

    plt.show()