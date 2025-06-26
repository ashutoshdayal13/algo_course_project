# Object Detection and Instance Segmentation in 2D Matrices

This project consists of two major components implemented in Python:

1. **Object Tracking in Random Matrices** – Identifying horizontally moving objects across two 2D matrices using MSE-based matching and optimized hashing.
2. **Instance Segmentation from Semantic Labels** – Converting a semantic segmentation mask into an instance segmentation mask using graph-based connected components.

---

## Post Mid-sem: Object Tracking in 2D Matrices

### Problem
Given two 2D matrices (`mat1` and `mat2`), where an object moves horizontally to the left from `mat1` to `mat2`, the goal is to detect and generate a mask of the moving object. The match is constrained row-wise using window-based mean squared error (MSE) metrics.

### Features
- Dynamic programming-based object matching.
- Multiple window types (3x3, 2x3, 2x2) to handle edges and corners.
- Constraint-aware pixel matching with sequential position consistency.
- Optimized version using **polynomial rolling hash** for fast pixel-window comparison.

### Technologies
- Python
- NumPy
- Matplotlib

---

## Pre Mid-sem: Instance Segmentation from Semantic Masks

### Problem
Given a semantic segmentation mask (2D image with class labels), generate an instance segmentation mask where each connected component of a class is assigned a unique instance ID.

### Features
- Each pixel treated as a graph node; 8-way connectivity defines edges.
- Graph traversal identifies connected components per class.
- Uses RGB-sum to determine semantic labels.
- Fully dynamic handling of any number of classes or object shapes.

### Technologies
- Python
- OpenCV
- NumPy
- Matplotlib

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/object-instance-segmentation.git
   cd object-instance-segmentation
