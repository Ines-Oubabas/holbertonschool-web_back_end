-- Task 3: List all bands with Glam rock as main style, ranked by longevity
-- Columns: band_name, lifespan (in years) using formed and split (0 or NULL = still active)
SELECT
  band_name,
  (COALESCE(NULLIF(split, 0), YEAR(CURDATE())) - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC, band_name ASC;
