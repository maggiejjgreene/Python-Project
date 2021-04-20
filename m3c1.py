import pandas as pd
data = pd.read_csv("homelessness.csv")
print(data.head())

homelessness = "data"



# Print the head of the homelessness data
print(data.head())

# Print information about homelessness
print(data.info())

# Print the shape of homelessness
print(data.shape)

# Print a description of homelessness
print(data.describe())

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(data.values)

# Print the column index of homelessness
print(data.columns)

# Print the row index of homelessness
print(data.index)

# Sort homelessness by individual
homelessness_ind = data.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = data.sort_values('family_members', ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = data.sort_values(['region','family_members'], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Select the individuals column
individuals = data["individuals"]

# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = data[['state', 'family_members']]

# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = data[['individuals','state']]

# Print the head of the result
print(ind_state.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = data[data['individuals'] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = data[data['region']=='Mountain']

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = data[(data['family_members'] < 1000) & (data['region'] =='Pacific')]

# See the result
print(fam_lt_1k_pac)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = data[data['region'].isin(['South Atlantic', 'Mid-Atlantic'])]
region=['South Atlantic', 'Mid-Atlantic']

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = data[data['state'].isin(['California','Arizona','Nevada','Utah'])]

# See the result
print(mojave_homelessness)

# Add total col as sum of individuals and family_members
data['total'] = data['individuals'] + data['family_members']

# Add p_individuals col as proportion of individuals
data['p_individuals'] = data['individuals']/data['total']

# See the result
print(homelessness)

# Create indiv_per_10k col as homeless individuals per 10k state
data["indiv_per_10k"] = 10000 * data['individuals'] / data['state_pop']

# Subset rows for indiv_per_10k greater than 20
high_homelessness = data[data['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)



