# Day 3 — Notes

### 1. What does an IoU of 1 mean? What does an IoU near 0.14 mean at a 0.5 threshold?

An IoU of 1 means both bounding boxes are exactly the same and have 100% overlap. An IoU near 0.14 means the boxes have very little overlap. Since 0.14 is below the threshold of 0.5, the boxes are considered unmatched.

### 2. Why is an empty file different from a missing file?

An empty label file means we have checked the image and intentionally recorded that there are no objects present. A missing file means the label file was not created or is not available. Therefore, an empty file represents a valid no-object example, whereas a missing file does not.

### 3. What do the four numbers after the class id mean?

The four numbers in YOLO format represent the normalized center X, center Y, width, and height of the bounding box.

- Center X: Horizontal center of the box divided by image width.
- Center Y: Vertical center of the box divided by image height.
- Width: Box width divided by image width.
- Height: Box height divided by image height.

These values are normalized between 0 and 1 so that bounding boxes can be represented relative to the image dimensions.