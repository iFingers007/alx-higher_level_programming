-- a script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT g.name AS genre, COUNT(tvg.show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tvg ON g.id = tvg.genre_id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
