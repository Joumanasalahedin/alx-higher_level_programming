-- Lists all genres not liniked to the show Dexter
SELECT DISTINCT genres.name FROM tv_genres AS genres
    INNER JOIN tv_show_genres AS mix
    ON genres.id = mix.genre_id

    INNER JOIN tv_shows AS shows
    ON shows.id = mix.show_id
    WHERE genres.name NOT IN
        (SELECT genres.name FROM tv_genres AS genres
            INNER JOIN tv_show_genres AS mix
            ON genres.id = mix.genre_id

            INNER JOIN tv_shows AS shows
            ON shows.id = mix.show_id
            WHERE shows.title = 'Dexter')
ORDER BY genres.name ASC;
