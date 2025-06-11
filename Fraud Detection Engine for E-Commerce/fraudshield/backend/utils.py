import pandas as pd

def load_features(file_path):
    df = pd.read_csv(file_path)
    X = df[["order_value", "num_items", "time_to_checkout", "refund_count", "is_bot"]]
    return X

def preprocess_order(data):
    return [[
        data["order_value"],
        data["num_items"],
        data["time_to_checkout"],
        data["refund_count"],
        data["is_bot"],
    ]]
