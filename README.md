[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uJ5CHUfF)
# Domácí úkol č. 4
> **Upravujte pouze soubor `assignment_4_1.py` a v něm pouze nahraďte `...` podle zadání!**

Vaším úkolem bude vytvořit jednoduchý program pro zašifrování zprávy pomocí tabulky záměn.

Šifra je založena na principu záměny znaku za jiný bez jakékoli vnitřní souvislosti či na základě znalosti klíče 
(hesla). Prvním krokem je vytvoření šifrovací tabulky podle zadaného klíče `code`. Postupujte dle přiloženého příkladu, 
kde je heslem slovo `ALGORITMUS`. Po hesle následují v tabulce zbylá písmena anglické abecedy dle standartního pořadí. 
V případě konce abecedy se do tabulky vloží první znak ze začátku abecedy, který v tabulce chybí atd., dokud tabulka 
není kompletní.

| Původní znak     | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|------------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zašifrovaný znak | A | L | G | O | R | I | T | M | U | S | V | W | X | Y | Z | B | C | D | E | F | H | J | K | N | P | Q |

Tato tabulka záměn bude fungovat jen pro velká písmena, proto zajistěte, aby klíč i zpráva obsahovali jen velká písmena.

Na závěr se proveďte šifrování zprávy pomocí vytvořené tabulky záměn. 
Například zpráva `"hello"` se převede na `"MRWWZ"`. Zašifrovanou zprávu přiřaďte do proměnné `encoded_message`.

Přesný postup řešení je na Vás, nicméně zde je několik nápověd:
1. Zamyslete se, jaký datový typ nebo jaká datová struktura bude vhodná pro tvorbu šifrovací tabulky.
2. Znaky v tabulce je možné také reprezentovat číslem (viz [wiki](https://en.wikipedia.org/wiki/ASCII#Printable_characters)).
   Šlo by toho využít?
3. Nejste si jisti, jak postupovat? Zkuste se zamyslet, jaké kroky bude potřeba postupně provést, zakreslete si je do 
   vývojového diagramu a následně jednotlivé kroky implementujte.
