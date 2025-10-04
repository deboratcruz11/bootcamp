"""Conta quantos dias do ano (1..365/366) são números primos.

Funções:
 - is_prime(n): verifica primalidade de um inteiro n.
 - is_leap(year): verifica se o ano é bissexto.
 - count_prime_days(year=None): retorna a quantidade de dias cujo número é primo
   no ano fornecido (se year for None, usa o ano atual).

Uso como script:
 python test.py --year 2025
"""
from __future__ import annotations

import argparse
import datetime
import math
from typing import List, Tuple


def is_prime(n: int) -> bool:
	"""Retorna True se n for primo (n >= 2)."""
	if n < 2:
		return False
	if n % 2 == 0:
		return n == 2
	limit = int(math.isqrt(n))
	for i in range(3, limit + 1, 2):
		if n % i == 0:
			return False
	return True


def is_leap(year: int) -> bool:
	"""Retorna True se o ano for bissexto."""
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def primes_of_year(year: int) -> List[int]:
	"""Retorna a lista de números de dias (1..365/366) que são primos para o ano dado."""
	days = 366 if is_leap(year) else 365
	return [d for d in range(1, days + 1) if is_prime(d)]


def count_prime_days(year: int | None = None) -> int:
	"""Retorna a quantidade de dias do ano cujo número é primo.

	Se year for None, usa o ano atual.
	"""
	if year is None:
		year = datetime.datetime.now().year
	return len(primes_of_year(year))


def fibonacci_upto(n: int) -> List[int]:
	"""Gera números de Fibonacci (1,1,2,3,5,...) até <= n."""
	if n < 1:
		return []
	fibs = [1, 1]
	while True:
		nxt = fibs[-1] + fibs[-2]
		if nxt > n:
			break
		fibs.append(nxt)
	# Remover duplicação do primeiro 1 se desejarmos valores distintos
	return fibs


def primes_in_fibonacci(year: int | None = None) -> Tuple[int, List[int]]:
	"""Retorna (quantidade, lista) de dias primos que estão na sequência de Fibonacci."""
	if year is None:
		year = datetime.datetime.now().year
	days = 366 if is_leap(year) else 365
	primes = primes_of_year(year)
	fibs = set(fibonacci_upto(days))
	common = [p for p in primes if p in fibs]
	return len(common), common


def main(argv: List[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description="Conta dias do ano que são números primos")
	parser.add_argument("--year", "-y", type=int, help="Ano (por exemplo 2025). Se ausente, usa o ano atual.")
	args = parser.parse_args(argv)
	year = args.year if args.year is not None else None
	if year is None:
		year = datetime.datetime.now().year
	primes = primes_of_year(year)
	count = len(primes)
	print(f"Ano: {year}")
	print(f"Dias no ano com número primo: {count}")
	# Mostrar os primeiros 20 primos como amostra
	print("Primeiros (até 20):", primes[:20])
	# Contagem de primos que também são Fibonacci
	fib_count, fib_list = primes_in_fibonacci(year)
	print(f"Primos que também aparecem na sequência de Fibonacci: {fib_count}")
	print("Lista:", fib_list)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
