import pandas as pd
import psutil

# CSVファイルのパス
file_path = ''

# チャンクサイズの計算
total_memory_gb = psutil.virtual_memory().total / (1024 ** 3)  # メモリ容量をGBで取得
chunk_size = int((total_memory_gb / 4) * 1024)  # メモリ容量の1/4をchunk_sizeとする

# プレイヤーごとのスコアの合計とプレイ回数を追跡する辞書を作成
scores_dict = {}
play_counts = {}

# CSVファイルを読み込みながら処理
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # player_idごとにスコアとプレイ回数を加算
    for idx, row in chunk.iterrows():
        player_id = row['player_id']
        score = row['score']
        scores_dict[player_id] = scores_dict.get(player_id, 0) + score
        play_counts[player_id] = play_counts.get(player_id, 0) + 1

# 平均スコアを計算する
mean_scores = {player_id: scores_dict[player_id] / play_counts[player_id] for player_id in scores_dict}

# 平均スコアで降順にソートする
sorted_scores = sorted(mean_scores.items(), key=lambda x: x[1], reverse=True)

# 同じスコアのプレイヤーをグループ化してランキングを割り当てる
rank = 1
prev_score = None
for idx, (player_id, score) in enumerate(sorted_scores, start=1):
    mean_score = round(score)
    if prev_score != mean_score:
        rank = idx 
    if rank >= 10:
        break
    print(f"{rank},{player_id},{mean_score}")
    prev_score = mean_score
