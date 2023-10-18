# import warnings
# warnings.filterwarnings("ignore")


#!/usr/bin/env python
# coding: utf-8

# In[316]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec
from IPython.display import clear_output
import matplotlib.patches as patches


# In[317]:


df = pd.read_csv("Palestine Body Count.csv")


# In[318]:


df


# In[319]:


df.info()


# In[320]:


df.isna().sum()


# In[321]:


df.columns = df.columns.str.replace(" ", "_")


# In[322]:


df['Israelis_Injuries'].replace(np.nan, int(0), inplace=True)
df['Palestinians_Injuries'].replace(np.nan, int(0), inplace=True)


# In[323]:


df


# In[324]:


df.columns


# In[325]:


df.dropna(subset=["Year", "Month"], inplace=True)


# In[326]:


# Fill the missing values in Palestines_killed and Isrealis_Killed columns with 0
df[['Palestinians_Killed', 'Israelis_Killed']] = df[['Palestinians_Killed', 'Israelis_Killed']].fillna(0).astype(int)


# In[327]:


df.Year = df['Year'].astype(int)


# In[328]:


df.isnull().sum()


# In[329]:


df


# In[ ]:





# In[330]:


# df['Palestinians_Injuries'] = pd.to_numeric(df['Palestinians_Injuries'], errors='coerce')
# df['Israelis_Injuries'] = pd.to_numeric(df['Israelis_Injuries'], errors='coerce')
# df['Palestinians_Killed'] = pd.to_numeric(df['Palestinians_Killed'], errors='coerce')
# df['Israelis_Killed'] = pd.to_numeric(df['Israelis_Killed'], errors='coerce')

# # Create a summary dataframe for yearly and monthly trends
# df_yearly = df.groupby('Year').sum(numeric_only=True).reset_index()
# df_monthly = df.groupby('Month').sum(numeric_only=True).reset_index()

# # Prepare data for proportion calculations
# df_total = df.sum(numeric_only=True)

# # Code for the dashboard
# def create_dashboard():
#     plt.figure(figsize=(27, 17), facecolor='black')
#     plt.suptitle("Conflict Impact Analysis: Palestinian and Israeli Casualties Over Time", fontsize=25, color='yellow', y=0.98)
#     # Adjust the layout to add some margin at the top and bottom
#     plt.subplots_adjust(top=0.92, bottom=0.08)
#     # plt.figure(figsize=(10.8, 6.8), facecolor='black')
#     plt.rcParams['text.color'] = 'white'
#     plt.rcParams['axes.labelcolor'] = 'white'
#     plt.rcParams['xtick.color'] = 'white'
#     plt.rcParams['ytick.color'] = 'white'

#     # plt.rcParams['axes.facecolor'] = 'black'

#     # Yearly Trends
#     plt.subplot(3, 2, 1)
#     sns.lineplot(x='Year', y='Palestinians_Injuries', data=df_yearly, label='Palestinians_Injuries')
#     sns.lineplot(x='Year', y='Israelis_Injuries', data=df_yearly, label='Israelis_Injuries')
#     plt.title('Yearly Trends: Injuries')
#     plt.legend()

#     plt.subplot(3, 2, 2)
#     sns.lineplot(x='Year', y='Palestinians_Killed', data=df_yearly, label='Palestinians_Killed')
#     sns.lineplot(x='Year', y='Israelis_Killed', data=df_yearly, label='Israelis_Killed')
#     plt.title('Yearly Trends: Deaths')
#     plt.legend()

#     df_yearly = df.groupby('Year').sum(numeric_only=True).reset_index()
#     df_monthly = df.groupby('Month').sum(numeric_only=True).reset_index()
#     # Monthly Patterns
#     plt.subplot(3, 2, 3)
#     sns.barplot(x='Month', y='Palestinians_Injuries', data=df_monthly)
#     plt.title('Monthly Patterns: Palestinians Injuries')
#     plt.xticks(rotation=45)

