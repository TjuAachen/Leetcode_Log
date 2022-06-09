# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e left join Department d
on e.departmentId = d.id
where 
3 > (select
     count(Distinct e2.salary)
    from Employee e2
    where e2.salary > e.salary 
    AND e.departmentId = e2.departmentId
    )