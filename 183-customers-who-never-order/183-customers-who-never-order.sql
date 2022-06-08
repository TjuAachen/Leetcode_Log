# Write your MySQL query statement below
select c.name as 'Customers'
from customers c
where not exists (select customerId from orders where c.id = customerId);
