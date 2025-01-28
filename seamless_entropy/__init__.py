try:
    from entropy_c import binary_entropy
    binary_entropy._platform = "Pure C"
    
except ImportError:
    try:
        import scipy # type: ignore
        from .use_scipy import binary_entropy
    except ImportError:
        from .pure_python import binary_entropy
