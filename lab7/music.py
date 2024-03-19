import pygame
import os

music_folder = "/Users/Timur/Documents/PP2/lab7"

if not os.path.exists(music_folder):
    print("Указанная папка с музыкой не существует!")
    exit()

os.chdir(music_folder)

pygame.init()

pygame.display.set_mode((100, 100))
 
music_files = os.listdir()

music_files = [file for file in music_files if file.endswith(('.mp3', '.wav'))]

playlist = music_files.copy()
current_track_index = 0

pygame.mixer.music.load(playlist[current_track_index])

pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:  
                current_track_index = (current_track_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:  
                current_track_index = (current_track_index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_ESCAPE: 
                running = False


pygame.quit()
