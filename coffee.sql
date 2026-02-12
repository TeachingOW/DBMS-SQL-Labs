CREATE TABLE pur (
    purchase_id INT PRIMARY KEY,
    purchase_date DATETIME NOT NULL,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(30) NOT NULL,   -- Coffee, Bagel, Donut
    size VARCHAR(20),                -- Small, Medium, Large (NULL for food)
    quantity INT NOT NULL,
    unit_price DECIMAL(6,2) NOT NULL,
    total_amount DECIMAL(8,2) NOT NULL,
    payment_method VARCHAR(20)       -- Cash, Card, Mobile
);

INSERT INTO pur
(purchase_id, purchase_date, item_name, category, size, quantity, unit_price, total_amount, payment_method) VALUES

(1, '2026-02-10 08:05:00', 'Latte', 'Coffee', 'Medium', 1, 4.00, 4.00, 'Card'),
(2, '2026-02-10 08:12:00', 'Glazed Donut', 'Donut', NULL, 2, 1.20, 2.40, 'Cash'),
(3, '2026-02-10 08:20:00', 'Espresso', 'Coffee', 'Small', 1, 2.50, 2.50, 'Mobile'),
(4, '2026-02-10 08:45:00', 'Plain Bagel', 'Bagel', NULL, 3, 1.50, 4.50, 'Card'),
(5, '2026-02-10 09:02:00', 'Cappuccino', 'Coffee', 'Large', 1, 4.40, 4.40, 'Card'),
(6, '2026-02-10 09:15:00', 'Mocha', 'Coffee', 'Medium', 2, 4.30, 8.60, 'Mobile'),
(7, '2026-02-10 09:32:00', 'Chocolate Donut', 'Donut', NULL, 1, 1.30, 1.30, 'Cash'),
(8, '2026-02-10 09:40:00', 'Everything Bagel', 'Bagel', NULL, 2, 1.90, 3.80, 'Card'),
(9, '2026-02-10 10:05:00', 'Americano', 'Coffee', 'Large', 1, 3.80, 3.80, 'Card'),
(10, '2026-02-10 10:22:00', 'Boston Cream Donut', 'Donut', NULL, 2, 1.50, 3.00, 'Cash'),

(11, '2026-02-10 10:35:00', 'Latte', 'Coffee', 'Small', 1, 3.50, 3.50, 'Mobile'),
(12, '2026-02-10 11:00:00', 'Sesame Bagel', 'Bagel', NULL, 1, 1.70, 1.70, 'Card'),
(13, '2026-02-10 11:18:00', 'Vanilla Frosted Donut', 'Donut', NULL, 3, 1.40, 4.20, 'Cash'),
(14, '2026-02-10 11:45:00', 'Cappuccino', 'Coffee', 'Medium', 2, 3.90, 7.80, 'Card'),
(15, '2026-02-10 12:05:00', 'Blueberry Bagel', 'Bagel', NULL, 1, 2.00, 2.00, 'Mobile'),
(16, '2026-02-10 12:30:00', 'Mocha', 'Coffee', 'Large', 1, 4.80, 4.80, 'Card'),
(17, '2026-02-10 12:45:00', 'Jelly Filled Donut', 'Donut', NULL, 2, 1.45, 2.90, 'Cash'),
(18, '2026-02-10 13:05:00', 'Americano', 'Coffee', 'Medium', 1, 3.30, 3.30, 'Card'),
(19, '2026-02-10 13:20:00', 'Cheese Bagel', 'Bagel', NULL, 2, 2.20, 4.40, 'Mobile'),
(20, '2026-02-10 13:45:00', 'Sprinkle Donut', 'Donut', NULL, 4, 1.35, 5.40, 'Card'),

(21, '2026-02-10 14:10:00', 'Latte', 'Coffee', 'Large', 1, 4.50, 4.50, 'Cash'),
(22, '2026-02-10 14:22:00', 'Glazed Donut', 'Donut', NULL, 1, 1.20, 1.20, 'Card'),
(23, '2026-02-10 14:40:00', 'Whole Wheat Bagel', 'Bagel', NULL, 2, 1.90, 3.80, 'Mobile'),
(24, '2026-02-10 15:05:00', 'Espresso', 'Coffee', 'Small', 2, 2.50, 5.00, 'Card'),
(25, '2026-02-10 15:30:00', 'Maple Donut', 'Donut', NULL, 3, 1.35, 4.05, 'Cash'),
(26, '2026-02-10 15:45:00', 'Cappuccino', 'Coffee', 'Small', 1, 3.40, 3.40, 'Card'),
(27, '2026-02-10 16:10:00', 'Garlic Bagel', 'Bagel', NULL, 1, 1.80, 1.80, 'Mobile'),
(28, '2026-02-10 16:25:00', 'Double Chocolate Donut', 'Donut', NULL, 2, 1.60, 3.20, 'Cash'),
(29, '2026-02-10 16:50:00', 'Mocha', 'Coffee', 'Medium', 1, 4.30, 4.30, 'Card'),
(30, '2026-02-10 17:05:00', 'Onion Bagel', 'Bagel', NULL, 2, 1.85, 3.70, 'Card'),

(31, '2026-02-10 17:20:00', 'Americano', 'Coffee', 'Small', 1, 2.80, 2.80, 'Cash'),
(32, '2026-02-10 17:40:00', 'Coconut Donut', 'Donut', NULL, 2, 1.40, 2.80, 'Mobile'),
(33, '2026-02-10 18:00:00', 'Latte', 'Coffee', 'Medium', 2, 4.00, 8.00, 'Card'),
(34, '2026-02-10 18:15:00', 'Apple Cider Donut', 'Donut', NULL, 1, 1.55, 1.55, 'Cash'),
(35, '2026-02-10 18:30:00', 'Chocolate Chip Bagel', 'Bagel', NULL, 1, 2.30, 2.30, 'Card'),
(36, '2026-02-10 18:45:00', 'Espresso', 'Coffee', 'Large', 1, 3.50, 3.50, 'Mobile'),
(37, '2026-02-10 19:00:00', 'Hazelnut Donut', 'Donut', NULL, 2, 1.60, 3.20, 'Card'),
(38, '2026-02-10 19:15:00', 'Cinnamon Raisin Bagel', 'Bagel', NULL, 2, 2.10, 4.20, 'Cash'),
(39, '2026-02-10 19:30:00', 'Cappuccino', 'Coffee', 'Large', 1, 4.40, 4.40, 'Mobile'),
(40, '2026-02-10 19:50:00', 'Lemon Donut', 'Donut', NULL, 3, 1.45, 4.35, 'Card');
