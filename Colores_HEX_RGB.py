#   Funciones capaces de transformar colores HEX a RGB y viceversa.
#   Ejemplos:
#  RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#   HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)

import re

def convertion(hex_to_rgb, rgb_to_hex):

    def hex_to_rgb(hex: str) -> tuple:

        hex = hex.lstrip("#")

        regex = re.compile(r"^[0-9a-fA-F]{6}$")
        if regex.match(hex):

            r = int(hex[0:2], 16)
            g = int(hex[2:4], 16)
            b = int(hex[4:6], 16)

            return f"La conversión de #{hex} es: {(r, g, b)}"
    
        return 'No existe'


    def rgb_to_hex(r: int, g: int, b: int) -> str:

        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        return f"La conversión de {r,g,b} es: #{r:02x}{g:02x}{b:02x}"

    print(hex_to_rgb("#ffffff"))
    print(hex_to_rgb("#000000"))
    print(hex_to_rgb("#fabada"))
    print(rgb_to_hex(0, 0, 0))
    print(rgb_to_hex(255, 255, 255))
    print(rgb_to_hex(250, 186, 218))
    print(rgb_to_hex(255, 255, 0))


if __name__ == "__main__":
    convertion(hex_to_rgb="", rgb_to_hex="")
