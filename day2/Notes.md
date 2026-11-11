
# Day 2 - Notes

## 1. What does FPS mean?

FPS stands for Frames Per Second. It tells us how many pictures are shown in one second of a video. In our project, FPS is 30, which means 30 pictures are shown every second.

## 2. Why can timestamp × fps select the wrong picture?

Because the annotation clock and video clock may not be synchronized. In our project, the annotation clock is 0.2 seconds behind the video clock. So, we must add the offset before calculating the frame number.

## 3. What is the offset for clip_a, in seconds and in frames?

The offset for clip_a is +0.2 seconds. At 30 FPS, 0.2 × 30 = 6 frames. So, the offset is +0.2 seconds or +6 frames.

## 4. Why did channel 0 not mean red?

OpenCV uses BGR colour order instead of RGB. Channel 0 is Blue, channel 1 is Green, and channel 2 is Red. Therefore, we used (0, 0, 255) to get red.
