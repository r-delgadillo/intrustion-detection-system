[Link1](https://www.geeksforgeeks.org/decision-tree-implementation-python/)
[Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

# Decision Tree ML Algorithm
* Falls under supervised learning algorithms.

### Gini Index and Information Gain
Both of these methods are used to select from the 'n' attributes of the dataset which attribute would be placed at the root or the internal node

#### Gini Index
* Gini Index is ametric to measure how often a randomly chosen element would be incorrectly identified.
* It means an attribute with lower gini index should be preferred.

#### Entropy
* A measure of uncertainty of a random variable, it characterizes the impurity of an arbitrary collection of examples. The higher the entropy the more the information content.

#### Information Gain
* The entropy typically changes when we use a node in a decision tree to partition the training instances into smaller subsets. Information gain is a measure of change in entropy.

#### Accuracy score
* Used to calculate the accuracy of the trained classifier.

#### Confusion Matrix
* Confusion Matrix is used to understand the trained classifier behavior over the test dataset or calidate dataset.+

# Understanding Confusion Matrix
Nice [article](https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62) describing confusion matrics 

* It is a performance measurement for machine learning classification problems where output can be two or more classes.
* It is a table with 4 different combinations of predicted and actual values
* It is extremely useful for measuring Recall, Precision, Specificity, Accuracy, and AUC-ROC curve.

![image.png](attachment:image.png)

* True Positive (TP):
    * You predicted positive and it's true.
* True Negative (TN):
    * You predicted negative and it's true.
* False Positive (FP) (Type 1 Error):
    * You predicted positive and it's false.
* False Negative (FN) (Type 2 Error):
    * You predicted negative and it's false.

##### We describe predicted values as Postive and Negative and actual values as True and False
