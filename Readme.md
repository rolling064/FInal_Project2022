# Readme
## 目標:做出資料夾分類<br>
**用回復選項的方式做資料夾，分類出各種網站，方便找尋**<br>


## 環境架設<br>
使用以下指令裝設虛擬環境<br>
```pip3 install pipenv```<br>

```pipenv --three```<br>

```pipenv install flask```<br>

```pipenv install line-bot-sdk```<br>


## Ngrok<br>
**下載ngrok**
網址: https://ngrok.com/

**ngrok 架設教學**
https://www.wongwonggoods.com/python/python_chatbot/linebot-local-server-ngork/


## 我的程式架構
**資料夾分類**
![](https://i.imgur.com/sN8nt5X.png)


## 使用方式
**step0**<br>
任意輸入後，系統便會提示

![](https://i.imgur.com/aLrNHuW.png)

**step1**<br>
輸入**start**便會得到<br>
![](https://i.imgur.com/EipkEMF.png)

**step2**<br>
1.選擇你所要的資料夾以下用**ncku資料夾**做範例(如下圖)<br>
![](https://i.imgur.com/eqhrQtE.png)<br>
2.按下上一層則會跳回**step1**<br>

**step3**<br>
1.點擊選項便會跳出網址且狀態會跳回user(如下圖)<br>
![](https://i.imgur.com/9m9FthV.png)<br>
2.按下上一層則會跳回**step2**<br>

## 備註
若在中途未收到正確指令，便會跳出<br>
![](https://i.imgur.com/LSiMFeg.png)<br>
### 在此種狀況，加入了兩種除錯功能<br>
1.輸入"menu"後執行code後便會跳出選單，此除錯功能在各**資料夾階段**都有加入<br>
```{'trigger': 'advance', 'source': 'state_A', 'dest':'state_A','conditions':'is_going_to_menu'},```<br>
![](https://i.imgur.com/qc9M3YO.png)<br>
2.輸入"結束"便會將state轉移到end，此除錯功能在**任意階段**都有加入<br>
![](https://i.imgur.com/yxJWXQS.png)<br>

### fsm
在各個階段輸入"fsm"，便會得到狀態圖(範例為在娛樂資料夾輸入fsm)
![](https://i.imgur.com/h8Ti0KN.png)


**step bonus**<br>
在user階段 有設置無提示的路徑，若輸入開啟資料夾，便會進入密碼驗證階段<br>
![](https://i.imgur.com/BVcyhIZ.png)<br>

**密碼驗證階段**<br>
1.驗證失敗則會維持住狀態(如下圖)<br>
![](https://i.imgur.com/SkwwYoL.png)<br>
2.驗證成功則會進入最後階段(如下圖)<br>
![](https://i.imgur.com/ekxZ6HK.png)<br>

## 程式執行先前設置
### 設置伺服器
在V.S. Code的終端機開啟CMD輸入 ```ngrok http 5000```便會得到<br>
![](https://i.imgur.com/XohfsMR.png)<br>
將```(forwarding 後面的)and(->之前)```的網址複製到<br>
https://developers.line.biz/console/<br>
![](https://i.imgur.com/UXf3ljH.png)<br>
**複製過的網址後面要加上/callback**<br>

### 虛擬環境執行程式
在**終端機powershell**中使用```pipenv shell```進入虛擬環境<br>
於**終端機pipenv**環境中執行 ```python app.py```

### 兩者都完成後便可以到line中與機器人對話

