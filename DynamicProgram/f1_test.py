import random
from sklearn.metrics import f1_score, classification_report


def test_f1():
    labels = [0] * 1000 + [1] * 1000 + [2] * 1000
    predicts = [0] * 900 + [random.randint(0, 2) for i in range(2100)]
    # predicts = [random.randint(0, 2) for i in range(1100)]

    micro_f1 = f1_score(labels, predicts, average='micro')
    macro_f1 = f1_score(labels, predicts, average='macro')

    print(classification_report(labels, predicts, target_names=['A', 'B', 'C']))
    print(f"micro_f1: {micro_f1}")
    print(f"macro_f1: {macro_f1}")

