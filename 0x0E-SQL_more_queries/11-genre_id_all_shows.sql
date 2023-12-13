-- script that lists all shows contained in the database
SELECT tv_show.title, tv_shows_genres.genre_id
FROM tv_shows AS tv_shows
LEFT JOIN tv_show_genres AS tv_show_genres
ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id;
