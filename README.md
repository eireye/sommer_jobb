# sommer jobber

# Mangfold arbeid
Bruk repo:
https://github.com/statisticsnorway/FOU-Mangfold-421.git

I mappen

   /ssb/stamme03/fouoff_pii/Raadata/Mangfold/wk24 

ligger det en populasjonsfil. Denne skal det lages tabeller av. Se i mappen for å se lastefilene. De vil hete ting som Last_FoUoff019.txt o.l.

Disse tabellene lages per nå på en helt håpløs måte og de prikkes manuelt.
Her er måten det ble gjort på sist:
https://github.com/statisticsnorway/FOU-Mangfold-421/blob/main/src/notebooks/tabell_arbeid.ipynb

Det er skamfult arbeid og vil helst ikke gjøre det på den måten igjen.


Oppgaver
1. Lag tabellene på en bedre måte
   - Se helt vekk fra python koden her om mulig. Ønsker at dette skal gjøres i R fra nå av. Men der du kan gjenbruke kode som lager nye radnavn o.l. må du gjerne bruke på nytt.
Bruk gjerne R til å lage tabeller da prikke-pakken er laget i R og alt kan egentlig være i R. 
   - Lag alle tabellene. De bør ha relativt likt tall som på ssb.no, men noe vil variere fordi det er prikket på statbanken.
Under mangfoldsstatistiskk ligger tabellene som skal lages:
https://www.ssb.no/statbank/list/fouoff

Men bruk laste filene til å se hvilken struktur de skal ha.
     
   - Viktig at tabellene har rett kode slik som i lastefilene. Altså må det kanskje byttes om på navn på radene o.l. for å få disse lastekodene som skal brukes i statbanken.
2. Prikke tabellene
   - Per dags dato prikker vi manuelt. Det er en hodepine.
   - Bruk pakken fra SSB til å prikke. Klarer vi å få laget ferdig prikket tabeller her? Forsøk. Går det ikke så går det ikke.
  
   Mål: Få laget tabeller på en bedre måte i R.
   Drøm: Få automatisert prikkingen.



# Monitor-arbeid

## Oppgaver

1. [Oppgave 1: Fiksing av tabeller](./oppgaver/oppgave1.md)
2. [Oppgave 2: Monitor-arbeid 2](./oppgaver/oppgave2.md)

## Komme i gang

F
#### Oppgave 1 README.md


# Oppgave 1: Fiksing av tabeller

I mappen `sommerjobb` finner du en populasjonsfil for monitor. Denne filen skal brukes til å lage tabeller. Du kan se lastefilene i samme mappe.

## Mål

1. Lag tabellene på en mer effektiv måte.
   - Selv om tabellene allerede lages på en grei måte, bør hele prosessen flyttes over til et R-løp for bedre oversikt og vedlikehold.
   - Implementer R-skriptet du allerede har laget, men sørg for at det er mer oversiktlig og godt dokumentert.

## Oppgave 2: Prikke Tabellene

Per dags dato prikker vi tabellene manuelt, noe som er en tidkrevende og komplisert prosess.

### Mål

1. Automatiser prikkingen av tabellene.
   - Bruk SSB-pakken for prikkingen.
   - Forsøk å lage tabellene ferdig prikket automatisk. Hvis det ikke fungerer, dokumenter hvor det stopper opp.

## Innsending

Når du har fullført oppgaven, push endringene dine til en ny branch og opprett en pull request mot det originale repoet.

# Monitor-arbeid 2

I mappen `sommerjobb_dbh` ligger det tre filer:

1. To rensede filer fra et register som DBH sender oss:
   - Den ene filen har fødselsnummer som personidentifiserende tall (`fnr`).
   - Den andre filen har et "fnr" nummer, som er et generert nummer fra DBH (`f-x`).
2. Den tredje filen er forskningsmonitoren fra 2021.

## Mål

1. Flett DBH-dataen inn i monitoren fra 2021 i henhold til dokumentasjonen.
   - Se dokumentasjonen her: [link to documentation]

## Instruksjoner

### Steg 1: Kobling av data

1. **Koble fødselsnummer (`fnr`):**
   - Begynn med å koble filen som har fødselsnummer (`fnr`) mot `fnr`-kolonnen i monitor. Dette er da filen som heter dbh_fnr.csv
   - Vi skal da ha oppdatert monitoren så en ide er å bruke monitor for 2021 som den filen som dbh gjøres en left merge på.
   - Merk hver post med følgende utfall:
     - "monitor" hvis de finnes i monitoren men ikke i DBH-filen. Altså ingen treff
     - "DBH_Monitor" hvis de finnes i både DBH-filen og monitoren. Behold seneste "påbegynt" tidspunkt.
     - "DBH" hvis de er nye i DBH-filen.

2. **Koble genererte nummer (`f-x`):**
   - Koble deretter filen som har genererte nummer (`f-x`) mot `f-x`-kolonnen i monitor.
   - Følg samme merkingsregler som for fødselsnummer.

### Resultat

Til slutt skal du ha en oppdatert monitorfil som:
   - Har alle nye og oppdaterte poster korrekt merket.
   - Har ingen duplikater.
   - Har korrekt oppdatert fødselsnummer (`fnr`) og genererte nummer (`f-x`) kolonner, med ingen tomme fødselsnummerfelter for poster med kun genererte nummer.

## Innsending

Når du har fullført oppgavene, push endringene dine til en ny branch og opprett en pull request mot det originale repoet.

# Monitor oppgave 3
De genererte f-x numrene er upraktiske. Vi ønsker derfor å oppdatere disse til D-nummer eller fødselsnummer dersom de finnes i doktorgradregisteret eller forskerpersonalregisteret.
Mål

    Lag en funksjon/modul som bruker navn og fødselsdato til å lete etter fødselsnummer i disse to registrene.
        Oppdater f-x nummeret med fødselsnummer/D-nummer hvis det finnes.
        Lagre antall treff og oppdateringer som blir gjort.
        En modul/funksjon som vi enkelt kan bruke på dbh-filen og eksisterende monitor. Monitoren vil bli pseudonymisert og dette må da eventuelt gjøres på en annen måte... 

Instruksjoner

    Bruk navn og fødselsdato for å søke etter fødselsnummer i doktorgradregisteret og forskerpersonalregisteret.
    Oppdater f-x nummeret i monitorfilen med det funnede fødselsnummeret/D-nummeret.
    Lag en rapport som viser hvor mange poster som ble oppdatert.

Innsending

Når du har fullført oppgaven, push endringene dine til en ny branch og opprett en pull request mot det originale repoet.




Tips: Lag et program som kan lage en fil også loop på alle filene i etterkant. 
Typ som kan brukes slik i terminalen:

for year in {2012..2022}; do
  file="/ssb/stamme03/fouoff_pii/Raadata/forskerpersonale/wk01/fpreg_dump${year}.xlsx"
  if [ -f "$file" ]; then
    python main.py "$file"
  else
    echo "Fil ikke funnet: $file"
  fi
done
