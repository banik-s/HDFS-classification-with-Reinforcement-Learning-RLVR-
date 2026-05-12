from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from tqdm import tqdm
from openai import OpenAI
from dotenv import load_dotenv
import os
import json


# connect to openai API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_inference(model_name, examples, response_format, system_prompt="Classify this HDFS log block as anomalous or normal."):
    """Run inference on examples and return predictions."""
    predictions = []
    for ex in tqdm(examples, desc=f"Running {model_name}"):
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "developer", "content": system_prompt},
                {"role": "user", "content": ex["text"]}
            ],
            response_format=response_format
        )
        pred = json.loads(response.choices[0].message.content)
        predictions.append(pred)  # Return full dict with Anomalous + reasoning
    return predictions

def calculate_metrics(predictions, labels):
    """Calculate accuracy, precision, recall, F1 using sklearn."""
    return {
        "accuracy": accuracy_score(labels, predictions),
        "precision": precision_score(labels, predictions, zero_division=0),
        "recall": recall_score(labels, predictions, zero_division=0),
        "f1": f1_score(labels, predictions, zero_division=0)
    }
