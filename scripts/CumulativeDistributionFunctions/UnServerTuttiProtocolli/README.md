

Lo script plotCDF2.py permette di generare il grafico in cui vengono mostrare una CDF per ogni protocollo testato su un dato server.
Prende in input i seguenti campi:
- `titoloGrafico`: Il titolo che verrà mostrato sopra il grafico;
- `nomeImmagine`: Nome dell'immagine che verrà prodotta;
- `fileUDP`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo DNS-over-UDP sul server;
- `fileTCP`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo DNS-over-TCP sul server;
- `fileTLS`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo DNS-over-TLS sul server;
- `fileHTTPS`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo DNS-over-HTTPS sul server;
- `fileDNSSEC`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo DNS-over-DNSSEC sul server;

Esempio di utilizzo
Prendiamo in considerazione i file: `fileUDP.txt`, `fileTCP.txt`, `fileTLS.txt`, `fileHTTPS.txt`, `fileDNSSEC.txt` con all'interno la latenza di ogni richiesta formattata nel modo seguente: `0.0043662,0.0047483,0.0049923,0.0088992,0.0100398.....`

L'esecuzione del comando `python3 plotCDF2.py Benchmarking_ServerX Benchmarking_ServerX.png Latenze_UDP_SuServerX Latenze_TCP_SuServerX Latenze_TLS_SuServerX Latenze_HTTPS_SuServerX Latenze_DNSSEC_SuServerX` produrrà grafici come quelli presenti in [Benchmarking-DNS-Server/Results/One server with every protocol
/Cumulative Distribution Function (CDF)/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20server%20with%20every%20protocol/Cumulative%20Distribution%20Function%20(CDF))
