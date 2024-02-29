import reflex as rx
from Creymader.estilo.estilo import Size, EmSize
from Creymader.estilo.color import Color as Color
from Creymader.estilo.color import text_color as text_color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f"  {body}",
        font_size=EmSize.MEDIUM.value,
        color=text_color.BLANCO.value
        )
    )