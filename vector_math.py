# vector_math.py

import math


def dot_product(a, b):
    """
    Computes the dot product of two vectors.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")
    return sum(x * y for x, y in zip(a, b))


def magnitude(vector):
    """
    Computes the Euclidean norm (length) of a vector.
    """
    return math.sqrt(sum(x * x for x in vector))


def cosine_similarity(a, b):
    """
    Computes cosine similarity between two vectors.
    Returns a value between -1 and 1.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length.")

    mag_a = magnitude(a)
    mag_b = magnitude(b)

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot_product(a, b) / (mag_a * mag_b)