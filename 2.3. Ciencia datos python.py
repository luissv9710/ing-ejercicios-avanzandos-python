# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  2.3 Ejercicios de Programación Avanzada con Python
# Objetivo: Programación y ejecución de instrucciones que se aplican 
#           en la Ciencia de Datos, ETL's y generación de DataFrames para
#           el análisis y graficación de información
# Archivo fuente: [2.3. Ciencia datos python.pdf]
# --------------------------------------------------------------------------

#1
import json
import random
from datetime import date, timedelta
import faker
#2
fake = faker.Faker()
#3
usernames = set()
usernames_no = 1000
# populate the set with 1000 unique usernames
while len(usernames) < usernames_no:
    usernames.add(fake.user_name())
#4
def get_random_name_and_gender():
    skew = .6 # 60% of users will be female
    male = random.random() > skew
    if male:
        return fake.name_male(), 'M'
    else:
        return fake.name_female(), 'F'

def get_users(usernames):
    users = []
    for username in usernames:
        name, gender = get_random_name_and_gender()
        user = {
            'username': username,
            'name': name,
            'gender': gender,
            'email': fake.email(),
            'age': fake.random_int(min=18, max=90),
            'address': fake.address(),
        }
        users.append(json.dumps(user))
    return users

users = get_users(usernames)
print("\n\n")
print(users[:3])

# ------------------------------------------------------------
# ------------------------------------------------------------

#5
def get_type():
    # just some gibberish internal codes
    types = ['AKX', 'BYU', 'GRZ', 'KTR']
    return random.choice(types)

def get_start_end_dates():
    duration = random.randint(1, 2 * 365)
    offset = random.randint(-365, 365)
    start = date.today() - timedelta(days=offset)
    end = start + timedelta(days=duration)

    def _format_date(date_):
        return date_.strftime("%Y%m%d")
    return _format_date(start), _format_date(end)

def get_age():
    age = random.randrange(20, 46, 5)
    diff = random.randrange(5, 26, 5)
    return '{}-{}'.format(age, age + diff)

def get_gender():
    return random.choice(('M', 'F', 'B'))

def get_currency():
    return random.choice(('GBP', 'EUR', 'USD'))

def get_campaign_name():
    separator = '_'
    type_ = get_type()
    start, end = get_start_end_dates()
    age = get_age()
    gender = get_gender()
    currency = get_currency()
    return separator.join((type_, start, end, age, gender, currency))

#6
# campaign data:
# name, budget, spent, clicks, impressions
def get_campaign_data():
    name = get_campaign_name()
    budget = random.randint(10**3, 10**6)
    spent = random.randint(10**2, budget)
    clicks = int(random.triangular(10**2, 10**5, 0.2 * 10**5))
    impressions = int(random.gauss(0.5 * 10**6, 2))
    return {
        'cmp_name': name,
        'cmp_bgt': budget,
        'cmp_spent': spent,
        'cmp_clicks': clicks,
        'cmp_impr': impressions
    }

#7
def get_data(users):
    data = []
    for user in users:
        campaigns = [get_campaign_data()
            for _ in range(random.randint(2, 8))]
        data.append({'user': user, 'campaigns': campaigns})
    return data

#8
rough_data = get_data(users)
print("\n")
print("-------------------------------")
print(rough_data[:2]) # let's take a peek

#9
data = []
for datum in rough_data:
    for campaign in datum['campaigns']:
        campaign.update({'user': datum['user']})
        data.append(campaign)

print("\n")
print("-------------------------------")
print(data[:2]) # let's take another peek

#10
with open('data.json', 'w') as stream:
    stream.write(json.dumps(data))

# ------------------------------------------------------------
# ------------------------------------------------------------

#1
import json
import arrow
import numpy as np
import pandas as pd
from pandas import DataFrame

#2
df = pd.read_json("data.json")
df.head()
#3
df.count()
#4
df.describe()
#5
df.sort_values(by=['cmp_bgt'], ascending=False).head(3)
#6
df.sort_values(by=['cmp_bgt'], ascending=False).tail(3)

#7
def unpack_campaign_name(name):
    # the method assumes data in campaign name is always in good state
    type_, start, end, age, gender, currency = name.split('_')
    start = arrow.get(start, 'YYYYMMDD').date()
    end = arrow.get(end, 'YYYYMMDD').date()
    return type_, start, end, age, gender, currency

