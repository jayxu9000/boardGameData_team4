drop database if exists boardgame;
create database boardgame;
use boardgame;

create table boardgame_primary (
    boardgame_id int primary key auto_increment,
    bgg_id int unique, 
    boardgame_name varchar(255) not null,
    users_rated int,
    year_published int,
    boardgame_rank int,
    bayes_average float,
    average float,
    is_expansion boolean,
    abstracts_rank int null,
    cgs_rank int null,
    childrensgames_rank int null,
    familygames_rank int null,
    partygames_rank int null,
    strategygames_rank int null, 
    thematic_rank int null,
    wargames_rank int null,
    min_players int,
    max_players int,
    play_time int,
    min_age int,
    rating_average float,
    bgg_rank int,
    complexity_average float,
    owned_users int
);

-- create table boardgame_secondary (
--     boardgame_primary_id int primary key auto_increment,
--     boardgame_id int,
    
--     min_players int,
--     max_players int,
--     play_time int,
--     min_age int,
--     complexity_average float,
--     owned_users int,
--     rating_average float,

--     foreign key (boardgame_id) references boardgame(boardgame_id) on delete cascade
-- );
