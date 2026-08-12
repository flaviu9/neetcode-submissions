-- Write your query below
select seller_name
from seller
left join orders on seller.seller_id = orders.seller_id