#     plt.subplot(3, 2, 4)
#     sns.barplot(x='Month', y='Israelis_Injuries', data=df_monthly)
#     plt.title('Monthly Patterns: Israelis Injuries')
#     plt.xticks(rotation=45)

#     # Comparative Metrics
#     plt.subplot(3, 2, 5)
#     sns.barplot(x=['Palestinians', 'Israelis'], y=[df_total['Palestinians_Injuries'], df_total['Israelis_Injuries']])
#     plt.title('Comparative Metrics: Injuries')

#     plt.subplot(3, 2, 6)
#     sns.barplot(x=['Palestinians', 'Israelis'], y=[df_total['Palestinians_Killed'], df_total['Israelis_Killed']])
#     plt.title('Comparative Metrics: Deaths')

#     plt.tight_layout()
#     plt.show()

# # Run the function to create the dashboard
# create_dashboard()


# In[ ]:





# In[331]:


# df.to_csv("cleaned_isreal_palestine.csv", index=False)


# ## Empty Sketch

# In[332]:


# # Create the figure
# fig = plt.figure(figsize=(27, 17), facecolor='white')
# plt.rcParams['text.color'] = 'white'
# plt.rcParams['axes.labelcolor'] = 'white'
# plt.rcParams['xtick.color'] = 'white'
# plt.rcParams['ytick.color'] = 'white'

# # Define the gridspec
# gs = gridspec.GridSpec(8, 24)  # 4 rows and 12 columns to provide fine-grained control

# # First row, first column: 3 small divs within 2/12 width, arranged vertically
# ax1a = plt.subplot(gs[0:2, 0:3])
# ax1a.set_title("Small Div 1")
# ax1b = plt.subplot(gs[2:4, 0:3])
# ax1b.set_title("Small Div 2")
# ax1c = plt.subplot(gs[4:6, 0:3])
# ax1c.set_title("Small Div 3")

# # First row, second column: 1 big div (6/12 width)
# ax2 = plt.subplot(gs[0:6, 3:18])
# ax2.set_title("Big Div with Map")

# # First row, third column: 1 div (4/12 width), split into 2
# ax3a = plt.subplot(gs[0:4, 18:24])
# ax3a.set_title("Upper Div")
# ax3b = plt.subplot(gs[4:8, 18:24])
# ax3b.set_title("Lower Div")

# # Second row, first column: 1 div (6/12 width)
# ax4 = plt.subplot(gs[6:8, 0:9])
# ax4.set_title("Second Row, First Column Div")

# # Second row, second column: 1 div (6/12 width)
# ax5 = plt.subplot(gs[6:8, 9:18])
# ax5.set_title("Second Row, Second Column Div")

# plt.tight_layout()
# plt.subplots_adjust(wspace=0.1, hspace=0.1)
# plt.show()


# In[333]:


# Remove extra spaces
df['Month'] = df['Month'].str.strip()

# Replace 'MAY & JUNE' with 'MAY'
df['Month'] = df['Month'].replace('MAY & JUNE', 'MAY')

# Convert to datetime
# df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01', format='%Y-%m-%d', errors='coerce')


# In[334]:


df.Month.unique()


# In[335]:


df


# In[336]:


df.dropna(inplace=True)


# In[337]:


# # df["Palestinians_Injuries"] = df.Palestinians_Injuries.astype(int)
# df.Palestinians_Injuries.unique()

df['Palestinians_Injuries'] = pd.to_numeric(df['Palestinians_Injuries'], errors='coerce')
df['Palestinians_Injuries'].fillna(0, inplace=True) 
df['Israelis_Injuries'] = pd.to_numeric(df['Israelis_Injuries'], errors='coerce')
df['Israelis_Injuries'].fillna(0, inplace=True) 

df[["Palestinians_Injuries", "Israelis_Injuries"]] = df[["Palestinians_Injuries", "Israelis_Injuries"]].astype(int)


# In[338]:


df.info()


# In[339]:


# import geopandas as gpd
# # Read the shapefile or GeoJSON file
# gdf = gpd.read_file("naturalEarth/ne_50m_admin_0_countries.shp")

