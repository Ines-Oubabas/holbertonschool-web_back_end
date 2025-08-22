-- Task 2: Rank country origins of bands by total (non-unique) fans
-- Columns returned: origin, nb_fans
SELECT
  origin,
  SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
