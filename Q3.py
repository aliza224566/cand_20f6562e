import math

def top_k_cosine(query, docs, k):
    def norm(v):
        return math.sqrt(sum(x * x for x in v))
    
    q_norm = norm(query)
    similarities = []
    
    for i, d in enumerate(docs):
        d_norm = norm(d)
        if q_norm == 0 or d_norm == 0:
            sim = 0
        else:
            sim = sum(query[j] * d[j] for j in range(len(query))) / (q_norm * d_norm)
        similarities.append((sim, i))
    
    similarities.sort(key=lambda x: (-x[0], x[1]))
    return [idx for _, idx in similarities[:k]]
