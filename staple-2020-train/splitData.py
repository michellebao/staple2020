import os
import random

trainProp = 0.8
devProp = 0.1
testProp = 0.1

langDirectories = [x[0] for x in os.walk(os.getcwd())][1:]

for path in langDirectories:
    lang = path[-5:]
    trainSet = open(path + '/train.' + lang + '.2020-01-13.gold.txt', 'w')
    devSet = open(path + '/dev.' + lang + '.2020-01-13.gold.txt', 'w')
    testSet = open(path + '/test.' + lang + '.2020-01-13.gold.txt', 'w')
    # lines = open(path + '/train.' + lang + '.2020-01-13.gold.txt').read()
    officialFile = open(path + '/official_train.' + lang + '.2020-01-13.gold.txt', 'r')
    # with open(path + 'official_/train.' + lang + '.2020-01-13.gold.txt') as f:
    #     for line in f:
    #         if line[:6] == 'prompt':
    #             choice = randrange(1)
    #             if choice <= testProp:
    #                 trainSet.write(line)
    #         if "ROW" in line:
    #             f1.write(line)

    while True :
        line = officialFile.readline()
        if line:
            if line[:6] == 'prompt':
                choice = random.random()
                train = False
                dev = False
                test = False

                if choice <= trainProp:
                    train = True
                elif (choice > testProp and choice <= (trainProp + devProp)):
                    dev = True
                else:
                    test = True

                if train:
                    trainSet.write(line)
                if dev:
                    devSet.write(line)
                if test:
                    testSet.write(line)
                line = officialFile.readline()
                while line and line != "\n" :
                    if train:
                        trainSet.write(line)
                    if dev:
                        devSet.write(line)
                    if test:
                        testSet.write(line)
                    line = officialFile.readline()

                if train:
                    trainSet.write('\n')
                if dev:
                    devSet.write('\n')
                if test:
                    testSet.write('\n')

        else :
            officialFile.close()
            trainSet.close()
            devSet.close()
            testSet.close()
            break
