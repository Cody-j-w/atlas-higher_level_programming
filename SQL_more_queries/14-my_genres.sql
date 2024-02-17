SELECT name
    FROM tv_genres AS genre
    LEFT JOIN tv_show_genres AS sg
    ON (sg.genre_id = genre.id)
    LEFT JOIN tv_shows AS shows
    ON (shows.id = sg.show_id)
    WHERE shows.title = 'Dexter';