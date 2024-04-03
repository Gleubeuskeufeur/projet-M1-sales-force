import csv
import sqlite3
import os



n = 100
liste_chemin_csv = [
    'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_0_Lille.csv',
    'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_1_Lyon.csv',
    'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_2_Rennes.csv'
]
#[chemin_csv_1,chemin_csv_2,chemin_csv_3] = liste_chemin_csv



def csv_vers_sql(liste_chemin_csv, chemin_complet_db):
    # Connexion à la base de données SQLite au chemin spécifié
    conn = sqlite3.connect(chemin_complet_db)
    
    
    for chemin_csv in liste_chemin_csv :
        with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            premiere_ligne = next(lecteur_csv)  # Première ligne pour les en-têtes
            # Séparation du chemin en segments basés sur le caractère '/'
            segments = chemin_csv.split('//')
            # Extraction du nom de fichier (dernier segment)
            nom_fichier = segments[-1]
            # Séparation du nom de fichier en segments basés sur le caractère '_'
            parties_nom_fichier = nom_fichier.split('_')
            # Le mot d'intérêt est l'avant-dernier segment après la séparation par '_'
            mot_interet = parties_nom_fichier[-1]
            # Séparation pour enlever l'extension '.csv'
            mot_inter = mot_interet.split('.')
            # Le mot voulu est avant l'extension '.csv'
            nom_table = mot_inter[0]  # Utilisation de [0] pour obtenir le premier élément
            # Colonnes sélectionnées avec types et tailles appropriées
            colonnes = [premiere_ligne[15],premiere_ligne[1], premiere_ligne[4], premiere_ligne[31], premiere_ligne[37]]
            # Ajout de dix colonnes supplémentaires pour les valeurs répétées de premiere_ligne[4]
            colonnes_supplementaires = [f"Date_{i} DATE, Vente_{i} VARCHAR, Surface_Reelle_Bati_{i} VARCHAR, Surface_Terrain_{i} VARCHAR" for i in range(1, n + 1)]
            # Construction de la chaîne de caractères pour les colonnes SQL avec PRIMARY KEY
            nom_colonne_primaire = premiere_ligne[15].replace(' ', '_')
            colonnes_sql = ', '.join([f"{nom_colonne_primaire} TEXT PRIMARY KEY"] + [f"{col.replace(' ', '_')} TEXT" for col in colonnes if col != premiere_ligne[15]] + colonnes_supplementaires)
    
            
            
            cur = conn.cursor()
            cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
            cur.execute(f"CREATE TABLE {nom_table} ({colonnes_sql})")
            
            
            
            # Préparation de la commande SQL INSERT INTO
            placeholders = ', '.join(['?' for _ in colonnes + [''] * n*4])# Ajout des placeholders pour les colonnes supplémentaires
            sql_insert = f"INSERT INTO {nom_table} VALUES ({placeholders})"
            
            
            for ligne in lecteur_csv:
                # Ignorer les lignes où ligne[31] ou ligne[37] est vide et on saute la ligne 1
                if ligne[31] == '' or ligne[37] == '' or ligne[0] == 'id_mutation' :
                    continue  # Passe à la prochaine itération sans insérer cette ligne
                
                
                
                else :
                    valeurs_cles_primaire = ligne[15]
                    valeurs_a_inserer = [valeurs_cles_primaire, ligne[1], ligne[4], ligne[31], ligne[37]] + [''] * n*4
                    
                    cur.execute(f"SELECT * FROM {nom_table} WHERE {nom_colonne_primaire} = ?", (valeurs_cles_primaire,))
                    existing_row = cur.fetchone()
                    
                    
                    
                    if existing_row is None:
                        cur.execute(sql_insert, valeurs_a_inserer)
                        
                        
                                        
                    else :
                        # Mise à jour de la ligne existante avec la nouvelle valeur dans la première colonne vide
                        for i in range(5, len(existing_row), 4):  # Commencez à 5 car les premières colonnes sont fixes et ignorez par quadruplet
                            if existing_row[i] == '':
                                index_colonne = (i - 5) // 4 + 1  # Calculer l'index du quadruplet vide
                                cur.execute(f"UPDATE {nom_table} SET Date_{index_colonne} = ?, Vente_{index_colonne} = ?, Surface_Reelle_Bati_{index_colonne} = ?, Surface_Terrain_{index_colonne} = ? WHERE {nom_colonne_primaire} = ?", (valeurs_a_inserer[1], valeurs_a_inserer[2], valeurs_a_inserer[3], valeurs_a_inserer[4], valeurs_cles_primaire))
                                break
                


            conn.commit()
    conn.close()



emplacement_db = 'C://Users//griii//Documents//IS_P6_Projet_Sales_Force_V1//bases_de_donnees'
if not os.path.exists(emplacement_db):
    os.makedirs(emplacement_db)



#for chemin_csv in liste_chemin_csv:
chemin_complet_db = os.path.join(emplacement_db, 'Ma_Base_De_Donnees_v2.db')
csv_vers_sql(liste_chemin_csv, chemin_complet_db)