# # Filter for Israel and Palestine
# gdf_filtered = gdf[gdf['NAME'].isin(['Israel', 'Palestine'])]


# START

# In[ ]:





# # In[340]:


# # Calculate the key metrics for the first three divs
# total_palestinian_injuries = df['Palestinians_Injuries'].sum().astype(int)
# total_palestinian_injuries = f"{total_palestinian_injuries:,}"
# total_israeli_injuries = df['Israelis_Injuries'].sum().astype(int)
# total_israeli_injuries = f"{total_israeli_injuries:,}"

# # Summing up the total killings
# total_killed = df[['Palestinians_Killed', 'Israelis_Killed']].sum()
# # total_killed = f"{total_killed:,}"
# # Calculate total injuries for Palestine and Israel
# total_injuries = df[['Palestinians_Injuries', 'Israelis_Injuries']].sum()
# # total_injuries = f"{total_injuries:,}"

# # Define colors for the wedges
# colors = ['#2171b5', '#fd8d3c']

# df_yearly = df.groupby('Year').sum(numeric_only=True).reset_index()
# df_monthly = df.groupby('Month').sum(numeric_only=True).reset_index()
# # Define the correct order for the months
# month_order = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']

# total_deaths = df['Palestinians_Killed'].sum() + df['Israelis_Killed'].sum()
# total_deaths = f"{total_deaths:,}"


# # Create the figure
# fig = plt.figure(figsize=(30, 20), facecolor='#F0F0F0') #333333 #F0F0F0
# plt.rcParams.update({'font.size': 14, 'font.family': 'Arial', 'text.color': 'brown'})
# plt.rcParams['font.weight'] = 'bold'

# # Define the gridspec
# gs = gridspec.GridSpec(8, 24)  # 4 rows and 12 columns to provide fine-grained control

# # First row, first column: 3 small divs within 2/12 width, arranged vertically
# ax1a = plt.subplot(gs[0:1, 0:3])
# ax1a.text(0.5, 0.8, 'Palestinian Injuries', horizontalalignment='center', verticalalignment='center', color="brown", fontsize=20, fontweight='bold', fontname='Comic Sans MS')
# ax1a.text(0.5, 0.3, f'{total_palestinian_injuries}', horizontalalignment='center', verticalalignment='center', fontsize=40, fontname="Clarendon Blk BT", color='#2171b5', fontweight='bold')
# ax1a.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)

# ax1b = plt.subplot(gs[1:2, 0:3])
# ax1b.text(0.5, 0.8, 'Israelis Injuries', horizontalalignment='center', verticalalignment='center', color="brown", fontsize=24, fontweight='bold', fontname='Comic Sans MS')
# ax1b.text(0.5, 0.3, f'{total_israeli_injuries}', horizontalalignment='center', verticalalignment='center', fontsize=40, color='#2171b5', fontname="Clarendon Blk BT", fontweight='bold')
# ax1b.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)

# ax1c = plt.subplot(gs[2:3, 0:3])
# ax1c.text(0.5, 0.8, 'Deaths', horizontalalignment='center', verticalalignment='center', color="brown", fontsize=24, fontweight='bold', fontname='Comic Sans MS')
# ax1c.text(0.5, 0.3, f'{total_deaths}', horizontalalignment='center', verticalalignment='center', fontsize=40, color='#2171b5', fontweight='bold', fontname="Clarendon Blk BT")
# ax1c.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)


