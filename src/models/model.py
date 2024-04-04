from os import listdir
from os.path import join


def serializeCSVDB(source_dir):
    """
    """
    json_data = {}
    for city_file in listdir(source_dir):
        city_name = city_file.split('.')[0]
        json_data[city_name] = {}
        city_dict = json_data[city_name]
        with open(join(source_dir, city_file), 'r',encoding='utf-8') as csvfile:
            for line in csvfile.readlines()[1:]:
                split_line = line.split(';')
                id_parcelle = split_line[15]
                postal_code = id_parcelle[:5]
                section = id_parcelle[5:10]
                parcelle = id_parcelle[10:]
                date_mutation = split_line[1]
                if split_line[4] and not split_line[4] == 'valeur_fonciere' and id_parcelle and date_mutation and postal_code and section and parcelle:
                    price = float(split_line[4])
                    if section not in city_dict:
                        city_dict[section] = {parcelle: [(date_mutation, price)]}
                    elif parcelle not in city_dict[section]:
                        city_dict[section][parcelle] = [(date_mutation, price)]
                    else:
                        city_dict[section][parcelle].append((date_mutation, price))
    return json_data
