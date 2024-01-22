Lo script `plotCDF2.py` permette di generare il grafico in cui vengono mostrare tre CDF riguardo il benchmarking di un protocollo, eseguito su tre server.
Prende in input i seguenti campi: 
- `titoloGrafico`: Il titolo che verrà mostrato sopra il grafico;
- `nomeImmagine`: Nome dell'immagine che verrà prodotta;
- `fileBind`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo sul server BIND;
- `filePower`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo sul server PowerDNS;
- `fileTECH`: File con valori separati da virgola che contiene le latenze delle richieste effettuate durante il benchmarking del protocollo sul server Technitium;

#### Esempio di utilizzo 
Prendiamo in considerazione i tre file: `fileBind.txt`, `filePower.txt`, `fileTECH.txt` con all'interno la latenza di ogni richiesta formattata nel modo seguente: `0.0043662,0.0047483,0.0049923,0.0088992,0.0100398.....`

L'esecuzione del comando `python3 plotCDF2.py TLS_Benchmarking TLS_Benchmarking.png fileBind.txt filePower.txt fileTECH.txt` produrrà grafici come quelli presenti in [Benchmarking-DNS-Server/Results/One protocol on all servers/TLS/Comparisons
/Cumulative Distribution Function (CDF)/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TLS/Comparisons/Cumulative%20Distribution%20Function%20(CDF))
