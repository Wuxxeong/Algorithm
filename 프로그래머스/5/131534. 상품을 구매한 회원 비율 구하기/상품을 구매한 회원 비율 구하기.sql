# -- 코드를 입력하세요
SELECT EXTRACT(YEAR FROM O.SALES_DATE) AS YEAR, EXTRACT(MONTH FROM O.SALES_DATE) AS MONTH, 
    COUNT(DISTINCT(O.USER_ID)) AS PUCHASED_USERS	,
    ROUND((COUNT(DISTINCT(O.USER_ID)) / (SELECT COUNT(*) FROM USER_INFO WHERE EXTRACT(YEAR FROM JOINED) = '2021')) ,1) AS PUCHASED_RATIO
FROM ONLINE_SALE O JOIN USER_INFO I ON O.USER_ID=I.USER_ID
WHERE EXTRACT(YEAR FROM I.JOINED) = '2021'
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH


# SELECT EXTRACT(YEAR FROM O.SALES_DATE) AS YEAR, 
#         EXTRACT(MONTH FROM O.SALES_DATE) AS MONTH, 
#         COUNT(DISTINCT(O.USER_ID)) AS PUCHASED_USERS,
#         ROUND(COUNT(DISTINCT(O.USER_ID))/(SELECT COUNT(USER_ID) FROM USER_INFO WHERE DATE_FORMAT(JOINED, '%Y')='2021'),1) AS PUCHASED_RATIO
# FROM ONLINE_SALE O JOIN USER_INFO I ON I.USER_ID=O.USER_ID
# WHERE DATE_FORMAT(I.JOINED, '%Y')='2021'
# GROUP BY EXTRACT(YEAR FROM O.SALES_DATE), EXTRACT(MONTH FROM O.SALES_DATE)
# ORDER BY YEAR ASC, MONTH ASC