import numpy as np

def accuracy_score(y_true, y_pred):
    total_predictions = len(y_true)
    correct_prdictions = 0
    for i in range(total_predictions):
        if y_true[i] == y_pred[i]:
            correct_prdictions += 1
    
    return correct_prdictions / total_predictions