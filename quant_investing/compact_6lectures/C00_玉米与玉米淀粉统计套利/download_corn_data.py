import akshare as ak
import pandas as pd
import os

def download_futures_data():
    # 设置存储目录
    save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(save_dir, exist_ok=True)
    
    # 设置下载的时间范围
    start_date = "20150101"
    end_date = "20261231"
    
    print("正在下载玉米(c0)的主力合约连续数据...")
    try:
        # 下载玉米主力连续合约数据 (c0为新浪的连续主力合约)
        corn_df = ak.futures_main_sina(symbol="c0", start_date=start_date, end_date=end_date)
        if not corn_df.empty:
            corn_file = os.path.join(save_dir, "corn_main_c0.csv")
            corn_df.to_csv(corn_file, index=False, encoding="utf-8-sig")
            print(f"✅ 玉米数据已成功保存至: {corn_file} (共{len(corn_df)}条数据)")
        else:
            print("玉米数据下载为空！")
    except Exception as e:
        print(f"❌ 玉米数据下载失败: {e}")
        
    print("-" * 50)
    print("正在下载玉米淀粉(cs0)的主力合约连续数据...")
    try:
        # 下载玉米淀粉主力连续合约数据 (cs0为新浪的连续主力合约)
        starch_df = ak.futures_main_sina(symbol="cs0", start_date=start_date, end_date=end_date)
        if not starch_df.empty:
            starch_file = os.path.join(save_dir, "corn_starch_main_cs0.csv")
            starch_df.to_csv(starch_file, index=False, encoding="utf-8-sig")
            print(f"✅ 玉米淀粉数据已成功保存至: {starch_file} (共{len(starch_df)}条数据)")
        else:
            print("玉米淀粉数据下载为空！")
    except Exception as e:
        print(f"❌ 玉米淀粉数据下载失败: {e}")

if __name__ == "__main__":
    download_futures_data()
    print("全部数据下载任务完成。")
