-- script that lists all genres from
-- displays the number of shows linked to each
SELECT tv_genres.name
FROM tv_genres AS tv_genres
INNER JOIN tv_show_genres AS tv_show_genre
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows AS tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show.title = 'Dexter'
ORDER BY tv_genres.name;
