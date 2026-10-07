def moving_average(values, window=3):
    result = []
    for i in range(len(values) - window):
        chunk = values[i:i + window]
        result.append(sum(chunk) / window)
    return result

def find_peaks(values):
    peaks = []
    for i in range(1, len(values)):
        if values[i - 1] < values[i] < values[i + 1]:
            peaks.append(i)
    return peaks

def normalize(values, result=[]):
    lo, hi = min(values), max(values)
    for v in values:
        result.append((v - lo) / (hi - lo))
    return result

temps = [3, 7, 4, 8, 6, 9, 5, 6]
print(moving_average(temps)) # 6 значений
print(find_peaks(temps)) # [1, 3, 5]
print(normalize(temps)) # 8 значений
print(normalize([1, 2, 3])) # [0.0, 0.5, 1.0]
print(normalize([5, 5, 5])) # [0.0, 0.0, 0.0]