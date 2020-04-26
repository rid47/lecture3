SELECT * FROM flights;
SELECT destination,duration from flights;
SELECT destination,duration from flights where destination = "Paris";
SELECT AVG(duration) FROM flights;
SELECT AVG(duration) FROM flights WHERE origin = 'NewYork';
SELECT COUNT(*) FROM flights;
SELECT COUNT(*) FROM flights WHERE origin = 'NewYork';
SELECT MIN(duration) from flights;
SELECT * FROM flights WHERE origin IN ('DRC', 'NewYork');
