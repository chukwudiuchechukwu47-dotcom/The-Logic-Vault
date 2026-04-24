import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')
sns.set_theme(style="dark", rc={"axes.facecolor": "black", "figure.facecolor": "black"})
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
data = {
    'session_id': ['001','002','003','004','005','006','007','008','009','010'],
    'timestamp': ['2025-08-20','2025-06-20','2025-04-20','2025-05-20','2025-02-20','2025-06-20','2025-04-20','2025-09-20','2025-05-20','2025-04-20'],
    'airplane_mode': [None,None,'ON',None,None,'ON',None,'ON',None,None],
    'radio_override_active': [None,None,False,None,None,True,None,False,None,None],
    'data_used_mb':[12.4,11.9,None,25.8,13.2,None,8.5,None,14.7,30.2],
    'battery_drain_percent': [None,2.5,None,None,2.7,None,None,None,3.0,None],
    'carrier_ip_range_match': [True,True,False,True,True,False,True,False,True,True],
    'latency_ms': [45,48,None,42,51,None,47,None,53,44]
}

df = pd.DataFrame(data)
print(df)

#df['airplane_mode'] = df['airplane_mode'].fillna('OFF')
df['radio_override_active'] = df['radio_override_active'].replace([None], False).astype(bool)


df.loc[df['radio_override_active'] == False,'airplane_mode'] = 'OFF'
print(df)

df.loc[df['carrier_ip_range_match'] == False,'data_used_mb'] = 0.0
print(df)

median_value = df['battery_drain_percent'].median()
df['battery_drain_percent'] = df['battery_drain_percent'].fillna(median_value)
print(df)

df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df)

latency = df["latency_ms"].median()
df["latency_ms"] = df["latency_ms"].fillna(latency)
print(df.round(2))


sns.set_theme(style="ticks")

fig, axes = plt.subplots(3,2, figsize=(12,8))

sns.barplot(data=df, x='airplane_mode', y='data_used_mb', ax=axes[0,0], estimator='mean', errorbar=None, color="green")
axes[0,0].set_title('Avg Data Usage: Airplane Mode ON vs OFF')

sns.histplot(data=df, x='latency_ms', bins=6, ax=axes[0,1], kde=True, color="green")
axes[0,1].set_title('latency Distribution (ms)')

sns.lineplot(data=df, x='data_used_mb', y='battery_drain_percent', 
        hue='carrier_ip_range_match', ax=axes[1,0], color="green")
axes[1,0].set_title('Battery Drain vs Data Usage')

sns.boxplot(data=df, x='radio_override_active', y='latency_ms', ax=axes[1,1], color="green")
axes[1,1].set_title('latency by Radio Override Status')

sns.histplot(data=df, x="timestamp", ax=axes[2,0], color="green", bins=10)
axes[2,0].set_title('session Timestamps')
plt.setp(axes[2,0].get_xticklabels(), rotation=30)

sns.countplot(data=df, x="session_id", ax=axes[2,1], palette="rocket")
axes[2,1].set_title('Session Activity Over Time')

plt.tight_layout()
fig.patch.set_facecolor('black')
for ax in axes.flatten():
    ax.set_facecolor('black')
    ax.title.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='both', color='white', labelcolor='white', which='both')
    ax.tick_params(axis='x', color='white', labelsize=10)
    ax.tick_params(axis='y', color='white', labelsize=10)

    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    leg = ax.get_legend()
    if leg is not None:
       leg.get_frame().set_facecolor('black')

       leg.get_frame().set_edgecolor('white')
       for text in leg.get_texts():
         text.set_color('white')

plt.tight_layout(pad = 3.0)
plt.show()
