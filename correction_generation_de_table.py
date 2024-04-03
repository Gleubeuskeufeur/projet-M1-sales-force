import csv
import sqlite3
import os

# Fonction pour créer une table et insérer des données à partir d'un fichier CSV
def csv_vers_sql(liste_chemin, conn):
    for chemin_csv in liste_chemin:
        with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            premiere_ligne = next(lecteur_csv)  # Première ligne pour obtenir les noms des colonnes
            nom_table = os.path.splitext(os.path.basename(chemin_csv))[0]  # Utiliser le nom du fichier comme nom de la table

            # Définition des colonnes à partir de certains indices de la première ligne
            colonnes = [premiere_ligne[5], premiere_ligne[16], premiere_ligne[20], premiere_ligne[32], premiere_ligne[38]]
            colonnes_sql = ', '.join([f"{col.replace(' ', '_')} TEXT" for col in colonnes])

            # Création de la table avec les colonnes sélectionnées
            cur = conn.cursor()
            cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
            cur.execute(f"CREATE TABLE {nom_table} ({colonnes_sql})")

            # Préparation de la commande SQL INSERT INTO avec le bon nombre de placeholders
            placeholders = ', '.join(['?' for _ in colonnes])
            sql_insert = f"INSERT INTO {nom_table} VALUES ({placeholders})"

            # Insertion des données dans la table
            for ligne in lecteur_csv:
                # Sélectionner uniquement les valeurs des colonnes spécifiées pour l'insertion
                valeurs_a_inserer = [ligne[5], ligne[16], ligne[20], ligne[32], ligne[38]]
                cur.execute(sql_insert, valeurs_a_inserer)

            conn.commit()

# Nom de la base de données SQLite et connexion
nom_db = 'ma_base_de_donnees.db'
conn = sqlite3.connect(nom_db)

# Chemins vers vos fichiers CSV
chemin_csv1 = 'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf.csv'
chemin_csv2 = 'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_1.csv'
chemin_csv3 = 'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_2.csv'
liste_chemin = [chemin_csv1, chemin_csv2, chemin_csv3]

# Conversion des fichiers CSV en tables SQL
csv_vers_sql(liste_chemin, conn)

# Fermeture de la connexion à la base de données
conn.close()




def csv_vers_sql(liste_chemin, conn):
    for chemin_csv in liste_chemin:
        with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            premiere_ligne = next(lecteur_csv)  # Première ligne pour obtenir les noms des colonnes
            nom_table = os.path.splitext(os.path.basename(chemin_csv))[0]  # Utiliser le nom du fichier comme nom de la table

            # Sélection des colonnes à insérer
            indices_colonnes = [5, 16, 20, 32, 38]
            colonnes = [premiere_ligne[i] for i in indices_colonnes]
            colonnes_sql = ', '.join([f"'{col.replace(' ', '_')}' TEXT" for col in colonnes])

            cur = conn.cursor()
            cur.execute(f"DROP TABLE IF EXISTS '{nom_table}'")
            cur.execute(f"CREATE TABLE '{nom_table}' ({colonnes_sql})")

            # Préparation de la commande SQL INSERT INTO avec le bon nombre de placeholders
            placeholders = ', '.join(['?' for _ in indices_colonnes])
            sql_insert = f"INSERT INTO '{nom_table}' VALUES ({placeholders})"

            # Insertion des données dans la table
            for ligne in lecteur_csv:
                valeurs_a_inserer = [ligne[i] for i in indices_colonnes]
                cur.execute(sql_insert, valeurs_a_inserer)

            conn.commit()