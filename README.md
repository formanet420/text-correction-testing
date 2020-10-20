# text-correction-testing

vyhodnocení úspěšnosti vašeho opravovače
----------------------------------------

Použijte váš kód k tomu, abyste opravili chyby v souboru data/lingvistika_errors3.txt. Výstupem vašeho programu bude textový soubor. Použijte skript v této složce k vyhodnocení úspěšnosti.

Naklonujete si tento repozitář.

Před prvním spuštěním spusťte z této složky příkaz:

```
pip3 install -r requirements.txt
```

Potom můžete použít vyhodnocovací skritp následovně:

```
python3 evaluate_correction.py data/lingvistika_orig.txt cesta/k/vasemu/opravenemu/souboru.txt
```

Skript by vám měl vypsat číslo, které říká, kolik chyb ve vašem opraveném textu zůstalo.

Svůj výsledek zapište každý týden do tabulky:

https://docs.google.com/spreadsheets/d/1o8p7lxZBsTRjNfhalspq_vyKj-wVHs1sb4RD-gCoqew/edit?usp=sharing

Nezapomeňte také pushnout svoje změny do svého repozitáře.


