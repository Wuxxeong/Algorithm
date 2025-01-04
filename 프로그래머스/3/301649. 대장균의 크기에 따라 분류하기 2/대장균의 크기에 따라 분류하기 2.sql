-- 코드를 작성해주세요
SELECT ID,
    (CASE
        WHEN PER_RANK<=0.25 THEN 'CRITICAL'
        WHEN PER_RANK<=0.5 THEN 'HIGH'
        WHEN PER_RANK <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END) AS COLONY_NAME
FROM (
    SELECT ID, PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS PER_RANK
    FROM ECOLI_DATA
) AS D
ORDER BY ID