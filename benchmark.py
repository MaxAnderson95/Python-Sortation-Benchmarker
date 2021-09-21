from algorithms import selection_sort
from algorithms import bubble_sort
from algorithms import insertion_sort

from util import benchmark
from util import gen_random_list

list = gen_random_list(10)
passes = 1000000

print(f"The list to sort is {list}")
for algo in [selection_sort, bubble_sort, insertion_sort]:
    benchmark(algo, list, passes)