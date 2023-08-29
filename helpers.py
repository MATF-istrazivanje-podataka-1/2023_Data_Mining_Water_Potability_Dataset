import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
import joblib


def report(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Tačnost: {accuracy}')
    print("Izvestaj:")
    print(classification_report(y_test, y_pred))

    print("Matrica konfuzije:")
    print(pd.DataFrame(confusion_matrix(y_test, y_pred)))


def print_roc_curve(models: dict, X_test, y_test):
    for model_name, model in models.items():
        y_pred = model.predict(X_test)
        fpr, tpr, _ = roc_curve(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred)
        lab = model_name + "(auc: " + str(round(auc, 2)) + ")"
        plt.plot(fpr, tpr, label=lab)

    plt.plot([0, 1], [0, 1], label='Random (auc: 0.5)', color='red')
    plt.title("Poređenje modela")
    plt.legend()
    plt.show()


def save_model(model, filename):
    with open(filename, 'wb') as file:
        joblib.dump(model, file)
