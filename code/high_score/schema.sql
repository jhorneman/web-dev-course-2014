drop table if exists scores;
create table scores (
  id integer primary key autoincrement,
  player_name text not null,
  score integer
);