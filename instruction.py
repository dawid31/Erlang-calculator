instruction_text_1 = '''
        Czym jest model erlanga?
        
        Modele Erlanga to matematyczne narzędzie do analizy ruchu w systemach kolejkowych. Stworzył je Agner Krarup Erlang.
        Mogą być stosowane w sieciach telekomunikacyjnych, supermarketach lub stacjach benzynowych.
        Pozwalają oszacować prawdopodobieństwo blokady klienta w zależności od parametrów modelu.
        Ta wiedza pomaga dostosować parametry systemu, aby osiągnąć wymaganą jakość usługi (QOS).

        Jeśli używasz trybu
        a) Do liczenia intensywność przychodzących zgłoszeń
        To obliczasz liczbę zgłoszeń, które występują w danej jednostce czasu. Miara ta pomaga nam pomaga zobaczyć nam jak bardzo obciążony jest system telekomunikacyjny.
        Jednostką jest jeden Erlang, jednostka zależy od wybranej przez nas jednostki czasu oraz od ilości zgłoszeń, które w niej napłyneły.

        b) Do wyznaczania współczynnika blokady
        Współczynnik blokady jest to inaczej prawdopodobieństwo odrzucenia zgłoszenia. Inaczej można powiedzieć, że jest to miara nieosiągalności stystemu dla nowych zgłoszeń oraz informuje nas o poziomie zatłoczenia.
        (Wspólczynnik blokady przyjmuje zawsze wartości od 0 do 1.)

        c) Do liczenia ilości kanałów
        Ilość kanałów informuje nas o ilości dostępnych kanałów, każdy kanał reprezentuje zdolność systemu do obsługi jednego zgłoszenia jednocześnie.
        Dobór odpowiedniej ilości kanałów jest niezbędny do zapewnienia odpowiedniej wydajności.

        Wartości zmiennoprzecinwkowe powinny być podawane tylko używając kropki "." jako separatora. Nie należy używać przecinka "," jako separatora.
        Ilość linii/kanałów powinna być liczbą dodatnią całkowitą natomiast zarówno współczynnik blokady jak i intensywność zgłoszeń mogą być liczbami zmiennoprzecinkowymi jak i całkowitymi.
        '''

instruction_text_2 = '''
        Czym jest model erlanga?

        Modele Erlanga to matematyczne narzędzie do analizy ruchu w systemach kolejkowych. Stworzył je Agner Krarup Erlang.
        Mogą być stosowane w sieciach telekomunikacyjnych, supermarketach lub stacjach benzynowych.
        Pozwalają oszacować prawdopodobieństwo blokady klienta w zależności od parametrów modelu.
        Ta wiedza pomaga dostosować parametry systemu, aby osiągnąć wymaganą jakość usługi (QOS).

        Jeśli używasz trybu generowania wykresu pamiętaj o następujących rzeczach

        1) Wypełnij wszystkie pola

        2) Pierwsze dwa pola dotyczą przedziału intensywności zgłoszeń dla którego zostanie stworzony wykres. Można tam wpisać zarówno wartości całkowite jak i zmiennoprzecinkowe

        3) Trzecie pole dotyczy ilości linii/kanałów w podanym modelu. Należy tam wpisać liczbę całkowitą

        4) Wartości zmiennoprzecinwkowe powinny być podawane tylko używając kropki "." jako separatora. Nie należy używać przecinka "," jako separatora.
        '''
