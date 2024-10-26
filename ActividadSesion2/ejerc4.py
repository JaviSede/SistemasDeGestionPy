def suma_y_muestra(*args, **kwargs):
    suma_args = sum(args)
    suma_kwargs = sum(kwargs.values())
    print(suma_args)
    print(suma_kwargs)
