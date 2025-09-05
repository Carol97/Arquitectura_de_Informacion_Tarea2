# scripts/generar_markdown.py

import csv, pathlib, re, unicodedata

CSV_FILE = "laptops.csv"
OUT_DIR = pathlib.Path("../content/laptops")

HEADERS = {                                
    "num": "Num",                           
    "brand": "Brand",                      
    "model": "Model_Name",                  
    "processor": "Processor",              
    "os": "Operating_System",               
    "storage_mb": "Storage_MB",             
    "ram_gb": "RAM_GB",                    
    "screen_size": "Screen_Size",          
    "touch": "Touch_Screen",                
    "price": "Price",                       
}

def slugify(s: str) -> str:                
    s = str(s or "").strip().lower()
    # Quita acentos á->a, ñ->n
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    # Reemplaza todo lo que no sea [a-z0-9] por guiones y limpia extremos
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    # Devuelve el slug o “item” si quedó vacío
    return s or "item"

OUT_DIR.mkdir(parents=True, exist_ok=True)
# Abre el CSV en modo lectura con UTF-8
with open(CSV_FILE, newline="", encoding="utf-8") as file:   
    reader = csv.DictReader(file)
    for row in reader:
        num = (row.get(HEADERS["num"], "") or "").strip() 
        brand = (row.get(HEADERS["brand"], "") or "").strip()
        model = (row.get(HEADERS["model"], "") or "").strip()
        cpu = (row.get(HEADERS["processor"], "") or "").strip()
        os = (row.get(HEADERS["os"], "") or "").strip()
        storage_mb = (row.get(HEADERS["storage_mb"], "") or "").strip()
        ram_gb = (row.get(HEADERS["ram_gb"], "") or "").strip()
        screen = (row.get(HEADERS["screen_size"], "") or "").strip()
        touch = (row.get(HEADERS["touch"], "") or "").strip()
        price = (row.get(HEADERS["price"], "") or "").strip()

        # Construye un nombre de archivo único con marca y modelo
        fname = f"{slugify(brand)}-{slugify(model or num)}.md"
        path = OUT_DIR / fname

        # Título 
        title = f"{model} — {brand}" if model else (brand or f"Equipo {num}")  

        front_matter = [
            "---",
            f'title: "{title}"',
            f'num: "{num}"',
            f'marca: "{brand}"',
            f'modelo: "{model}"',
            f'procesador: "{cpu}"',
            f'sistema_operativo: "{os}"',
            f'almacenamiento_mb: "{storage_mb}"',
            f'ram_gb: "{ram_gb}"',
            f'tamano_pantalla: "{screen}"',
            f'touch_screen: "{touch}"',
            f'precio: "{price}"',
            "---",
            "<ul>",
            f"<li><strong>Marca:</strong> {brand}</li>",
            f"<li><strong>Modelo:</strong> {model}</li>",
            f"<li><strong>Sistema Operativo:</strong> {os}</li>",
            f"<li><strong>Procesador:</strong> {cpu} </li>",
            f"<li><strong>Tamaño de pantalla:</strong> {screen}</li>",
            f"<li><strong>Touch Screen:</strong> {touch}</li>",
            f"<li><strong>RAM (GB):</strong> {ram_gb}</li>",
            f"<li><strong>Almacenamiento (MB):</strong> {storage_mb}</li>",
            f"<li><strong>Precio:</strong> {price}</li>",
            "</ul>",
        ]

        path.write_text("\n".join(front_matter), encoding="utf-8")

print(f"Markdowns creados {OUT_DIR.resolve()}")
