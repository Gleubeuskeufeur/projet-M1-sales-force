import csv
import sqlite3
import os



# Fonction pour créer une table et insérer des données à partir d'un fichier CSV
def csv_vers_sql(liste_chemin, conn):
    
    
    
    for chemin_csv in liste_chemin :
        with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            premiere_ligne = next(lecteur_csv)  # Première ligne
            nom_table = premiere_ligne[1]
            colonnes = [premiere_ligne[4],premiere_ligne[15],premiere_ligne[31],premiere_ligne[37]]
            colonnes_sql = ', '.join([f"{col.replace(' ', '_')} TEXT" for col in colonnes])
            
            
            
            # Création de la chaîne de caractères pour la commande SQL CREATE TABLE
            #colonnes = ', '.join([f"{en_tete.replace(' ', '_')} TEXT" for en_tete in en_tetes])
            cur = conn.cursor()
            cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
            cur.execute(f"CREATE TABLE {nom_table} ({colonnes_sql})")



            # Préparation de la commande SQL INSERT INTO
            placeholders = ', '.join(['?' for _ in colonnes])
            sql_insert = f"INSERT INTO {nom_table} VALUES ({placeholders})"



            # Insertion des données dans la table
            for ligne in lecteur_csv:
                # Sélectionner uniquement les valeurs des colonnes spécifiées pour l'insertion
                valeurs_a_inserer = [ligne[4], ligne[15], ligne[31], ligne[37]]
                cur.execute(sql_insert, valeurs_a_inserer)



            conn.commit()



# Emplacement souhaité pour la base de données
emplacement_db = 'C://Users//griii//Documents//IS_P6_Projet_Sales_Force_V1'
nom_fichier_db = 'ma_base_de_donnees_v2.db'
chemin_complet_db = os.path.join(emplacement_db, nom_fichier_db)



# Vérification de l'existence du répertoire
if not os.path.exists(emplacement_db):
    os.makedirs(emplacement_db)



# Connexion à la base de données SQLite au chemin spécifié
conn = sqlite3.connect(chemin_complet_db)



# Chemins vers vos fichiers CSV
chemin_csv1 = 'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf.csv'
chemin_csv2 = 'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_1.csv'
chemin_csv3 = 'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_2.csv'
liste_chemin = [chemin_csv1, chemin_csv2, chemin_csv3]



# Conversion des fichiers CSV en tables SQL
csv_vers_sql(liste_chemin, conn)



# Fermeture de la connexion à la base de données
conn.close()