# vna
Programsnutter og filer som support for VNA boken

*Vær obs på at programsnuttene er enkle, og inneholder ikke feilsjekking. Det kan være at ditt oppsett bruker . og ikke , som komma.* 

### BPF_filter.py
Sett filterparameterene i bunnen av skriptet og kjør det. Utfører beregningen for standard, 2. ordens kondensatorkoblet båndpassfilter: 
![bpf_c2](https://github.com/user-attachments/assets/be107097-914f-421f-ac48-2219b2e048de)


### BPF_inductive.py
Sett filterparameterene i bunnen av skriptet og kjør det. Utfører beregningen for transformatorkoblet, 2. ordens båndpassfilter.
Skriptet gir ut beregnet antall turns på TOKO 10mm kjerne (MF trafoer fra transistormottaker).
![bpf_trafo](https://github.com/user-attachments/assets/7d2a5372-1d31-4cf7-87f7-8c37eb636b7f)


### krystallfilter.py
Kjør skriptet. Dette ber om verdiene i skriptet. 
![sch_xtal_filter](https://github.com/user-attachments/assets/6d322096-4905-44d7-a4ac-2e84f138266a)


### commonmode.py <s21.s2p> <s31.s2p>
Beregner common mode dempning basert på 2 komplette s-parameter filer. Se kapittelet i boken.


### Rollet.py S-parameter.s2p
Beregner Rollets stabilitetsfaktor for en gitt forsterker ut fra S-parameterene. Plotter en graf. 


### NanoVNA_set_F.py
Eksempelkode for å sette nettverksanalysatoren til en enkel frekvens, gjøre måling og skrive ut dataene. 


### NanoVNA_plots11.py <start_frekvens> <slutt_frekvens>
Eksempelkode for å gjøre ett sweep, regne om S-parameterene til impedans og fase, og plotte dataene. 


### combine_s2p.py <file_S11_S21.s2p> <file_S22_S12.s2p> <output_file.s2p>
Kombinerer S-parameter filer fra NanoVNA, hvor S12 og S22 er tomme, til korrekte Touchstonefiler. Dette krever at det måles fremover og revers, at filene lagres som separate filer og kombineres med dette programmet. 


------


For å installere matplotlib, numpy og pyserial i Python, kan du bruke pip-kommandoen i terminalen. Skriv følgende kommando:
*pip install matplotlib numpy pyserial*
