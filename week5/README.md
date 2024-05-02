# MySQL pratice


## Task2 : Create database and table in MySQL server

- [x] Create a new database named website.


<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-2-1.JPG" width="800">


- [x] Create a new table named member, in the website database, designed as below:

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-2-2.JPG" width="800">

## Task3 : SQL CRUD

- [x] INSERT rows

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-1.JPG" width="800">

- [x] SELECT all rows

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-2.JPG" width="800">

- [x] SELECT all rows from the member table, in descending order of time.

    Ans : ORDER BY

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-3.JPG" width="800">

- [x] SELECT total 3 rows, second to fourth, from the member table, in descending order
of time.

    Ans : LIMIT

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-4.JPG" width="800">

- [x] SELECT rows where username equals to test.

    Ans : WHERE

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-5.JPG" width="800">

- [x] SELECT rows where name includes the es keyword.

    Ans : LIKE

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-6+.JPG" width="800">

- [x] SELECT rows where both username and password equal to test.

    Ans : AND

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-7.JPG" width="800">

- [x] UPDATE data in name column to test2 where username equals to test.

    Ans : UPDATE

<img src="https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-3-8++.JPG" width="800">


## Task4 : Aggregation

- [x] SELECT how many rows from the member table.

    Ans : COUNT ROWS

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-4-1.JPG)

- [x] SELECT the sum of follower_count of all the rows from the member table.

    Ans : SUM

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-4-2.JPG)

- [x] SELECT the average of follower_count of all the rows from the member table.

    Ans : AVG

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-4-3.JPG)

- [x] SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.

    Ans : SUBQUERY

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-4-4.JPG)



## Task5 : JOIN

- [x] CREATE NEW TABLE

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-1.JPG)

- [x] JOIN tables

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-2.JPG)
![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-2+.JPG)

- [x] SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.

    Ans : JOIN + WHERE

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-3.JPG)

- [x] Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.

    Ans : JOIN + AVG

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-4.JPG)

- [x] Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.

    Ans : GROUP BY

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-5.JPG)
![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/task5-5-5+.JPG)


## Export .sql file

- [x] Export .sql file

![](https://github.com/chienhuak/chienhuak.github.io/blob/main/week5/screenshot/export.JPG)









