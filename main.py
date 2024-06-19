import duckdb

import sys

# CSVファイルのパス
file_path = sys.argv[1]

# DuckDBでCSVファイルを読み込む
con = duckdb.connect()
con.execute(f"""
    CREATE TABLE game_scores AS 
    SELECT * FROM read_csv_auto('{file_path}')
""")

# プレイヤーごとの平均スコアを計算する
mean_scores_df = con.execute("""
    SELECT 
        player_id, 
        ROUND(AVG(score)) AS mean_score 
    FROM 
        game_scores 
    GROUP BY 
        player_id
""").fetchdf()

# 平均スコアの順位を計算し、上位10人を出力する
mean_scores_df['rank'] = mean_scores_df['mean_score'].rank(method='min', ascending=False)
mean_scores_df = mean_scores_df.sort_values(by=['mean_score', 'player_id'], ascending=[False, True]).reset_index(drop=True)

# 上位10人のプレイヤーの情報を出力する
print('rank,player_id,mean_score')
for idx, row in mean_scores_df.iterrows():
    if row['rank'] > 10:
        break
    print(f"{int(row['rank'])},{row['player_id']},{int(row['mean_score'])}")

# データベースの接続を閉じる
con.close()
