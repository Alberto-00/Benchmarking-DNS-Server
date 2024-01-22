# Scripts
In questa cartella sono presenti gli script Python e Shell utilizzati per l'analisi, l'estrazione, la manipolazione e la visualizzazione dei dati.

## Cartelle
- CumulativeDistributionFunctions:
  - UnProtocolloTuttiServer
  - UnServerTuttiProtocolli
- GraficoDeiBins:
  - `creaBuckets_DNSSEC_HTTPS.py`: date le latenze per ogni richiesta permette di calcolare i bins con lo stesso calcolo di dnsperf;
  - `creaGrafici_DNSSEC_HTTPS.sh`: dati i bins calcolati con lo script precedente permette di generare il grafico dei bins;
  - `plotG_DNSSEC_HTTPS.py`: file utilizzato da `creaGrafici_DNSSEC_HTTPS.sh`;
  - `create_plot.sh`: dato il file output di dnsperf permette di generare il grafico dei bins;
  - `plot.py`: file utilizzato da `create_plot.sh`.
- GraficoDelleLatenze:
  - `plotA.sh`: date le latenze per ogni richiesta permette di generare il grafico delle latenze;
  - `plotA.py`: file utilizzato da `plotA.sh`.
- GraficoLatenzaMaxMinMediaDevStd:
  - `plotBarreErrori.sh`: dati i file di output di dnsperf permette di generare un grafico a barre per la latenza minima, massima, media e deviazione standard;
  - `plotBarreErrori2.py`: file utilizzato da `plotBarreErrori.sh`;
  - `plotBarreErroriDNSSEC_HTTPS.py`: dati i file delle latenze di ogni richiesta permette di generare un grafico a barre per la latenza minima, massima, media e deviazione standard.
