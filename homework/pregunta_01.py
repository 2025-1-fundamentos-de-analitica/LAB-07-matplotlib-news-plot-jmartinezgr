"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import matplotlib.pyplot as plt


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    # Data for years and media usage percentage
    years = list(range(2001, 2011))
    tv_usage = [74, 76, 75, 72, 70, 69, 70, 68, 68, 66]
    newspaper_usage = [45, 43, 48, 46, 40, 35, 34, 34, 30, 31]
    radio_usage = [18, 20, 17, 18, 16, 15, 14, 13, 16, 16]
    internet_usage = [13, 14, 17, 20, 18, 20, 22, 22, 40, 41]

    # Create figure with custom size
    plt.figure(figsize=(8, 6))

    # Plot each medium with its color and label
    plt.plot(years, tv_usage, label="Televisión", color="black")
    plt.plot(years, newspaper_usage, label="Periódico", color="gray")
    plt.plot(years, radio_usage, label="Radio", color="lightgray")
    plt.plot(years, internet_usage, label="Internet", color="dodgerblue", marker="o")

    # Add labels at the end of each line
    plt.text(
        2010, tv_usage[-1], f"{tv_usage[-1]}%", va="center", ha="left", color="black"
    )
    plt.text(
        2010,
        newspaper_usage[-1],
        f"{newspaper_usage[-1]}%",
        va="center",
        ha="left",
        color="gray",
    )
    plt.text(
        2010,
        radio_usage[-1],
        f"{radio_usage[-1]}%",
        va="center",
        ha="left",
        color="lightgray",
    )
    plt.text(
        2010,
        internet_usage[-1],
        f"{internet_usage[-1]}%",
        va="center",
        ha="left",
        color="dodgerblue",
    )

    # Add labels at the beginning of each line
    plt.text(
        2001,
        tv_usage[0],
        f"Televisión {tv_usage[0]}%",
        va="center",
        ha="right",
        color="black",
    )
    plt.text(
        2001,
        newspaper_usage[0],
        f"Periódico {newspaper_usage[0]}%",
        va="center",
        ha="right",
        color="gray",
    )
    plt.text(
        2001,
        radio_usage[0],
        f"Radio {radio_usage[0]}%",
        va="center",
        ha="right",
        color="lightgray",
    )
    plt.text(
        2001,
        internet_usage[0],
        f"Internet {internet_usage[0]}%",
        va="center",
        ha="right",
        color="dodgerblue",
    )

    # Main title and subtitle
    plt.title("Cómo la gente obtiene sus noticias", fontsize=14, weight="bold")
    plt.suptitle(
        "Una proporción creciente cita Internet como su fuente principal de noticias",
        y=0.91,
        fontsize=10,
    )

    # Configure axes: show only years, hide y ticks and remove frame
    plt.xticks(years)
    plt.yticks([])
    plt.box(False)

    # Create folder to save image if it doesn't exist
    os.makedirs("files/plots", exist_ok=True)

    # Save the chart to PNG file with tight cropping
    plt.savefig("files/plots/news.png", bbox_inches="tight")
    plt.close()
