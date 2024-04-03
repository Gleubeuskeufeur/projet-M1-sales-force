import csv
import sqlite3
import os

def creer_et_inserer_depuis_csv(chemin_csv, conn):
    """
    Crée une table et insère des données dans une base de données SQLite à partir d'un fichier CSV.
    """
    with open(chemin_csv, mode='r', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        premiere_ligne = next(lecteur_csv)
        nom_table = premiere_ligne[1].replace(' ', '_')
        colonnes = [premiere_ligne[i].replace(' ', '_') for i in [15, 4, 31, 37]]
        colonnes_sql = ', '.join([f"{col} TEXT" for col in colonnes[:-1]] + [f"{colonnes[-1]} TEXT PRIMARY KEY"])
        
        cur = conn.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {nom_table}")
        cur.execute(f"CREATE TABLE {nom_table} ({colonnes_sql})")
        
        sql_insert = f"INSERT INTO {nom_table} ({', '.join(colonnes)}) VALUES ({', '.join(['?' for _ in colonnes])})"
        
        for ligne in lecteur_csv:
            valeurs_a_inserer = [ligne[i] for i in [4, 15, 31, 37]]
            cur.execute(f"SELECT * FROM {nom_table} WHERE {colonnes[-1]} = ?", (valeurs_a_inserer[1],))
            if cur.fetchone() is None:
                cur.execute(sql_insert, valeurs_a_inserer)
        
        conn.commit()

def main():
    emplacement_db = 'C://Users//griii//Documents//IS_P6_Projet_Sales_Force_V1'
    nom_fichier_db = 'ma_base_de_donnees_doc3.db'
    chemin_complet_db = os.path.join(emplacement_db, nom_fichier_db)

    if not os.path.exists(emplacement_db):
        os.makedirs(emplacement_db)

    conn = sqlite3.connect(chemin_complet_db)
    
    chemins_csv = [
        'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf.csv',
        'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_1.csv',
        'C://Users//griii/Documents//IS_P6_Projet_Sales_Force_V1//total_3_csv//dvf_2.csv'
    ]
    
    for chemin_csv in chemins_csv:
        creer_et_inserer_depuis_csv(chemin_csv, conn)

    conn.close()

if __name__ == "__main__":
    main()