# # Subset of the gridspec for the bar plot
# ax1d = plt.subplot(gs[3:6, 0:3])
# # Sort the data by 'Israelis_Killed' in descending order and take top 5
# top_5_deaths = df.groupby("Year").sum().nlargest(7, 'Israelis_Killed')
# # Extracting the year and death counts
# years = top_5_deaths.index.astype(str).tolist()
# deaths = top_5_deaths["Israelis_Killed"].astype(int).tolist()
# # Combining the two lists to form the cell text
# cell_text = list(map(list, zip(years, deaths)))
# # Plotting the table in ax1d
# ax1d.axis('off')  # Turn off the axis
# ax1d.set_title("Israelis Deaths(year)", fontdict={'color': 'brown', 'weight': 'bold', 'size': 19,'family': 'Comic Sans MS'}, y=0.90)
# # ax1d.title.set_position([.5, 1.05])
# columns = ["Year", "Deaths"]
# # Alternating cell colors
# colors = ['#2171b5', '#fd8d3c']
# cell_colors = [[colors[i % len(colors)] for i in range(len(columns))] for _ in range(len(cell_text))]
# table = ax1d.table(cellText=cell_text, colLabels=columns, loc='center')
# table.auto_set_font_size(False)
# table.set_fontsize(16)  # You can adjust this value for font size
# table.scale(1, 3)  # Adjust the scale for the table cells
# for key, cell in table.get_celld().items():
#     cell.set_edgecolor('#2171b5')  # To keep the border color if you want
#     cell.set_facecolor('none')


# ax1a.set_facecolor('none')
# ax1b.set_facecolor('none')
# ax1c.set_facecolor('none')
# ax1d.set_facecolor('none')
# #################################################################################################
# # Create a subplot within the specified gridspec
# ax_title = plt.subplot(gs[0:1, 3:18])
# ax_title.axis('off')
# title_text = ax_title.text(0.5, 0.8, 'Comparative Analysis of Palestinian and Israeli War Overtime',
#                            ha='center', va='center', fontsize=35, fontweight='bold')

# ###################################################################################################
# # Create a nested GridSpec within ax2's area
# nested_gs = gs[1:5, 3:18].subgridspec(1, 2, wspace=0.1, hspace=0.2)

# # Create the bar plot for total killings in ax2a
# ax2a = plt.subplot(nested_gs[0, 0])
# sns.barplot(x=total_killed.index, y=total_killed.values, ax=ax2a, palette=colors)
# ax2a.set_title('Total Killings: Palestine vs Israel')
# # Add total counts on top of each bar
# for p in ax2a.patches:
#     ax2a.annotate(f"{int(p.get_height())}", 
#                  (p.get_x() + p.get_width() / 2., p.get_height()), 
#                  ha='center', va='center', 
#                  xytext=(0, 10), 
#                  textcoords='offset points')

# # Explicitly set x-axis labels
# ax2a.set_xticklabels(['Palestine Killed', 'Israeli Killed'])
# ax2a.tick_params(axis='x', colors='brown')

# # Common settings for the plot
# ax2a.tick_params(axis='y', labelleft=False)  # Set y-tick label color to white



# # Create the bar plot for total injuries in ax2b
# ax2b = plt.subplot(nested_gs[0, 1])
# barplot_injuries = sns.barplot(x=total_injuries.index, y=total_injuries.values, ax=ax2b, palette=colors)
# ax2b.set_title('Total Injuries: Palestine vs Israel')

# # Explicitly set x-axis labels
# ax2b.set_xticklabels(['Palestine Injured', 'Israeli Injured'])
# ax2b.tick_params(axis='x', colors='brown')

# # Add total counts on top of each bar
# for p in barplot_injuries.patches:
#     barplot_injuries.annotate(f"{int(p.get_height())}", 
#                               (p.get_x() + p.get_width() / 2., p.get_height()), 
#                               ha='center', va='center', 
#                               xytext=(0, 10), 
#                               textcoords='offset points')

# # Common settings for the plot
# ax2b.tick_params(axis='x')  # Set x-tick label color to white
# ax2b.tick_params(axis='y', labelleft=False)  # Set y-tick label color to white


# ax2a.set_facecolor('none')
# ax2b.set_facecolor('none')
# ####################################################################################################
# # Sum the total injuries for Palestinians and Israelis
# total_injuries_palestinians = df['Palestinians_Injuries'].sum()
# total_injuries_israelis = df['Israelis_Injuries'].sum()

