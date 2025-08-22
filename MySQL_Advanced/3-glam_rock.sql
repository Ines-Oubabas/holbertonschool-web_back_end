-- Task 3: List all bands with Glam rock as main style, ranked by longevity (in years)
-- Columns returned: band_name, lifespan
-- Longevity computed from formed and split (use current year when split IS NULL)
SELECT
  band_name,
  (COALESCE(split, YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC, band_name ASC;
