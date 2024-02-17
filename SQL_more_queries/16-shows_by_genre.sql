-- List all show titles and associated genre names

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres AS sg
ON (sg.show_id = tv_shows.id)
LEFT JOIN tv_genres
ON (tv_genres.id = sg.genre_id)
ORDER BY title, name ASC;