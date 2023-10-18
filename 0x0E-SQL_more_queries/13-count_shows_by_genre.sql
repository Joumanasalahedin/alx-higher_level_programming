-- Lists all genres and displays the number of shows linked to each
SELECT genres.name AS genre, COUNT(*) AS number_of_shows
    FROM tv_genres AS genres
        INNER JOIN tv_show_genres as mix
        ON genres.id = mix.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
