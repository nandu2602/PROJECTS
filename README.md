# 🌱 Crop Prediction using Machine Learning

A machine learning–based crop prediction model designed to help farmers make informed decisions about crop selection, planting, and harvesting through data-driven insights and a user-friendly web interface.

---

## 🚀 Project Overview

- Used a balanced dataset of 2,200 samples across 22 crop types, with features like NPK levels (Nitrogen, Phosphorus, Potassium), soil pH, temperature, humidity, and rainfall  
- Built a Deep Neural Network (PyTorch) with three hidden layers (64-128-64 units + SeLU activations) and a softmax output layer for multi-class crop classification  
- Achieved ~99% accuracy on both train and test sets (80/20 split)  
- Deployed with a web interface and integrated APIs for dynamic weather and geolocation data  

---

## 📂 Data & Preprocessing

- **Primary Dataset**: Crop-Prediction CSV – 2200 samples equally representing 22 crops  
- **Weather Dataset**: Rainfall-in-India (used to correlate geolocations and rainfall)  
- **Preprocessing steps**:
  - Cleaned missing values  
  - Scaled/normalized numerical features  
  - Visualized correlations and feature distributions  

Visualizations include pair plots, correlation matrices, and interactive feature charts.

---

## 🧠 Model Architecture & Training

- **Model**: 3-hidden-layer DNN (64 → 128 → 64 units) + softmax output layer  
- **Activation**: SeLU for hidden layers; softmax for output  
- **Loss**: Categorical cross-entropy  
- **Optimizer**: Adam  
- **Training**: 100 epochs on 80/20 train-test split  
- **Performance**: ~99% test accuracy  
