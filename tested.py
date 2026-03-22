import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import joblib

# Load dataset
df = pd.read_csv("Battery_dataset.csv")  # 🔁 Change path if needed

# Encode battery_id
le = LabelEncoder()
df['battery_id'] = le.fit_transform(df['battery_id'])

# Features and targets
features = ['battery_id', 'cycle', 'chI', 'chV', 'chT', 'disI', 'disV', 'disT', 'BCt']
target_soh = 'SOH'
target_rul = 'RUL'

X = df[features]
y_soh = df[target_soh]
y_rul = df[target_rul]

# Train-test split
X_train, X_test, y_soh_train, y_soh_test, y_rul_train, y_rul_test = train_test_split(
    X, y_soh, y_rul, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 🎯 Train Random Forest for SOH
rf_soh = RandomForestRegressor(n_estimators=100, random_state=42)
rf_soh.fit(X_train_scaled, y_soh_train)

# 🎯 Train XGBoost for RUL
xgb_rul = XGBRegressor(n_estimators=100, random_state=42)
xgb_rul.fit(X_train_scaled, y_rul_train)

# 💾 Save the models
joblib.dump(rf_soh, "soh_model.pkl")
joblib.dump(xgb_rul, "rul_model.pkl")
joblib.dump(scaler, "scaler.pkl")  # Save the scaler too
print("✅ Models and scaler saved successfully!")