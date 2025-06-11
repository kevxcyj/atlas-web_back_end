-- Lists all bands with Glam rock
SELECT name AS band_name,
       (COALESCE(split, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
