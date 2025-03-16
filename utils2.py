import pandas as pd
import matplotlib.pyplot as plt

csv_files = [
    # 'ml_nanosleep',
    'ml_signal_latency',
    # 'ml_timer_jitter',
    # 'ml_usleep_jitter',
    # 'nanosleep',
    'signal_latency',
    # 'timer_jitter',
    # 'usleep_jitter'
]

for i in range(len(csv_files)):
    csv_files[i] = csv_files[i] + '.csv'

cpu_low = []
cpu_med = []
cpu_high = []
cpu_mew_with_memory = []
cpu_high_with_memory = []

ml_cpu_low = []
ml_cpu_med = []
ml_cpu_high = []
ml_cpu_mew_with_memory = []
ml_cpu_high_with_memory = []

for file in csv_files:
    df = pd.read_csv(file)

    # print out the name of the cols
    print(df.columns)

    if 'ml' in file:
        ml_cpu_low.append(df['CPU Low (ns)'][:1000])
        ml_cpu_med.append(df['CPU Medium (ns)'][:1000])
        ml_cpu_high.append(df['CPU High (ns)'][:1000])
        ml_cpu_mew_with_memory.append(df['CPU Medium & Memory Intensity (ns)'][:1000])
        ml_cpu_high_with_memory.append(df['CPU High & Memory Intensity (ns)'][:1000])
    else:
        cpu_low.append(df['CPU Low (ns)'][:1000])
        cpu_med.append(df['CPU Medium (ns)'][:1000])
        cpu_high.append(df['CPU High (ns)'][:1000])
        cpu_mew_with_memory.append(df['CPU Medium & Memory Intensity (ns)'][:1000])
        cpu_high_with_memory.append(df['CPU High (ns)'][:1000])

cpu_low =  cpu_low+ml_cpu_low
cpu_med =cpu_med+  ml_cpu_med
cpu_high = cpu_high+ ml_cpu_high
cpu_mew_with_memory =cpu_mew_with_memory+ ml_cpu_mew_with_memory
cpu_high_with_memory =  cpu_high_with_memory + ml_cpu_high_with_memory

# each of the lists contain a list of dataframes, these are the different csv files
plt.figure(figsize=(10, 6))
for i, df in enumerate(cpu_low):
    label = ['Signal Latency', 'Memory Locked Signal Latency'][i]
    plt.plot(df.index, df, linestyle='-', label=label)
plt.title('CPU Low Jitter (ns)')
plt.xlabel('Index')
plt.ylabel('CPU Low (ns)')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
for i, df in enumerate(cpu_med):
    label = ['Signal Latency', 'Memory Locked Signal Latency'][i]
    plt.plot(df.index, df, linestyle='-', label=label)
plt.title('CPU Medium Jitter (ns)')
plt.xlabel('Index')
plt.ylabel('CPU Medium (ns)')
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
for i, df in enumerate(cpu_high):
    label = ['Signal Latency', 'Memory Locked Signal Latency'][i]
    plt.plot(df.index, df, linestyle='-', label=label)
plt.title('CPU High Jitter (ns)')
plt.xlabel('Index')
plt.ylabel('CPU High (ns)')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
for i, df in enumerate(cpu_mew_with_memory):
    label = ['Signal Latency', 'Memory Locked Signal Latency'][i]
    plt.plot(df.index, df, linestyle='-', label=label)
plt.title('CPU Medium with Memory Load Jitter (ns)')
plt.xlabel('Index')
plt.ylabel('CPU Medium with Memory Load (ns)')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
for i, df in enumerate(cpu_high_with_memory):
    label = ['Signal Latency', 'Memory Locked Signal Latency'][i]
    plt.plot(df.index, df, linestyle='-', label=label)
plt.title('CPU High with Memory Load Jitter (ns)')
plt.xlabel('Index')
plt.ylabel('CPU High with Memory Load (ns)')
plt.legend()
plt.tight_layout()
plt.show()