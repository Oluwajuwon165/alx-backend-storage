-- This script lists all bands with Glam rock as their main style, ranked by their longevity

USE holberton;

SELECT band_name, 
       (SUBSTRING_INDEX(lifespan,'-',1)+0) - (SUBSTRING_INDEX(lifespan,'-',-1)+0) AS lifespan 
FROM metal_bands 
WHERE style LIKE '%Glam rock%' 
ORDER BY lifespan DESC;
