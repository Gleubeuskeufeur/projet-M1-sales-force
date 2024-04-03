import os

def convert_txt_to_dat(txt_file, dat_file, nom):
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    # Récupération des données
    C = int(lines[0].strip())  # Première valeur C
    n = int(lines[1].strip())  # Deuxième valeur n
    T = [int(line.strip()) for line in lines[2:n+2]]  # Temps de traitement des tâches

    # Récupération des conditions
    W = []
    for line in lines[n+2:]:
        if line.strip() == "-1,-1":
            break
        W.append(line.strip())

            # Écriture dans le fichier .dat
    with open(dat_file, 'w') as f:
        f.write (f"Nom =\"{nom}\";\n")
        f.write(f"C = {C};\n")
        f.write(f"n = {n};\n")
        f.write('T = [')
        f.write(', '.join(map(str, T)))
        f.write('];\n')

        f.write('W = {<')
        f.write('>,<'.join(map(str, W)))
        f.write('>};\n')


def convert_all_csv_to_dat(origin_path, destination_path):
    # Vérifier si le répertoire final existe, sinon le créer
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Parcourir tous les fichiers .txt dans le répertoire d'origine
    file_counter = 1
    for filename in os.listdir(origin_path):
        if filename.endswith(".csv"):
            input_path = os.path.join(origin_path, filename)
            output_path = os.path.join(destination_path, f"{file_counter}.dat")
            nom = filename [:-4]
            convert_txt_to_dat(input_path, output_path, nom)
            print(f"Conversion de {filename} terminée.")
            file_counter += 1

# Répertoire d'origine et répertoire final
origin_path = r"C:\Users\griii\Documents\IS_P6_Projet_Sales_Force\Données_point_virgule_csv"
#origin_path = r"C:\Users\griii\Documents\IS_P6_Projet_Sales_Force\Données_virgule_csv"
destination_path = r"C:\Users\griii\Documents\IS_P6_Projet_Sales_Force\Données_converti"

# Appel de la fonction pour convertir tous les fichiers .txt en .dat
convert_all_csv_to_dat(origin_path, destination_path)