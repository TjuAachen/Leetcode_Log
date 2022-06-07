CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare M int;
set M = N -1;
  RETURN (
      # Write your MySQL query statement below.
SELECT DISTINCT(salary) AS salary
FROM Employee
ORDER BY salary DESC
Limit M, 1
  );
END