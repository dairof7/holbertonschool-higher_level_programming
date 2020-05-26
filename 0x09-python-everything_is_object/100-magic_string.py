def magic_string(x=[0]):
    """Initialize class"""
    x[0] = x[0] + 1
    return ((("Holberton" + ", ") * x[0])[:-2])
