import reflex as rx
import datetime
import Creymader.constants as const
from Creymader.estilo.estilo import Size,EmSize
from Creymader.estilo.color import text_color as text_color
from Creymader.estilo.color import Color as Color



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logocrebla.png",
            height=EmSize.BIG.value,     #alto del logo
            weight=EmSize.BIG.value,      #ancho del logo
            padding_x=EmSize.SMALL.value,
            alt="logotipo de no se que\"eme\"entre llaves"  #esto es para personas ividentes
        ),
        rx.link(
            rx.box(
                f"fecha {datetime.date.today()} trabajo con excelencia",
                padding_top=EmSize.MEDIUM.value
            ),
                href=const.CATALOGO,
                is_external=True,
                font_size=EmSize.SMALL.value
        ),
        rx.text(
            "Innovación en Madera: Inspirando Espacios, Creando Historias.",
            font_size=EmSize.SMALL.value,
            margin_top=EmSize.ZERO.value       #quita el espacio entre los textos que los distancia en el eje Y
        ),
        margin_bottom=EmSize.BIG.value,
        padding_botttom=EmSize.BIG.value,
        padding_x=EmSize.BIG.value,
        spacing=Size.ZERO.value,
        color=text_color.BLANCO.value,
        align_items="center"
    )