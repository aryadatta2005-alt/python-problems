def get_correlation(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    
    # Covariance numerator
    num = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    
    # Standard deviation denominator
    den_x = sum((xi - mean_x)**2 for xi in x)
    den_y = sum((yi - mean_y)**2 for yi in y)
    den = (den_x * den_y)**0.5
    
    return num / den