# # Sum the total killings for Palestinians and Israelis
# total_killed_palestinians = df['Palestinians_Killed'].sum()
# total_killed_israelis = df['Israelis_Killed'].sum()

# # Update the color of the labels to match the wedges
# # for i, text in enumerate(texts):
# #     text.set_color(colors[i])

# # Create a nested GridSpec within ax3's area
# nested_gs = gs[0:6, 18:24].subgridspec(2, 1, wspace=0.1, hspace=0.2)
# ax3a = plt.subplot(nested_gs[0, 0])
# labels = ['Palestinians Injured', 'Israelis Injured']
# sizes = [total_injuries_palestinians, total_injuries_israelis]
# wedges, texts, autotexts = ax3a.pie(sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.5))
# # ax3a.set_title('Total Injuries: Palestine vs Israel')
# ax3a.legend(labels, loc='best', frameon=False).set_bbox_to_anchor((1.05, 1.05))


# ax3b = plt.subplot(nested_gs[1, 0])
# labels = ['Palestinians Killed', 'Israelis Killed']
# sizes = [total_killed_palestinians, total_killed_israelis]
# wedges, texts, autotexts = ax3b.pie(sizes, labels=None, autopct='%1.1f%%', startangle=90, colors=colors)
# ax3b.legend(labels, loc='best', frameon=False).set_bbox_to_anchor((1.05, 1.05))
# # ax3b.set_title('Total Killings: Palestine vs Israel')



# ax_heatmap = plt.subplot(gs[6:8, 18:24])
# heatmap_gs = gs[6:8, 18:24].subgridspec(1, 1, wspace=0.1, hspace=0.1)
# ax3c = plt.subplot(heatmap_gs[0, 0])
# ax3c.tick_params(axis='y', labelleft=False)
# # Pivot the data to create a matrix of Year x Month
# heatmap_data = df.pivot(index="Year", columns="Month", values="Palestinians_Injuries")
# heatmap_data = heatmap_data.fillna(0)
# # Calculating the key insights
# year_sum = heatmap_data.sum(axis=1)
# month_avg = heatmap_data.mean()

# highest_injury_year = year_sum.idxmax()
# lowest_injury_year = year_sum.idxmin()
# highest_injury_month = month_avg.idxmax()
# lowest_injury_month = month_avg.idxmin()

# # Define a dictionary with font properties
# font = {
#     'family': 'Clarendon Blk BT',
#     'color':  '#2171b5',
#     'weight': 'bold',
#     'size': 25,
# }

# # Summary text with light shadow using '#2171b5'
# shadow_offset_x = 0.095
# shadow_offset_y = 0.495
# title_text = "Injury Summary(Palestinians)"
# # Position for shadow using '#2171b5'
# shadow_offset_x_title = 0.5 - 0.01  
# shadow_offset_y_title = 1.03 + 0.01

# summary_text_shadow = f"""
# \u2022 Highest injuries: \u2022 {highest_injury_year} ({int(year_sum[highest_injury_year])})

# \u2022 Lowest injuries: \u2022 {lowest_injury_year} ({int(year_sum[lowest_injury_year])})

# \u2022 Peak month: \u2022 {highest_injury_month} ({int(month_avg[highest_injury_month])})

# \u2022 Low month: \u2022 {lowest_injury_month} ({int(month_avg[lowest_injury_month])})
# """

# ax3c.text(shadow_offset_x, shadow_offset_y, summary_text_shadow, ha='left', va='center', wrap=True, fontdict=font, color=colors[1])

# # Original summary text using '#fd8d3c'
# ax3c.text(0.1, 0.5, summary_text_shadow, ha='left', va='center', wrap=True, fontdict=font, color=colors[0])
# ax3c.axis('off')
# # Adding shadow to the title
# ax3c.text(shadow_offset_x_title, shadow_offset_y_title, title_text, ha='center', va='center', fontdict=font, color=colors[1], transform=ax3c.transAxes)
# ax3c.set_title(title_text, fontdict={**font, 'color': colors[0]})


# ax3a.set_facecolor("none")
# ax3b.set_facecolor("none")
# ######################################################################################################


