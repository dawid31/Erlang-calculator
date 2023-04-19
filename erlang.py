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
#calculates value of a^n / n! for big nums to avoid overflow
def ann(n, a):
        """
        :param n: lines
        :param a: traffic
        :return: a^n / n!
        """
        result = 1
        for n in range(1, n + 1):
            result = result * a / n

        return result     
     

def calculate_erlang_b(traffic, lines):
        tab = [x for x in range(lines + 1)]
        sum = 0
        for idx, val in enumerate(tab):
            sum += ann(idx, traffic)

        blocking_rate = ann(lines, traffic) / sum

        return blocking_rate


def calculate_erlang_n(traffic, blocking_rate):
        """
        calculate the number of lines in a trunk group // oblicza ilosc linii
        :param traffic: the traffic in Erlangs // natezenie ruchu w erlangach
        :param blocking_rate: blocking rate / wspolczynnik blokady
        :return: number of lines / ilosc linii
        """
        lines = 1
        blocking_rate_searched = blocking_rate
        while blocking_rate_searched >= blocking_rate:
            lines += 1
            blocking_rate_searched = calculate_erlang_b(traffic, lines)

        return lines-1


def calculate_erlang_a(lines, blocking_rate):
    return "work in progress"

print(calculate_erlang_b(100, 10))
#print(calculate_erlang_n(100, 0.901074))
#print(calculate_erlang_a(123, 123))