campaign_data = df['cmp_name'].apply(unpack_campaign_name)
campaign_cols = ['Type', 'Start', 'End', 'Target Age', 'Target Gender','Currency']
campaign_df = DataFrame(campaign_data.tolist(), columns=campaign_cols, index=df.index)
campaign_df.head(3)

#8
df = df.join(campaign_df)
#9
df[['cmp_name'] + campaign_cols].head(3)

#10
def unpack_user_json(user):
    # the method expects user objects  to have all attributes
    user = json.loads(user.strip())
    return [
        user['username'],
        user['email'],
        user['name'],
        user['gender'],
        user['age'],
        user['address'],
    ]

user_data = df['user'].apply(unpack_user_json)
user_cols = ['username', 'email', 'name', 'gender', 'age', 'address']
user_df = DataFrame(user_data.tolist(), columns=user_cols, index=df.index)

#11
df = df.join(user_df)
#12
df[['user'] + user_cols].head(2)

#13
new_column_names = {
   'cmp_bgt': 'Budget',
   'cmp_spent': 'Spent',
   'cmp_clicks': 'Clicks',
   'cmp_impr': 'Impressions',
}
df.rename(columns=new_column_names, inplace=True)

#14
def calculate_extra_columns(df):
    # Click Through Rate
    df['CTR'] = df['Clicks'] / df['Impressions']
    # Cost Per Click
    df['CPC'] = df['Spent'] / df['Clicks']
    # Cost Per Impression
    df['CPI'] = df['Spent'] / df['Impressions']

calculate_extra_columns(df)

#15
df[['Spent', 'Clicks', 'Impressions','CTR', 'CPC', 'CPI']].head(3)

#16
clicks = df['Clicks'][0]
impressions = df['Impressions'][0]
spent = df['Spent'][0]
CTR = df['CTR'][0]
CPC = df['CPC'][0]
CPI = df['CPI'][0]

print("\n")
print('CTR:', CTR, clicks / impressions)
print('CPC:', CPC, spent / clicks)
print('CPI:', CPI, spent / impressions)

#17
def get_day_of_the_week(day):
    return day.strftime("%A")

def get_duration(row):
    return (row['End'] - row['Start']).days

df['Day of Week'] = df['Start'].apply(get_day_of_the_week)
df['Duration'] = df.apply(get_duration, axis=1)

#18
df[['Start', 'End', 'Duration', 'Day of Week']].head(3)

#19
final_columns = [
    'Type', 'Start', 'End', 'Duration', 'Day of Week', 'Budget',
    'Currency', 'Clicks', 'Impressions', 'Spent', 'CTR', 'CPC',
    'CPI', 'Target Age', 'Target Gender', 'username', 'email',
    'name', 'gender', 'age'
    ]

print("\n")
print(df.columns.tolist())
df = df[final_columns]
#20
df.to_csv('df.csv')
#21
df.to_json('df.json')
#22
df.to_excel('df.xlsx')


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

#24
import matplotlib.pyplot as plt
plt.style.use(['classic', 'ggplot'])
plt.rc('font', family='serif')

#26
df[['Budget', 'Spent', 'Clicks', 'Impressions']].hist(bins=16, figsize=(16, 6), color='yellow');
plt.show()

#27
df[['CTR', 'CPC', 'CPI']].hist(bins=20, figsize=(16, 6), grid=True, color='magenta')
plt.show()

#28
selector = (df.Spent > 0.75 * df.Budget)
df[selector][['Budget', 'Spent', 'Clicks', 'Impressions']].hist(bins=15, figsize=(16, 6), color='blue');
plt.show()

#29
df_weekday = df.groupby('Day of Week')[['Impressions', 'Spent', 'Clicks']].sum()
df_weekday.plot(figsize=(16, 6), subplots=True);
plt.show()


#30
agg_config = {
    'Impressions': ['mean', 'std'],
    'Spent': ['mean', 'std'],
}
df.groupby(['Target Gender', 'Target Age']).agg(agg_config)

#31
df.pivot_table(
    values=['Impressions', 'Clicks', 'Spent'],
    index=['Target Age'],
    columns=['Target Gender'],
    aggfunc='sum'
)


