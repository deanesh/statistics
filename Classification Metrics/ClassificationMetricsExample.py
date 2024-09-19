import sys

import numpy as np
'''
Explanation
Metrics Calculation:
Accuracy: The proportion of true results among the total cases.
Precision: The ratio of true positives to the sum of true and false positives.
Recall: The ratio of true positives to the sum of true positives and false negatives.
F1 Score: The harmonic mean of precision and recall.
Confusion Matrix: A summary of prediction results showing true positives, false positives, 
true negatives, and false negatives.
Classification Report: A comprehensive report including precision, recall, F1 score, 
and support for each class.
'''
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score, confusion_matrix, classification_report)

# Create a synthetic dataset
X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42); model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Print metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
