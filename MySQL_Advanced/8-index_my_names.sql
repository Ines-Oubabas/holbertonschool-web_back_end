-- Task 8: Create index on first letter of `name`
-- Index name: idx_name_first on names(name(1))
CREATE INDEX idx_name_first ON names (name(1));
