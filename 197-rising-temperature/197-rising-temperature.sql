# Write your MySQL query statement below
select w1.id
from weather w1, weather w2
where w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY) and w2.temperature < w1.temperature