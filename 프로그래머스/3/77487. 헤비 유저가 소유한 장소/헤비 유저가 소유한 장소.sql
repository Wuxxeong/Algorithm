-- 코드를 입력하세요
WITH H_N AS (
SELECT HOST_ID, COUNT(NAME) AS NUM
FROM PLACES
GROUP BY HOST_ID)

SELECT P.ID, P.NAME, P.HOST_ID
FROM H_N H JOIN PLACES P ON H.HOST_ID=P.HOST_ID
WHERE H.NUM >= 2
ORDER BY P.ID