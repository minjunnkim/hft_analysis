# High-Frequency Trading Data Analysis Project

## Project Overview
This project involves analyzing high-frequency trading data to identify patterns, anomalies, and insights. The analysis includes data preprocessing, exploratory data analysis (EDA), model training, impact analysis, and visualization. The project leverages Python libraries such as Pandas, Matplotlib, Seaborn, and Scikit-learn.

## Data Preprocessing
### Steps
1. **Fetch Data**: Use the Alpha Vantage API to fetch intraday trading data for multiple companies.
2. **Load and Preprocess Data**: Convert date columns to datetime, normalize closing prices, and create lagged features.
3. **Combine Data**: Combine data from multiple companies into a single dataset for training.

## Exploratory Data Analysis (EDA)
### Steps
1. **Basic Statistics**: Calculate and display basic statistics for the data.
2. **Time Series Plots**: Plot the raw closing prices and trading volumes for each symbol.
3. **Distribution Analysis**: Analyze the distribution of closing prices and trading volumes.
4. **Correlation Analysis**: Calculate and visualize the correlation matrix for each symbol.

## Model Training
### Steps

1. **Train-Test Split**: Split the combined data into training and testing sets.
2. **Train Models**: Train multiple models, including Linear Regression, Decision Tree, Random Forest, and Gradient Boosting.
3. **Evaluate Models**: Evaluate the performance of each model on the test set.

## Impact Analysis and Visualization
### Steps

1. **Volatility Analysis**: Calculate and visualize the rolling volatility of the stock prices.
2. **Price Change and Volume Relationship**: Analyze the relationship between price changes and trading volume.
3. **Feature Importance**: Identify and visualize the importance of different features in the model.

## How to Run the Project
1. Clone the repository.
2. Install the required packages.
3. Run the fetch_data.py by doing:
```bash
python scripts/fetch_data.py
```
(Note that you may change the symbols to change which companies data you use to train the model. Make sure that symbols in fetch_data.py contains all company tickers, data_processing.ipynb contain all training company tickers, and model_training.ipynb contain the one testing company ticker.)

4. Run the notebooks in the following order:
    - data_preprocessing.ipynb
    - EDA.ipynb
    - model_training.ipynb
    - impact_analysis.ipynb

## Conclusion

This project provides a comprehensive analysis of high-frequency trading data, including data preprocessing, EDA, model training, impact analysis, and visualization. The insights gained from this analysis can help in understanding market behavior and making informed trading decisions.