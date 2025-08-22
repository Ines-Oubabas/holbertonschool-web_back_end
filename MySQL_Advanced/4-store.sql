-- Task 4: Create trigger that decreases items.quantity after inserting into orders
-- Effect: AFTER INSERT ON orders => UPDATE items.quantity -= NEW.number WHERE items.name = NEW.item_name
DROP TRIGGER IF EXISTS decrease_quantity;
DELIMITER //
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
    SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
END//
DELIMITER ;
