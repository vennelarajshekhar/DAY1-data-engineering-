def xyxy_to_yolo(box, width, height, class_id):
    left, top, right, bottom = box
    bw = right - left
    bh = bottom - top
    cx = left + bw / 2
    cy = top + bh / 2
    return f"{class_id} {cx / width:.6f} {cy / height:.6f} {bw / width:.6f} {bh / height:.6f}"


def yolo_to_xyxy(line, width, height):
    class_id, cx, cy, bw, bh = line.split()
    cx, cy, bw, bh = (float(v) for v in (cx, cy, bw, bh))
    cx *= width
    cy *= height
    bw *= width
    bh *= height
    left = cx - bw / 2
    top = cy - bh / 2
    return int(class_id), (left, top, left + bw, top + bh)

if __name__ == "__main__":
    width = 100
    height = 100

    files = [
        "day03/labels/example_100.txt",
        "day03/labels/a.txt"
    ]

    for file in files:
        with open(file, "r") as f:
            line = f.readline().strip()

        class_id, box = yolo_to_xyxy(line, width, height)

        print(file, ":", box)
