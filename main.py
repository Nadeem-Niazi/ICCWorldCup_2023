import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import streamlit as st
import pyarrow as pa
import ydata_profiling as yd
# i want to ignore warning
import warnings
warnings.filterwarnings('ignore')
import io



st.set_page_config(page_title="Cricket Analysis", page_icon=":bar_chart", layout='wide')

## Title and padding 
st.title(":bar_chart: Cricket World Cup 2023 Analysis")
st.markdown("<style>div.block-container</style>", unsafe_allow_html=True)

## Adding Style.css 
st.markdown(
    '''
   <style>
    .hover-effect {
        color: white;
        background-color: #155630;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        border-radius: 20px;
        transition-property: background-color, color;
        cursor: pointer;
    }
    .hover-effect:hover {
        background-color: #155655;
        color: #FFF;
        
    }
    hr{
    color:white;
    padding:5px;

    }
    </style>
    ''',
    unsafe_allow_html=True
)

def main():
    df=pd.read_csv('./Data/batting_summary.csv')
    
    # '''I can use ydata_profiling because of its key feature which are:

    #  1.Data Overview:
    #  Provides basic statistics for each column, such as data types, number of unique values, missing values, and memory usage.
    
    #  2.Data Visualizations:
    
    #  Visualizes the distributions of numerical columns (e.g., histograms), the frequencies of categorical variables, 
    #  and box plots.

    #  3.Correlations:
    
    #  Highlights correlations between columns to help identify relationships between different variables in the dataset.
    
    #  4.Missing Data Analysis:
   
    #  Displays the amount and pattern of missing values, helping you understand where data is missing you can easily see on web page 
     
    #  that how much values are missing from which columns
    
    #  5.HTML Report:
    
    #  Generates a ready-to-share HTML report that includes all the above insights. This can be saved or shared for collaborative 
    
    #  -------------------HOW TO USE--------------------**
    
    #  First you can select the kernel, but it’s important to note that the **Python version should be 3.10 or below** otherwise it 
    
    # might not work or could cause issues.Once you create an HTML report, you can save it on your local machine or share it.
    
    # I makes HTML File so i can commented these line of code which are given below and use updated version of python 3.13.0 ''' 

    
    st.sidebar.image("images/chmp.webp")
    page = st.sidebar.radio("Select One Of Them", ["Home","Data-Set","EDA"])
    page = page.split(" ")[0]
    if page == "Home":
        
        
        st.write("***********************************************************************")
        st.title("World-Cup 2023 Data Set ")
        st.write(df)
        st.write("***********************************************************************")
        # Create a profile report
        prfile = yd.ProfileReport(df, explorative=True)

        # Save the report to a temporary HTML file
        report_file_path = 'batting_report.html'
        prfile.to_file(report_file_path)

        # Function to render the HTML in Streamlit
        def render_html(file):
            with open(file, 'r', encoding='utf-8') as f:
                return f.read()

        # Use the function to render the report in Streamlit
        html_report = render_html(report_file_path)

        # Display the report in Streamlit
        st.components.v1.html(html_report, height=800, scrolling=True)
        st.write("***********************************************************************")
        
        st.header("World Cup 2023 Dataset Overview")
        st.markdown("""
        ************************
        1. **Match_Between** : The names of the teams that competed in each match.
        ************************
        2. **Team_Innings**  : The name of the team that batted first.
        ************************
        3. **Batting_Position** : The batting order number of each batsman.
        ************************
        4. **Dismissal** : The details of how each player was dismissed, including the bowler responsible.
        ************************
        5. **Runs** : The number of runs scored by each player in each match.
        ************************
        6. **Balls** : The total number of balls faced by each player.
        ************************
        7. **4s** : The total number of fours hit by each player during their innings.
        ************************
        8. **6s** : The total number of sixes hit by each player during their innings.
        ************************
        9. **Strike_Rate** : The strike rate for each player in their respective innings.
        
        """)

        st.write("***********************************************************************")
    
   
    # prfile=yd.ProfileReport(df)
    # prfile.to_file(output_file='./output/batting.html')
    # **************************************************************************
    # 
    # And after i get this html file i can observe that there are two missing value in any clumns...
    # **************************************************************************
    # And in this file i can find Dismissal column have two null value... 
    # **************************************************************************
    # one player has maximum score which are 201 and minimum is 0 and 83 player out on zero score...
    # **************************************************************************
    # One player  playing a maximum of 143 balls in a single innings...
    # **************************************************************************
    # A record of 21 maximum fours in a single match was set by one player...
    # **************************************************************************
    # A record of 11 maximum six in a single match was set by one player...
    # **************************************************************************
    # Now i stop kenrnal with version 3.10.0 and start new kernel with updated version of python...
    # **************************************************************************
    # i get html file using ydata_prfiling so i can commented that block of code...
    # 
    # **************************************************************************
        st.title("Data Set")

        # Display the datasets using Streamlit components
        st.header("Head Value")
        st.write(df.head())

        st.header("Tail Value")
        st.write(df.tail())

        st.header("10 Sample Value")
        st.write(df.sample(10))
        
        st.header("Columns Name")
        st.write(df.columns)

        st.header("Shape Of Data_Set")
        st.write(df.shape)
        
        # Display DataFrame information in Streamlit
        st.header("Information of Data Set")

        # Capture the output of df.info() using StringIO
        buffer = io.StringIO()
        df.info(buf=buffer)
        info = buffer.getvalue()

        # Display the captured info in Streamlit
        st.text(info)
    

        
        # ****************************************************
        # **FROM ABOVE CELL RESULT**
        # ***************************************************
        # **There are two missing value in Dismissal column.**
        # ***************************************************
        # **info function very usefull and will give all information about data set in this data set there are 916 rows and 11 columns.**
        # 
        # **6 columns data type is int and 5 columns data type is object.**
        # ***************************************************
        # 

        
        # # These line of code Show all the columns & rows of data_set
        # pd.set_option('display.max_columns', None)
        # pd.set_option('display.max_rows', None)

        
        # #Another way to find missing values count true means there are two missing value
        # df['Dismissal'].isnull().value_counts()

        
        # missing_dismissal_rows = df[df['Dismissal'].isna()]
        # print(missing_dismissal_rows)
         # Import necessary libraries


        # Title of the app
        st.header("Dataset Columns and Row Viewing ")

        # Checkbox to display all columns and rows
        if st.checkbox("Show all columns and rows"):
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            st.write(df)  # Display the entire dataset if checked

        st.write("we notice that there are two missing value in Dismissal column") 

        st.subheader("Missing Values in Dismissal Column")
        missing_values = df['Dismissal'].isnull().value_counts()
        st.write("Count of Missing Values (True indicates missing):")
        st.write(missing_values)

        # Show rows with missing values in the 'Dismissal' column
        if st.checkbox("Show rows with missing values in Dismissal column"):
            missing_dismissal_rows = df[df['Dismissal'].isna()]
            st.write("Rows with missing values in 'Dismissal' column:")
            st.write(missing_dismissal_rows)

        
        # ************************************
        # **Handle missing Values**
        # ************************************
        # There are many way to handle missing values e.g(mean,median,mod) But in this case
        # 
        # I researched this from various sources and found that there are NaN values in the 'Dismissal' column
        # 
        # like 'c Scott Edwards b Logan Van Beek' and 'Timed out'.Timed out' isn’t the name of a bowler who dismissed Angelo Mathews
        # 
        # rather, it's a rule. If a player doesn’t enter the field within a specified time (2 minutes), they are considered out. 
        # ************************************

        

        # #Filling vAlue
        # df.loc[(df['Match_no'] == 34) & 
        #     (df['Match_Between'] == 'Netherlands vs Afghanistan') & 
        #     (df['Team_Innings'] == 'Afghanistan') & 
        #     (df['Batsman_Name'] == 'Rahmanullah Gurbaz') & 
        #     (df['Dismissal'].isna()), 'Dismissal'] = 'c Scott Edwards b Logan Van Beek'

        

        # df.loc[(df['Match_no'] == 38) & 
        #     (df['Match_Between'] == 'Sri Lanka vs Bangladesh') & 
        #     (df['Team_Innings'] == 'Sri Lanka') & 
        #     (df['Batsman_Name'] == 'Angelo Mathews') & 
        #     (df['Dismissal'].isna()), 'Dismissal'] = 'Timed out'

        # Header for the dataset
        st.header("Data Set with Missing Value Filling")

        # Display dataset before filling missing values
        st.subheader("Data Before Filling Missing Values")
        st.write(df[df['Dismissal'].isna()])

        # Fill missing values based on specific conditions
        df.loc[(df['Match_no'] == 34) & 
            (df['Match_Between'] == 'Netherlands vs Afghanistan') & 
            (df['Team_Innings'] == 'Afghanistan') & 
            (df['Batsman_Name'] == 'Rahmanullah Gurbaz') & 
            (df['Dismissal'].isna()), 'Dismissal'] = 'c Scott Edwards b Logan Van Beek'

        df.loc[(df['Match_no'] == 38) & 
            (df['Match_Between'] == 'Sri Lanka vs Bangladesh') & 
            (df['Team_Innings'] == 'Sri Lanka') & 
            (df['Batsman_Name'] == 'Angelo Mathews') & 
            (df['Dismissal'].isna()), 'Dismissal'] = 'Timed out'
        # Filter the DataFrame to show only the rows where missing values were filled
        filled_dismissal_rows = df[((df['Match_no'] == 34) & (df['Batsman_Name'] == 'Rahmanullah Gurbaz')) |
                           ((df['Match_no'] == 38) & (df['Batsman_Name'] == 'Angelo Mathews'))]

        # Show rows where missing values have been filled for verification
        filled_dismissal_rows = df[(df['Match_no'].isin([34, 38])) & df['Dismissal'].notna()]
        st.subheader("Rows with Filled Dismissal Values")
        st.write(filled_dismissal_rows)
        
        st.subheader("After Filling Missing Values in Dismissal Column")
        st.write(df['Dismissal'].isnull().value_counts())
        
        st.header("Before Strike Rate Error Value (----)")

        st.write(df[(df['Match_no'] == 27) & 
            (df['Match_Between'] == 'Australia vs New Zealand') & 
            (df['Team_Innings'] == 'Australia') & 
            (df['Batsman_Name'] == 'Josh Hazlewood')])
        
        # After that i see strike rate like that --- 
        df.loc[(df['Match_no'] == 27) & 
            (df['Match_Between'] == 'Australia vs New Zealand') & 
            (df['Team_Innings'] == 'Australia') & 
            (df['Batsman_Name'] == 'Josh Hazlewood'), 'Strike_Rate'] = 0.00
        
        st.header("After Strike Rate Filling Value with 0")
        st.write(df[(df['Match_no'] == 27) & 
            (df['Match_Between'] == 'Australia vs New Zealand') & 
            (df['Team_Innings'] == 'Australia') & 
            (df['Batsman_Name'] == 'Josh Hazlewood')])



        
        st.header("Missing Values Count in Each Column")
        st.write(df.isnull().sum())

        
        # ********************************************************
        # I noted from the dataset that all rows are in ascending order according to match numbers, except for match number 47, which is
        # 
        # mixed with match number 10. There is one row for match 10, followed by one for match 47, then again for match 10, and then 47.
        # 
        # I researched the dataset further and found that in one match, each team has 20 players who have batted, even though the rule
        # 
        # allows only 11 players to bat. In matches numbered 10 and 47, 20 players from each team are shown as having batted. I think 
        # 
        # this might be happening due to duplicate values.
        # 
        # ********************************************************

        

        # df_match_10 = df[df['Match_no'] == 10][['Team_Innings', 'Batsman_Name', 'Runs']]
        # # Display the result
        # print("Rows with Match_no 10:")
        # print(df_match_10)

        
        # df_match_47 = df[df['Match_no'] == 47][['Team_Innings', 'Batsman_Name', 'Runs']]
        # # Display the result
        # print("Rows with Match_no 47:")
        # print(df_match_47)
        st.write("I noted from the dataset that all rows are in ascending order according to match numbers, except for match number 47, which is mixed with match number 10.I researched the dataset further and found that in one match, each team has 20 players who have batted, even though the rule allows only 11 players to bat. In matches numbered 10 and 47, 20 players from each team are shown as having batted. I think this might be happening due to duplicate values")
        # Filter for Match_no 10 and display relevant columns
        df_match_10 = df[df['Match_no'] == 10][['Team_Innings', 'Batsman_Name', 'Runs']]
        st.header("Rows with Match_no 10")
        st.write(df_match_10)

        # Filter for Match_no 47 and display relevant columns
        df_match_47 = df[df['Match_no'] == 47][['Team_Innings', 'Batsman_Name', 'Runs']]
        st.header("Rows with Match_no 47")
        st.write(df_match_47)
