-- Write your query below

select name, sum(distance) as travelled_distance
from users
left join rides on users.id = rides.user_id
group by users.id, name
order by travelled_distance desc, name asc;