drop database if exists boardgame;
create database boardgame;
use boardgame;

create table boardgame_primary (
    boardgame_id int primary key auto_increment,
    bgg_id int unique, 
    boardgame_name varchar(255) not null,
    users_rated int,
    year_published int,
    bayes_average float,
    average float,
    is_expansion boolean,
    min_players int,
    max_players int,
    play_time int,
    min_age int,
    rating_average float,
    complexity_average float,
    owned_users int
);

create table boardgame_rank (
    boardgame_rank_id int primary key auto_increment,
    -- boardgame_id int,
    
    boardgame_rank int,
    abstracts_rank int null,
    cgs_rank int null,
    childrensgames_rank int null,
    familygames_rank int null,
    partygames_rank int null,
    strategygames_rank int null, 
    thematic_rank int null,
    wargames_rank int null,
    bgg_rank int

    -- foreign key (boardgame_id) references boardgame_primary(boardgame_id) ON DELETE CASCADE ON UPDATE CASCADE  
);
