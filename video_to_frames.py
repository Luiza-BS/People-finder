import cv2
import os

VIDEOS_FOLDER = 'videos'
FRAMES_BASE_FOLDER = 'frames'

os.makedirs(FRAMES_BASE_FOLDER, exist_ok=True)

print("Iniciando o processamento de vídeos...")
print(f"Buscando vídeos na pasta: {VIDEOS_FOLDER}")
print(f"Os frames serão salvos em: {FRAMES_BASE_FOLDER}")

# Percorre todos os arquivos na pasta de vídeos
for video_filename in os.listdir(VIDEOS_FOLDER):
    # Verifica se o arquivo é um vídeo
    if video_filename.endswith(('.mp4')):
        nome_pessoa = os.path.splitext(video_filename)[0] # Pega o nome do arquivo sem a extensão
        video_path = os.path.join(VIDEOS_FOLDER, video_filename)
        output_folder = os.path.join(FRAMES_BASE_FOLDER, nome_pessoa)

        # --- Verificação de frames existentes ---
        # Verifica se a pasta de saída para este vídeo já existe e se tem arquivos dentro
        if os.path.exists(output_folder) and len(os.listdir(output_folder)) > 0:
            print(f"--- Frames para '{nome_pessoa}' já existem. Pulando. ---")
            continue # Pula para o próximo vídeo

        print(f"\n--- Processando vídeo de: {nome_pessoa} ---")
        os.makedirs(output_folder, exist_ok=True) # Cria a pasta para os frames, se não existir

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"[ERRO] Não foi possível abrir o vídeo em: {video_path}")
            continue # Pula para o próximo vídeo se não conseguir abrir

        frame_number = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break # Fim do vídeo

            frame_filename = os.path.join(output_folder, f'frame_{frame_number:04d}.jpg')
            cv2.imwrite(frame_filename, frame)

            # Para evitar muita saída no console, você pode imprimir a cada 20 frames
            if frame_number % 20 == 0:
                print(f'  Salvando frame {frame_number} de {nome_pessoa}...')
            frame_number += 1

        cap.release()
        print(f'Captura de frames de {nome_pessoa} finalizada. Total de {frame_number} frames.')

print("\nProcessamento de todos os vídeos concluído.")