"""
Дадено е податочно множество за класификација на квалитет на вино. Секоја инстанца е претставена со 11 хемиски карактеристики и една класа за добар ('good') и лош ('bad') квалитет на вино. Променете го податочното множество така што првата и последната хемиска карактеристика ќе ги замените со збирот на соодветните вредности. Новата карактеристика поставете ја како прва колона во множеството. Новата верзија на податочното множество треба да има 10 хемиски карактеристики.

Поделете го податочното множество на множества за тренирање и тестирање на следниот начин. Ако критериумот за поделба C има вредност 0 за тренирање се користат првите P проценти од секоја од класите, а за тестирање останатите 100 - P проценти. Ако критериумот за поделба C има вредност 1 за тренирање се користат последните P проценти од секоја од класите, а за тестирање останатите 100 - P проценти. При поделба користете ја прво класата good, а потоа класата bad. Потоа скалирајте ги атрибутите во рангот [-1, 1].

Направете наивен баесов класификатор кој ќе го тренирате со верзијата на податочното множество во која првата и последната хемиска карактеристика се заменети со нивниот збир без примена на скалирање. Потоа, направете и втор наивен баесов класификатор кој ќе го тренирате со верзијата на податочното множество во која првата и последната хемиска карактеристика се заменети со нивниот збир и потоа е применето скалирање. Испечатете ја точноста на двата класификатори.

Од стандарден влез прво се чита критериумот за поделба C, а потоа се чита процентот за поделба P.

На стандарден излез да се испечати точноста добиена со двата класификатори.
"""

import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    for i, x in enumerate(dataset):
        sum = x[0] + x[-2]
        kraen = x[-1]
        dataset[i] = dataset[i][1:-2] + [kraen]
        dataset[i] = [sum] + dataset[i]

    dataset_0 = [row for row in dataset if row[-1] == 'bad']
    dataset_1 = [row for row in dataset if row[-1] == 'good']

    skros = int(input())
    p = float(input())

    if (skros == 0):
        train_set_0 = dataset_0[:int(len(dataset_0) * p / 100)]
        test_set_0 = dataset_0[int(len(dataset_0) * p / 100):]
        train_set_1 = dataset_1[:int(len(dataset_1) * p / 100)]
        test_set_1 = dataset_1[int(len(dataset_1) * p / 100):]
    else:
        train_set_0 = dataset_0[(int(len(dataset_0) * (100 - p) / 100)):]
        test_set_0 = dataset_0[:int(len(dataset_0) * (100 - p) / 100)]
        train_set_1 = dataset_1[(int(len(dataset_1) * (100 - p) / 100)):]
        test_set_1 = dataset_1[:int(len(dataset_1) * (100 - p) / 100)]

    train_set = train_set_0 + train_set_1
    test_set = test_set_0 + test_set_1

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_x)
    train_x_scaled = scaler.transform(train_x)
    test_x_scaled = scaler.transform(test_x)

    c1 = GaussianNB()
    c2 = GaussianNB()
    c1.fit(train_x, train_y)
    c2.fit(train_x_scaled, train_y)

    accuracy = 0
    predictions = c1.predict(test_x)
    for pred, known in zip(predictions, test_y):
        if pred == known:
            accuracy += 1
    print(f"Tochnost so zbir na koloni: {accuracy/len(test_x)}")
    accuracy = 0
    predictions = c2.predict(test_x_scaled)
    for pred, known in zip(predictions, test_y):
        if pred == known:
            accuracy += 1
    print(f"Tochnost so zbir na koloni i skaliranje: {accuracy/len(test_x)}")


