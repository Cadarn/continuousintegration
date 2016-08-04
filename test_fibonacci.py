def test_fibonacci():
    """
    In this function we import the module fibonacci.py,
    and test it the function Fibonacci against known
    values.
    Fibonacci(n)
    """
    import fibonacci as fb
    assert fb.fib(10) == 55
    assert fb.fib(5) == 5

