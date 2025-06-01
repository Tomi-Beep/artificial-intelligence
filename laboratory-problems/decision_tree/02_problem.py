import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    col_index = int(input())
    num_trees = int(input())
    kriterium = input()
    podatochno_mnozhestvo = input().split()
    podatochno_mnozhestvo.pop(col_index)

    classifier = RandomForestClassifier(criterion=kriterium, n_estimators=num_trees, random_state=0)

    test_set = dataset[int(0.85 * len(dataset)):]
    train_set = dataset[:int(0.85 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    train_x_2 = list()
    test_x_2 = list()

    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != col_index]
        train_x_2.append(row)

    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != col_index]
        test_x_2.append(row)


    classifier.fit(train_x_2, train_y)

    predictions = classifier.predict(test_x_2)
    print(f'Accuracy: {accuracy_score(test_y, predictions)}')
    print(classifier.predict([podatochno_mnozhestvo])[0])
    print(classifier.predict_proba([podatochno_mnozhestvo])[0])

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_x_2, train_y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_x_2, test_y)

    # submit na klasifikatorot
    submit_classifier(classifier)
