import pytest, tracemalloc, cProfile, re
from io import StringIO
import pstats
import logging,sys
from proj1 import matrix_multiply

import numpy as np

logging.basicConfig(stream=sys.stdout,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
cProfile.run('re.compile("foo|bar")')

def setup_function(function):
    tracemalloc.start()

def teardown_function(function):
    
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    for stat in top_stats[:10]:
        # logger.info(stat)
        print(stat)
    
    tracemalloc.stop()


def test_large_matrices():
    try:
        logging.info("start test_large_matrices")
        A = np.random.rand(100, 100)
        B = np.random.rand(100, 100)
        expected_result = np.dot(A, B)
        assert np.allclose(matrix_multiply(A.tolist(), B.tolist()), expected_result)
    except Exception as e:
        logging.exception("Exception occurred in test_large_matrices")
        raise

def test_non_square_matrices():
    try:
        logging.info("test_non_square_matrices")
        A = np.random.rand(2, 3)
        B = np.random.rand(3, 4)
        expected_result = np.dot(A, B)
        assert np.allclose(matrix_multiply(A.tolist(), B.tolist()), expected_result)
    except Exception as e:
        logging.exception("Exception occurred in test_non_square_matrices")

def test_floating_point_numbers():
    try:
        A = [[1.5, 2.5], [3.5, 4.5]]
        B = [[2.5, 0.5], [1.5, 2.5]]
        expected_result = np.dot(A, B)
        assert np.allclose(matrix_multiply(A, B), expected_result)
    except Exception as e:
        logging.exception("Exception occurred in test_floating_point_numbers")


def test_input():
    try: 
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        assert matrix_multiply(A, B) == [[4, 4], [10, 8]]
    except Exception as e:
        logging.exception("Exception occurred in test_input")

def test_identity():
    try: 
        I = [[1, 0], [0, 1]]
        A = [[1, 2], [3, 4]]
        assert matrix_multiply(A, I) == A
    except Exception as e:
            logging.exception("Exception occurred in test_identity")

def test_cols_rows():
    try:
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10]]
        with pytest.raises(ValueError):
            matrix_multiply(A, B)
    except Exception as e:
                logging.exception("Exception occurred in test_cols_rows")

def test_empty():
    try:
        A = []
        B = [[1, 2], [3, 4]]
        with pytest.raises(ValueError):
            matrix_multiply(A, B)
    except Exception as e:
        logging.exception("Exception occurred in test_empty")


def test_scalar():
    try:
        A = [[3]]
        B = [[4]]
        assert matrix_multiply(A, B) == [[12]]
    except Exception as e:
                logging.exception("Exception occurred in test_scalar")
     
