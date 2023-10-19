-- Lists all shows without the genre Comedy
SELECT DISTINCT shows.title FROM tv_shows AS shows
    LEFT JOIN tv_show_genres AS mix
    ON shows.id = mix.show_id

    LEFT JOIN tv_genres AS genres
    ON genres.id = mix.genre_id
    WHERE shows.title NOT IN
    (SELECT shows.title FROM tv_shows AS shows
        INNER JOIN tv_show_genres AS mix
        ON shows.id = mix.show_id

        INNER JOIN tv_genres AS genres
        ON genres.id = mix.genre_id

        WHERE genres.name = 'Comedy')
ORDER BY shows.title ASC;
