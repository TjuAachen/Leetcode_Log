# Write your MySQL query statement below
select distinct email
from Person
group by email
having count(*) > 1;