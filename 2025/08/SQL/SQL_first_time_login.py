with first_login AS (
    SELECT
        user_id,
        min(activity_date)AS frst_login
    FROM
        traffic
    WHERE
        activity = 'login'
    GROUP BY
        user_id
)

SELECT
    frst_login AS login_date,
    COUNT(user_id) AS user_count
FROM
    first_login
WHERE
    frst_login between '2019-04-01' AND '2019-06-30'
GROUP BY
    frst_login
ORDER BY
    login_date