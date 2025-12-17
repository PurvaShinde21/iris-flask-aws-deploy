# 🌸 Iris Species Classification – Random Forest ML API

This project demonstrates a **Random Forest machine learning model** trained on the classic **Iris dataset**, exposed via a **Flask REST API**. The API predicts the iris species based on four flower measurements.

---

## Project Overview

* **Model**: Random Forest Classifier (scikit-learn)
* **Dataset**: Iris dataset
* **API Framework**: Flask
* **Model Persistence**: joblib
* **Deployment-ready**: Suitable for Docker / AWS / EC2 / ECS

The model predicts one of three iris species based on:

1. Sepal length
2. Sepal width
3. Petal length
4. Petal width

---

## Project Structure

```
iris-classifier/
│
├── app.py              # Flask API
├── train.py            # Model training script
├── utils.py            # Model loading & prediction helpers
├── model.joblib        # Trained Random Forest model
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1 Clone the Repository

```bash
git clone <your-repo-url>
cd iris-classifier
```

### 2 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Train the Model

Run the training script to train and save the Random Forest model:

```bash
python train.py
```

### Output

* Prints model accuracy and classification report
* Saves trained model as:

```
model.joblib
```

---

## Run the Flask API

Start the Flask application:

```bash
python app.py
```

The API will be available at:

```
http://localhost:5000
```

---

##  API Endpoints

###  Health Check

**GET /**

```bash
curl http://localhost:5000/
```

**Response**

```json
"🌸 Iris Classifier API is running!"
```

---

###  Predict Iris Species

**POST /predict**

#### Request Body

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

>  The `features` list must contain exactly **4 numeric values**.

#### Response

```json
{
  "prediction": 0
}
```

### Prediction Mapping

| Label | Species    |
| ----- | ---------- |
| 0     | Setosa     |
| 1     | Versicolor |
| 2     | Virginica  |

---

## Technologies Used

* Python 3.x
* Flask
* scikit-learn
* NumPy
* joblib

---

## Dependencies

From `requirements.txt`:

```
flask
scikit-learn
joblib
```

