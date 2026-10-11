Experiment 1: Plotting and Visualizing Time Series Data
Aim: To write a Python program to create line plots, seasonal plots, and perform time series decomposition on a real-world dataset (e.g., stock prices, temperature, or sales data).
Algorithm:
1. Start the program.
2. Import required libraries such as pandas, matplotlib, seaborn, and statsmodels.
3. Load the time series data from a CSV file or dataset containing time series data (e.g., sales, temperature, stock prices).
4. Ensure the date column is in datetime format and set as the index.
5. Plot the raw time series data using matplotlib or seaborn to plot the series over time.
6. Create seasonal plots — if the data has seasonal patterns (e.g., monthly), group by month or quarter to visualize seasonality.
7. Decompose the time series using seasonal decompose to split the series into trend, seasonal, and residual components.
8. Analyze trends and patterns visually.
9. Stop the program.


Experiment 2: Autocorrelation and Partial Autocorrelation Analysis
Aim: To create a Python program to compute and interpret ACF and PACF plots to identify patterns and determine suitable lag values.
Algorithm:
1. Start the program.
2. Import the necessary libraries like pandas, matplotlib, plot_acf, and plot_pacf to work with time series data and to compute ACF/PACF.
3. Read the dataset in CSV format into a pandas DataFrame and parse the date column, if applicable.
4. Plot the time series to understand trends or seasonality.
5. Compute and plot Autocorrelation Function (ACF) to show the correlation of the series with its own lags.
6. Compute and plot Partial Autocorrelation Function (PACF) that removes the indirect effect of intermediate lags.
7. Interpret significant spikes in ACF may indicate seasonality or lag relationships.
8. If lags exceed the 95% confidence interval in ACF/PACF plots, they are considered statistically significant.
9. Stop the program.


Experiment 3: First-Order Exponential Smoothing
Aim: To create a Python program to implement and apply single exponential smoothing to forecast short-term trends in time series data.
Algorithm:
1. Start the program.
2. Import necessary libraries like pandas, matplotlib.pyplot, and SimpleExpSmoothing from statsmodels.
3. Read the dataset in CSV format using pandas read_csv() and parse the date column, if applicable.
4. Extract the time series column (e.g., sales, temperature) from the DataFrame for analysis.
5. Plot the original time series using matplotlib to visualize the raw data.
6. Initialize the smoothing model by passing the series into SimpleExpSmoothing().
7. Fit the model using a specified smoothing parameter α (or let the model optimize it automatically).
8. Generate the smoothed values and plot the result alongside the original series for comparison.
9. Evaluate the forecast performance visually or using error metrics such as MAE or RMSE if test data is available.
10. Stop the program.


Experiment 4: Linear Regression and Transformations for Time Series
Aim: To create a Python program to apply linear regression, logarithmic transformations, differencing, and moving averages to model and forecast time series data and to plot and compare predictions with actual values.
Algorithm:
1. Start the program.
2. Import the necessary libraries such as pandas for handling time series data, numpy for numerical operations, matplotlib.pyplot for plotting, and statsmodels.api or sklearn.linear_model for regression modeling.
3. Read the dataset (e.g., CSV file) into a pandas DataFrame and parse the date column if applicable using parse_dates and set it as the index.
4. Plot the original time series to understand trends, seasonality, and variance.
5. Apply transformation techniques such as log transformation to stabilize variance and differencing to remove trend and achieve stationarity.
6. Create time-based features like time index or lags (e.g., df['Time'] = np.arange(len(df))).
7. Split the data into input variables X (like time index) and output variable y (transformed or original series).
8. Fit a linear regression model using LinearRegression() from sklearn or OLS() from statsmodels.
9. Predict values using the fitted model and compare the predicted values with actual values.
10. Plot actual vs. predicted values to visually assess model performance.
11. Evaluate model performance using metrics such as RMSE or MAE and residual analysis.
12. Inverse-transform the predictions if a log transformation was applied earlier (e.g., use np.exp() to return to the original scale).
13. Stop the program.


Experiment 5: ARIMA Model for Forecasting
Aim: To create a Python program to identify appropriate ARIMA parameters, build the model, and generate forecasts for non-seasonal time series.
Algorithm:
1. Start the program.
2. Import necessary libraries such as pandas, numpy, matplotlib.pyplot, statsmodels, and optionally pmdarima for auto parameter selection.
3. Load the dataset (e.g., CSV) into a pandas DataFrame.
4. Parse dates and set the date column as the index.
5. Visualize the original time series using matplotlib to understand trends and stationarity.
6. Check stationarity using plots and statistical tests like Augmented Dickey-Fuller (ADF) test.
7. If non-stationary, apply the following transformations:
   - a. Log transformation (to stabilize variance).
   - b. Differencing (to stabilize the mean).
