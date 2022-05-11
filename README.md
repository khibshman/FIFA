# Data Mining Final Project
## Data Description
For our project, we are using the “FIFA 22 Players Dataset”. This data was originally scraped from the sofifa.com website, although we are sourcing it indirectly through Kaggle. (See below for details). This dataset includes information on roughly 14,000 FIFA players, including their salary, value, club name and various other features. It is current as of May 1st, 2022.

|Variable Name|Data Type|Description|Comments|
|---|---|---|---|
|ID|Object|Player ID Number||
|Name|Object|Player Name||	
|Age|Integer|Player Age||	
|Nationality|Object|Player Nationality||	
|Overall|Integer|Base Player Quality Rating||	
|Potential|Integer|Highest Possible Player Rating||
|Club|Object|Club Name|Missing data: ~1%|
|Contract|Object|Contract Length (Starting Year to Ending Year)||
|Value|Float|Overall Player Salary||
|Wage|Float|Weekly Player Salary||
## Research Questions
1.	Is it possible to predict a player’s salary? In other words, what variables influence a player’s wages, and can we quantify the impact that these relevant variables have? This question could be answered with techniques such as linear regression and possibly linear mixed models.
2.	Can we organize players into clusters based on these variables? For example, are there relationships between club, salary, and nationality that segment players into groups. This question could be answered with PCA or other clustering techniques.
## Data Concerns
•	It is likely that there are additional groupings that are not being captured here. For example, player positions or number of goals scored may impact wages, but this is not included in our data.
•	The “Club” field contains a small number of records with missing values. However, this is only about 1% and it is the only field with missing data.
## Data Source
Data was sourced from the FIFA 22 Player dataset on Kaggle, which was in turn scrapped from sofifa.com. 
The dataset can be accessed here: https://www.kaggle.com/datasets/minhnguyen147/fifa-22-players-dataset?select=basic_info.csv


