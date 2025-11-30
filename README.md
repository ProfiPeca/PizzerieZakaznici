# Aplikace pro rozvržení práce pecí v Pizzerii
Autor: Petr Čermák

Datum vytvoření: 23. 11. 2025
## Úvod
- Projekt vytvořil Petr Čermák, student Střední Průmyslové Školy Elektrotechnické Ječná
- Jedná se o příklad systému, který by zjednodušil komunikaci zákazníků s pizzerií
- Pekař, který peče pizzu v peci, čeká na objednávku, kterou si vezme z listu, který sdílí mezi ostatními pekaři
## Hlavní funkce
- Pec, která průběžně peče pizzy
    - Defaultně jsou 3 pece, dle pobočky jde ale přidat počet
- Pec má svoje id, aby se poznalo, která pec to je
- Seznam objednávek, ke kterým pekaři (pece) přistupují pomocí locku, aby nedošlo k dvojitému upečení té samé objednávky
- Simulace zákazníků, kteří si objednávají pizzy, dokud není list objednávek plný (potom je restaurace odmítne)
    - Defaultně je maximum objednávek 20, to se může zvýšit dle potřeb
### Běh programu
- Deklaruje se manager, kterým procesy sdílí informace mezi sebou, např. list queue, který obsahuje všechny objednávky
- Program vytvoří počet pecí dle nastavené hodnoty "oven_number" a přiřadí je do vytvořených procesů, které simulují pečení pizzy v troubě
- Program vytvoří "customersim"
  - proces který spustí metodu "customer_simulation", který simuluje objednávání zákazníků tím, že se periodicky posílají do queue pizzy
- Program spustí všechny procesy
