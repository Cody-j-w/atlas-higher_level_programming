-- list all tv shows associated with a particular genre

SELECT title
    FROM tv_shows
    LEFT JOIN tv_show_genres AS sg
    ON (sg.show_id = tv_shows.id)
    LEFT JOIN tv_genres AS genre
    ON (sg.genre_id = genre.id)
    WHERE genre.name = 'Comedy'
    ORDER BY title ASC;