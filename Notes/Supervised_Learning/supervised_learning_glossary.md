# 🎯 Supervised Learning Glossary & Theory

Supervised learning is the process of learning a function that maps an input to an output based on example input-output pairs. It requires labeled training data.

## 1. Linear and Logistic Regression
* **Linear Regression:** Predicts a continuous numerical value. It assumes a linear relationship between features ($X$) and the target ($y$).
  * **Loss Function:** Mean Squared Error (MSE). It measures the average of the squares of the errors (the difference between the estimated values and the actual value).
  * **Optimization:** Gradient Descent is used to iteratively tweak parameters (weights) to minimize the MSE.
* **Logistic Regression:** Used for binary classification (predicting 0 or 1). It uses the **Sigmoid Function** to squash the output of a linear equation into a probability between 0 and 1.

## 2. Tree-Based Models
* **Decision Trees:** Split the data into subsets based on feature values. 
  * **Splitting Criteria:** It uses metrics like **Gini Impurity** or **Information Gain (Entropy)** to decide which feature splits the data most perfectly into pure classes.
  * *Risk:* Highly prone to overfitting. A deep tree will perfectly memorize the training data but fail on new data.
* **Random Forests:** An ensemble method. Instead of one tree, it builds hundreds of shallow "stumps" or trees, each trained on a random subset of data and features. The final prediction is a majority vote (for classification) or an average (for regression). This significantly reduces overfitting.

## 3. Distance and Margin Models
* **K-Nearest Neighbors (KNN):** A "lazy" algorithm. To classify a new data point, it looks at the $K$ closest training data points (using Euclidean distance) and assigns the majority class.
* **Support Vector Machines (SVM):** Finds a "hyperplane" that perfectly separates different classes while maximizing the "margin" (the distance between the line and the closest data points). 
  * **The Kernel Trick:** When data is not linearly separable, SVM uses a kernel (like Polynomial or RBF) to project the data into a higher mathematical dimension where a straight line *can* separate it.

## 4. Evaluation Metrics
### For Classification (e.g., Cancer Detection, Spam Filter)
* **Accuracy:** Total correct predictions / Total predictions. (Misleading if classes are imbalanced).
* **Precision:** Out of all the instances the model *predicted* as positive, how many were actually positive? (Crucial when false positives are costly).
* **Recall (Sensitivity):** Out of all the *actual* positive instances, how many did the model find? (Crucial in healthcare—you don't want to miss a disease!).
* **F1-Score:** The harmonic mean of Precision and Recall.

### For Regression (e.g., House Prices, Temperature)
* **Mean Absolute Error (MAE):** The average absolute difference between predictions and actual values.
* **Root Mean Squared Error (RMSE):** The square root of MSE. It heavily penalizes large errors because the differences are squared before averaging.
