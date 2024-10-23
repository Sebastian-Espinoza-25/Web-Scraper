DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS Tornillos;
DROP TABLE IF EXISTS Arte;
DROP TABLE IF EXISTS Esculturas;
DROP TABLE IF EXISTS user_content_selection;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE Tornillos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Producto TEXT NOT NULL,
  Precio REAL NOT NULL
);

CREATE TABLE Arte (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Titulo TEXT NOT NULL,
  Precio TEXT NOT NULL
);

CREATE TABLE Esculturas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Producto TEXT NOT NULL,
  Precio TEXT NOT NULL
);

-- Nueva tabla para almacenar las selecciones de contenido de los usuarios
CREATE TABLE user_content_selection (
  user_id INTEGER,
  content_type TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
