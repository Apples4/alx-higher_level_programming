-- script that lists all shows, and 
-- all genres linked to that show, from the database
SELECT shows.title, tv_g.name
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres
ON shows.id = show_genres.show_id
LEFT JOIN tv_genres AS tv_g
ON show_genres.genre_id = tv_g.id
ORDER BY shows.title, tv_g.name;
