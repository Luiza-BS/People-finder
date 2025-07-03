import cv2
import os

VIDEOS_FOLDER = 'videos'
FRAMES_BASE_FOLDER = 'frames'

os.makedirs(FRAMES_BASE_FOLDER, exist_ok=True)

print("Iniciando o processamento de vídeos...")
print(f"Buscando vídeos na pasta: {VIDEOS_FOLDER}")
print(f"Os frames serão salvos em: {FRAMES_BASE_FOLDER}")


for video_filename in os.listdir(VIDEOS_FOLDER):
    
    if video_filename.endswith(('.mp4')):
        person_name = os.path.splitext(video_filename)[0]
        video_path = os.path.join(VIDEOS_FOLDER, video_filename)
        output_folder = os.path.join(FRAMES_BASE_FOLDER, person_name)
        
        if os.path.exists(output_folder) and len(os.listdir(output_folder)) > 0:
            print(f"--- Frames para '{person_name}' já existem. Pulando. ---")
            continue

        print(f"\n--- Processando vídeo de: {person_name} ---")
        os.makedirs(output_folder, exist_ok=True)

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"[ERRO] Não foi possível abrir o vídeo em: {video_path}")
            continue

        frame_number = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_filename = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
            cv2.imwrite(frame_filename, frame)

            if frame_number % 20 == 0:
                print(f'  Salvando frame {frame_number} de {person_name}...')
            frame_number += 1

        cap.release()
        print(f'Captura de frames de {person_name} finalizada. Total de {frame_number} frames.')

print("\nProcessamento de todos os vídeos concluído.")