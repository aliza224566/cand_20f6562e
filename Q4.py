import math

def kmeans_assign(points, centroids):
    assignments = []
    
    for p in points:
        best_idx = 0
        best_dist = None
        
        for i, c in enumerate(centroids):
            dist = math.sqrt(sum((p[j] - c[j]) ** 2 for j in range(len(p))))
            if best_dist is None or dist < best_dist:
                best_dist = dist
                best_idx = i
        
        assignments.append(best_idx)
    
    return assignments
