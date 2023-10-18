-- Lists all shows and all genres linked to that show
SELECT shows.title, genres.name 
    FROM tv_shows AS shows
        LEFT JOIN tv_show_genres AS mix
        ON shows.id = mix.show_id

        LEFT JOIN tv_genres AS genres
        ON genres.id = mix.genre_id
ORDER BY shows.title ASC, genres.name;
