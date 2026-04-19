SELECT price, COUNT(*) FROM crypto GROUP BY price;

SELECT price, AVG(price) OVER() FROM crypto;

SELECT * FROM crypto WHERE price > (SELECT AVG(price) FROM crypto);