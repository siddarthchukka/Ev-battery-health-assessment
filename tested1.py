from sklearn.preprocessing import LabelEncoder
import joblib

battery_ids = ["B5", "B6", "B7"]
le_battery = LabelEncoder()
le_battery.fit(battery_ids)

joblib.dump(le_battery, "battery_le.pkl")

print("LabelEncoder saved as battery_le.pkl")
