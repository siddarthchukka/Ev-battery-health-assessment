import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Optional: XGBoost
try:
    from xgboost import XGBRegressor
    xgb_installed = True
except ImportError:
    xgb_installed = False

# Load dataset
df = pd.read_csv("Battery_dataset.csv")  # Replace with your actual file path

# Encode 'battery_id'
le = LabelEncoder()
df['battery_id'] = le.fit_transform(df['battery_id'])

# Features and Targets
features = ['battery_id', 'cycle', 'chI', 'chV', 'chT', 'disI', 'disV', 'disT', 'BCt']
target_soh = 'SOH'
target_rul = 'RUL'

X = df[features]
y_soh = df[target_soh]
y_rul = df[target_rul]

# Train-Test Split
X_train, X_test, y_soh_train, y_soh_test, y_rul_train, y_rul_test = train_test_split(
    X, y_soh, y_rul, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models
models = {
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
}

if xgb_installed:
    models["XGBoost"] = XGBRegressor(n_estimators=100, random_state=42)

# Training and Evaluation
print("====== Predicting SOH ======")
for name, model in models.items():
    model.fit(X_train_scaled, y_soh_train)
    preds = model.predict(X_test_scaled)
    print(f"{name} - R2: {r2_score(y_soh_test, preds):.4f}, MSE: {mean_squared_error(y_soh_test, preds):.4f}")

print("\n====== Predicting RUL ======")
for name, model in models.items():
    model.fit(X_train_scaled, y_rul_train)
    preds = model.predict(X_test_scaled)
    print(f"{name} - R2: {r2_score(y_rul_test, preds):.4f}, MSE: {mean_squared_error(y_rul_test, preds):.4f}")
