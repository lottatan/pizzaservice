# PIZZA PALVELU

Ideana olisi luoda online-pizzapalvelu, josta voi tilata pizzaa ja juomia.
 
Kun on luonut käyttäjän, on mahdollista tarkastella omia vanhoja tilauksia, nähdä kuinka paljon on käyttänyt yhteensä rahaa pizzapalveluun,
suosituimmat tuotteensa, ja jättää arvosteluja ja kommentteja.

Pizzapalvelun nettisivulta voi tilataamisen lisäksi nähdä annettuja arvosteluja, sekä kuinka monta tähteä palvelu on keskimäärin saanut.
Sivulla näkee myös, mitkä ovat olleet suosituimmat pizzat.

Sivulta löytyy pizzojen ainekset ja allergenit, pizzerioiden sijaintitiedot ja tiedot yrityksen henkilökunnasta.

Tilauksessa voi ruksia ruutuun tahtomansa pizzat ja juomat. Tilaajan täytyy hänen ilmoittaa myös toimitusosoite ja antaa tarkat saapumisohjeet.

Kun tilaus on tehty, sovellus näyttää myös arvioidun toimituskeston.

## Sovelluksen toiminnot

- Käyttäjä voi rekisteröidä uuden käyttäjätilin tai kirjautua sisään

- Jos käyttäjä on kirjautunut sisään, pystyy hän jättämään kommentteja tai arvosteluja

- Kuka tahansa pystyy tarkastelemaan arvosteluja ja kommentteja

- Käyttäjä pystyy tarkastelemaan omaa tilaushistoriaansa ja suosikkituotteitaan

- On mahdollista nähdä myös PizzaServicen suosituin pizza ja juoma


## Sovelluksen käynnistysohjeet

1. Kloonaa repositorio ja siirry sen juureen komennolla " cd pizzaservice"

2. Luo uusi ".env" -niminen tiedosto hakemiston juureen ja lisää sinne seuraavat tiedot:

    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>

3. Aktivoi virtuaaliympäristö ja asenna sovellukseen riippuvuudet:

        $ python3 -m venv venv
        $ source venv/bin/activate

4. Lisää myös requirements tiedosto ja määritä tietokanta:
        
        $ pip install -r ./requirements.txt
        $ psql < schema.sql

5. Käynnistä sovellus komennolla "flask run"