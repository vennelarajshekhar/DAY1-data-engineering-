# Day 4 — Metrics Worksheet

### 1. Given information

- Total candidates: 10
- Negative/passive candidates: 8
- Positive/active candidates: 2
- The model predicts 3 candidates as positive.
- Out of those 3 predicted positive candidates, only 1 is actually positive.

### 2. Metric calculations

| Quantity | Value |
|---|---:|
| True Positives (TP) | 1 |
| False Positives (FP) | 2 |
| False Negatives (FN) | 1 |
| True Negatives (TN) | 6 |
| Accuracy | 70% |
| Precision | 33.33% |
| Recall | 50% |

### 3. Formulas

**Accuracy**

Accuracy = (TP + TN) / Total

= (1 + 6) / 10

= 0.70 (70%)

**Precision**

Precision = TP / (TP + FP)

= 1 / (1 + 2)

= 0.3333 (33.33%)

**Recall**

Recall = TP / (TP + FN)

= 1 / (1 + 1)

= 0.50 (50%)

### 4. What do these metrics mean?

- **Accuracy:** Out of all 10 candidates, the model made 7 correct predictions.
- **Precision:** Out of the 3 candidates predicted as positive, only 1 was actually positive.
- **Recall:** Out of the 2 actual positive candidates, the model correctly identified only 1.

### 5. Conclusion

Accuracy tells us how many predictions were correct overall.

Precision tells us how many predicted positive candidates were actually positive.

Recall tells us how many actual positive candidates the model successfully identified.