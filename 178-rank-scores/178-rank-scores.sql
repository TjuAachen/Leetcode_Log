# Write your MySQL query statement below
Select s1.score,
(Select count(Distinct s2.score)
 from Scores s2
 where s2.score >= s1.score) 
 as 'rank'
from Scores s1
Order By s1.score Desc;