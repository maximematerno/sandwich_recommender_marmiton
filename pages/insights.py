import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """        
            #### Data Science - Sandwich Recommender Marmiton App
            This is the Data Science portion for an Application that uses Machine Learning to build a Sandwich Recommender Marmiton App based on the movies descriptions which is then put through a rigorous NLP analysis and NearestNeighbors model.
            #### Flowchart
            """,
        className='mb-4'),
        (
            html.Img(src='assets/FlowChart.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """  
             #### Project Info   
            For the Data Science portion of this application, I had to web scrabe the data on Marmiton. Within it, you will find a number of description from Marmiton website on a variety of sandwiches. 
            For this project, I analyze the Sandwich on Marmiton. I used a variety of tools such as Pandas, TFIDF, and Sklearn for our simpler models. 
            My primary strategy was to clean the data to keep just the Sandwich recipes and create a Sandwich Recommender using NLP and TFIDF vectorizer and A Kmeans model with the algorythm of NearestNeighbors models. I trained the tokenized/vectorized data on our target(description) and apply NearestNeighbors.
            I create a list of ingredients and the model give me the sandwich recipes wich had similar ingredients.


            """,
        className='mb-4'),
        
        # dcc.Markdown(
        #     """ 
        #     #### Logs       
        #     October 21, 2019 Exploratory Data Analysis & Initial Modeling, Mock Data To Backend

        #     October 22, 2019 Optimize Model for better accuracy, Set up End points for Backend

        #     October 23, 2019 Completed the bulk of both MVP and Stretch Requirements. DS team is on stand-by in case additional data engineering or model optimization is required.

        #     October 24, 2019 Final day, just standing by incase our team needs us. Otherwise we're making little tweaks here and there, improving what can be improved upon, and otherwise just allow the rest of the areas of our team to do what they do best.        
        #     """,
        # className='mb-4'),
        
        dcc.Markdown(
            """
            #### Contributing         
            Pull requests are welcome. However for major changes, please open an issue first to discuss what you would like to change.

            Please make sure to update tests as appropriate.           
            """,
        className='mb-4'),
        
        dcc.Markdown(
            """
            #### License 
            MIT
            """,   
        className='mb-4'),
             
    ],
)

layout = dbc.Row([column1])