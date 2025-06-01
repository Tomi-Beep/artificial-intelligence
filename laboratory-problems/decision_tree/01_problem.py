import os

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    procenti = float(input()) / 100
    kriterium = input()
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    classifier = DecisionTreeClassifier(criterion=kriterium, random_state=0)
    test_set = dataset[:int(len(dataset) * (1 - procenti))]
    train_set = dataset[int(len(dataset) * (1 - procenti)):]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    train_x = encoder.transform(train_x)
    test_x = encoder.transform(test_x)

    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')
    predictions = classifier.predict(test_x)
    print(f'Accuracy: {accuracy_score(test_y, predictions)}')
    features_importances = list(classifier.feature_importances_)
    print(f'Most important feature: {features_importances.index(max(features_importances))}')
    print(f'Least important feature: {features_importances.index(min(features_importances))}')

# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
    submit_train_data(train_x,train_y)

# submit na testirachkoto mnozestvo
    submit_test_data(test_x, test_y)

# submit na klasifikatorot
    submit_classifier(classifier)

# submit na encoderot
    submit_encoder(encoder)
