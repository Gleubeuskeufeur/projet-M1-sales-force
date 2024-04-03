import csv
import sqlite3
import os



# Fonction pour créer une table et insérer des données à partir d'un fichier CSV
def csv_vers_sql(chemin_csv, conn):
    
    
    #for chemin in liste_chemin :
    with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
        #Extraire le nom du fichier pour nommer la table
        #nom_table = os.path.splitext(os.path.basename(chemin_csv))[0].replace('-', '_').replace(' ', '_')#splitext enleve l'extension
        
        
        
        lecteur_csv = csv.reader(fichier_csv)
        nom_ancien = next(lecteur_csv)[16]
        for ligne in lecteur_csv:
            nom_ancien = nom_actuel
            
            
            if nombre_maison_actuel < nombre_max_de_maison :
                nom_actuel = next(lecteur_csv)[16]
                
                
                
                if nom_actuel == nom_ancien :
                    nombre_maison_actuel = nombre_maison_actuel + 1
                    
                
                    
            else :
                break
        
       
#        for ligne in lecteur:
#            # Accès aux valeurs par leur position
#            print(ligne[0])  # Affiche la première colonne de chaque ligne
        
    
    
    
        # Création de la chaîne de caractères pour la commande SQL CREATE TABLE
        colonnes = ', '.join([f"{en_tete.replace(' ', '_')} TEXT" for en_tete in en_tetes])
        cur = conn.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
        cur.execute(f"CREATE TABLE {nom_table} ({colonnes})")



        # Préparation de la commande SQL INSERT INTO
        placeholders = ', '.join(['?' for _ in en_tetes])
        sql_insert = f"INSERT INTO {nom_table} VALUES ({placeholders})"



        # Insertion des données dans la table
        for ligne in lecteur_csv:
            cur.execute(sql_insert, ligne)



        conn.commit()






# Nom de la base de données SQLite
nom_db = 'ma_base_de_donnees.db'



# Connexion à la base de données SQLite
conn = sqlite3.connect(nom_db)



# Chemins vers vos fichiers CSV
chemin_csv1 = 'chemin/vers/votre/fichier1.csv'



# Conversion des fichiers CSV en tables SQL
csv_vers_sql(chemin_csv1, conn)



# Fermeture de la connexion à la base de données
conn.close()