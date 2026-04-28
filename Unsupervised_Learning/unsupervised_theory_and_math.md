# 🧩 Unsupervised Learning Theory & Mathematics

Unsupervised learning algorithms process data without pre-existing labels ($y$). Their goal is to discover underlying structures, patterns, or groupings within the features ($X$) themselves.

## 1. Clustering: K-Means Algorithm
Clustering attempts to group similar data points together. K-Means is a centroid-based algorithm.

* **How it works:**
  1. You choose the number of clusters ($K$).
  2. The algorithm randomly places $K$ centroids in the data space.
  3. Every point is assigned to the nearest centroid.
  4. The centroids move to the average (mean) location of all the points assigned to them.
  5. Repeat steps 3 and 4 until the centroids stop moving (convergence).
* **Evaluating K-Means:** Since there are no labels, we cannot use Accuracy.
  * **WCSS (Within-Cluster Sum of Squares) & The Elbow Method:** WCSS measures the variance within each cluster. We run K-Means for $K=1, 2, 3...$ and plot the WCSS. The optimal $K$ is at the "elbow" of the curve where adding more clusters doesn't significantly reduce WCSS.
  * **Silhouette Score:** Measures how similar an object is to its own cluster compared to other clusters. A score close to 1 means the clustering is excellent.

## 2. Dimensionality Reduction: Principal Component Analysis (PCA)
Datasets often have dozens or hundreds of features. The "Curse of Dimensionality" states that as dimensions increase, data becomes sparse, making it incredibly hard for models to find patterns.

* **What is PCA?** It is a mathematical technique that transforms a large set of variables into a smaller one that still contains most of the original information (variance).
* **The Mathematics:**
  1. Center the data (subtract the mean).
  2. Calculate the Covariance Matrix to see how features vary with each other.
  3. Calculate the **Eigenvectors** and **Eigenvalues** of the matrix. 
     * *Eigenvectors* dictate the direction of the new feature space (the "Principal Components").
     * *Eigenvalues* determine the magnitude (how much variance that Principal Component explains).
  4. Project the original data onto the top Principal Components.
* **Why use PCA?** It speeds up machine learning algorithms significantly and allows us to visualize 10-dimensional data on a 2D or 3D scatter plot.

## 3. Association Rules (Market Basket Analysis)
Used to discover "if-then" relationships in large datasets, typically transaction data (e.g., "If a customer buys bread, they are 80% likely to buy butter").
* **Key Metrics:**
  * **Support:** How frequently the itemset appears in the dataset.
  * **Confidence:** How often the rule has been found to be true.
  * **Lift:** The ratio of the observed support to that expected if the items were independent. A lift > 1 implies a strong association.
* **Common Algorithms:** Apriori and FP-Growth.
