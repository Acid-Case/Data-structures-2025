import numpy as np
from time import perf_counter


def generate_complex_matrix(n):
    """Генерация случайной комплексной матрицы"""
    real_part = np.random.rand(n, n)
    imag_part = np.random.rand(n, n)
    return real_part + 1j * imag_part


def naive_matrix_mult(a, b):
    """Наивное умножение матриц по формуле из линейной алгебры"""
    n = a.shape[0]
    result = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i, j] += a[i, k] * b[k, j]
    return result


def optimized_matrix_mult(a, b, block_size=64):
    """Оптимизированное умножение матриц с использованием блочного алгоритма"""
    n = a.shape[0]
    result = np.zeros((n, n), dtype=np.complex128)
    
    for i_block in range(0, n, block_size):
        i_end = min(i_block + block_size, n)
        for j_block in range(0, n, block_size):
            j_end = min(j_block + block_size, n)
            for k_block in range(0, n, block_size):
                k_end = min(k_block + block_size, n)
                for i in range(i_block, i_end):
                    for k in range(k_block, k_end):
                        a_ik = a[i, k]
                        for j in range(j_block, j_end):
                            result[i, j] += a_ik * b[k, j]
    return result


def main():

    matrix_size = 2048

    # Генерация матриц
    print(f"Генерация матриц {matrix_size}x{matrix_size}...")
    a = generate_complex_matrix(matrix_size)
    b = generate_complex_matrix(matrix_size)
    
    # Cложность алгоритма
    complexity = 2 * matrix_size ** 3
    
    # 1. Наивное умножение
    # print("\n1. Наивное умножение матриц")
    # start = perf_counter()
    # naive_result = naive_matrix_mult(a, b)
    # naive_time = perf_counter() - start
    # naive_perf = complexity / naive_time * 1e-6
    # print(f"Время: {naive_time:.2f} сек")
    # print(f"Производительность: {naive_perf:.2f} MFlops")
    
    # 2. BLAS через numpy
    print("\n2. Умножение матриц с помощью BLAS (numpy.dot)")
    start = perf_counter()
    blas_result = np.dot(a, b)
    blas_time = perf_counter() - start
    blas_perf = complexity / blas_time * 1e-6
    print(f"Время: {blas_time:.2f} сек")
    print(f"Производительность: {blas_perf:.2f} MFlops")
    
    # 3. Оптимизированное умножение
    print("\n3. Оптимизированное умножение матриц (блочный алгоритм)")
    start = perf_counter()
    optimized_result = optimized_matrix_mult(a, b)
    optimized_time = perf_counter() - start
    optimized_perf = complexity / optimized_time * 1e-6
    print(f"Время: {optimized_time:.2f} сек")
    print(f"Производительность: {optimized_perf:.2f} MFlops")


if __name__ == "__main__":
    main()
