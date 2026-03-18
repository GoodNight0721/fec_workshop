import pandas as pd
import os
import time
import rqdatac

# 把教育版 license 直接粘贴到 PASSWD
PASSWD = ""

def download_etf_data():
    if PASSWD:
        rqdatac.init('license', PASSWD)
        print("rqdatac 初始化成功")
    else:
        print("请先填写 PASSWD，再运行本脚本")
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    # 包含具体的后缀以适配 rqdatac
    etf_pool = {
        '518880.XSHG': '黄金ETF',
        '513100.XSHG': '纳指100',
        '159915.XSHE': '创业板100',
        '510180.XSHG': '上证180'
    }

    start_date = '2014-01-01'
    # 获取当前日期
    end_date = time.strftime('%Y-%m-%d')
    universe = list(etf_pool.keys())

    print("开始获取数据...")
    try:
        # 获取后复权数据
        df_all = rqdatac.get_price(
            order_book_ids=universe, 
            start_date=start_date, 
            end_date=end_date, 
            frequency='1d',
            adjust_type='post' # 后复权
        )
        
        if df_all is not None and not df_all.empty:
            df_all = df_all.reset_index()
            for code, name in etf_pool.items():
                df_code = df_all[df_all['order_book_id'] == code]
                
                if not df_code.empty:
                    # 文件名依旧保留不带后缀的版本格式
                    short_code = code.split('.')[0]
                    file_path = os.path.join(data_dir, f"{short_code}.csv")
                    df_code.to_csv(file_path, index=False, encoding='utf-8-sig')
                    print(f"✅ {name} ({code}) 数据已成功保存至: {file_path} (共{len(df_code)}条数据)")
                else:
                    print(f"⚠️ {name} ({code}) 的数据下载为空！")
        else:
            print("⚠️ 未获取到任何数据！")
            
    except Exception as e:
        print(f"❌ 数据获取失败: {e}")

if __name__ == "__main__":
    download_etf_data()
    print("全部ETF数据下载任务完成。")