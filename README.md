# Visualizing the Perfect Cup of Coffee

<p align="center">
  <img src="https://github.com/kellyshreeve/Coffee_Quality_Visualizations/blob/main/images/coffee.png" 
  alt="Purple car cartoon">
</p>

# Project Overview

This project uses high-level plotly visualizations to visualize coffee quality across the world. Using a dataset of 207 coffee batches from different regions and of different varieties, the purpose is to determine which region, variety, and altitude produce the best quality coffee. 

# Installation and Setup

## Codes and Resources Used

  - <b>Editor Used</b>: Visual Studio Code
  - <b>Python Version</b>: 3.10.9

## Python Packages Used

  - <b>Data Manipulation</b>: ```pandas```
  - <b>Data Visualization</b>: ```matplotlib, plotly.express```

# Data

## Source Data

Coffee Quality and Sustainability
  * *country_of_origin*: Country coffee was grown in  
  * *color*: Color of the coffee bean
  * *variety*: Coffee bean variety
  * *Aroma*: Refers to the sent or fragrance of the coffee
  * *Flavor*: The flavor of coffee is evaluated based on the taste, including any sweetness, bitterness, acidity, and other flavor notes.
  * *Aftertaste*: Refers to the lingering taste that remains in the mouth after swallowing the coffee.   
  * *Acidity*: Acidity in coffee refers to the brightness or liveliness of the taste.
  * *Body*: The body of coffee refers to the thickness or viscosity of the coffee in the mouth.
  * *Balance*: Balance refers to how well the different flavor components of the coffee work together.
  * *Uniformity*: Uniformity refers to the consistency of the coffee from cup to cup.
  * *Clean Cup*: A clean cup refers to a coffee that is free of any off-flavors or defects, such as sourness, mustiness, or staleness.
  * *Sweetness*: It can be described as caramel-like, fruity, or floral, and is a desirable quality in coffee.
  * *Category One Defects*: Primary defects perceived through visual inspection of the coffee beans
  * *Category Two Defects*: Secondary defects that can only be percieved through tasting

## Data Acquisition

The data come originally from the CQI web database on coffee quality and sustainability and were made available through TripleTen.

## Data Preprocessing

Missing values in string variables were imputed with 'unknown'. There was only one missing quantitative observation, and the row was dropped from the dataset. Implicit duplicates in color were cleaned by combining similar categories. Altitude values entered into the dataset as ranges were used to calculate an average altitude feature, representing the average of the two endpoints of the altitude range.
 
# Code Structure
```
  ├── README.md          
  │
  ├── images
  │   └── coffee.png    
  │
  ├── notebooks  
  │   └── coffee_analysis.ipynb
  │
  ├── modules  
  │   └── __init__.cypthon-310.pyc
  │
  └── requirements.txt  
```

# Results and Evaluation

<p align="center">
  <img src="https://github.com/kellyshreeve/Zuber_Rides_Analysis/blob/main/images/trips-company.png" 
  alt="Bar graph of total trips by company">
</p>

<p align="center">
  <img src="https://github.com/kellyshreeve/Zuber_Rides_Analysis/blob/main/images/drop-offs.png" 
  alt="Bar graph of average drop offs by neighborhood">
</p>

<p align="center">
  <img src="https://github.com/kellyshreeve/Zuber_Rides_Analysis/blob/main/images/hypothesis-test.png" 
  alt="Statistical output of two-indpendent samples t-test comparing average trip length in good vs bad weather">
</p>

# Future Work

# Acknowledgments/References

