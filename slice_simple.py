def slice_simple():
    texto = "Awesome"
    texto = texto.lower()
    print(texto[:3])

    medio=len(texto) // 2
    print(texto[medio-1 : medio+2])
    
    print(texto[:4] + texto[-3:])

slice_simple()

