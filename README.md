# Snake Peli
Pelin tarkoitus on liikkua käärmeellä ruudulla ja kasvattaa sitä syömällä ruokaa, sekä pysyä hengissä/pelissä niin kauan kuin mahdollista.

### Python-versio
Toimii versiolla 3.8 ja uudemmilla

### Dokumentaatio
- [Vaatimusmäärittely](https://github.com/lottapispa/ot-harjoitystyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/lottapispa/ot-harjoitystyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/lottapispa/ot-harjoitystyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/lottapispa/ot-harjoitystyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/lottapispa/ot-harjoitystyo/blob/master/dokumentaatio/kayttoohje.md)
- [Testausdokumentti][https://github.com/lottapispa/ot-harjoitystyo/blob/master/dokumentaatio/testaus.md)

### Komentorivitoiminnot
#### Riippuvuuksien asennus:
`poetry install`
#### Alustustoimenpiteiden suoritus:
`poetry run invoke build`
#### Ohjelman käynnistys:
`poetry run invoke start`
#### Ohjelman testaus:
`poetry run invoke test`
#### Ohjelman testikattavuus:
`poetry run invoke coverage`
#### Ohjelman testikattavuusraportti:
`poetry run invoke coverage-report`
#### Pylint tarkistus:
`poetry run invoke lint`
