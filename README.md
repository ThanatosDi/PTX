![GitHub release](https://img.shields.io/badge/Python-3.x-brightgreen?style=for-the-badge&logo=python)
# PTX
 「公共運輸整合資訊流通服務平臺」(Public Transport Data eXchange，PTX) Python API 範例

# 申請 API
API 申請不多加闡述  
請至「[公共運輸整合資訊流通服務平臺](https://ptx.transportdata.tw/PTX/)」自行申請

# 使用

1. 將 `auth.py` 放入專案中
2. 在需要的檔案中 import 
    ```Python
    from auth import Auth 
    ```
3. 建立物件查詢
   ```Python
   # 申請帳號完成後 app_id, app_key 會自動寄送到信箱中
   ptx = Auth(app_id, app_key)
   # 例如查詢 2019-09-11 岡山->大橋 火車班次
   OriginStationID = 4310 # 岡山車站代碼
   DestinationStationID = 4210 #大橋車站代碼
   TrainDate = '2019-09-11'

   # 請注意 endpoint 並沒有包含 Root 
   # https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/DailyTrainTimetable/OD/4310/to/4210/2019-09-11
   ptx.request(f'/v3/Rail/TRA/DailyTrainTimetable/OD/{OriginStationID}/to/{DestinationStationID}/{TrainDate}')
   # 帶有參數的請求
   # https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/DailyTrainTimetable/OD/4310/to/4210/2019-09-11?$format=JSON&$orderby=TrainInfo/TrainNo
   ptx.request(f'/v3/Rail/TRA/DailyTrainTimetable/OD/{OriginStationID}/to/{DestinationStationID}/{TrainDate}', {'$orderby': 'TrainInfo/TrainNo', '$format': 'json'})
   ```
