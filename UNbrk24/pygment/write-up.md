Dupa foarte mult fiddling cu parametrii a si b in interiorul URL-ului, am incercat `?a=;&b=;`, moment in care am observat ca lipseste doar pygmentize.
Cu toate acestea, aparea un -O acolo asa ca m-am gandit ca e posibil sa fie un flag al unei comenzi, iar din lipsa de preocupatie, am incercat `?a=;&b=;ls`, moment in care mi-a fost confirmata ipoteza.
Pentru a scapa de acel lucru am folosit `?a=;&b=;echo`, moment in care am ramas fara erori, iar singurul output era argumentul echo-ului.
Acum ca puteam introduce orice comanda, am folosit `?a=;&b=;ls;echo`, iar de aici a inceput aventura.
Dupa un scurt `cat flag.php` fara prea mult succes, am inceput sa ma 'plimb' prin sistem, folosind chiar si `grep -r`, insa fara succes.
Intr-un final, cand am observat ca aproape toate fisierele aveau probleme atunci cand le afisam cu utilitarul `cat`, am incercat base64 pe `flag.php`, am decodat si am primit flag-ul.
