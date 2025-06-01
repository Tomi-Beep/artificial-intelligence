import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka

    classifier = GaussianNB()

    dataset_v2 = []
    for row in dataset:
        processed_row = [float(val) for val in row[:-1]] + [int(row[-1])]
        dataset_v2.append(processed_row)

    train_set = dataset_v2[:int(len(dataset_v2) * 0.85)]
    test_set = dataset_v2[int(len(dataset_v2) * 0.85):]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)

    print(accuracy_score(test_y, predictions))
    new_sample = input().split()
    predicted_class = classifier.predict([new_sample])[0]
    probabilities = classifier.predict_proba([new_sample])
    print(predicted_class)
    print(probabilities)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_x, train_y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_x, test_y)

    # submit na klasifikatorot
    submit_classifier(classifier)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija
