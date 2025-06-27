'''

Práctica Métodos y Ayuda 1
Remueve los caracteres a la izquierda de nuestro texto principal:

,

:

%

_

#

Utiliza el método lstrip(). Imprime el resultado en pantalla:

",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.
'''

# Texto original con símbolos no deseados al inicio, medio y final
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

# Elimina caracteres no deseados al inicio
texto = texto.lstrip(",:_#%")

# Elimina caracteres no deseados al final
texto = texto.rstrip("#:,")  # eliminamos también ':' y ',' del final

# Reemplaza el símbolo '%' por la letra correcta
texto = texto.replace("%", "h")

# Elimina los guines bajos '_'
texto = texto.replace("_", "")

# Muestra el resultado final limpio
print(texto)  # Python Total
