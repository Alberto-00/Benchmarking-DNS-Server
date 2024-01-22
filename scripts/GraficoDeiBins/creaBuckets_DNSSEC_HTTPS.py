import numpy as np
import sys
def quantize_latency(latencies, resolution_percent, test):
    #print(resolution_percent)
    #Step 1: Quantizzazione della Latenza in Blocchi
    bin_size = (np.percentile(latencies, resolution_percent)/test)
    bins = np.arange(0, max(latencies) + bin_size, bin_size)
    
    # Controlla se ci sono zeri nei bins
    if 0 in bins:
        bins = bins[bins > 0]
    
    # Se i bins sono troppo piccoli, usa una quantizzazione lineare
    if bin_size < 1e-6:
        bins = np.linspace(0, max(latencies), int(max(latencies) / bin_size) + 1)
    
    # Step 2: Aumento Logaritmico dell'Intervallo di Latenza
    if len(bins) > 1:
        log_bins = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
    else:
        log_bins = bins
    
    # Controlla se ci sono NaN nei log_bins
    if np.isnan(log_bins).any():
        log_bins = bins
    
    # Step 3: Costruzione di Istogrammi Percentili Logaritmici
    hist, bin_edges = np.histogram(latencies, bins=log_bins)
    #print("qua")
    # Step 4: Stampa dei Blocchi con Range di Latenze e Numero di Richieste
    for i in range(len(hist)):
        print(f"Bin {i + 1}: Range {bin_edges[i]:.6f} - {bin_edges[i + 1]:.6f} ms, Richieste: {hist[i]}")

# Apre il file in modalità lettura
with open(sys.argv[1], 'r') as file:
    # Legge il contenuto del file
    content = file.read()

# Divide la stringa in una lista di stringhe usando la virgola come separatore e rimuove gli spazi vuoti
    numbers_str = content.split(',')
# Converte le stringhe in numeri decimali
    numbers = [float(num) for num in numbers_str]
    #print(numbers)
    quantize_latency(numbers, float(sys.argv[2]), float(sys.argv[3]))
