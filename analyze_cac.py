import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cac_2024.csv")
avg = round(df["CAC"].mean(), 2)
print(f"Average CAC (2024): {avg}")  # must print 230.17

# Line chart for CAC trend with industry benchmark line at 150
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(df["Quarter"], df["CAC"], marker="o")
ax.axhline(150, linestyle="--", linewidth=1.0)
ax.set_title("Customer Acquisition Cost (CAC) – 2024 Quarterly Trend")
ax.set_xlabel("Quarter")
ax.set_ylabel("CAC")
ax.grid(axis="y", linestyle="--", linewidth=0.5, alpha=0.6)
fig.tight_layout()
fig.savefig("outputs/cac_trend.png", dpi=150, bbox_inches="tight")
plt.close(fig)
