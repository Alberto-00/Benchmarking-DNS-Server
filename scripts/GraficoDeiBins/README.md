## Per DNS-over-UDP, DNS-over-TCP e DNS-over-TLS
Lo script `create_plot.sh` permette di generare il grafico in cui vengono mostrari i bins risultanti dal benchmarking di un protocollo su un server
Prende in input i seguenti campi:
- file output di dnssperf;
- titolo del grafico che verrà mostrato nel grafico;
- nome dell'immagine che verrà generata.

##### Esempio di utilizzo
Prendiamo in considerazione il file ottenuto da dnsperf: `tls_bench_dnsperf_results.txt`.
L'esecuzione del comando `./create_plot.sh tls_bench_dnsperf_results.txt TLS_Benchmarking TLS_Benchmarking.png` produrrà grafici come quelli presenti in [Benchmarking-DNS-Server/Results/One protocol on all servers/UDP/BIND
/Bins Histogram/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/UDP/BIND/Bins%20Histogram)

**NOTA:** il file `plot.py` verrà eseguito automaticamente da `create_plot.sh`

## Per DNSSEC e DNS-over-HTTPS
Per questi due protocolli è stato necessario utilizzare `scriptKdig.sh`, quindi non si hanno i file di dnsperf ma si hanno i file con all'interno la latenze separate da virgola. Di conseguenza bisogna innanzitutto generare i buckets eseguendo il comando `python3 creaBuckets_DNSSEC_HTTPS.py fileLatenze.txt`. Oltre al file lo script prende in input due float: il primo è la risoluzione dei bins (nelle sperimentazioni è stata settata a 3 per replicare il processo matematico di dnsperf), il secondo indica il divisore della taglia dei bins (questo permette di ottenere più o meno bins a seconda della precisione grafica che si vuole ottenere, nelle sperimentazioni tale valore è stato incrementato o decrementato al fine di ottenere tra i 300 e 400 bins)
