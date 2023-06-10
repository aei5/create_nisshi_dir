
"""
ここに開始日と終了日を入力する
例: 開始日 2023/6/10
start_year  = 2023
start_month = 6
start_day   = 10
"""

### 入力 ##################################################


dir_name    = "nisshi"

start_year  = 2023
start_month = 6
start_day   = 8

end_year    = 2023
end_month   = 6
end_day     = 20


###########################################################

import os
from datetime import datetime, timedelta

def main(dir_name, start_date, end_date):
    if not os.path.isdir(dir_name): os.mkdir(dir_name)
    i = 0
    while True:
        now_date = start_date + timedelta(days=i)
        dir_path = "./"+ dir_name+ "/" + now_date.strftime("%Y-%m-%d")
        end_path = "./"+ dir_name+ "/" + end_date.strftime("%Y-%m-%d")
        if os.path.isdir(dir_path):
            print("{} is already exist".format(dir_path))
            if dir_path == (end_path): return 0
            i += 1
            continue
        elif os.path.isdir(end_path): return 0
        print("create {}".format(dir_path))
        os.mkdir(dir_path)
        i += 1
        # if i > 100: return 0

if __name__ == "__main__":
    start_date = datetime(start_year, start_month, start_day)
    end_date   = datetime(end_year, end_month, end_day)
    main(dir_name, start_date, end_date)

