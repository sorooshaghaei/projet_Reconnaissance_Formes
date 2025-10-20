# knn_demo.py
import numpy as np
from collections import Counter
from sklearn.metrics import accuracy_score


def simple_knn_train_predict(X_train, y_train, X_test, k=3, p=2):
    # calcule distances entre chaque test et tout train
    # implémentation très simple
    preds = []
    for xt in X_test:
        # distances
        if p == 2:
            dists = np.sqrt(((X_train - xt) ** 2).sum(axis=1))
        else:
            dists = np.abs(X_train - xt).sum(axis=1)
        idx = np.argsort(dists)[:k]
        lab = Counter(y_train[idx]).most_common(1)[0][0]
        preds.append(lab)
    return np.array(preds)


if __name__ == "__main__":
    # Exemple: données simulées
    # 9 classes, 11 échantillons chacune -> total 99 (mais on simule 90)
    np.random.seed(0)
    n_samples = 90
    n_features = 36
    X = np.random.randn(n_samples, n_features)
    y = np.repeat(np.arange(1, 10), 10)[:n_samples]  # classes 1..9 répétés

    # split simple train/test
    n_train = int(0.7 * n_samples)
    X_train, X_test = X[:n_train], X[n_train:]
    y_train, y_test = y[:n_train], y[n_train:]

    preds = simple_knn_train_predict(X_train, y_train, X_test, k=3, p=2)
    print("Accuracy:", accuracy_score(y_test, preds))
    print("Predict exemples :", preds[:10])
