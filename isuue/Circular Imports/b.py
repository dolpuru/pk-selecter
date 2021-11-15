def function_b():
    print('function_b')


def function_c():
    import a

    print('function_c')
    return a.function_a()