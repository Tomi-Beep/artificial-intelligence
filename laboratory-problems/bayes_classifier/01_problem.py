import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]
if __name__ == '__main__':
    # Vashiot kod tuka
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    train_set = dataset[:int(0.75 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_set = dataset[int(0.75 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    classifier = CategoricalNB()
    train_x = encoder.transform(train_x)
    test_x = encoder.transform(test_x)
    classifier.fit(train_x, train_y)
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii
    correct = 0
    for x, y in zip(test_x, test_y):
        predicted = classifier.predict([x])[0]
        if y == predicted:
            correct += 1
    print(correct / len(test_set))
    new_sample = input().split()
    new_sample = encoder.transform([new_sample])
    predicted_class = classifier.predict(new_sample)[0]
    probabilities = classifier.predict_proba(new_sample)
    
    print(predicted_class)
    print(probabilities)
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_x, train_y)
    # submit na testirachkoto mnozestvo
    submit_test_data(test_x, test_y)
    # submit na klasifikatorot
    submit_classifier(classifier)
    # submit na encoderot
    submit_encoder(encoder)
