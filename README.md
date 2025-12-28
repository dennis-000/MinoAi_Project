# MinoAI Project - NYC Airbnb Data Analysis

## Project Overview
This project performs comprehensive data analysis and machine learning on the NYC Airbnb dataset. The analysis follows industry best practices with a structured multi-notebook approach for clarity, reproducibility, and maintainability.

## Dataset Description
The dataset contains information about Airbnb listings in New York City, including:
- Listing details (id, name, host information)
- Location data (neighbourhood, latitude, longitude)
- Property characteristics (room type, price, minimum nights)
- Review metrics (number of reviews, reviews per month, last review date)
- Availability information

## Project Structure
```
MinoAI_Project/
│
├── data/
│   └── MinoAI_dataset.csv          # Raw dataset
│
├── notebooks/
│   ├── 01_data_loading_and_overview.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_modeling.ipynb
│   └── 06_evaluation_and_insights.ipynb
│
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Notebooks Overview

### 01. Data Loading and Overview
- Load the dataset
- Understand data structure and types
- Identify initial data quality issues
- Generate summary statistics

### 02. Data Cleaning
- Handle missing values using multiple techniques:
  - Forward fill
  - Backward fill
  - Interpolation
  - Mean/median imputation
- Remove duplicates
- Fix data type inconsistencies

### 03. Exploratory Data Analysis (EDA)
- Statistical analysis
- Visualizations (histograms, boxplots, scatter plots)
- Correlation analysis
- Pattern and trend discovery

### 04. Feature Engineering
- Encode categorical variables
- Feature scaling and normalization
- Create derived features
- Feature selection

### 05. Modeling
- Problem formulation (regression/classification)
- Train-test split
- Model selection and training
- Hyperparameter tuning

### 06. Evaluation and Insights
- Model performance metrics
- Results interpretation
- Limitations and future improvements
- Real-world applications

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the notebooks in sequential order (01 through 06) to reproduce the analysis.

## Tools and Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib & seaborn**: Data visualization
- **scikit-learn**: Machine learning algorithms
- **jupyter**: Interactive notebook environment

## Academic Integrity
This project represents original work completed for academic purposes. All external resources and libraries used are properly cited within the notebooks.

## Author
Eugene - IT Student
Submission Date: January 3rd, 2026

## License
This project is for educational purposes only.
