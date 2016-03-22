CREATE TABLE IF NOT EXISTS vinbudin_products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  supplier TEXT NOT NULL,
  country_of_origin TEXT,
  district_of_origin TEXT,
  place_of_origin TEXT,
  year INTEGER,
  alcohol_volume DECIMAL(3, 1),
  grape TEXT,
  taste_group TEXT,
  is_organic BOOLEAN NOT NULL,
  bottled_volume NUMERIC(6, 1) NOT NULL,
  seal TEXT,
  container TEXT,
  category TEXT NOT NULL,
  sub_category TEXT,
  goes_with TEXT[],
  price INTEGER NOT NULL,
  is_temp_sale BOOLEAN NOT NULL,
  is_special_order BOOLEAN NOT NULL,
  is_special_reserve BOOLEAN NOT NULL,
  date_on_market DATE NOT NULL,
  is_available BOOLEAN NOT NULL,
  is_gift BOOLEAN NOT NULL
);
TRUNCATE TABLE vinbudin_products;
CREATE TABLE IF NOT EXISTS vinbudin_stock (
  product_id INTEGER REFERENCES vinbudin_products(id),
  region TEXT NOT NULL,
  store TEXT NOT NULL,
  quantity INTEGER NOT NULL
);
TRUNCATE TABLE vinbudin_stock;

\COPY vinbudin_products FROM './data/products.csv' DELIMITER ',' CSV HEADER;
\COPY vinbudin_stock FROM './data/stock.csv' DELIMITER ',' CSV HEADER;
