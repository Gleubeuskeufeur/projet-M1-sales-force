import csv
import sqlite3



# Chemin vers votre fichier CSV
origin_path = r"C:\Users\griii\Documents\IS_P6_Projet_Sales_Force\Données_point_virgule_csv"
#origin_path = r"C:\Users\griii\Documents\IS_P6_Projet_Sales_Force\Données_virgule_csv"



destination_path = r"C:\Users\griii\Documents\IS_P6_Projet_Sales_Force\Données_converti"
# Nom de la base de données SQLite (sera créée si elle n'existe pas)
ma_base_de_donnees = 'bse_de_données_pour_batiments.db'



# Connexion à la base de données SQLite
connection_a_la_base_de_donnees = sqlite3.connect(ma_base_de_donnees)
curseur = connection_a_la_base_de_donnees.cursor()



# Créer une table
curseur.execute('''
CREATE TABLE IF NOT EXISTS table_batiment (
    id INTEGER PRIMARY KEY,
    colonne1 TEXT,
    colonne2 TEXT,
    colonne3 INTEGER
)
''')



# Lire le fichier CSV et insérer les données dans la table SQL
with open(origin_path, 'r', encoding='utf-8') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv) # Utiliser DictReader pour faciliter l'insertion
    
    for ligne in lecteur_csv:
        # Adaptez les champs et la table selon vos besoins
        curseur.execute('''
        INSERT INTO ma_table (colonne1, colonne2, colonne3) VALUES (?, ?, ?)
        ''', (ligne['En-tête1'], ligne['En-tête2'], ligne['En-tête3']))
        
        
        
# Valider les changements et fermer la connexion
connection_a_la_base_de_donnees.commit()
connection_a_la_base_de_donnees.close()



print("Les données CSV ont été importées avec succès dans la base de données SQL.")
