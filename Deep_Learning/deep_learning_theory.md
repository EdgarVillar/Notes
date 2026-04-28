# 🧠 Deep Learning & Neural Network Architectures

Deep Learning is a subset of Machine Learning that uses Artificial Neural Networks with multiple layers (hence "deep") to extract higher-level features from raw input. It excels at unstructured data like images, audio, and text.

## 1. Fundamentals of Neural Networks
* **The Perceptron & Nodes:** The building block of a neural network. It takes inputs, multiplies them by weights, adds a bias, and passes the result through an activation function.
* **Activation Functions:** 
  * *ReLU (Rectified Linear Unit):* $f(x) = max(0, x)$. The standard default. It solves the vanishing gradient problem.
  * *Sigmoid:* Squashes values between 0 and 1. Used in the final layer for binary classification.
  * *Softmax:* Used in the final layer for multi-class classification. It outputs a probability distribution across all classes.
* **Backpropagation:** The algorithm used to calculate the gradient of the loss function with respect to the weights. It uses the chain rule from calculus to update weights and "learn."

## 2. Convolutional Neural Networks (CNNs)
Standard neural networks flatten images into a single 1D array of pixels, which destroys spatial relationships (an eye is near a nose). CNNs preserve the 2D topology of an image.

* **Convolutional Layers:** Slide a "filter" (or kernel) across the image to detect features like edges, textures, and eventually complex objects like faces.
* **Max Pooling Layers:** Down-sample the image. It takes the maximum pixel value from a patch, reducing computational load and preventing overfitting while retaining the most prominent features.
* **Flatten & Dense Layers:** After extracting features via convolutions, the final 2D maps are flattened into 1D and passed to a standard neural network for final classification.

## 3. Transformers & Large Language Models (LLMs)
Before 2017, text was processed sequentially using Recurrent Neural Networks (RNNs). The Transformer architecture revolutionized NLP by processing all words simultaneously.

* **Self-Attention Mechanism:** Allows the model to weigh the importance of different words in a sentence relative to a specific word. 
  * **Query (Q):** What am I looking for?
  * **Key (K):** What do I contain?
  * **Value (V):** What information do I pass on?
* By calculating the dot product of Queries and Keys, the network learns the *context* of a word (e.g., the word "bank" in "river bank" vs. "money bank").
