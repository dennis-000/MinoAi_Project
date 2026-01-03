# MinoAI: NYC Airbnb Price Prediction Project
## Official Reporting Document & Technical Narrative

**Student Name:** Dennis Opoku Asiedu
**Submission For:** Level 400
**Date:** January 2026
**Course:** Information Technology
**Index Number:** PUIT/22210058
**Lecturer:** Mr. Harry Atieku-Boateng
**Submission Date:** 3rd January 2026

---

## 1. Introduction

This project presents a comprehensive data analytics and machine learning study conducted using a real-world dataset provided for academic practice. The dataset was intentionally delivered in a raw and unrefined form to simulate realistic data challenges commonly encountered in industry and research settings.

The primary objective of this work is to apply data exploration, data cleaning, feature engineering, and machine learning techniques to extract meaningful insights and build predictive models. When I began this project, I noticed a recurring problem: hosts were often guessing their nightly rates, either pricing themselves out of the market or leaving significant revenue on the table. My goal with **MinoAI** was to move beyond guesswork and build an intelligent assistant based on evidence, not intuition.

## 2. Dataset Description

The dataset consists of structured records containing both numerical and categorical variables. It represents real-world observations related to property listings and associated attributes in New York City (2019).

Key characteristics include:
*   **Multiple numerical features:** Prices, review counts, and location coordinates.
*   **Categorical variables:** Room types (Entire home, Private, Shared) and Boroughs.
*   **Presence of missing values:** High variance in the `reviews_per_month` column.
*   **Realistic variability:** Extreme outliers in the luxury pricing tier.

## 3. Data Quality Assessment

An initial assessment revealed several data quality issues:
*   **Missing (null) values:** Multiple columns required imputation.
*   **Potential outliers:** Listings priced at $0 or extreme high-end prices.
*   **Non-uniform labels:** Neighborhood names required careful mapping.

## 4. Data Cleaning and Preprocessing

I started with the raw 2019 NYC Airbnb dataset (MinoAI_Dataset.csv). The first human difficulty was realizing that data is never clean. I spent a significant amount of time handling missing values in the review columns.

### 4.1 Handling Missing Values
The following methods were explored and applied where appropriate:
*   **Forward/Backward Fill:** Propagating observations for timeline consistency.
*   **Interpolation:** Estimating missing values based on surrounding listing points.
*   **Mean/Zero Imputation:** I chose to impute missing reviews with zero, reflecting the reality of new listings. This was crucial for mathematical stability.
*   **Outlier Removal:** I made the critical decision to filter out listings priced at $0, which were clearly clerical errors.

### 4.2 Data Type Correction
Incorrect data types were identified and converted (e.g., ensuring IDs were handled as strings and latitude/longitude as floats) to ensure compatibility with modelling processes.

## 5. Exploratory Data Analysis (EDA)

Exploratory Analysis was conducted to find the "story" in the numbers:
*   **Location isn't just a label:** The difference between Manhattan and the Bronx is a fundamental shift in price distribution.
*   **The Power of Room Type:** I saw a massive gap between shared rooms and entire apartments.
*   **Spatial Correlation:** The closer a listing is to the city center, the more the price variance explodes.

## 6. Feature Engineering: Thinking Like a Real Estate Agent

To make my models smarter, I created derived features:
*   **The Popularity Index:** I created `reviews_per_availability` to identify high-demand "gems."
*   **Neighborhood Frequency:** Instead of one-hot encoding 200+ neighborhoods, I mapped them by frequency to tell the model how "saturated" a market is.
*   **Log-Price Correction:** I applied a log transformation to "flatten" the price curve, allowing the model to learn the middle market more accurately.

## 7. Machine Learning Modelling

I set up a competition between six different algorithms to see which could master the NYC market.

| Model | MAE ($ Error) | $R^2$ (Accuracy) | Verdict |
| :--- | :--- | :--- | :--- |
| **Random Forest** | **$61.49** | **0.2003** | **Grand Champion** |
| Linear Regression | $71.36 | 0.1156 | Too simplistic |
| Ridge Regression | $71.36 | 0.1156 | Basic Regularization |
| Decision Tree | $64.44 | -0.2962 | Suffered from overfitting |

## 8. Model Evaluation

Model performance was evaluated using multiple metrics:
*   **Accuracy ($R^2$):** Successfully captured 20% of market variance.
*   **MAE:** My champion model was off by an average of $61, but has a median error of only ~$35 for budget listings.
*   **Train-Test Split:** Each model was tested using an 80-20 split to ensure unbiased evaluation.

## 9. Interpretation of Results

The Random Forest won because it understood the "corners" of NYC—how a listing can be expensive just by being a few blocks closer to a subway station or Central Park.
*   **Privacy Premium:** Upgrading from Shared to Private room is the best way to jump pricing tiers.
*   **Social Proof:** The jump from 0 reviews to 1 review is statistically massive.

## 10. Limitations of the Study

Working on MinoAI taught me that AI is not perfect. My accuracy reflects an honest truth: real estate is part science and part art. The model cannot yet "see" a beautiful sunset or high-end interior design, which accounts for the remaining variance.

## 11. Conclusion and Recommendations

This project successfully demonstrated the application of machine learning on a real-world dataset.
**Recommendations:**
1.  **Image Analysis:** Integrate photography quality into the model.
2.  **Hyperparameter Tuning:** Explore more deep-learning architectures.
3.  **Deployment:** I have successfully deployed this as a web app on Hugging Face.

## 12. Tools and Libraries Used

*   **Python:** Core programming logic.
*   **Pandas/NumPy:** Data cleaning and structure.
*   **Scikit-Learn:** Machine Learning algorithms.
*   **Matplotlib/Seaborn:** EDA Visual analytics.
*   **Streamlit:** Web deployment.

## 13. References

The dataset (MinoAI_Dataset.csv) was sourced and provided by my lecturer, **Mr. Harry Atieku-Boateng**, as part of the academic curriculum for simulated real-world data practice. All software libraries used (Scikit-Learn, Pandas, NumPy, etc.) are acknowledged under their respective open-source licenses.

---
**Dennis Opoku Asiedu**  