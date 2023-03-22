import math

'''
Wzór dla modelu Erlanga służącego do wyznaczania współczynnika blokady w systemach z jednym kanałem
(czyli jedną linią obsługi) to:

B = (A^N / N!) / (sum(k=0 to N) (A^k / k!) )

gdzie:

B oznacza współczynnik blokady, czyli prawdopodobieństwo, że zgłoszenie nie zostanie obsłużone,
A to intensywność przychodzących zgłoszeń (liczba zgłoszeń na jednostkę czasu),
N to liczba kanałów (linii obsługi),
sum(k=0 to N) (A^k / k!) to suma prawdopodobieństw, że kanały będą zajęte.
'''

def erlang_b(A, N):
    numerator  = (A**N) / math.factorial(N)
    denominator = 0

    for k in range(N+1):
        denominator += (A**k)/math.factorial(k)

    B = numerator/denominator
    return B

erlang_value = erlang_b(100, 10)
