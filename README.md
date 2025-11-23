# PizzerieZakaznici
## Úvod
- Jedná se o příklad systému, který by zjednodušil komunikaci zákazníků s pizzerií
- Pekař, který peče pizzu v peci, čeká na objednávku, kterou si vezme z listu, který sdílí mezi ostatními pekaři
## Hlavní funkce
- Pec, která průběžně peče pizzy
    - Defaultně jsou 3 pece, dle pobočky jde ale přidat počet
- Pec má svoje id, aby se poznalo, která pec to je
- Seznam objednávek, ke kterým pekaři (pece) přistupují pomocí locku, aby nedošlo k dvojitému upečení té samé objednávky
- Simulace zákazníků, kteří si objednávají pizzy, dokud není list objednávek plný (potom je restaurace odmítne)
    - Defaultně je maximum objednávek 20, to se může zvýšit dle potřeb
