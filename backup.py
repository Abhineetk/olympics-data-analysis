data=pd.read_csv('olympics.csv')
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
data.head()
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'], 'summer', 'winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'], 'Both', data['Better_Event'])
data['Better_Event'].value_counts()

top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]


top_10_summer=[]
top_10_winter=[]
top_10=[]


def top_ten(data, col):
    
    #Creating a new list
    country_list=[]
    
    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))
    
    #Returning the top 10 list
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')

common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))


summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=(12,7))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.title('Top 10 Summer')

plt.figure(figsize=(12,7))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])


plt.figure(figsize=(12,7))
plt.bar(winter_df['Country_Name'], winter_df['Total_Medals'])

summer_df['Golden_Ratio']= summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio =summer_df['Golden_Ratio'].max()

summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
summer_country_gold

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold= winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio= max(top_df['Golden_Ratio'])
top_country_gold= top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

data_1=data[:-1]
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1  # Use of position index to handle the ambiguity of having same name columns
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

best=data[data['Country_Name']==best_country]
best.reset_index(drop = True, inplace = True)
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.head()
best.plot.bar(stacked=True)

#Changing the x-axis label
plt.xlabel('United States')

#Changing the y-axis label
plt.ylabel('Medals Tally')

plt.xticks(rotation=45)
