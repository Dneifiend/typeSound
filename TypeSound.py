import pygame, keyboard, os

pygame.init()
os.system("cls")

print("[TypeSound v1.0]")
print("키보드 입력 시 사운드가 출력됩니다.")
print("\n")
print("이 창을 닫거나, 활성화 한 상태로 Crtl+C 를 입력하면 종료됩니다.")


def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        play_music("down.mp3")
    if event.event_type == keyboard.KEY_UP:
        play_music("up.mp3")