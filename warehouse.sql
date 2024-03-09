-- delete all rows from the warehouse_material table and reset id
TRUNCATE TABLE warehouse_material RESTART IDENTITY CASCADE;
-- insert new rows into warehouse_material table
INSERT INTO warehouse_material (title)
VALUES
	('Mato'),
	('Ip'),
	('Tugma'),
	('Zamok');


-- delete all rows from the warehouse_product table and reset id
TRUNCATE TABLE warehouse_product RESTART IDENTITY CASCADE;
-- alter guid data type to uuid and set default uuid generator
ALTER TABLE warehouse_product
	ALTER COLUMN guid TYPE uuid,
	ALTER COLUMN guid SET DEFAULT gen_random_uuid();
-- insert new rows into warehouse_product table
INSERT INTO warehouse_product (title)
VALUES
	('Koylak'),
	('Shim');


-- delete all rows from the warehouse_productmaterial table and reset id
TRUNCATE TABLE warehouse_productmaterial RESTART IDENTITY;
-- delete constraint if it exists
ALTER TABLE warehouse_productmaterial DROP CONSTRAINT IF EXISTS numeric_quantity;
-- add constraint to check that quantity column only contains integer or decimal value
ALTER TABLE warehouse_productmaterial ADD CONSTRAINT numeric_quantity CHECK(quantity ~ '^\d*[,.]?\d*$');
--insert new rows into warehouse_product_material table
INSERT INTO warehouse_productmaterial (quantity, material_id, product_id, quantity_type)
VALUES
	('0.8', 1, 1, 'MTSQ'),
	('5', 3, 1, 'PC'),
	('10', 2, 1, 'MT'),
	('1.4', 1, 2, 'MTSQ'),
	('15', 2, 2, 'MT'),
	('1', 4, 2, 'PC');


--delete all rows from the warehouse_warehouse table and reset id
TRUNCATE TABLE warehouse_warehouse RESTART IDENTITY;
--insert new rows into warehouse_warehouse table
INSERT INTO warehouse_warehouse (remainder, price, material_id)
VALUES
	(12, 1500, 1),
	(200, 1600, 1),
	(40, 500, 2),
	(300, 550, 2),
	(500, 300, 3),
	(1000, 2000, 4);
	