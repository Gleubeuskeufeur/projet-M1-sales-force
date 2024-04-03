import csv
import sqlite3
import os



n = 30



def csv_vers_sql(chemin_csv, chemin_db):
    # Connexion à la base de données SQLite au chemin spécifié
    conn = sqlite3.connect(chemin_db)
    
    
    
    with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        premiere_ligne = next(lecteur_csv)  # Première ligne pour les en-têtes
        nom_table = 'db_Lille'
        colonnes = [premiere_ligne[15], premiere_ligne[4], premiere_ligne[31], premiere_ligne[37]]
        # Ajout de dix colonnes supplémentaires pour les valeurs répétées de premiere_ligne[4]
        colonnes_supplementaires = [f"Vente_{i} TEXT" for i in range(1, n + 1)]
        # Construction de la chaîne de caractères pour les colonnes SQL avec PRIMARY KEY
        nom_colonne_primaire = premiere_ligne[15].replace(' ', '_')
        colonnes_sql = ', '.join([f"{nom_colonne_primaire} TEXT PRIMARY KEY"] + [f"{col.replace(' ', '_')} TEXT" for col in colonnes if col != premiere_ligne[15]] + colonnes_supplementaires)

        
        
        cur = conn.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
        cur.execute(f"CREATE TABLE {nom_table} ({colonnes_sql})")
        
        
        
        # Préparation de la commande SQL INSERT INTO
        placeholders = ', '.join(['?' for _ in colonnes + [''] * n])# Ajout des placeholders pour les colonnes supplémentaires
        sql_insert = f"INSERT INTO {nom_table} VALUES ({placeholders})"
        
        
        for ligne in lecteur_csv:
            valeurs_cles_primaire = ligne[15]  # Pas besoin de faire une liste ici
            valeurs_a_inserer = [valeurs_cles_primaire, ligne[4], ligne[31], ligne[37]] + [''] * n  # Ajoutez la clé primaire ici
            cur.execute(f"SELECT * FROM {nom_table} WHERE {nom_colonne_primaire} = ?", (valeurs_cles_primaire,))
            existing_row = cur.fetchone()
            
            
            
            if existing_row is None:
                cur.execute(sql_insert, valeurs_a_inserer)
                
                
                                
            else:
                # Mise à jour de la ligne existante avec la nouvelle valeur dans la première colonne vide
                for i in range(len(colonnes), len(existing_row)):
                    if existing_row[i] == '':
                        cur.execute(f"UPDATE {nom_table} SET Vente_{i-len(colonnes)+1} = ? WHERE {nom_colonne_primaire} = ?", (valeurs_a_inserer[1], valeurs_a_inserer[0]))
                        break
                
                
                
            '''   
            else:
                # Ici, nous supposons que vous voulez concaténer les valeurs des colonnes répétées
                # Cela nécessiterait de modifier la structure de votre table pour supporter ces données concaténées
                # ou d'avoir une logique spécifique pour gérer ce cas.
                updated_values = [existing_row[i] + ', ' + valeurs_a_inserer[i] for i in range(1, len(valeurs_a_inserer))]
                sql_update = f"UPDATE {nom_table} SET {colonnes[1].replace(' ', '_')} = ?, {colonnes[2].replace(' ', '_')} = ?, {colonnes[3].replace(' ', '_')} = ? WHERE {nom_colonne_primaire} = ?"
                cur.execute(sql_update, updated_values + [valeurs_a_inserer[0]])
            '''
            
            
            

        
        
        
        conn.commit()
    conn.close()



emplacement_db = 'C://Users//griii//Documents//IS_P6_Projet_Sales_Force_V1//bases_de_donnees'
if not os.path.exists(emplacement_db):
    os.makedirs(emplacement_db)




liste_chemin_csv = [
    'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_0_Lille.csv',
    'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_1_Lyon.csv',
    'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_2_Rennes.csv'
]



[chemin_csv_1,chemin_csv_2,chemin_csv_3] = liste_chemin_csv



#for chemin_csv in liste_chemin_csv:
nom_fichier_db = os.path.basename(chemin_csv_1).replace('.csv', '_db.db')
chemin_complet_db = os.path.join(emplacement_db, nom_fichier_db)
csv_vers_sql(chemin_csv_1, chemin_complet_db)