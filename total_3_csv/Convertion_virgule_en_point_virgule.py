def convertion_virgule_en_point_virgule(file_path):
    # Lire le contenu du fichier original
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remplacer les virgules par des points-virgules
    modified_content = content.replace(',', ';')
    
    # Créer un nouveau chemin pour le fichier modifié
    new_file_path = file_path.replace('.csv', '_modified.csv')
    
    # Sauvegarder le contenu modifié dans un nouveau fichier
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)
    print(f'Fichier converti et sauvegardé sous : {new_file_path}')

# Liste des chemins vers vos fichiers CSV
file_paths = file_paths = [
    'C:\\Users\\griii\\Documents\\IS_P6_Projet_Sales_Force_V1\\total_3_csv\\dvf.csv',
    'C:\\Users\\griii\\Documents\\IS_P6_Projet_Sales_Force_V1\\total_3_csv\\dvf_1.csv',
    'C:\\Users\\griii\\Documents\\IS_P6_Projet_Sales_Force_V1\\total_3_csv\\dvf_2.csv'
]

# Convertir chaque fichier
for path in file_paths:
    convertion_virgule_en_point_virgule(path)
