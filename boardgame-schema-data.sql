drop database if exists boardgame;
create database boardgame;
use boardgame;

create table boardgame(
boardgame_id int primary key auto_increment,
id int,
boardgame_name varchar(255) not null,
yearpublished int
);

create table boardgame_primary(
boardgame_primary_id int primary key auto_increment,
boardgame_id int,

boardgame_rank int,
bayesaverage float,
average float,
usersrated int,
is_expansion boolean,
abstracts_rank int,
cgs_rank int,
childrensgames_rank int,
familygames_rank int,
partygames_rank int,
strategygames_rank int, 
thematic_rank int,
wargames_rank int,

foreign key (boardgame_id) references boardgame(boardgame_id)
);

create table boardgame_secondary(
boardgame_secondary_id int primary key auto_increment,
boardgame_id int,

min_players int,
max_players int,
play_time int,
min_age int,
users_rated int,
rating_average float,
bgg_rank int,
complexity_average float,
owned_users int,

foreign key (boardgame_id) references boardgame(boardgame_id)
);