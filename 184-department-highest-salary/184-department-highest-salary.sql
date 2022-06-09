# Write your MySQL query statement below
select Department.name as 'Department', 
Employee.name as 'Employee', Employee.salary as Salary
from Employee left join Department
on Department.id = Employee.departmentId
where (Employee.departmentId,Salary) IN 
(Select 
      DepartmentId ,max(Salary)
From Employee
Group by DepartmentId)