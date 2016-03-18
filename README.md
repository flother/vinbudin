Load the data into PostgreSQL:

    CREATE TABLE vinbudin (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      country_of_origin TEXT,
      district_of_origin TEXT,
      place_of_origin TEXT,
      year INTEGER,
      alcohol_volume DECIMAL(3, 1),
      wine_category TEXT,
      taste_group TEXT,
      is_organic BOOLEAN NOT NULL,
      bottled_volume NUMERIC(6, 1) NOT NULL,
      packaging_closing TEXT,
      container_type TEXT,
      category TEXT NOT NULL,
      sub_category TEXT,
      price INTEGER NOT NULL,
      inventory INTEGER NOT NULL,
      is_on_sale BOOLEAN NOT NULL,
      is_special_order BOOLEAN NOT NULL,
      is_special_reserve BOOLEAN NOT NULL,
      date_on_market DATE NOT NULL,
      is_available BOOLEAN NOT NULL,
      is_gift BOOLEAN NOT NULL
    );
    COPY vinbudin FROM 'data/catalogue.csv' DELIMITER ',' CSV HEADER;
