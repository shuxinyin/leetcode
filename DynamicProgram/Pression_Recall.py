from sklearn.metrics import confusion_matrix, classification_report


def test():
    predicts = [1, 1, 2, 3, 2, 2, 3, 2, 3]
    labels = [1, 1, 1, 1, 2, 2, 2, 3, 3]

    predicts = [0, 0, 1, 2, 1, 1, 2, 1, 2]
    labels = [0, 0, 0, 0, 1, 1, 1, 2, 2]
    report = classification_report(labels, predicts, target_names=['A', 'B', 'C'], digits=3)
    confusion = confusion_matrix(labels, predicts)

    print(report)
    print(confusion)


if __name__ == '__main__':
    print(1111)
    test()
