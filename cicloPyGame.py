import pygame, sys

width = 640
height = 480

#Pasos a seguir, necesarios:
# 1) Manejar eventos
# 2) Refrescar pantalla (imagen) 
# 3) Actualizar objetos en la pantalla 

screen = pygame.display.set_mode ((width, height)) #  Medidas de la pantalla 
screen.fill((246,147, 48)) #  Colores de la pantalla
# Estoy actualizando los objetos de la pantalla, pero necesito que se actualice la pantalla (paso2), para que se dé el cambio de color.  
pygame.display.set_caption ("Ciclo básico de pygame") #  Título

# Sin embargo, si no se ha inicializado pygame, no muestra los cambios de colores o títulos.
pygame.init() #Si no llegase a funcionar, poner: pygame.font.init()

gameOver = False
while not gameOver:
    # 1) Manejar/gestionar eventos
    for event in pygame.event.get(): #En pygame.event es donde pygame almacena los eventos (un iterable) que van sucediendo
        if event.type ==pygame.QUIT: # Es un evento que siempre tenemos que usar. Significa que si le damamos a salir -->
            gameOver = True #Se termina el juego y Salimos del bucle.
    pygame.display.flip() # también podría ser pygame.display.update() para 2) Refrescar la imagen (pantalla) 
            

pygame.quit() #Se termina pygame
sys.exit() #Nos aseguramos que el sale del juego y del sistema (Por si se queda bloqueada la app) 
     
    

