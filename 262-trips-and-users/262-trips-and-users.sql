# Write your MySQL query statement below
select request_at as Day,
cast(COUNT(CASE WHEN s2.status <> 'completed' THEN 1 END)/count(s2.status) as decimal(10,2)) as 'Cancellation Rate'

from (select status, request_at
from (select * from Trips t join Users u1 on u1.users_id = t.client_id where u1.banned = 'No' and t.request_at <= '2013-10-03' and t.request_at >= '2013-10-01') as s1 join Users u2 on s1.driver_id = u2.users_id where u2.banned = 'No') as s2 group by s2.request_at
