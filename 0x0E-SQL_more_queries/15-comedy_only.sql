-- Lists all Comedy shows
SELECT shows.title FROM tv_shows AS shows
    INNER JOIN tv_show_genres AS mix
    ON shows.id = mix.show_id

    INNER JOIN tv_genres AS genres
    ON genres.id = mix.genre_id

    WHERE genres.name = 'Comedy'
ORDER BY shows.title ASC;
