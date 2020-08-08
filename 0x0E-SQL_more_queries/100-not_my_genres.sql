-- list all genres not linked to the show Dexter
-- list all genres not linked to the show Dexter
SELECT name FROM tv_genres
WHERE name NOT IN (
    SELECT distinct name 
    FROM tv_shows 
    RIGHT JOIN tv_show_genres 
    ON tv_show_genres.show_id = tv_shows.id 
    LEFT JOIN tv_genres 
    ON tv_genres.id = tv_show_genres.genre_id 
    WHERE title='Dexter') 
    ORDER BY name;