import math

def knn_predict(train_X, train_y, test_X, k):
    predictions = []
    
    for tx in test_X:
        distances = []
        for i in range(len(train_X)):
            dist = math.sqrt(sum((tx[j] - train_X[i][j]) ** 2 for j in range(len(tx))))
            distances.append((dist, train_y[i]))
        
        distances.sort(key=lambda x: (x[0], x[1]))
        k_neighbors = distances[:k]
        
        votes = {}
        for _, label in k_neighbors:
            votes[label] = votes.get(label, 0) + 1
        
        max_votes = max(votes.values())
        best_labels = [label for label, count in votes.items() if count == max_votes]
        predictions.append(min(best_labels))
    
    return predictions
