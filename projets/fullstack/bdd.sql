
drop table if exists eleves;
drop table if exists Classe;

create table eleves(
    id SERIAL primary key,
    nom text not null,
    prenom text not null,
    age integer,
    classe text
);

insert into eleves(id, nom, prenom, age, classe) 
values
(1, 'Dupont', 'Jean', 16, 'T09'),
(3, 'Durand', 'Pierre', 16, 'T09'),
(4, 'Dufour', 'Paul', 15, 'T09');

create table Classe(
    id SERIAL primary key,
    nom text not null,
);

insert into Classe(id, nom,) 
values
(1, 'T09');