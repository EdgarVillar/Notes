# 🧹 Data Preprocessing and Cleaning Theory

## 1. Introduction: The KDD Process
Data mining and machine learning are parts of a larger framework known as **Knowledge Discovery in Databases (KDD)**. The KDD process emphasizes that algorithm selection is only a fraction of the work. The quality of a model's output is directly dependent on the quality of its input data. 

* **The Golden Rule:** Garbage In = Garbage Out (GIGO). If a model is trained on noisy, incomplete, or unscaled data, its predictions will inherently be flawed, regardless of how advanced the algorithm (like a Transformer or CNN) is.

## 2. Handling Missing Values (Imputation)
Real-world datasets are rarely perfect. Missing data can cause algorithms to fail or introduce bias. 

* **Deletion:** Dropping rows/columns with missing values. *Risk:* Loss of valuable information if the dataset is small.
* **Mean/Median Imputation:** Replacing missing continuous values with the mean or median of the feature. *Tip:* Use Median if the data has heavy outliers (which distort the mean).
* **Mode Imputation:** Replacing missing categorical values with the most frequent class.
* **Predictive Imputation:** Using algorithms like KNN to predict and fill in the missing values based on similar data points.

## 3. Outlier Detection
Outliers are extreme values that deviate significantly from the rest of the data.
* **Z-Score Method:** Measures how many standard deviations a data point is from the mean. Typically, a Z-score > 3 or < -3 is considered an outlier.
* **Interquartile Range (IQR):** Measures the spread of the middle 50% of data. Any value outside `[Q1 - 1.5 * IQR, Q3 + 1.5 * IQR]` is flagged as an outlier.

## 4. Feature Scaling: The Mathematics
Machine learning algorithms that rely on distance metrics (like KNN and SVM) or gradient descent (like Linear Regression and Neural Networks) are highly sensitive to the scale of the data. If one feature ranges from 0-1 and another from 0-1000, the larger feature will dominate the model's weight updates.

### Standard Scaling (Z-Score Normalization)
Transforms data so it has a mean ($\mu$) of 0 and a standard deviation ($\sigma$) of 1. It does not bound the data to a specific range.
* **Formula:** $z = \frac{x - \mu}{\sigma}$
* **When to use:** When the algorithm assumes the data is normally distributed (e.g., Logistic Regression, SVM) or when outliers are present (as it is less affected by them than Min-Max scaling).

### Min-Max Scaling (Normalization)
Transforms data to fit within a specific range, usually [0, 1].
* **Formula:** $x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$
* **When to use:** When you need a bounded interval. Often used in Neural Networks and Image Processing (scaling pixel values from 0-255 to 0-1).

## 5. Encoding Categorical Data
Machine learning models require numerical inputs. Categorical data (like "City" or "Gender") must be converted.
* **Label Encoding:** Assigns a unique integer to each category (e.g., Apple=0, Banana=1, Orange=2). *Risk:* Algorithms might misinterpret the integers as having an ordinal relationship (meaning Orange > Apple), which is incorrect for nominal data.
* **One-Hot Encoding:** Creates a new binary column for each category. (e.g., `is_Apple`, `is_Banana`). *Benefit:* Eliminates the ordinality problem. *Risk:* Can lead to the "Curse of Dimensionality" if there are hundreds of unique categories.
