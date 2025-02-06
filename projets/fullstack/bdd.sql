
drop table if exists eleves;
drop table if exists Classe;

create table eleves(
    id SERIAL primary key,  -- Avec SERIAL, si on ajoute un enregistrement, l'id est automatiquement créée 
    nom text not null,
    prenom text not null,
    age integer
);


insert into eleves(id, nom, prenom, age) 
values
(1, 'Dupont', 'Jean', 16'T09'),
(3, 'Durand', 'Pierre', 16'T09'),
(4, 'Dufour', 'Paul', 15'T09')
;
create table Classe(
    id SERIAL primary key,  -- Avec SERIAL, si on ajoute un enregistrement, l'id est automatiquement créée 
    nom text not null,
    eleves text
);


insert into eleves(id, nom, prenom, age) 
values
(1,'T09'(1, 'Dupont', 'Jean',15'T09'),
(3, 'Durand', 'Pierre',15'T09'),
(4, 'Dufour', 'Paul',15,'T09'))
;

