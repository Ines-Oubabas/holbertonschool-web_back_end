-- Task 9: Create composite index on first letter of `name` AND `score`
-- Index name: idx_name_first_score on names(name(1), score)
CREATE INDEX idx_name_first_score ON names (name(1), score);
