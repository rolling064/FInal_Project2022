# Readme
## 目標:做出資料夾分類
**用回復選項的方式做資料夾，分類出各種網站，方便找尋**


## 環境架設
使用以下指令裝設虛擬環境
```pip3 install pipenv```

```pipenv --three```

```pipenv install flask```

```pipenv install line-bot-sdk```


## Ngrok
**下載ngrok**
網址: https://ngrok.com/

**ngrok 架設教學**
https://www.wongwonggoods.com/python/python_chatbot/linebot-local-server-ngork/


## 我的程式架構
**資料夾分類**
![](https://i.imgur.com/JEufvdq.png)


## 使用方式
**step0**
任意輸入後，系統便會提示

![](https://i.imgur.com/aLrNHuW.png)

**step1**
輸入**start**便會得到

![](https://i.imgur.com/EipkEMF.png)

**step2**
1.選擇你所要的資料夾以下用**ncku資料夾**做範例(如下圖)

![](https://i.imgur.com/eqhrQtE.png)
2.按下上一層則會跳回**step1**

**step3**
1.點擊選項便會跳出網址且狀態會跳回user(如下圖)

![](https://i.imgur.com/9m9FthV.png)
2.按下上一層則會跳回**step2**

**備註**
若在中途未收到正確指令，使用
```transition中的{'trigger': 'advance', 'source': 'state_A', 'dest':'state_A'}```
除錯便會維持相同狀態持續跳出選項通知(如下圖)

![](https://i.imgur.com/xNb8MyY.png)

**step bonus**
在user階段 有設置無提示的路徑，若輸入開啟資料夾，便會進入密碼驗證階段

![](https://i.imgur.com/BVcyhIZ.png)

**密碼驗證階段**
1.驗證失敗則會維持住狀態(如下圖)

**備註**:此階段的開始和除錯不同訊息因此不能transition到自己

![](https://i.imgur.com/SkwwYoL.png)

2.驗證成功則會進入最後階段(如下圖)

![](https://i.imgur.com/ekxZ6HK.png)

## 程式執行先前設置
### 設置伺服器
在V.S. Code的終端機開啟CMD
輸入 ```ngrok http 5000```便會得到
![](https://i.imgur.com/XohfsMR.png)

將```(forwarding 後面的)and(->之前)```的網址複製到
https://developers.line.biz/console/
![](https://i.imgur.com/UXf3ljH.png)

**複製過的網址後面要加上/callback**

### 虛擬環境執行程式
在**終端機powershell**中使用```pipenv shell```進入虛擬環境
於**終端機pipenv**環境中執行 ```python app.py```

### 兩者都完成後便可以到line中與機器人對話

