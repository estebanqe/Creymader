import reflex as rx
import Creymader.estilo.estilo as style
from Creymader.estilo.estilo import Size, EmSize

def Link_sponsor(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=EmSize.DEFAULT.value,
            height=EmSize.LARGE.value,
            alt=alt     
        ),
        href=url,
        is_external=True
    )
    