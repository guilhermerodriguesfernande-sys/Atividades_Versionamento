import pyshorteners

def encurtar_url(url_longa):
    try:
        # Inicializa o encurtador
        s = pyshorteners.Shortener()
        # Usa o serviço TinyURL para encurtar
        url_curta = s.tinyurl.short(url_longa)
        return url_curta
    except Exception as e:
        return f"Erro ao encurtar: {e}"

def main():
    print("--- ENCURTADOR DE LINKS DO GUILHERME ---")
    link = input("Cole a URL que deseja encurtar: ")
    
    print("\nProcessando...")
    resultado = encurtar_url(link)
    
    print(f"\nSucesso! Sua URL curta é: {resultado}")

if __name__ == "__main__":
    main()
