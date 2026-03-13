import pandas as pd

data = {
    "test": ["test_login", "test_payment", "test_signup"],
    "fail_rate": [0.6, 0.2, 0.8]
}

df = pd.DataFrame(data)

df = df.sort_values(by="fail_rate", ascending=False)

print("Prioritized Tests:")
print(df["test"])

