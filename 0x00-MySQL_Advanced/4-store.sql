-- Initial
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);

CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);

-- Create the trigger
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END;
