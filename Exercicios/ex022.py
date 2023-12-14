import pygame

# Inicializar o pygame
pygame.init()

# Carregar o arquivo de música
pygame.mixer.music.load('C:\\xampp\\htdocs\\Aulas\\Python\\Exercicios\\louvor1.mp3')

# Definir o volume (opcional)
  # Valor entre 0.0 e 1.0

# Iniciar a reprodução da música
pygame.mixer.music.play()

# Aguardar até que a música termine
pygame.time.delay(5000)  # Espera 5 segundos (ajuste conforme necessário)

# Parar a reprodução da música


# Encerrar o pygame
pygame.quit()
