import csv
import sqlite3
import os



# Liste des chemins vers vos fichiers CSV
chemins_csv = ['chemin/vers/csv1.csv', 'chemin/vers/csv2.csv', ...]  # Ajoutez les 25 chemins



# Nom de la base de données SQLite
nom_db = 'ma_base_de_donnees.db'



# Connexion à la base de données SQLite
conn = sqlite3.connect(nom_db)
cur = conn.cursor()



def creer_et_inserer(chemin_csv):
    # Extraire le nom du fichier pour nommer la table
    nom_table = os.path.splitext(os.path.basename(chemin_csv))[0]
    
    
    
    with open(chemin_csv, 'r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        en_tetes = next(lecteur_csv)  # Première ligne pour les noms des colonnes
        
        
        
        # Création de la chaîne de caractères pour la commande SQL CREATE TABLE
        colonnes = ', '.join([f"{en_tete} TEXT" for en_tete in en_tetes])
        cur.execute(f"CREATE TABLE IF NOT EXISTS {nom_table} (id INTEGER PRIMARY KEY AUTOINCREMENT, {colonnes})")
        
        
        
        # Préparation de la commande SQL INSERT INTO
        placeholders = ', '.join(['?' for _ in en_tetes])
        cmd_insertion = f"INSERT INTO {nom_table} ({', '.join(en_tetes)}) VALUES ({placeholders})"
        
        
        
        # Insertion des données
        for ligne in lecteur_csv:
            cur.execute(cmd_insertion, ligne)
        
        
        
        conn.commit()



# Parcourir chaque fichier CSV et effectuer les opérations de création et d'insertion
for chemin in chemins_csv:
    creer_et_inserer(chemin)



# Fermeture de la connexion à la base de données
conn.close()
