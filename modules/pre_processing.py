from packages_data import *
pd.options.mode.chained_assignment = None

## DATA PRE PROCESSING
# Column names in snake case
coffee.columns = coffee.columns.str.lower().str.replace(' ', '_')

# Replace missing strings with unknown
str_cols = ['farm_name', 'lot_number', 'mill', 'ico_number', 'region', 'producer', 'variety', 'processing_method']

for col in str_cols:
    coffee[col] = coffee[col].fillna('unknown')
    
# Drop row with missing altitude
coffee = coffee.dropna()

# Create new altitude_mean variable 
coffee['altitude_mean'] = coffee['altitude'].str.replace('~', '-').str.replace(' ', '').str.replace('A', '-')

coffee['altitude_mean'] = coffee['altitude_mean'].str.split('-', expand=True).astype('float64').mean(axis=1)

coffee['altitude_mean'] = coffee['altitude_mean'].fillna(coffee['altitude'])

# Combine color variations
yellow_greens = ['yellow green', 'yellow- green', 'yello-green']

for yellow in yellow_greens:
    coffee['color'] = coffee['color'].replace(yellow, 'yellow-green')
    
coffee['color'] = coffee['color'].replace('bluish-green', 'blue-green')

coffee['color'] = coffee['color'].replace(['yellowish', 'pale yellow'], 'pale-yellow')

coffee['color'] = coffee['color'].replace('greenish', 'green')

coffee['color'] = coffee['color'].replace(['brownish', 'browish-green'], 'brown')

# Shorten Tanzania to 'Tanzania'
coffee['country_of_origin'] = coffee['country_of_origin'].replace(
    'Tanzania, United Republic Of', 'Tanzania')

coffee['country_of_origin'].value_counts()

# Replace 'unkow' with 'unkown'
coffee['variety'] = coffee['variety'].replace('unkow', 'unknown')

print('\033[1m Cleaned Coffee Dataset: \033[0m')
print()

print(coffee.info())
display(coffee.head())