# Bus Arrival Time Prediction Project

## Overview

The Bus Arrival Time Prediction Project aims to improve the accuracy of bus arrival time predictions by considering drivers' behavior patterns and preparing a dashboard. This README file provides an overview of the project, its goals, and the steps taken to achieve those goals.

## Project Goal

The primary goal of this project is to enhance bus arrival time predictions by incorporating drivers' driving behavior data. By analyzing and modeling this data, we aim to create more accurate and reliable predictions for bus arrival times. Then prepare a dashboard to provide arrival time information and insights from the analyzed data.

## Project Workflow

Here's a summary of the key steps taken in this project:

### Data Preprocessing

1. **Data Labeling**: The raw data was segmented into trip IDs and assigned bus stop labels and segment labels. This labeling process helps organize the data for further analysis.

2. **Trip Filtering**: Trips with erroneous or anomalous data were identified and removed from the dataset. This step ensures that only high-quality data is used for analysis.

### Feature Engineering

3. **Feature Creation**: Several new features were created using the available data, including longitude, latitude, speed, and time. These features include acceleration, radial acceleration, distance from the start, acceleration derivative, throttle count, and brake count. These features capture important aspects of driver behavior.

### Clustering

4. **Time Series Clustering**: Time series clustering was performed using various techniques, including k-means clustering with Dynamic Time Warping (DTW), soft DTW, and without DTW. This clustering process grouped similar driver behavior patterns into clusters.

### Arrival Time Prediction

5. **Modeling**: Using the cluster labels and the averaged driver behavior features, an arrival time prediction model was built. This model leverages the relationships between driver behavior and arrival times to make predictions.

### Implement the Dashboard

6. Implement a dashboard to provide arrival time information and insights from the analyzed data.
   
   Dashboard link: https://github.com/sheshan1/DSE_Dashboard

## Getting Started

To use this project or replicate its results, follow these steps:

1. **Data Preparation**: Organize your raw data into trip IDs and ensure it has bus stop and segment labels.

2. **Data Cleaning**: Filter out trips with erroneous or anomalous data to ensure data quality.

3. **Feature Engineering**: Create the specified features from your data, including acceleration, radial acceleration, distance from the start, acceleration derivative, throttle count, and brake count.

4. **Clustering**: Apply time series clustering techniques, such as k-means with DTW, soft DTW, and without DTW, to cluster driver behavior patterns.

5. **Model Development**: Build an arrival time prediction model using the cluster labels and averaged driver behavior features.

## Video

YouTube: https://youtu.be/pn6dXRJYx8g find the detailed explanation and the demo of the dashboard

## Contributors

- Ginushmal Wikumjith
- Sheshan Premathilaka
- H.M.M.Baqir

## Acknowledgments

- Yin, Z.; Zhang, B. Construction of Personalized Bus Travel Time Prediction Intervals Based on Hierarchical Clustering and the Bootstrap Method. Electronics 2023, 12, 1917. https://doi.org/10.3390/electronics12081917
- Ratneswaran, S., & Thayasivam, U. (2021). An Improved Bus Travel Time Prediction using Multi-Model Ensemble Approach for Heterogeneous Traffic Conditions. In 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC). IEEE
  

## Conclusion

The Bus Arrival Time Prediction Project represents a significant step toward improving bus arrival time predictions by considering driver behavior patterns. By leveraging clustering and modeling techniques, we aim to provide more accurate and reliable predictions for bus commuters and operators.

For more details, please refer to the project's documentation and codebase.
