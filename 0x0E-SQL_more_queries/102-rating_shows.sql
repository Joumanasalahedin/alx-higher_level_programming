-- Lists all shows by their rating
SELECT shows.title, SUM(rates.rate) AS rating
    FROM tv_shows AS SHOWS
        INNER JOIN tv_show_ratings AS rates
        ON shows.id = rates.show_id
GROUP BY shows.title
ORDER BY rating DESC;