8. Determine ARIMA parameters (p, d, q).
9. Use ACF to determine q (MA term).
10. Use PACF to determine p (AR term).
11. Determine d (number of differencing steps) based on stationarity.
12. Alternatively, use auto_arima() from pmdarima to automatically identify the best (p, d, q).
13. Build the ARIMA model using ARIMA() from statsmodels.
14. Fit the model for the training data.
15. Forecast future values using .forecast() or .get_forecast().
16. Plot actual vs. predicted values to visually evaluate the model.
17. Calculate error metrics like RMSE or MAE for quantitative evaluation.
18. Stop the program.


Experiment 6: Seasonal ARIMA (SARIMA) Modeling
Aim: To create a Python program to build and evaluate SARIMA models for seasonal datasets (e.g., monthly or quarterly data) and assess forecast accuracy.
Algorithm:
1. Start the program.
2. Import necessary libraries such as pandas for data handling, matplotlib.pyplot or seaborn for plotting, statsmodels.tsa.statespace.sarimax for SARIMA modeling, and sklearn.metrics for calculating performance metrics (e.g., RMSE).
3. Load the time series dataset as a CSV file.
   - a. Parse the date column and set it as the index.
   - b. Ensure the data has a regular frequency (monthly, quarterly).
4. Visualize the raw time series data using line plots to inspect trends and seasonality.
5. Perform stationarity checks using rolling mean/variance plots or statistical tests like Augmented Dickey-Fuller (ADF) to assess stationarity.
6. If the series is non-stationary, apply differencing (regular and/or seasonal) as needed.
7. Specify SARIMA parameters:
   - a. (p, d, q) for non-seasonal part.
   - b. (P, D, Q, s) for seasonal part (e.g., 12 for monthly data).
8. Split the dataset into training set (e.g., first 80%) and test set (remaining 20%).
9. Build and fit the SARIMA model on the training data using SARIMAX().
10. Generate forecasts on the test period.
11. Plot the original series and forecasted values for visual comparison.
12. To evaluate forecast performance, compute metrics like MAE, RMSE, or MAPE comparing forecast vs. actuals.
13. Tune parameters (manually or using grid search) if accuracy is unsatisfactory.
14. Forecast future values beyond the test set and plot.
15. Stop the program.


Experiment 7: Multivariate Time Series Forecasting with VAR
Aim: To create a Python program using Vector Autoregression (VAR) to analyze relationships between multiple time series and make multivariate forecasts.
Algorithm:
1. Start the program.
2. Import necessary libraries: pandas, matplotlib, statsmodels.tsa.api.VAR, an ADF test from statsmodels, mean squared error from sklearn.metrics, and numpy.
3. Load the multivariate time series dataset (e.g., GDP, Inflation, Unemployment).
4. Convert the date column to datetime and set it as the index.
5. Check for stationarity of each time series using the ADF (Augmented Dickey-Fuller) test.
6. Difference non-stationary series to make them stationary (usually first difference).
7. Split the data into training and testing sets (e.g., 80% training).
8. Create and fit the VAR model on the training data using the optimal lag order (based on AIC or BIC).
9. Generate forecasts for the test period using the fitted model.
10. Convert forecasts into a DataFrame and assign appropriate column names.
11. Plot actual vs. forecasted values for each variable.
12. Calculate and print forecast accuracy using RMSE or MAE for each time series.
13. Stop the program.


Experiment 8: Comparison of Forecasting Methods
Aim: To create a Python program to implement and compare naive, mean, and exponential smoothing forecasting techniques and to evaluate model performance using RMSE and MAE.
Algorithm:
1. Start the program.
2. Import necessary libraries such as pandas for data handling, numpy for numerical operations, matplotlib.pyplot for plotting, mean_squared_error and mean_absolute_error from sklearn.metrics for evaluation, and SimpleExpSmoothing from statsmodels.tsa.holtwinters for exponential smoothing.
3. Load the time series dataset as a CSV file using pandas read_csv() and parse the date column, if applicable, and set the date column as the index.
4. Split the data into training and test sets, using 80% for training and 20% for testing.
5. Apply Naive Forecasting and forecast all test values using the last value from the training set.
6. Apply Mean Forecasting and forecast all test values using the mean of the training set.
7. Apply Exponential Smoothing by initializing SimpleExpSmoothing with the training data and fitting the model, then forecast for the test period.
8. To evaluate all three methods:
   - a. Calculate RMSE and MAE for each method.
   - b. Compare results.
9. Plot actual vs. forecasted values for each method.
10. Stop the program.