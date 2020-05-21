import pandas as pd
import time

start = time.time()

file_path = 'C:/Users/Ghassen/Documents/Projects/Immobilier/1_Project/Data_assets/Processed/'
file_name = 'Destination_2015_2019.csv'

df = pd.read_csv(
    file_path + file_name,
    low_memory=False,
    parse_dates=[2],
    squeeze=True
)

# We select only Paris transactions data
df = df[df['Code_postal'] // 1000 == 75]

# And only appartements transactions
df = df[df['Type_local'] == 'Appartement']

# And only purchase transactions
df = df[df['Nature_mutation'] == 'Vente']

#We define a list of columns to drop
columns_to_drop = [
        'No_disposition', 'Nature_mutation', 'No_voie', 'Type_de_voie', 'Voie', 
        'Code_departement', '1er_lot', 'Surface_Carrez_du_1er_lot', '2eme_lot',
        'Surface_Carrez_du_2eme_lot', '3eme_lot', 'Surface_Carrez_du_3eme_lot',
        '4eme_lot', 'Surface_Carrez_du_4eme_lot', '5eme_lot',
        'Surface_Carrez_du_5eme_lot', 'Nombre_de_lots', 'Code_type_local', 'Type_local'
]

df.drop(columns = columns_to_drop, axis=1, inplace = True)

df.to_csv('../Data_assets/Processed/Paris_selection/reduced_data.csv')

print(int(time.time() - start), 'sec')