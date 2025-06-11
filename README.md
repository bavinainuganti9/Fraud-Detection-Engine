# Fraud Detection Engine

## Overview / Description  
Fraud-Detection-Engine (FraudShield) is a backend machine learning system designed to detect fraudulent activity in e-commerce transactions such as fake orders, bot activity, and refund fraud. It applies semi-supervised anomaly detection techniques on behavioral features extracted from transaction data to identify suspicious patterns in real time.

This tool is ideal for ML engineers and backend developers working on real-world fraud detection systems with business impact, especially in fintech and e-commerce domains.

## Features  
- Ingests transaction data (CSV/JSON) and extracts key behavioral features  
- Trains IsolationForest anomaly detection models to detect fraud patterns  
- Provides an API endpoint to score new transactions with fraud risk  
- Flags high-risk orders with clear alerts  
- Easily extensible for real-time streaming and dashboards  

## Architecture  
Backend: Python FastAPI serving REST API for prediction  
ML: IsolationForest anomaly detection model using scikit-learn  
Storage: CSV for demo, scalable to PostgreSQL for production  
Server: Uvicorn ASGI server for deployment  

## Tech Stack  
Backend: Python, FastAPI  
ML: scikit-learn (IsolationForest)  
Data: pandas, NumPy  
Storage: CSV (demo), PostgreSQL (prod)  
Server: Uvicorn  
