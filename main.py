def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    if r > 0 and h > 0:
        pole_powierzchni = math.pi * 2 * (r ^ 2) + 2*h*math.pi*h
        return pole_powierzchni
    else:
        return np.NaN

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    ciag_fib = np.array([1,1])
    if n <= 0:
        return 0
    elif n == 1:
        return np.array([1])
    elif n == 2:
        return ciag_fib
    else:
        for a in range (2,n):
            nty_element = ciag_fib[-1] + ciag_fib[-2]
            ciag_fib = np.append(ciag_fib, [nty_element])
    return np.reshape(ciag_fib, (1, n))

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    macierz = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mdet = np.linalg.det(macierz)
    if Mdet == 0:
        Minv = np.NaN
    else:
        Minv = np.linalg.inv(macierz)
    Mt = np.transpose(macierz)
    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if m <= 0 or n <= 0:
        return None
    macierz = np.zeror((m,n))
    for  x in range(m):
        for y in range(n):
            if x > y:
                macierz[x][y]=x+3
            else:
                macierz[x][y]=y+3
    return macierz
