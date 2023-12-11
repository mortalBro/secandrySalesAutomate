#sql querries for getting all trasaction orders date wises
'''

SELECT
  DAY(order_date) AS day_of_month,
  COUNT(*) AS mortal
FROM
  db_mtprod.orders
WHERE
  YEAR(order_date) = 2023
  AND MONTH(order_date) = 11
  AND DAY(order_date) BETWEEN 2 AND 8
GROUP BY
  DAY(order_date);
  
'''

#for count attendance
'''

SELECT
   DAY(checkin_date) AS day_of_month,
   COUNT(*) AS mortal
FROM
   db_mtprod.attendances
WHERE
   YEAR(checkin_date) = 2023
   AND MONTH(checkin_date) = 11
   AND DAY(checkin_date) BETWEEN 26 AND 30
   AND checkin_date LIKE '2023-11%'
GROUP BY
   DAY(checkin_date);
   
'''