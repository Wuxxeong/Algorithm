-- 코드를 작성해주세요
SELECT EXTRACT(YEAR FROM YM) AS YEAR, ROUND(SUM(PM_VAL1)/COUNT(PM_VAL1),2) AS 'PM10', ROUND(SUM(PM_VAL2)/COUNT(PM_VAL2),2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY EXTRACT(YEAR FROM YM)
ORDER BY YEAR