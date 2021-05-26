import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.width', 700)
pd.set_option('display.max_columns', 20)

# #import CSV
# gas = pd.read_csv('gas_prices.csv')
#
# plt.figure(figsize=(8, 5))
#
# #Title
# plt.title('Gas Prices Over Time (In USD)', fontdict={'fontweight': 'bold', 'fontsize': 18})
#
# plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
# plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
# plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
# plt.plot(gas.Year, gas.Australia, 'y.-', label='Canada')
#
# # # Another to plot many Values!
# # countries_to_look_at = ['Australia', 'USA', 'Canada','South Korea']
# # for country in gas[1:]:
# #     if country in countries_to_look_at:
# #         plt.plot(gas.Year, gas[country], marker='.')
#
#
# print(gas.Year[::3])
#
# plt.xticks(gas.Year[::3].to_list()+[2011])
#
# plt.xlabel('Year')
# plt.ylabel('US Dollars')
#
# plt.legend()
#
# plt.savefig('Gas_price_figure.png', dpi=300)
#
# plt.show()


### Load fifa Data

fifa = pd.read_csv('fifa_data.csv')
# print(fifa.head(5))

##Histograms

# bins = [40, 50, 60, 70, 80, 90, 100]
#
# plt.hist(fifa.Overall, bins, color='#abcdef')
#
# plt.xticks(bins)
#
# plt.ylabel('Number of Players')
# plt.xlabel('Skill Level')
# plt.title('Distribution of Player Skill in FIFA 2018')
#
#
# plt.show()

### Pie Chart 1
# left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
# right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
#
# labels = ['left', 'Right']
# colors = ['#abcedf', '#aabbcc']
#
# plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')
#
# plt.title('Foot Preference of FIFA Players')
#
# plt.show()


### Pie Chart 2

# fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
#
# plt.style.use('ggplot')
#
# light = fifa.loc[fifa.Weight < 125].count()[0]
# light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
# medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
# medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
# heavy = fifa.loc[(fifa.Weight >= 200)].count()[0]
#
# weights = [light,light_medium, medium, medium_heavy, heavy]
# label = ['under 125', '125-150', '150-175', '175-200', 'over 200']
# explode = (.4, .2, 0, 0, .4)
#
# plt.title('Weight of Professional Soccer Players (lbs)')
#
# plt.pie(weights, labels=label, explode=explode, pctdistance=0.8, autopct='%.2f %%')
# plt.show()

plt.style.use('default')

plt.figure(figsize=(5, 8))

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']

label = ['FC Barcelona', 'Real Madrid', 'NE Revolution']

boxes = plt.boxplot([barcelona, madrid, revs], labels=label, patch_artist=True, medianprops={'linewidth': 2})

colors = []
for box in boxes['boxes']:
    # set edge color
    box.set(color='#4286f4', linewidth=2)

    # Change fill color
    box.set(facecolor='#e0e0e0e0')

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')


print(barcelona)

plt.show()