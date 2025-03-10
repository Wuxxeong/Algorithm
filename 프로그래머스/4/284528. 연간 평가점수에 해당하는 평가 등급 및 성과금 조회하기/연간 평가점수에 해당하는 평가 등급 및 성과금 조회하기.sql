WITH HR_AVG_GRADE AS(
    SELECT E.EMP_NO, E.EMP_NAME, E.SAL, AVG(G.SCORE) AS AVG_SCORE
    FROM HR_EMPLOYEES E JOIN HR_GRADE G ON E.EMP_NO=G.EMP_NO
    GROUP BY E.EMP_NO
)

SELECT EMP_NO, EMP_NAME,
    CASE
        WHEN AVG_SCORE>=96 THEN 'S'
        WHEN AVG_SCORE>=90 THEN 'A'
        WHEN AVG_SCORE>=80 THEN 'B'
        ELSE 'C'
    END
    AS GRADE,
    CASE
        WHEN AVG_SCORE>=96 THEN SAL*0.2
        WHEN AVG_SCORE>=90 THEN SAL*0.15
        WHEN AVG_SCORE>=80 THEN SAL*0.1
        ELSE SAL*0
    END
    AS BONUS
FROM HR_AVG_GRADE
ORDER BY EMP_NO
