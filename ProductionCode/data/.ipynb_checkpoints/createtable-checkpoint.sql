DROP TABLE IF EXISTS artist_data;
CREATE TABLE artist_data (
  artist text,
  origin text,
  image_link text
);

DROP TABLE IF EXISTS interpol_data;
CREATE TABLE interpol_data (
  artwork text,
  artist text,
  medium text
);