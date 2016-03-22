-- PostgreSQL query to get the total number of items for each supplier as a
-- percentage of the total stock, and the price for all those items as a
-- percentage of the sum of all prices.
SELECT
  supplier,
  Round(100 * Sum(supplier_quantity) / Sum(Sum(supplier_quantity)) OVER (), 2) AS stock_share,
  Round(100 * Sum(supplier_price) / Sum(Sum(supplier_price)) OVER (), 2) AS price_share
FROM
  (
    SELECT
      supplier,
      Sum(quantity) AS supplier_quantity,
      Sum(price) AS supplier_price
    FROM
      vinbudin_products p,
      vinbudin_stock s
    WHERE
      p.id = s.product_id
      AND
      quantity > 0
    GROUP BY
      supplier
    ORDER BY
      supplier_quantity DESC
  ) AS sq
GROUP BY
  supplier
ORDER BY
  stock_share DESC
;
