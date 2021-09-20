# Hell-INC

Hell-INC jest to program stworzony na prośbę kolegi z klasy by ułatwić prace jego tacie w pracy.

Działanie:
Program loguje się na skrzynkę pocztową (w kodzie jest mail używany przezemnie tylko do testów)
a następnie wysyła pliki o kontretnych rozszerzeniach z folderu "Data" do przypisanych do nich maili
z folderu "Bases" plik "ext" zawiera roszerzenia a plik "mail" maile wystarczy dopisać kolejne rozszerzenie
oraz mail na końcu obu plików i już dane rozszerzenie jest obsługiwane.

Program jest dostosowany do dowolnej liczby rozszerzeń i przypisanych maili a same pliki usuwa dopiero po
upewnieniu się że pliki zostały wysłane.

W planach było:
-Zabezpieczenia(Nie przechowywanie maila oraz hasła w kodzie tylko np. w Pendrive o konkretnej nazwie 
skąd dopiero program brałby hasło oraz mail)
-Uproszczenie dopisywania rozszerzeń i maili oraz zamiana 2 plików na jeden("ext","mail")
-Optymalizacja kodu

Nie ma tego w samym programie gdyż kolega zrezygnował z tego a ja nie miałem
potrzeby na rozwijanie tego projektu

Efektywność:
Po testach (jeśli dobrze pamiętam) wyszło mi z 2-3 godz jak nie mniej na wysłanie 10k plików
Niestety robiłem to poprzez gmail i google nie pozwalał zrobić testu na 10k wiec czas był obliczany 
z testów do 100 plików gdyż dalej przekraczał limit gmail na wysyłanie maili w tak krótkim okresie czasu. 
