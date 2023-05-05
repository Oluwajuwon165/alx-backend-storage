-- This SQL script lists all bands with Glam rock as their main style, ranked by their longevity

SELECT band_name, (YEAR(MAX(SUBSTRING_INDEX(split, '-', -1))) - YEAR(MIN(Formed))) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
GROUP BY band_name
ORDER BY lifespan DESC;
