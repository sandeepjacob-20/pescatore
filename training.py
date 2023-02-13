# -*- coding: utf-8 -*-
"""model_prep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a3MQpnhHGUWpDIuW6o52UtyXgOUl3Q7M
"""

#importing basic packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""Loading the data"""

def train_model():
    #Loading the data
    data0 = pd.read_csv('urldata.csv')
    data0.head()

    data0.shape

    """Data Preprocessing and cleaning """

    data0.describe()

    #Dropping the Domain column
    data = data0.drop(['Domain'], axis=1).copy()

    #checking the data for null or missing values
    data.isnull().sum()

    # shuffling the rows in the dataset so that when splitting the train and test set are equally distributed
    data = data.sample(frac=1).reset_index(drop=True)
    data.head()

    """Spliting the data into training and testing dataset"""

    # Sepratating & assigning features and target columns to X & y
    y = data['Label']
    X = data.drop('Label', axis=1)
    X.shape, y.shape

    # Splitting the dataset into train and test sets: 80-20 split
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2, random_state=12)
    X_train.shape, X_test.shape

    """Machine learning models & training """

    #importing packages
    from sklearn.metrics import accuracy_score

    """1. Decision Tree Classifier"""

    # Decision Tree model
    from sklearn.tree import DecisionTreeClassifier

    # instantiate the model
    tree = DecisionTreeClassifier()
    tree.fit(X_train.values,y_train)

    #predicting the target value from the model for the samples
    y_test_tree = tree.predict(X_test)
    y_train_tree = tree.predict(X_train)

    #computing the accuracy of the model performance
    acc_train_tree = accuracy_score(y_train, y_train_tree)
    acc_test_tree = accuracy_score(y_test, y_test_tree)

    print("Decision Tree: Accuracy on training Data: {:.3f}".format(
        acc_train_tree))
    print("Decision Tree: Accuracy on test Data: {:.3f}".format(acc_test_tree))

    """2. Random Forest"""

    # Random Forest model
    from sklearn.ensemble import RandomForestClassifier

    # instantiate the model
    forest = RandomForestClassifier()

    # fit the model 
    forest.fit(X_train.values, y_train)

    #predicting the target value from the model for the samples
    y_test_forest = forest.predict(X_test)
    y_train_forest = forest.predict(X_train)

    #computing the accuracy of the model performance
    acc_train_forest = accuracy_score(y_train, y_train_forest)
    acc_test_forest = accuracy_score(y_test, y_test_forest)

    print("Random forest: Accuracy on training Data: {:.3f}".format(
        acc_train_forest))
    print("Random forest: Accuracy on test Data: {:.3f}".format(acc_test_forest))

    """3. Multilayer Perceptron(MLPs)"""

    # Multilayer Perceptrons model
    from sklearn.neural_network import MLPClassifier

    # instantiate the model
    mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=([100, 100, 100]))

    # fit the model
    mlp.fit(X_train.values, y_train)

    #predicting the target value from the model for the samples
    y_test_mlp = mlp.predict(X_test)
    y_train_mlp = mlp.predict(X_train)

    #computing the accuracy of the model performance
    acc_train_mlp = accuracy_score(y_train, y_train_mlp)
    acc_test_mlp = accuracy_score(y_test, y_test_mlp)

    print("Multilayer Perceptrons: Accuracy on training Data: {:.3f}".format(
        acc_train_mlp))
    print("Multilayer Perceptrons: Accuracy on test Data: {:.3f}".format(
        acc_test_mlp))


    """4. Support Vector Machine"""

    #Support vector machine model
    from sklearn.svm import SVC

    # instantiate the model
    svm = SVC(kernel='linear', C=1.0, random_state=12)
    #fit the model
    svm.fit(X_train.values, y_train)

    #predicting the target value from the model for the samples
    y_test_svm = svm.predict(X_test)
    y_train_svm = svm.predict(X_train)

    #computing the accuracy of the model performance
    acc_train_svm = accuracy_score(y_train, y_train_svm)
    acc_test_svm = accuracy_score(y_test, y_test_svm)

    print("SVM: Accuracy on training Data: {:.3f}".format(acc_train_svm))
    print("SVM : Accuracy on test Data: {:.3f}".format(acc_test_svm))

    """5. Naive Bayes"""

    from sklearn.naive_bayes import MultinomialNB

    nb=MultinomialNB()
    nb.fit(X_train.values,y_train)

    #predicting the target value from the model for the samples
    y_test_nb = nb.predict(X_test)
    y_train_nb = nb.predict(X_train)

    #computing the accuracy of the model performance
    acc_train_nb = accuracy_score(y_train, y_train_nb)
    acc_test_nb = accuracy_score(y_test, y_test_nb)

    print("NB: Accuracy on training Data: {:.3f}".format(acc_train_nb))
    print("NB : Accuracy on test Data: {:.3f}".format(acc_test_nb))

    """6. AdaBoost"""

    from sklearn.ensemble import AdaBoostClassifier

    aB = AdaBoostClassifier(n_estimators=50,
                            learning_rate=1)

    aB.fit(X_train.values, y_train)

    #predicting the target value from the model for the samples
    y_test_aB = aB.predict(X_test)
    y_train_aB = aB.predict(X_train)

    #computing the accuracy of the model performance
    acc_train_aB = accuracy_score(y_train, y_train_aB)
    acc_test_aB = accuracy_score(y_test, y_test_aB)

    print("aB: Accuracy on training Data: {:.3f}".format(acc_train_aB))
    print("aB : Accuracy on test Data: {:.3f}".format(acc_test_aB))

    """Stacking Models - Bagging"""

    from sklearn.ensemble import StackingClassifier

    estimators = [('tree', tree), ('rf', forest), ('mlp', mlp), ('svm', svm), ('nb',nb), ('aB',aB)]
    final_estimator = svm

    classifier = StackingClassifier(estimators=estimators, final_estimator=final_estimator)

    classifier.fit(X_train.values, y_train)

    y_test_classifier = classifier.predict(X_test)
    y_train_classifier = classifier.predict(X_train)

    acc_classifier_train = accuracy_score(y_train, y_train_classifier)
    acc_classifier_test = accuracy_score(y_test, y_test_classifier)
    print("Accuracy on test Data: ", acc_classifier_test)
    print("Accuracy on training Data:", acc_classifier_train)

    """Saving the model as a pickle file"""

    import pickle
    pickle.dump(classifier, open('phishing_model.pkl', 'wb'))

    return {
        "status":"training complete",
        "Accuracy on test data":acc_classifier_test,
        "Accuracy on training Data":acc_classifier_train
    }