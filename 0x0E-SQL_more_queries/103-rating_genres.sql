-- Lists all genres by their rating
SELECT genres.name, SUM(rates.rate) AS rating
    FROM tv_genres AS genres
        INNER JOIN tv_show_genres AS mix
        ON genres.id = mix.genre_id

        INNER JOIN tv_shows AS shows
        ON shows.id = mix.show_id

        INNER JOIN tv_show_ratings AS rates
        ON shows.id = rates.show_id
GROUP BY genres.name
ORDER BY rating DESC;