# ********************************************************
        
        # **************************************
        # Even after dropping the duplicate values, errors were still present in the data set due to incorrect runs being included for
        # 
        # certain players. Therefore, I decided to drop matches numbered 10 and 47, search for the real data myself, and then add the
        # 
        # correct data for match numbers 10 and 47 back into the dataset.
        # **************************************

        
        # Step 1: Filter for Match_no 10 and drop duplicates in 'Batsman_Name', keeping the first occurrence

       
        st.header("Dropping Duplicate Entries for Match_no 10")
        st.write(df[df['Match_no'] == 10].drop_duplicates(subset='Batsman_Name', keep='first'))
        st.write("Even after dropping the duplicate values, errors were still present in the data set due to incorrect runs being included for certain players. Therefore, I decided to drop matches numbered 10 and 47, search for the real data myself, and then add the correct data for match numbers 10 and 47 back into the dataset")
        
        st.header("Create New Data Based on Match_10")
        df = df[df['Match_no'] != 10]

        # Step 2: Create new data for Match_no 10
        new_data = {
            'Match_no': [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
            'Match_Between':['South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia'],
            'Team_Innings':['South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Australia'],
            'Batsman_Name': ['Quinton de Kock','Temba Bavuma (c)','Rassie van der Dussen','Aiden Markram','Heinrich Klaasen','David Miller','Marco Jansen','Kagiso Rabada','Keshav Maharaj','Mitchell Marsh','David Warner','Steven Smith','Marnus Labuschagne','Josh Inglis','Glenn Maxwell','Marcus Stoinis','Mitchell Starc','Pat Cummins (c)','Adam Zampa ','Josh Hazlewood'],
            'Batting_Position': [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10,11],
            'Dismissal': ['b Maxwell','c Warner b Maxwell','c sub (SA Abbott) b Zampa','c Hazlewood b Cummins','c †Inglis b Hazlewood','b Starc','c Warner b Starc','not out','not out','c Bavuma b Jansen','c van der Dussen b Ngidi','lbw b Rabada','c Bavuma b Maharaj','b Rabada','c & b Maharaj','c de Kock b Rabada','c de Kock b Jansen','c Miller b Shamsi','not out','c Rabada b Shamsi'],
            'Runs': [109,35,26,56,29,17,26,0,0,7,13,19,46,5,3,5,27,22,11,2],
            'Balls': [106,55,30,44,27,13,22,1,2,15,27,16,74,4,17,4,51,21,16,2],
            '4s': [8,2,2,7,3,1,3,0,0,0,2,0,3,1,0,1,3,4,1,0],
            '6s': [5,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'Strike_Rate': [102.83,63.64,86.67,127.27,107.41,130.77,118.18,0.0,0.0,46.67,48.15,118.75,62.16,125.00,17.65,125.00,52.94,104.76,68.75,100.00],
            #'Team1': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Team2': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Match_Type	': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Total_Team_Runs':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Extras':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Total_Runs':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

        }

        # Create a new DataFrame from the new data
        df_new = pd.DataFrame(new_data)

        # Step 3: Concatenate the original DataFrame with the new data
        df = pd.concat([df, df_new], ignore_index=True)

        
        df_match_10_updated = df[df['Match_no'] == 10][['Team_Innings', 'Batsman_Name', 'Runs']]
        # Display the result
        st.header("Rows with Match_no 10:")
        st.write(df_match_10_updated)

        st.header("Create New Data Based on Match_47")
        df = df[df['Match_no'] != 47]

        # Step 2: Define new data for Match_no 47
        new_data = {
            'Match_no': [47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47],
            'Match_Between':['South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia','South Africa vs Australia'],
            'Team_Innings':['South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','South Africa','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Australia','Australia'],
            'Batsman_Name': ['Quinton de Kock','Temba Bavuma (c)','Rassie van der Dussen','Aiden Markram','Heinrich Klaasen','David Miller','Marco Jansen','Gerald Coetzee','Keshav Maharaj','Kagiso Rabada','Tabraiz Shamsi','Travis Head','David Warner','Mitchell Marsh','Steven Smith','Marnus Labuschagne','Josh Inglis','Glenn Maxwell','Mitchell Starc','Pat Cummins (c)'],
            'Batting_Position': [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,10,11],
            'Dismissal': ['c Cummins b Hazlewood','c Inglis b Starc','c Smith b Hazlewood','c Warner b Starc','b Head','c Head b Cummins','lbw b Head','c †Inglis b Cummins','c Smith b Starc','c Maxwell b Cummins','not out','b Maharaj','b Markram','c van der Dussen b Rabada','c de Kock b Coetzee','lbw b Shamsi','b Shamsi','b Coetzee','not out','not out'],
            'Runs': [3,0,6,10,47,101,0,19,4,10,1,62,29,0,30,18,1,28,16,14],
            'Balls': [14,4,31,20,48,116,1,39,8,12,5,48,18,6,62,31,5,49,38,29],
            '4s': [0,0,0,2,4,8,0,2,0,0,0,9,1,0,2,2,0,3,2,2],
            '6s': [0,0,0,0,2,5,0,0,0,1,0,2,4,0,0,0,0,0,0,0],
            'Strike_Rate': [21.43,0.00,19.35,50.00,97.92,87.07,0.00,48.72,50.00,83.33,20.00,129.17,161.11,0.00,48.39,58.06,20.00,57.14,42.11,48.28],
            #'Team1': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Team2': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Match_Type	': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Total_Team_Runs':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Extras':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #'Total_Runs':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        }

        # Convert new data to DataFrame
        new_data_df = pd.DataFrame(new_data)

        # Step 3: Append the new data to the original DataFrame
        df = pd.concat([df, new_data_df], ignore_index=True)

        
        df_match_47_updated = df[df['Match_no'] == 47][['Team_Innings', 'Batsman_Name', 'Runs']]
        # Display the result
        st.write("Rows with Match_no 47:")
        st.write(df_match_47_updated)

        # *********************************************
        # **Sorting data set according to match number and batting possition**
        # *********************************************

      
        df.sort_values(by=['Match_no', 'Batting_Position'], inplace=True)

        # Display the sorted DataFrame
        st.header("Sorted Data by Match Number and Batting Position")
        st.write(df)
        
        # ***************************************
        # **I felt the need to do this when I wanted to know which player made a high score against which team.**
        # 
        # **For this reason, I converted the 'Match Between' column into 'Team1' and 'Team2' columns.**
        # ***************************************

        
        df[['Team1','Team2']] = df['Match_Between'].str.split(' vs ', expand=True)
        def match_type(match_no):
            if match_no == 48:
                return 'Final'
            elif match_no in [46, 47]:
                return 'Semi-final'
            else:
                return 'Regular'

        # Apply the function to create a new column 'Match_Type'
        df['Match_Type'] = df['Match_no'].apply(match_type)
        st.header("Updated Data with New Columns Team1 , Team2 and Match_Type")
        st.write(df)

        st.header("Creat Column that have total runs of every that was not in data_set ")
        df['Total_Team_Runs'] = df.groupby(['Match_no', 'Team_Innings'])['Runs'].transform('sum')


        st.header("Now Columns Name are")
        st.write(df.columns)

        
        
        df['Extras'] = 0

        def calculate_extras(row):

            #************************************For ENGLAND Extras*****************************************************

            if ((row['Team1'] == 'England' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 19
            elif ((row['Team1'] == 'England' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 13
            elif ((row['Team1'] == 'England' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 15
            elif ((row['Team1'] == 'England' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 14
            elif ((row['Team1'] == 'England' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 6
            elif ((row['Team1'] == 'England' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 7
            elif ((row['Team1'] == 'England' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 7
            elif ((row['Team1'] == 'England' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 21
            elif ((row['Team1'] == 'England' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 10
            elif ((row['Team1'] == 'England' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'England')) and (row['Team_Innings'] == 'England'):
                return 8
            
            #************************************For AFGHANISTAN Extras*****************************************************
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 9
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 15
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 15
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 16
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 5
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 10
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 8
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 12
            elif ((row['Team1'] == 'Afghanistan' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Afghanistan')) and (row['Team_Innings'] == 'Afghanistan'):
                return 15

            #************************************For PAKISTAN Extras*****************************************************
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 17
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 6
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 19
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 19
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 4
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 26
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 4
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 9
            elif ((row['Team1'] == 'Pakistan' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Pakistan')) and (row['Team_Innings'] == 'Pakistan'):
                return 4
            #************************************For AUSTRALIA Extras*****************************************************

            # We see that Australia and India played final and two time played in world cup so we have two matches extras 
            # and 48 match is the last match that was i compared base on macth no in this line of code

            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Australia')) and (row['Team_Innings']=='Australia' and row['Match_Type'] == 'Final'):
                return 18
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Australia')) and (row['Team_Innings']=='Australia' and row['Match_Type'] == 'Regular'):
                return 12
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 25
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 15
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 10
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 17
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 9
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 2
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 4
            elif ((row['Team1'] == 'Australia' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'Australia')) and (row['Team_Innings'] == 'Australia'):
                return 12
            


            
            #************************************For NEW ZEALAND Extras*****************************************************
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 26
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 10
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 8
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 12
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 26
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 2
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 11
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand'):
                return 13
            
            # INDIA VS NEW ZEALAND PLAYED SAMI FINAL THAT WHY ITS HAVE TWO MATCHES EXTRAS

            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'New Zealand')) and (row['Team_Innings']=='New Zealand' and row['Match_Type'] =='Semi-final'):
                return 29
            elif ((row['Team1'] == 'New Zealand' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'New Zealand')) and (row['Team_Innings'] == 'New Zealand' and row['Match_Type'] =='Regular'):
                return 15

        

            #************************************For SOUTH AFRICA Extras*****************************************************
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 15
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 9
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 21
            
            #AUSTRALIA VS SOUTH AFRICE SEMIFINAL

            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'South Africa')) and (row['Match_Type'] == 'Semi-final' and row['Team_Innings']=='South Africa'):
                return 11
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'South Africa')) and (row['Match_Type'] == 'Regular' and row['Team_Innings']=='South Africa'):
                return 13
            
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 12
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 23
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 10
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 8
            elif ((row['Team1'] == 'South Africa' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'South Africa')) and (row['Team_Innings'] == 'South Africa'):
                return 2
            
            #************************************For INDIA Extras*****************************************************
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'India')) and (row['Team_Innings'] == 'India'):
                return 2
            elif ((row['Team1'] == 'India' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'India')) and (row['Team_Innings'] == 'India'):
                return 7
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'India')) and (row['Team_Innings'] == 'India'):
                return 15
            elif ((row['Team1'] == 'India' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'India')) and (row['Team_Innings'] == 'India'):
                return 26
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'India')) and (row['Team_Innings']=='India' and row['Match_Type']=='Regular'):
                return 8
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'India')) and (row['Team_Innings']=='India' and row['Match_Type']=='Final'):
                return 12
            
            #INDIA VS NEWZEALAND SEMIFINAL
            elif ((row['Team1'] == 'India' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'India')) and (row['Team_Innings']=='India' and row['Match_Type']=='Semi-final' ) :
                return 8
            elif ((row['Team1'] == 'India' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'India')) and  (row['Team_Innings']=='India' and row['Match_Type']=='Regular') :
                return 5
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'India')) and (row['Team_Innings']=='India'):
                return 20
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'India')) and (row['Team_Innings']=='India') :
                return 4
            elif ((row['Team1'] == 'India' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'India')) and (row['Team_Innings']=='India'):
                return 15

            #************************************For SRI LANKA Extras*****************************************************
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 14
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'Sri Lanka'))and (row['Team_Innings']=='Sri Lanka'):
                return 3
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 11
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 20
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 13
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 4
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 7
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings']=='Sri Lanka'):
                return 24
            elif ((row['Team1'] == 'Sri Lanka' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Sri Lanka')) and (row['Team_Innings'] == 'Sri Lanka'):
                return 10
            

            #************************************For BANGLADESH Extras*****************************************************

            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 9
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 7
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 8
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 17
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 24
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 9
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 23
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'Netherlands') or (row['Team1'] == 'Netherlands' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 6
            elif ((row['Team1'] == 'Bangladesh' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Bangladesh')) and (row['Team_Innings']=='Bangladesh'):
                return 6
            

            #************************************For NETHERLANDS Extras*****************************************************
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'Pakistan') or (row['Team1'] == 'Pakistan' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 9
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'England') or (row['Team1'] == 'England' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 8
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'Afghanistan') or (row['Team1'] == 'Afghanistan' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 16
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'South Africa') or (row['Team1'] == 'South Africa' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 32
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'Australia') or (row['Team1'] == 'Australia' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 7
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'New Zealand') or (row['Team1'] == 'New Zealand' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 4
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'Sri Lanka') or (row['Team1'] == 'Sri Lanka' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 33
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'Bangladesh') or (row['Team1'] == 'Bangladesh' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 12
            elif ((row['Team1'] == 'Netherlands' and row['Team2'] == 'India') or (row['Team1'] == 'India' and row['Team2'] == 'Netherlands')) and (row['Team_Innings']=='Netherlands'):
                return 13
            
            # Add more conditions for other teams as needed
            else:
                return 0  # Default if no condition matches

        # Apply the function to create the Extras column
        df['Extras'] = df.apply(calculate_extras, axis=1)
        st.header("In Data_Set Total_Team_Runs give error because Extras not included in that columns")
        st.header("So we creat a new column Extras and add it to the Data_Set")
        st.write(df)

        st.header("Create new column that have Totall Runs with Extras")
        df['Total_Runs'] = df['Total_Team_Runs'] + df['Extras']
        st.write(df)

        st.header("I creat two column Team1_Runs and Team2_Runs")
        df['Team1_Runs'] = df.apply(lambda row: row['Total_Runs'] if row['Team_Innings'] == row['Team1'] else None, axis=1)
        df['Team2_Runs'] = df.apply(lambda row: row['Total_Runs'] if row['Team_Innings'] == row['Team2'] else None, axis=1)
        df['Team1_Runs'] = df.groupby('Match_no')['Team1_Runs'].transform('first').astype(int)
        df['Team2_Runs'] = df.groupby('Match_no')['Team2_Runs'].transform('last').astype(int)

        #df_final = df.drop_duplicates(subset='Match_no')[['Match_no', 'Match_Between', 'Team1', 'Team2', 'Team1_Runs', 'Team2_Runs']]
        #st.write(df_final)
        
        st.write(df)

        st.header("Create Column Winner_Team")

        df['Winner_Team'] = df.apply(
            lambda row: row['Team1'] if row['Team1_Runs'] > row['Team2_Runs'] else (row['Team2'] if row['Team2_Runs'] > row['Team1_Runs'] else 'Tie'),
            axis=1
        )

        # Drop duplicate rows to get a single row per match and display results
        unique_matches = df.drop_duplicates(subset='Match_no').reset_index(drop=True)

        st.write(df)

    elif page =="Data-Set":
        

        df = pd.read_csv('./Data/ICC_World_Cup2023.csv')

        st.header("Updated Accurate Data Set Ready to download without any error")
        st.write(df)

        
        # **************************************************
        # **END_OF_DATA_CLEANING_&_ENGINEERING**
        # *************************************************

        #Now i want to see maximum score one player make in one innings his name and count of 4s and 6s
        #i want to see the player with maximum score in one innings


    
        max_score_row = df.loc[df['Runs'].idxmax()]

        bats_name = max_score_row['Batsman_Name']

        bats_runs = max_score_row['Runs']

        bats_balls = max_score_row['Balls']

        strike_rate = max_score_row['Strike_Rate']

        if max_score_row['Team_Innings']==max_score_row['Team1']:
            batsman_team = max_score_row['Team1']
            opposite_team = max_score_row['Team2']
        else:
            batsman_team=max_score_row['Team2']
            opposite_team=max_score_row['Team1']

        st.header("Heighst Score In One Innings player Information")  
        st.write(f'**{bats_name}** the **{batsman_team}** batsman, scored the highest runs of **{bats_runs}** in **{bats_balls}** balls, achieving a strike rate of **{strike_rate}** against **{opposite_team}**.')

        st.header("Heighest Score in World_Cup 2023")
        st.write(int(df['Total_Runs'].max()))
        heighst=df.loc[df['Total_Runs'].idxmax()]
        mat_n=heighst['Match_no']
        heighst_runs_team=heighst["Total_Runs"]
        if heighst['Team_Innings']==heighst['Team1']:
            team_name = heighst['Team1']
            opposite_team = heighst['Team2']
        else:
            batsman_team=heighst['Team2']
            opposite_team=heighst['Team1']
        st.write(f"In match Number **{mat_n}** The **{team_name}** team has scored the highest **{heighst_runs_team}** runs against **{opposite_team}**.")


        st.header("Lowest Score in world_Cup 2023")  

        st.write(int(df['Total_Runs'].min()))
        lowest=df.loc[df['Total_Runs'].idxmin()]
        mat_nmb=lowest['Match_no']
        # team_name_l=lowest['Team_Innings']
        # opp_team_l=lowest['Team2']
        lowest_runs_team=lowest["Total_Runs"]
        if lowest['Team_Innings']==lowest['Team1']:
            team_name = lowest['Team1']
            opposite_team = lowest['Team2']
        else:
            team_name=lowest['Team2']
            opposite_team=lowest['Team1']

        st.write(f"In match Number **{mat_nmb}** The **{team_name}** team has scored the lowest **{lowest_runs_team}** runs against **{opposite_team}**.")


        

        final_match = df[df['Match_Type'] == 'Final'][['Team1', 'Team2','Winner_Team']]

        # Remove duplicates based on Team1 and Team2
        final_match = final_match.drop_duplicates(subset=['Team1', 'Team2'])

        # Display the final match winners in the Streamlit app
        st.header("Final Match Winners")
        st.write(final_match)

        # Drop duplicate rows to get a single row per match
        unique_matches = df.drop_duplicates(subset='Match_no').reset_index(drop=True)
        # Loop over each unique match to determine and print the winner
        st.header("Match Results")
        for index, row in unique_matches.iterrows():
            team1 = row['Team1']
            team2 = row['Team2']
            team1_runs = row['Team1_Runs']
            team2_runs = row['Team2_Runs']
            match_between = row['Match_Between']
            match_num = row['Match_no']
            
            # Determine the winner
            if team1_runs > team2_runs:
                winner = team1
            elif team2_runs > team1_runs:
                winner = team2
            else:
                winner = "Tie"
            
            
            st.write(f"**Match {match_num}:** {match_between}  Winner Team ==> **{winner}**")
            

        

    
        # **************************************************
        # In above output you see all winner teams
        # **************************************************

        # def get_winner(match_between, match_type):
        #     # Split the input teams and normalize to lowercase
        #     teams = match_between.lower().split(" vs ")

        #     match_type = match_type.lower()

        #     # Filter the dataset based on match criteria, ignoring case and team order
        #     match_data = df[(df['Match_Type'].str.lower() == match_type) & 
        #                     (df['Team1'].str.lower().isin(teams)) & 
        #                     (df['Team2'].str.lower().isin(teams))]

        #     # Check if we found any rows for this match
        #     if match_data.empty:
        #         print("No match found with the given Match_Between and Match_Type.")
        #         return

        #     # Assume Team1 and Team2 scores are the same for all rows of this match
        #     team1 = match_data.iloc[0]['Team1']
        #     team2 = match_data.iloc[0]['Team2']
        #     team1_runs = match_data.iloc[0]['Team1_Runs']
        #     team2_runs = match_data.iloc[0]['Team2_Runs']

        #     # Determine the winner
        #     if team1_runs > team2_runs:
        #         winner = team1
        #     elif team2_runs > team1_runs:
        #         winner = team2
        #     else:
        #         winner = "Tie"

        #     # Output the result
        #     print(f"Match Between: {team1} vs {team2} | Match Type: {match_type.capitalize()} | Winner: {winner}")

        # # Example usage
        # #Enter the value ignoring case and team order

        # match_between_input = input("Enter the Teams Match between like that India vs Australia: ")
        # match_type_input = input("Enter the Match type  Regular  or Semi-final or final : ")

        # # Call the function with user inputs
        # get_winner(match_between_input, match_type_input)
      

# Load your DataFrame here (ensure the path is correct)
# df = pd.read_csv('path_to_your_csv_file.csv')

        def get_winner(match_between, match_type):
            # Split the input teams and normalize to lowercase
            teams = match_between.lower().split(" vs ")
            match_type = match_type.lower()

            # Filter the dataset based on match criteria, ignoring case and team order
            match_data = df[(df['Match_Type'].str.lower() == match_type) & 
                            (df['Team1'].str.lower().isin(teams)) & 
                            (df['Team2'].str.lower().isin(teams))]

            # Check if we found any rows for this match
            if match_data.empty:
                return "No match found with the given Match_Between and Match_Type."

            # Assume Team1 and Team2 scores are the same for all rows of this match
            team1 = match_data.iloc[0]['Team1']
            team2 = match_data.iloc[0]['Team2']
            team1_runs = match_data.iloc[0]['Team1_Runs']
            team2_runs = match_data.iloc[0]['Team2_Runs']

            # Determine the winner
            if team1_runs > team2_runs:
                winner = team1
            elif team2_runs > team1_runs:
                winner = team2
            else:
                winner = "Tie"

            # Return the result as a formatted string
            return f"Match Between: {team1} vs {team2} | Match Type: {match_type.capitalize()} | Winner Team : {winner}"

        # Streamlit app
        st.title("Match Winner Finder")

        # User inputs
        match_between_input = st.text_input("Enter the Teams Match between (e.g India vs Australia):")
        match_type_input = st.selectbox("Select the Match Type:", ["Regular", "Semi-final", "Final"])

        # Button to get the winner
        if st.button("Get Winner"):
            # Call the function with user inputs
            result = get_winner(match_between_input, match_type_input)
            # Display the result
            st.write(result)


        # %% [markdown]
        # ****************************************
        # In above code you give match between column value like australia vs india and match type and get winner team name
        # ****************************************

        # %%
        # semi_final_matches = df[df['Match_Type'].str.lower() == 'semi-final']  # Case insensitive comparison

        # # Use a set to store unique winner teams
        # winner_teams = set()
        # loser = set()
        # # Iterate through the filtered DataFrame and print full rows
        # for index, row in semi_final_matches.iterrows():
            
        #     winner_teams.add(row['Winner_Team'])  # Add winner team to the set

        #     if (row['Team1'] != row['Winner_Team']):
        #         loser.add(row['Team1'])
        #     else:
        #         loser.add(row['Team2'])
        # # Print unique winner teams
        # print('-----------Semi-Final-Match--------------')
        # for winner,los in zip(winner_teams,loser):
        #     print('---------------------------------------')
        #     print("Winner Team", winner,"& Losser Team",los)  

        # # %% [markdown]
        # # **************************************************
        # # Semi final winner teams
        # # **************************************************

        # # %%
        # final_matches = df[df['Match_Type'].str.lower() == 'final']  # Case insensitive comparison

        # # Use a set to store unique winner teams
        # winner_team = set()
        # Total_runs = set()
        # Teams=set()
        # # Iterate through the filtered DataFrame and print full rows
        # for index, row in final_matches.iterrows():
            
        #     winner_team.add(row['Winner_Team'])
        #     Total_runs.add(row['Total_Runs']) 
        #     Teams.add(row['Team_Innings'])  # Add winner team to the set

        # # Print unique winner teams
        # for runs, team in zip(Total_runs, Teams):
        #     print("----------------------------------")
        #     print(f"Final Team {team} Runs: {runs}")
        # print("----------------------------------")
        # for winner in winner_team:
        #     print("Final Winner Team:", winner)  
        # print("----------------------------------")



        # # %% [markdown]
        # # **************************************************
        # # World Cup 2023 Final winner Team
        # # **************************************************

        # # %%
        # # Filter for final matches with case insensitive comparison
        # final_matches = df[df['Match_Type'].str.lower() == 'regular']  # Case insensitive comparison

        # # Use dictionaries to store unique winner and loser matches
        # winner_count = {}
        # loser_count = {}

        # # Iterate through the filtered DataFrame
        # for index, row in final_matches.iterrows():
        #     winner = row['Winner_Team']
        #     loser = row['Team1'] if row['Team1'] != winner else row['Team2']
        #     match_no = row['Match_no']  # Assuming you have a unique identifier for each match
            
        #     # Count unique winners
        #     if winner not in winner_count:
        #         winner_count[winner] = set()  # Initialize a set for the winner
        #     winner_count[winner].add(match_no)

        #     # Count unique losers
        #     if loser not in loser_count:
        #         loser_count[loser] = set()  # Initialize a set for the loser
        #     loser_count[loser].add(match_no)

        # # Print the number of unique wins and losses for each team
        # print('-----------------------------')
        # print("Regular Wins:")
        # print('-----------------------------')
        # for winner, matches in winner_count.items():
        #     print(f"{winner} Wins: {len(matches)} out of 9 matches")
        #     print('-----------------------------------------------')
        # print('-----------------------------')
        # print("Regular Losses:")
        # print('-----------------------------')
        # for loser, matches in loser_count.items():
        #     print(f"{loser} Losses: {len(matches)} out of 9 matches")
        #     print('-------------------------------------------------')

        # # %% [markdown]
        # # **************************************************
        # # In regular matches totall win and lose match out of 9 matches every teams
        # # **************************************************

        # # %%
        # # Filter for final matches with case insensitive comparison
        # final_matches = df[df['Match_Type'].str.lower() == 'regular']  # Case insensitive comparison

        # # Create a dictionary to store unique wins and losses for each team
        # team_stats = {}

        # # Iterate through the filtered DataFrame to determine wins and losses
        # for index, row in final_matches.iterrows():
        #     winner = row['Winner_Team']
        #     match_no = row['Match_no']  # Assuming you have a unique identifier for each match
        #     team1 = row['Team1']
        #     team2 = row['Team2']
            
        #     # Initialize team stats if not already done
        #     if team1 not in team_stats:
        #         team_stats[team1] = {'Wins': set(), 'Losses': set()}
        #     if team2 not in team_stats:
        #         team_stats[team2] = {'Wins': set(), 'Losses': set()}

        #     # Add the match number to the winner's set
        #     team_stats[winner]['Wins'].add(match_no)
            
        #     # Add the match number to the loser's set
        #     if winner == team1:
        #         team_stats[team2]['Losses'].add(match_no)  # Team2 lost
        #     else:
        #         team_stats[team1]['Losses'].add(match_no)  # Team1 lost

        # # Print the number of unique wins and losses for each team
        # for team, stats in team_stats.items():
        #     total_matches=len(stats["Wins"]) + len(stats["Losses"])
        #     print(f"Team {team} Wins {len(stats['Wins'])} and losses {len(stats['Losses'])} Out of {total_matches} matches")
        #     print('-----------------------------------------------------------------------------')

        # %% [markdown]
        # **************************************************
        # In regular matches totall win and lose match out of 9 matches every teams
        # **************************************************

        # %% [markdown]
        # ********************************************************
        # Take User input of match type like final , semi-final and regular then you get result otherwise error shown
        # ********************************************************

        # %%
        # # Get user input for match type
        # user_match_type = input("Enter the match type like final semi-final and regular': ").strip().lower()
        # print('-----------------------------------------------------------------------------')
        # print(f'About {user_match_type} Macthes:')
        # print('-----------------------------------------------------------------------------')
        # # Filter the DataFrame based on the user-provided match type
        # filtered_matches = df[df['Match_Type'].str.lower() == user_match_type]

        # # Create a dictionary to store unique wins and losses for each team
        # team_stats = {}

        # # Iterate through the filtered DataFrame to determine wins and losses
        # for index, row in filtered_matches.iterrows():
        #     winner = row['Winner_Team']
        #     match_no = row['Match_no']  # Assuming you have a unique identifier for each match
        #     team1 = row['Team1']
        #     team2 = row['Team2']
            
        #     # Initialize team stats if not already done
        #     if team1 not in team_stats:
        #         team_stats[team1] = {'Wins': set(), 'Losses': set()}
        #     if team2 not in team_stats:
        #         team_stats[team2] = {'Wins': set(), 'Losses': set()}

        #     # Add the match number to the winner's set
        #     team_stats[winner]['Wins'].add(match_no)
            
        #     # Add the match number to the loser's set
        #     if winner == team1:
        #         team_stats[team2]['Losses'].add(match_no)  # Team2 lost
        #     else:
        #         team_stats[team1]['Losses'].add(match_no)  # Team1 lost
            
            
        # # Print the number of unique wins and losses for each team
        # for team, stats in team_stats.items():
        #     total_matches=len(stats["Wins"]) + len(stats["Losses"])
        #     print(f"Team {team} Wins {len(stats['Wins'])} and losses {len(stats['Losses'])} Out of {total_matches} matches")
        #     print('-----------------------------------------------------------------------------')
       

# Load your DataFrame here (make sure to provide the correct path)
# df = pd.read_csv('path_to_your_data.csv')

        # def calculate_team_stats(match_type):
        #     # Filter the DataFrame based on the user-provided match type
        #     filtered_matches = df[df['Match_Type'].str.lower() == match_type]

        #     # Create a dictionary to store unique wins and losses for each team
        #     team_stats = {}

        #     # Iterate through the filtered DataFrame to determine wins and losses
        #     for index, row in filtered_matches.iterrows():
        #         winner = row['Winner_Team']
        #         match_no = row['Match_no']
        #         team1 = row['Team1']
        #         team2 = row['Team2']
                
        #         # Initialize team stats if not already done
        #         if team1 not in team_stats:
        #             team_stats[team1] = {'Wins': set(), 'Losses': set()}
        #         if team2 not in team_stats:
        #             team_stats[team2] = {'Wins': set(), 'Losses': set()}

        #         # Add the match number to the winner's set
        #         team_stats[winner]['Wins'].add(match_no)
                
        #         # Add the match number to the loser's set
        #         if winner == team1:
        #             team_stats[team2]['Losses'].add(match_no)  # Team2 lost
        #         else:
        #             team_stats[team1]['Losses'].add(match_no)  # Team1 lost

        #     return team_stats

        # # Streamlit app
        # st.title("Match Statistics")

        # # Get user input for match type
        # user_match_type = st.selectbox("Select Match Type:", ["Regular", "Semi-final","Final"])

        # if st.button("Get Statistics"):
        #     st.write('-----------------------------------------------------------------------------')
        #     st.write(f'About {user_match_type.capitalize()} Matches:')
        #     st.write('-----------------------------------------------------------------------------')

        #     # Calculate team statistics based on match type
        #     team_stats = calculate_team_stats(user_match_type)

        #     # Display the number of unique wins and losses for each team
        #     for team, stats in team_stats.items():
        #         total_matches = len(stats["Wins"]) + len(stats["Losses"])
        #         st.write(f"Team {team} Wins {len(stats['Wins'])} and losses {len(stats['Losses'])} Out of {total_matches} matches")
        #         st.write('-----------------------------------------------------------------------------')

        st.title("Batsmen Dismissed for Zero Runs")
        st.write("This analysis shows the unique players with the maximum times out at zero runs.")

        # Count how many times each batsman got out for zero runs
        out_at_zero_counts = df[df['Runs'] == 0]["Batsman_Name"].value_counts()

        # Find the maximum and minimum times a batsman has been out for zero runs
        max_out_at_zero = out_at_zero_counts.max()
        

        # Get the names of batsmen with maximum and minimum outs at zero
        max_player = out_at_zero_counts[out_at_zero_counts == max_out_at_zero].index[0]
       

        # Display the results in Streamlit
        st.write(f'Unique player with maximum outs at zero: {max_player} ({max_out_at_zero} times)')

        def calculate_team_stats(match_type):
            # Filter the DataFrame based on the user-provided match type
            filtered_matches = df[df['Match_Type'].str.lower() == match_type]
            
            

            # Create a dictionary to store unique wins and losses for each team
            team_stats = {}

            # Iterate through the filtered DataFrame to determine wins and losses
            for index, row in filtered_matches.iterrows():
                winner = row['Winner_Team']
                match_no = row['Match_no']
                team1 = row['Team1']
                team2 = row['Team2']
                
                # Initialize team stats if not already done
                if team1 not in team_stats:
                    team_stats[team1] = {'Wins': set(), 'Losses': set()}
                if team2 not in team_stats:
                    team_stats[team2] = {'Wins': set(), 'Losses': set()}

                # Add the match number to the winner's set
                team_stats[winner]['Wins'].add(match_no)
                
                # Add the match number to the loser's set
                if winner == team1:
                    team_stats[team2]['Losses'].add(match_no)  # Team2 lost
                else:
                    team_stats[team1]['Losses'].add(match_no)  # Team1 lost

            return team_stats

        # Streamlit app
        st.title("Match Statistics")

        # Get user input for match type
        user_match_type = st.selectbox("Select Match Type:", ["final", "semi-final", "regular"])

        if st.button("Get Statistics"):
            st.write('-----------------------------------------------------------------------------')
            st.write(f'About {user_match_type.capitalize()} Matches:')
            st.write('-----------------------------------------------------------------------------')

            # Calculate team statistics based on match type
            team_stats = calculate_team_stats(user_match_type)

            # Check if any stats were calculated
            if not team_stats:
                st.write("No statistics available for the selected match type.")
            else:
                # Display the number of unique wins and losses for each team
                for team, stats in team_stats.items():
                    total_matches = len(stats["Wins"]) + len(stats["Losses"])
                    st.write(f"Team {team} Wins {len(stats['Wins'])} and losses {len(stats['Losses'])} Out of {total_matches} matches")
                    st.write('-----------------------------------------------------------------------------')

    elif page == "EDA":

        df=pd.read_csv('./Data/ICC_World_Cup2023.csv')
        st.write(df)

        st.write("************************************************************")

        st.title("--------------------Box plot---------------------")

       
        st.header("Information about Batsman and Team Innings ")

        # Create select boxes for filtering options (make sure they are unique)
        team_innings = st.selectbox("Select Team Innings:", df['Team_Innings'].unique(), key='team_innings_select')
        batsman_name = st.selectbox("Select Batsman:", df[df['Team_Innings'] == team_innings]['Batsman_Name'].unique(), key='batsman_name_select')

        # Filter the DataFrame based on selected values
        filtered_df = df[(df['Team_Innings'] == team_innings) & (df['Batsman_Name'] == batsman_name)]

        # Check if there is data available after filtering
        if not filtered_df.empty:
            # Create a box plot using Plotly
            st.subheader(f"Box Plot of Runs for {batsman_name} in {team_innings} Innings")
            
            fig = px.box(filtered_df, x='Batsman_Name', y='Runs',
                        title=f"Runs Scored by {batsman_name} in {team_innings} Innings",
                        labels={'Batsman_Name': 'Batsman Name', 'Runs': 'Runs'},hover_data=['Balls','6s','4s'],
                        color='Batsman_Name')

            # Display the plot in Streamlit
            st.plotly_chart(fig)
        else:
            st.write("No data available for the selected filters.")
        

        st.write("************************************************************")

        
        st.title("--------------------Scatter plot---------------------")

       
        st.header("Information about Batsman and Team Innings ")

        # Select a team innings
        team_innings = st.selectbox("Select Team Innings:", df['Team_Innings'].unique(), key="team_innings")

        # Filter data based on selected team innings
        filtered_df_team = df[df['Team_Innings'] == team_innings]

        # Select a batsman name based on the selected team innings
        batsman_name = st.selectbox("Select Batsman:", filtered_df_team['Batsman_Name'].unique(), key="batsman_name")

        # Select a metric to plot
        metric = st.selectbox("Select Metric:", ['Runs', 'Balls', '6s', '4s', 'Strike_Rate'], key="metric")

        # Further filter data for the selected batsman
        filtered_df = filtered_df_team[filtered_df_team['Batsman_Name'] == batsman_name]

        # Check if there is data available after filtering
        if not filtered_df.empty:
            # Create a scatter plot using the selected metric
            fig = px.scatter(
                filtered_df,
                x="Match_no",  # Use Match_no or any other column for x-axis
                y=metric,
                color=metric,
                size=metric,
                hover_data=['Batsman_Name', 'Runs', 'Balls', '6s', '4s', 'Strike_Rate']
            )

            # Customize the plot
            fig.update_layout(
                title=f"Scatter Plot of {metric} for {batsman_name} in {team_innings} Innings",
                xaxis_title="Match Number",
                yaxis_title=metric
            )

            # Display the plot in Streamlit
            st.plotly_chart(fig)
        else:
            st.write("No data available for the selected filters.")


        st.write("************************************************************")
        

        # Streamlit app title
        st.title("Scatter Plot of Total Runs by Match Number")

        # Plotly scatter plot with hover data and size based on 'Total_Runs'
        fig = px.scatter(
            df, 
            x="Match_no", 
            y="Total_Runs", 
            color="Team1",
            size="Total_Runs", 
            hover_data=['Team1_Runs', 'Team2_Runs', 'Team1', 'Team2', 'Winner_Team'],
            labels={"Match_no": "Match Number", "Total_Runs": "Total Runs Scored"}
        )

        # Customize the layout of the plot
        fig.update_layout(
            title="Total Runs per Match by Team",
            xaxis_title="Match Number",
            yaxis_title="Total Runs",
            legend_title="Team 1",
            template="plotly_white"
        )

        # Display the plot in the Streamlit app
        st.plotly_chart(fig)
            
        # Streamlit app title
        st.title("Scatter Plot of Sixes by Batsman")

        # Plotly scatter plot with hover data and size based on number of sixes
        fig = px.scatter(
            df, 
            x="Batsman_Name", 
            y="6s", 
            color="6s", 
            size="6s", 
            hover_data=['Batsman_Name', 'Runs', 'Balls'],
            labels={"Batsman_Name": "Batsman Name", "6s": "Number of Sixes"}
        )

        # Customize the layout of the plot
        fig.update_layout(
            title="Number of Sixes Hit by Each Batsman",
            xaxis_title="Batsman Name",
            yaxis_title="Number of Sixes",
            legend_title="Sixes",
            template="plotly_white"
        )

        # Display the plot in the Streamlit app
        st.plotly_chart(fig)

        # Streamlit app title
        st.title("Scatter Plot of Fours by Batsman")

        # Plotly scatter plot with hover data and size based on number of fours
        fig = px.scatter(
            df, 
            x="Batsman_Name", 
            y="4s", 
            color="4s", 
            size="4s", 
            hover_data=['Batsman_Name', 'Runs', 'Balls'],
            labels={"Batsman_Name": "Batsman Name", "4s": "Number of Fours"}
        )

        # Customize the layout of the plot
        fig.update_layout(
            title="Number of Fours Hit by Each Batsman",
            xaxis_title="Batsman Name",
            yaxis_title="Number of Fours",
            legend_title="Fours",
            template="plotly_white"
        )

        # Display the plot in the Streamlit app
        st.plotly_chart(fig)

        st.write("************************************************************")

        # Streamlit app title
        st.title("Match Winners by Match Number")

        # Plotly scatter plot showing match winners
        fig = px.scatter(
            df, 
            x="Match_no", 
            y="Winner_Team", 
            color="Team1", 
            size='Match_no', 
            hover_data=['Team1', 'Team2', 'Winner_Team', 'Match_Type'],
            labels={
                "Match_no": "Match Number",
                "Winner_Team": "Winning Team",
                "Team1": "Team 1"
            }
        )

        # Customize the layout of the plot
        fig.update_layout(
            title="Match Winners in Each Match",
            xaxis_title="Match Number",
            yaxis_title="Winning Team",
            legend_title="Team 1",
            template="plotly_white"
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig)
                

        st.write("************************************************************")

        st.title("--------------------Line Chart---------------------")

        st.header("Runs from Match 1 to 48")
        fig = px.line(df, x="Match_no", y="Total_Runs",
                    hover_data=['Match_Between', 'Winner_Team'],
                    title='Runs From Match 1 to 48')

        # Display the plot in Streamlit
        st.plotly_chart(fig)

        
        st.write("************************************************************")

        st.header("Dynamic Line Chart of Match Data")

        # Create a selectbox to choose which column to plot
        options = ["Total_Runs", "Runs", "Balls", "6s", "4s", "Strike_Rate", "Team1_Runs", "Team2_Runs","Team_Innings"]
        selected_column = st.selectbox("Select data to plot:", options)

        # Plot the line chart based on selected column
        fig = px.line(df, x="Match_no", y=selected_column, 
                    hover_data=['Match_Between', 'Winner_Team'],
                    title=f'{selected_column} from Match 1 to 48')

        # Display the plot in Streamlit
        st.plotly_chart(fig)


        st.write("************************************************************")

        st.title("--------------------Bar plot---------------------")

        st.header("Bar Chart of Sixes by Match Number")

        # Create a selectbox to choose which data to plot on the y-axis
        options = ['6s', 'Runs', '4s','Strike_Rate','Runs','Total_Runs']
        selected_y_column = st.selectbox("Select the column to plot on the y-axis:", options)

        # Plot the bar chart based on selected column
        fig = px.bar(
            df, 
            x='Match_no', 
            y=selected_y_column,
            color=selected_y_column,  # Coloring by the selected column
            hover_data=['Batsman_Name', 'Team_Innings']  # Additional data on hover
        )

        # Show the plot in Streamlit
        st.plotly_chart(fig)

        
        st.write("************************************************************")


        # Group by Match_no, Match_Type, and Team_Innings to get each team’s total runs per match
        team_totals = df.groupby(['Match_no', 'Match_Type', 'Team_Innings']).agg({
            'Total_Runs': 'first',  # Take the first entry for each unique Team_Innings
            '4s': 'sum',            # Sum up for 4s
            '6s': 'sum',            # Sum up for 6s
            'Balls': 'sum'          # Sum up for balls
        }).reset_index()

        # Create select boxes for filtering
        unique_match_type = st.selectbox("Select Match Type", team_totals['Match_Type'].unique(), key="match_type_selectbox")
        metric = st.selectbox("Select Metric", ['Total_Runs', '4s', '6s', 'Balls'], key="metric_selectbox")

        # Filter the DataFrame based on the selected match type
        filtered_summary = team_totals[team_totals['Match_Type'] == unique_match_type]

        # Plot each team’s total runs per match
        if not filtered_summary.empty:
            fig = px.bar(filtered_summary, x='Match_no', y=metric, color='Team_Innings',
                        title=f'{metric} by Team in Each Match ({unique_match_type})',
                        labels={'Match_no': 'Match Number', metric: f'{metric} by Team'},
                        hover_data={'Total_Runs': True, '4s': True, '6s': True, 'Balls': True})

            st.plotly_chart(fig)
        else:
            st.write("No data available for the selected match type.")


        st.write("************************************************************")

        # Create select boxes for filtering
        team = st.selectbox("Select Team", df['Team_Innings'].unique(), key="02_selectbox")
        metric = st.selectbox("Select Metric", ['Total_Runs'], key="03_selectbox")
        match_types = st.multiselect("Select Match Type", ['Regular', 'Semi-final', 'Final'], key="04_selectbox")

        # Filter the DataFrame based on selected values
        filtered_df = df[(df['Team_Innings'] == team) & (df['Match_Type'].isin(match_types))]

        # Drop duplicates to get unique match entries per match number
        filtered_df = filtered_df.drop_duplicates(subset='Match_no')

        # Check if there is data available after filtering
        if not filtered_df.empty:
            # Create a bar plot based on the selected metric
            fig = px.bar(
                filtered_df,
                x='Match_no',
                y=metric,
                color=metric,
                text_auto=True,
                hover_data=['Team_Innings', 'Team1', 'Team2','Team2_Runs','Team1_Runs', 'Winner_Team'],
                title=f"{metric} for {team} in Selected Match Types"
            )
            
            # Display the plot in Streamlit
            st.plotly_chart(fig)
        else:
            st.write("No data available for the selected filters.")


        st.write("************************************************************")
        


         # Grouping by Match_no, Team1, and Team2 to get unique total runs
        unique_runs_df = df.groupby(['Match_no', 'Team1', 'Team2']).agg({
            'Total_Runs': 'first',      # Taking the first occurrence of Total_Runs for each match
            'Team1_Runs': 'first',      # Similarly for Team1 Runs
            'Team2_Runs': 'first',      # Similarly for Team2 Runs
            'Extras': 'first' ,
            'Extras': 'sum',            # Total Extras
            '4s': 'sum',                # Total 4s
            '6s': 'sum',                # Total 6s
            'Balls': 'sum',             # Total Balls
            'Strike_Rate': 'count'          # Also taking the first occurrence of Extras
        }).reset_index()

        # Create select boxes for filtering
        metric = st.selectbox("Select Metric for Histogram", 
                            ['Total_Runs', 'Team1_Runs', 'Team2_Runs', 'Extras','4s','6s','Balls','Strike_Rate'],
                            key="06_selectbox")

        # Create the histogram based on the selected metric
        # We count the unique values of the metric to get a single occurrence per match
        fig = px.histogram(unique_runs_df, x=metric, color=metric, text_auto=True,
                        title=f'Histogram of Unique {metric}'
                        )  # This ensures we count occurrences

        # Display the plot in Streamlit
        st.plotly_chart(fig)

        st.write("************************************************************")

       
        st.write("************************************************************")
        
        # Create a unique list of match types and team innings from your DataFrame
        unique_match_types = df['Match_Type'].unique()
        unique_teams = pd.concat([df['Team1'], df['Team2']]).unique()  # Get unique team names

        # Create a multi-select box for match types (allowing up to 3 selections)
        selected_match_types = st.multiselect(
            "Select Match Types (up to 3)", 
            options=unique_match_types.tolist(), 
            default=[unique_match_types[0]],
            key='08'  # Default to the first match type
        )

        # Create a multi-select box for teams
        selected_teams = st.multiselect(
            "Select Teams", key='09',
            options=unique_teams.tolist()
        )

        # Limit selection to 3 match types
        if len(selected_match_types) > 3:
            selected_match_types = selected_match_types[:3]

        # Filter for matches based on user input
        filtered_matches = df[df['Match_Type'].str.lower().isin([mt.lower() for mt in selected_match_types])]

        # Initialize dictionaries to count wins and losses
        winner_count = {}
        loser_count = {}

        # Iterate through the filtered DataFrame
        for index, row in filtered_matches.iterrows():
            winner = row['Winner_Team']
            loser = row['Team1'] if row['Team1'] != winner else row['Team2']
            match_no = row['Match_no']
            
            # Count unique winners
            if winner not in winner_count:
                winner_count[winner] = set()
            winner_count[winner].add(match_no)

            # Count unique losers
            if loser not in loser_count:
                loser_count[loser] = set()
            loser_count[loser].add(match_no)

        # Prepare data for visualization based on selected teams
        win_lose_data = []
        for team in selected_teams:
            wins = len(winner_count.get(team, set()))
            losses = len(loser_count.get(team, set()))
            win_lose_data.append({'Team': team, 'Result': 'Wins', 'Count': wins})
            win_lose_data.append({'Team': team, 'Result': 'Losses', 'Count': losses})

        # Create DataFrame from the win & lose data
        df_win_lose = pd.DataFrame(win_lose_data)

        # Debugging: Check the content of df_win_lose
        st.write("Win/Loss DataFrame:", df_win_lose)

        # Create the bar plot with custom colors if data is present
        if not df_win_lose.empty:
            color_map = {'Wins': 'green', 'Losses': 'red'}  # Set custom colors for results
            fig = px.bar(df_win_lose, x='Team', y='Count', color='Result', barmode='stack', text_auto=True,
                        title=f"Team Wins and Losses for Match Types: {', '.join(selected_match_types)}",
                        labels={'Count': 'Number of Matches', 'Team': 'Team'},
                        color_discrete_map=color_map)
            # Show plot
            st.plotly_chart(fig)
            # st.plotly_chart(fig_bar)

            # Create and display a table
            fig_table = go.Figure(data=[go.Table(
                header=dict(values=["Team", "Result", "Count"], fill_color='black', align='left'),
                cells=dict(values=[df_win_lose.Team, df_win_lose.Result, df_win_lose.Count], fill_color='black', align='left'))
            ])

            st.plotly_chart(fig_table)

        else:
            st.write("No data available for the selected teams and match types.")


        st.write("************************************************************")

        st.header("--------------------------------Pie Chart---------------------------------")


        team_name = st.selectbox("Select Team Name", df['Team_Innings'].unique())
        filtered_batsmen = df[df['Team_Innings'] == team_name]['Batsman_Name'].unique()
        batsman_name = st.multiselect("Select Batsman Name", filtered_batsmen)
        metric = st.selectbox("Select Metric", ['Runs', 'Balls', '4s', '6s', 'Strike_Rate'])
        match_type = st.multiselect("Select Match Type", df['Match_Type'].unique())

        # Filter data based on the selected values
        filtered_data = df[(df['Batsman_Name'].isin(batsman_name)) &
                        (df['Team_Innings'] == team_name) &
                        (df['Match_Type'].isin(match_type))]

        # Ensure that data is not empty 
        if not filtered_data.empty:
            # Create pie chart based on the selected metric
            fig = px.pie(filtered_data, names='Batsman_Name', values=metric, 
                        title=f"{metric} Distribution for Selected Batsmen in {team_name} ({match_type})")
            fig.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
            st.plotly_chart(fig)
        else:
            st.write("No data available for the selected options.")

        st.write("************************************************************")\
        
        st.header("--------------------------------Subburst-----------------------------------")

        # Select boxes for filtering
        team_name = st.selectbox("Select Team Name", df['Team_Innings'].unique(),key='01')
        filtered_batsmen = df[df['Team_Innings'] == team_name]['Batsman_Name'].unique()
        batsman_name = st.multiselect("Select Batsman Name", filtered_batsmen,key='02')
        metric = st.selectbox("Select Metric", ['Runs', 'Balls', '4s', '6s', 'Strike_Rate'],key='03')
        match_type = st.multiselect("Select Match Type", df['Match_Type'].unique(),key='04')

        # Filter data based on the selected values
        filtered_data = df[
            (df['Batsman_Name'].isin(batsman_name)) &
            (df['Team_Innings'] == team_name) &
            (df['Match_Type'].isin(match_type))
        ]

        # Ensure that data is not empty 
        if not filtered_data.empty:
            # Create sunburst chart based on the selected metric
            fig = px.sunburst(
                filtered_data,
                path=['Team_Innings', 'Batsman_Name'],  # Hierarchy: Team -> Batsman
                values=metric,
                title=f"{metric} Distribution for Selected Batsmen in {team_name} (Match Types: {', '.join(match_type)})"
            )
            fig.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='white')
            st.plotly_chart(fig)
        else:
            st.write("No data available for the selected options.")


        


if __name__ == "__main__":
    main()