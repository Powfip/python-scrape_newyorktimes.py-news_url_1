import requests
from bs4 import BeautifulSoup
import sys

def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Buscar el título con seguridad
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else 'Título no encontrado'

    # Buscar los párrafos
    paragraphs = soup.find_all('p')
    content = '\n'.join(p.get_text(strip=True) for p in paragraphs)

    return title, content


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporciona la URL del artículo como argumento.")
        sys.exit(1)

    url = sys.argv[1]
    title, content = scrape_article(url)

    print("Título del artículo:\n", title)
    print("\nContenido del artículo:\n", content)
