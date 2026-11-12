# Day 4 — Leak Report

### 1. Validation frame IDs

The six frames selected for validation are:

- src02-f01
- src00-f03
- src02-f02
- src09-f00
- src06-f01
- src06-f00

### 2. Source with leftover frames

The source `src02` appears in the validation list.

The following frames from the same source are still available for training:

- src02-f00
- src02-f03

### 3. What can the model memorize?

The model can learn from some frames of the same video during training and then see similar frames during validation. This can make the model's performance look better than it actually is.

### Conclusion

We should split data by source (video), not by individual frames. All frames from the same video should stay in either training or validation.
