from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load sample dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Initialize and train Decision Tree
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(f"Decision Tree Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Print tree decision rules
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("\nDecision Tree Rules:\n", tree_rules)
