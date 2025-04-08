import os

# Lista de 100 videojuegos populares/indie (puedes modificarla)
videojuegos = [
    "Minecraft", "The Legend of Zelda: Breath of the Wild", "Fortnite", 
    "Among Us", "Stardew Valley", "Hollow Knight", "Celeste", "Undertale",
    "Cyberpunk 2077", "Elden Ring", "Valorant", "League of Legends",
    "God of War", "The Witcher 3", "Dark Souls", "Portal 2", "Half-Life",
    "Counter-Strike 2", "Dota 2", "Apex Legends", "Genshin Impact",
    "Overwatch 2", "Call of Duty: Warzone", "Red Dead Redemption 2",
    "Grand Theft Auto V", "Animal Crossing: New Horizons", "Hades",
    "Dead Cells", "Cuphead", "Terraria", "Rocket League", "Fall Guys",
    "PUBG", "Destiny 2", "Metroid Dread", "Super Smash Bros. Ultimate",
    "Splatoon 3", "Persona 5", "Final Fantasy XIV", "The Last of Us",
    "Horizon Zero Dawn", "Resident Evil Village", "Silent Hill",
    "Metal Gear Solid V", "Death Stranding", "Doom Eternal", "Skyrim",
    "Fallout 4", "Bioshock Infinite", "Mass Effect", "Starfield",
    "Sea of Thieves", "Forza Horizon 5", "FIFA 23", "NBA 2K23",
    "Street Fighter 6", "Tekken 8", "Mortal Kombat 1", "Disco Elysium",
    "Outer Wilds", "Returnal", "Kena: Bridge of Spirits", "It Takes Two",
    "Psychonauts 2", "Little Nightmares", "Inside", "Limbo", "Braid",
    "Super Meat Boy", "Shovel Knight", "Ori and the Blind Forest",
    "Firewatch", "What Remains of Edith Finch", "Gris", "Journey",
    "No Man's Sky", "Subnautica", "Slay the Spire", "Loop Hero",
    "Risk of Rain 2", "Dead by Daylight", "Phasmophobia", "Lethal Company",
    "Baldur's Gate 3", "Diablo IV", "Star Wars Jedi: Survivor",
    "Hogwarts Legacy", "Spider-Man 2", "Alan Wake 2", "Lies of P",
    "Armored Core VI", "Remnant 2", "Palworld", "Hi-Fi Rush", "The Talos Principle 2", 
    "Sifu", "BattleBit Remastered", 
    "Dave the Diver", "Cult of the Lamb", "The Stanley Parable", 
    "Tunic", "The Forest", "The Long Dark"
]

# Crear la carpeta si no existe
if not os.path.exists("ArchivosTXT_Videojuegos"):
    os.makedirs("ArchivosTXT_Videojuegos")
    
    print(f"Total de videojuegos: {len(videojuegos)}")


# Generar 100 archivos .txt
for i, juego in enumerate(videojuegos, 1):
    nombre_archivo = f"j_{i:3d}.txt"  # Formato: juego_001.txt, juego_002.txt, etc.
    ruta_archivo = os.path.join("ArchivosTXT_Videojuegos", nombre_archivo)
    
    contenido = f"""
    Información sobre el videojuego: {juego}
    
    - Género: (Ej: Aventura, RPG, FPS)
    - Año de lanzamiento: (Ej: 2020)
    - Desarrollador: (Ej: Mojang, Nintendo)
    - Plataformas: (Ej: PC, PlayStation, Xbox)
    - Puntuación en Metacritic: (Ej: 90/100)
    
    Descripción breve: 
    (Aquí puedes escribir una descripción ficticia o datos reales del juego)
    """
    
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
        
        print(f"Creando archivo: {nombre_archivo}")


print("¡Se han generado 100 archivos TXT en la carpeta 'ArchivosTXT_Videojuegos'!")