# SqlInt

Celem projektu jest stworznie Interpretera języka SQL.

Program pozwala na wyświetlanie w konsoli wyników zapytań do bazy danych ( która jest przechowywana w formacie csv).

**Zapytania:**

Obecnie możliwe jest wykonywnaie zapytań:
 * SELECT kolumny FROM tabela [WHERE warunki] [ORDER BY kolumny [ASC|DESC]] 
 * SELECT wyrażenia_matematyczne
 * UPDATE tabela SET kolumna = wartość [WHERE warunki]
 * INSERT INTO tabela [(kolumny)] VALUES (kolumny)
 * DELETE FROM table [WHERE warunek]
 
**Techonologie:**
 * Python
 * PLY
 * Pandas