# ######################################################################################################

# # Create a subplot for the larger area
# ax_large = plt.subplot(gs[6:8, 0:18])

# # Create a nested GridSpec within the larger subplot
# nested_gs = gs[6:8, 0:18].subgridspec(1, 2, wspace=0.1, hspace=0.1)

# # Create two subplots within the larger subplot
# ax4 = plt.subplot(nested_gs[0, 0])
# #ax5 = plt.subplot(nested_gs[0, 1])

# # ax4.set_title("First Nested Plot")
# #ax5.set_title("Second Nested Plot")

# # Seaborn Line Plot for the 7th div (subplot)
# sns.lineplot(data=df_yearly, x='Year', y='Palestinians_Injuries', marker='o', ax=ax4, label='Palestinians Injuries', palette=colors)
# sns.lineplot(data=df_yearly, x='Year', y='Israelis_Injuries', marker='o', ax=ax4, label='Israelis Injuries', palette=colors)
# sns.lineplot(data=df_yearly, x='Year', y='Palestinians_Killed', marker='o', ax=ax4, label='Palestinians Killed', color='brown')
# sns.lineplot(data=df_yearly, x='Year', y='Israelis_Killed', marker='o', ax=ax4, label='Israelis Killed', palette=colors)

# ax4.legend(frameon=False)


# # Add labels, title, and legend
# ax4.set_xlabel('Year', color='brown')
# ax4.set_ylabel('Number of Injuries')
# ax4.set_title('Injuries and Deaths by Year', color='brown')
# # ax4.legend().set_facecolor('none')
# ax4.set_xlabel('')
# ax4.set_facecolor("none")
# ax4.tick_params(axis='x', colors='brown')
# ax4.tick_params(axis='y', labelleft=False)
# ax4.yaxis.label.set_color('brown')

# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55FF', '#5c3a4d']


# # Monthly Patterns
# ax5 = plt.subplot(gs[6:8, 9:18])
# # sns.barplot(x='Month', y='Palestinians_Injuries', data=df_monthly, ax=ax5, order=month_order, palette=colors)
# sns.barplot(x='Month', y='Palestinians_Injuries', data=df_monthly, hue='Month', ax=ax5, order=month_order, palette=colors, legend=False)
# plt.title('Monthly Patterns: Palestinians Injuries')
# ax5.set_xlabel('')
# plt.xticks(rotation=45, color='brown');
# ax5.set_facecolor('none')
# ax5.tick_params(axis='y', labelleft=False)
# ax5.yaxis.label.set_color('brown')


# for ax in fig.axes:
#     for spine in ax.spines.values():
#         spine.set_edgecolor('#2171b5')
#         spine.set_linewidth(2)

# ########################################################################################################
# fig.text(0.5, 0.5, 'Jerryola1', fontsize=300,  color='gray', alpha=0.1, ha='center', va='center', rotation=45)
# plt.savefig('isreal_palentine_war.png', dpi=300, bbox_inches='tight')
# clear_output()


# In[341]:


# import matplotlib.font_manager
# fpaths = matplotlib.font_manager.findSystemFonts()

# for i in fpaths:
#     f = matplotlib.font_manager.get_font(i)
#     print(f.family_name)


# In[358]:

# END

import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# In[ ]:

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Button("Click me!", color="primary")
        ], width=4),
        dbc.Col([
            dbc.Alert("Hello Bootstrap!", color="success")
        ], width=8)
    ])
])




# In[359]:


fig_injuries = px.bar(df, x=['Palestinian', 'Israeli'], y=[df['Palestinians_Killed'].sum(), df['Israelis_Killed'].sum()],
                      labels={'y':'Injuries', 'x':'Group'}, title='Total Injuries Comparison')


# In[360]:


app.layout = html.Div([
    html.H1("Comparative Analysis Dashboard"),
    dcc.Graph(figure=fig_injuries, id='injuries-bar-chart'),
    # You'll add more components and visualizations as you create them.
])


# In[361]:


if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:



