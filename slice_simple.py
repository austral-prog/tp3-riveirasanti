def slice_simple():
    texto = "Awesome"
    texto=texto.lower()
    primeras_tres=texto[:3]
    print(primeras_tres)

    medio=len(texto)// 2
    medio_letras=texto[medio-1 : medio+2]
    print(medio_letras)

    primera_a_cuarta=texto[:4]
    ultimas_tres=texto[-3:]
    resultado=primera_a_cuarta + ultimas_tres
    print(resultado)

slice_simple()
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
