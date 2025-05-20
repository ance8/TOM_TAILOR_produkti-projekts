# TOM TAILOR produktu datu iegūšanas un šķirošanas rīks

## Autori

- **Aleksandrs Nogičevs**
- **Ance Adzilča**

---
## Projekta apraksts

Šī Python programma ir automatizēts rīks, kas iegūst produktu informāciju no **TOM TAILOR** oficiālās mājaslapas un nodrošina to šķirošanu un meklēšanu.  
Programmas mērķis ir padarīt lietotājam ērtu iespēju pārskatīt jaunākos produktus konkrētās kategorijās – sievietēm, vīriešiem un bērniem.  
Kategorijas produkti tiek atlasīti un sakārtoti pēc cenas vai nosaukuma, kā arī iespējams meklēt konkrētus produktus pēc atslēgvārdiem.

---

## Lietotāja iespējas

- Izvēlēties produktu kategoriju: `women`, `men`, `kids`
- Izvēlēties šķirošanas režīmu:
  1. Pēc cenas augošā secībā  
  2. Pēc cenas dilstošā secībā  
  3. Alfabētiski pēc nosaukuma
- Meklēt konkrētus produktus pēc nosaukuma
- Apskatīt visus produktus no izvēlētās kategorijas
- Interaktīva lietošana terminālī

---

## Izmantotās bibliotēkas

### `selenium`
Nodrošina tīmekļa automatizāciju – pārlūka atvēršanu, lapas skrollēšanu, sīkdatņu akceptēšanu un HTML satura iegūšanu.  
**Instalēšana:**  
```bash
pip install selenium
```

### `webdriver_manager`
Automātiski lejupielādē un pārvalda Google Chrome webdriver, novēršot nepieciešamību lietotājam manuāli iestatīt webdriver.  
**Instalēšana:**  
```bash
pip install webdriver-manager
```

### `re` (Regular Expressions)
Tiek izmantots, lai no HTML teksta izvilktu datus par produktiem – produktu nosaukumus un cenas, balstoties uz fiksētām datu struktūrām lapas kodā.  
**Nav nepieciešama instalēšana**, jo šis modulis ir iebūvēts Python standarta bibliotēkā.

---

## Datu struktūras

Programmas kodā izmantotas šādas datu struktūras:

| Datu struktūra | Lietojums                                                           | Piemērs                              |
|----------------|----------------------------------------------------------------------|--------------------------------------|
| `dict`         | Kategoriju un URL pārīšu glabāšana                                   | `URLS = {"women": "...", "men": "..."}` |
| `list`         | Produktu saraksts, meklēšanas rezultāti                              | `products`, `filtered`               |
| `tuple`        | Katrs produkts kā (`name`, `price`) pāris                            | `("T-krekls", 19.99)`                |
| `str`          | Lietotāja ievade, produkta nosaukums, HTML teksts                    | `"T-krekls"`                         |
| `float`        | Cenas vērtības pēc pārvēršanas no teksta                             | `19.99`                              |

---

## Algoritmi

| Algoritms                | Lietojums                                                  | Sarežģītība       |
|--------------------------|-------------------------------------------------------------|-------------------|
| **Tīmekļa lapas skrollēšana** | Ielādē visus produktus, simulējot `infinite scroll`      | `O(n)` (konstanta `n=10`) |
| **Regex meklēšana**      | Izvelk produktus no HTML teksta                            | `O(n)`            |
| **Lineārā meklēšana**    | Filtrē produktus pēc ievadītā nosaukuma                    | `O(n)`            |
| **Kārtošana (`sorted`)** | Kārto pēc cenas vai alfabēta (Timsort)                     | `O(n log n)`      |
| **Vadības plūsma**       | Lietotāja izvēles apstrāde ar `if`, `while`, `break`       | –                 |

---

## Piemērs: Produktu saraksts

Programmas kodā izmantota pašdefinēta datu struktūra – saraksts ar pāriem (`tuple`), kur katrs elements satur produkta nosaukumu (`str`) un cenu (`float`).

```python
products = [("T-krekls", 19.99), ("Džinsi", 49.99), ("Jaka", 89.99)]
```

---

## Programmas darbības apraksts

1. Lietotājs izvēlas produktu kategoriju (sievietes, vīrieši vai bērni).
2. Produkti tiek šķiroti atbilstoši lietotāja izvēlētajam režīmam.
3. Tiek uzsākta automātiska lapas atvēršana ar Google Chrome pārlūku (headless režīmā).
4. Ja nepieciešams, tiek apstiprinātas sīkdatnes.
5. Lapa tiek vairākkārtīgi skrollēta līdz apakšai, lai ielādētu visus produktus.
6. HTML kods tiek analizēts, izmantojot regulārās izteiksmes, un iegūti visi produkti ar cenām.
7. Lietotājs var meklēt produktus vai apskatīt visus.
8. Iespējams atgriezties izvēlnē, lai pārbaudītu citu kategoriju.

---

## Piemērs terminālī

```bash
Enter category (women, men or kids): women
Enter sorting mode: 1 - price↑  2 - price↓  3 - alphabetical: 2
Enter product name (or 'all' to show all products, 'back' to choose category again): hoodie

--- Found Products (sort mode 2) ---
Cotton Hoodie — 49.99 €
Basic Hoodie — 39.99 €
```
