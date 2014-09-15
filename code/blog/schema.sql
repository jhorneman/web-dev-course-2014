drop table if exists authors;
create table authors (
  id   INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

drop table if exists categories;
create table categories (
  id   INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

drop table if exists posts;
create table posts (
	id integer primary key autoincrement,
	author_id integer,
	category_id integer,
  title text,
  content text,
	foreign key(author_id) references authors(id),
	foreign key(category_id) references categories(id)
);
