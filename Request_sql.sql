CREATE TABLE Livres (
    id_livre INT PRIMARY KEY,
    titre VARCHAR(255),
    id_auteur INT,
    date_publication DATE,
    genre VARCHAR(50),
    disponible BOOLEAN
);



INSERT INTO Livres (id_livre, titre, id_auteur, date_publication, genre, disponible) VALUES
(1, 'La nuit des temps', 1, '1968-01-01', 'Science-fiction', TRUE),
(2, 'Les Misérables', 2, '1862-01-01', 'Roman historique', TRUE);


SELECT * FROM Livres WHERE disponible = TRUE;

