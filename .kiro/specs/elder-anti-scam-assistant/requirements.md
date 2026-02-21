# Requirements Document

## Introduction

本系統為針對長輩與高風險族群設計的防詐騙助手應用程式。台灣詐騙已演進為跨渠道、多步驟攻擊模式，受害者常在高壓、短時間內做出錯誤決策。本系統整合簡訊內容截圖辨識與電話號碼查詢功能，提供「少步驟、低門檻、快回覆」的防詐保護。

## Glossary

- **System**: 長輩防詐助手應用程式
- **User**: 使用本系統的長輩或高風險族群
- **Scam_Message**: 可疑的詐騙訊息（簡訊、Line 訊息等）
- **Risk_Score**: 系統計算的詐騙風險評分（0-100）
- **Risk_Level**: 風險等級（綠燈：安全、黃燈：可疑、紅燈：高風險）
- **OCR_Engine**: 光學字元辨識引擎，用於從截圖提取文字
- **AI_Analyzer**: AI 詐騙模式分析引擎
- **Phone_Database**: 電話號碼資料庫（整合 Whoscall API）
- **Action_Recommendation**: 系統提供的具體行動建議
- **Screenshot**: 使用者上傳的訊息截圖
- **Contact_Info**: 從訊息中提取的聯絡資訊（電話、網址、帳號等）

## Requirements

### Requirement 1: 截圖上傳與文字辨識

**User Story:** 作為長輩使用者，我想要透過截圖上傳可疑訊息，讓系統自動辨識內容，這樣我就不需要手動輸入複雜的文字或號碼。

**詐騙情境：** 長輩收到假冒健保局的簡訊「您的健保卡將於 3 日內停用，請立即撥打 02-XXXX-XXXX 確認身分」，感到緊張但不知如何查證。

#### Acceptance Criteria

1. WHEN User 上傳 Screenshot THEN THE System SHALL 使用 OCR_Engine 提取截圖中的所有文字內容
2. WHEN OCR_Engine 完成辨識 THEN THE System SHALL 在 3 秒內顯示提取的文字內容供 User 確認
3. WHEN 提取的文字包含電話號碼 THEN THE System SHALL 自動識別並標記所有 Contact_Info
4. WHEN 提取的文字包含網址或帳號 THEN THE System SHALL 自動識別並標記這些 Contact_Info
5. IF Screenshot 模糊或無法辨識 THEN THE System SHALL 提示 User 重新拍攝並提供拍攝建議
6. THE System SHALL 支援繁體中文、簡體中文、英文與數字的混合辨識

### Requirement 2: 電話號碼快速查詢

**User Story:** 作為長輩使用者，我想要快速查詢陌生來電號碼，了解是否為詐騙電話，這樣我就能決定是否接聽或回撥。

**詐騙情境：** 長輩接到自稱「法院書記官」的來電，對方聲稱有法律文件需要確認，要求提供個人資料，否則將發出拘票。

#### Acceptance Criteria

1. WHEN User 輸入電話號碼 THEN THE System SHALL 在 3 秒內查詢 Phone_Database 並返回結果
2. WHEN 查詢完成 THEN THE System SHALL 顯示該號碼的標記次數、標記類型與最近標記時間
3. WHEN 號碼在 Phone_Database 中被標記為詐騙 THEN THE System SHALL 顯示 Risk_Level 為紅燈
4. WHEN 號碼在 Phone_Database 中被標記為可疑 THEN THE System SHALL 顯示 Risk_Level 為黃燈
5. WHEN 號碼在 Phone_Database 中無不良紀錄 THEN THE System SHALL 顯示 Risk_Level 為綠燈
6. THE System SHALL 支援台灣市話、手機、國際電話格式的自動識別

### Requirement 3: AI 詐騙模式分析

**User Story:** 作為長輩使用者，我想要系統自動分析訊息內容是否符合詐騙模式，這樣我就能快速判斷訊息的可信度。

**詐騙情境：** 長輩收到 Line 訊息「恭喜您獲得百貨公司週年慶抽獎特獎，獎金 50 萬元，請先繳納 5% 稅金才能領取」。

#### Acceptance Criteria

1. WHEN System 取得訊息文字內容 THEN THE AI_Analyzer SHALL 分析內容是否包含詐騙關鍵字
2. WHEN AI_Analyzer 偵測到時間壓力用語（如「立即」、「馬上」、「3 日內」）THEN THE System SHALL 提高 Risk_Score
3. WHEN AI_Analyzer 偵測到金錢相關用語（如「匯款」、「繳費」、「稅金」、「手續費」）THEN THE System SHALL 提高 Risk_Score
4. WHEN AI_Analyzer 偵測到恐嚇用語（如「停用」、「凍結」、「法院」、「拘票」）THEN THE System SHALL 提高 Risk_Score
5. WHEN AI_Analyzer 偵測到利誘用語（如「中獎」、「高報酬」、「保證獲利」）THEN THE System SHALL 提高 Risk_Score
6. WHEN AI_Analyzer 偵測到假冒官方機構（如「健保局」、「國稅局」、「法院」）THEN THE System SHALL 提高 Risk_Score
7. WHEN AI_Analyzer 完成分析 THEN THE System SHALL 計算最終 Risk_Score 並轉換為對應的 Risk_Level

### Requirement 4: 風險評估與視覺化呈現

**User Story:** 作為長輩使用者，我想要看到清楚的風險評估結果，用簡單的顏色和文字告訴我這個訊息或電話是否危險。

#### Acceptance Criteria

1. WHEN System 完成風險分析 THEN THE System SHALL 在 3 秒內顯示 Risk_Level 結果
2. WHEN Risk_Level 為紅燈 THEN THE System SHALL 使用紅色背景、大字體顯示「高風險詐騙」
3. WHEN Risk_Level 為黃燈 THEN THE System SHALL 使用黃色背景、大字體顯示「可疑訊息」
4. WHEN Risk_Level 為綠燈 THEN THE System SHALL 使用綠色背景、大字體顯示「目前安全」
5. THE System SHALL 使用至少 24pt 字體大小顯示風險等級文字
6. THE System SHALL 提供高對比度配色（文字與背景對比度至少 7:1）
7. WHEN 顯示風險結果 THEN THE System SHALL 同時列出偵測到的可疑特徵清單

### Requirement 5: 即時行動建議

**User Story:** 作為長輩使用者，我想要系統告訴我接下來該怎麼做，這樣我就不會因為不知所措而做出錯誤決定。

#### Acceptance Criteria

1. WHEN Risk_Level 為紅燈 THEN THE System SHALL 提供 Action_Recommendation「請勿回撥、請勿匯款、請勿提供個人資料」
2. WHEN Risk_Level 為紅燈 THEN THE System SHALL 提供「一鍵撥打 165 反詐騙專線」按鈕
3. WHEN Risk_Level 為黃燈 THEN THE System SHALL 提供 Action_Recommendation「建議向官方機構查證」並列出官方聯絡方式
4. WHEN Risk_Level 為綠燈 THEN THE System SHALL 提供 Action_Recommendation「目前未發現異常，但仍需謹慎」
5. THE System SHALL 使用簡單明確的文字（避免專業術語）提供建議
6. WHEN 提供 Action_Recommendation THEN THE System SHALL 使用條列式呈現，每項建議不超過 20 字

### Requirement 6: 語音播報功能

**User Story:** 作為視力不佳的長輩使用者，我想要系統用語音告訴我分析結果，這樣我就不需要費力閱讀螢幕上的文字。

#### Acceptance Criteria

1. WHEN System 顯示風險評估結果 THEN THE System SHALL 自動播放語音播報
2. WHEN Risk_Level 為紅燈 THEN THE System SHALL 播報「警告！這是高風險詐騙訊息，請勿回應」
3. WHEN Risk_Level 為黃燈 THEN THE System SHALL 播報「注意！這是可疑訊息，建議向官方查證」
4. WHEN Risk_Level 為綠燈 THEN THE System SHALL 播報「目前安全，未發現異常」
5. THE System SHALL 提供語音播報開關設定，預設為開啟
6. THE System SHALL 使用清晰的中文語音，語速適中（每分鐘約 150 字）
7. WHEN User 點擊「重新播放」按鈕 THEN THE System SHALL 再次播放語音內容

### Requirement 7: 一鍵分享給家人

**User Story:** 作為長輩使用者，我想要快速將可疑訊息分享給家人確認，這樣我就能獲得家人的協助判斷。

#### Acceptance Criteria

1. WHEN System 顯示風險評估結果 THEN THE System SHALL 提供「分享給家人」按鈕
2. WHEN User 點擊「分享給家人」THEN THE System SHALL 產生包含截圖、風險評估、建議的分享內容
3. WHEN 分享內容產生完成 THEN THE System SHALL 開啟系統分享選單（Line、WhatsApp、簡訊等）
4. THE System SHALL 在分享內容中包含「由長輩防詐助手分析」的來源標記
5. WHEN 分享內容包含個人資料 THEN THE System SHALL 自動遮蔽敏感資訊（姓名、身分證字號、地址）

### Requirement 8: 快速啟動機制

**User Story:** 作為長輩使用者，我想要在收到可疑訊息時能快速開啟 App，不需要在手機裡找很久。

#### Acceptance Criteria

1. THE System SHALL 提供桌面小工具（Widget）快速啟動功能
2. WHEN User 安裝 App THEN THE System SHALL 引導 User 設定桌面小工具
3. THE System SHALL 提供「截圖後自動開啟」功能選項
4. WHEN User 啟用「截圖後自動開啟」且進行截圖 THEN THE System SHALL 在 1 秒內自動開啟並提示上傳
5. THE System SHALL 在通知欄提供常駐快捷按鈕
6. WHEN User 點擊通知欄快捷按鈕 THEN THE System SHALL 直接開啟查詢介面

### Requirement 9: 歷史紀錄與學習

**User Story:** 作為長輩使用者，我想要查看過去查詢過的訊息和電話，這樣我就能回顧之前的判斷結果。

#### Acceptance Criteria

1. WHEN User 完成一次查詢 THEN THE System SHALL 自動儲存查詢紀錄
2. THE System SHALL 提供「歷史紀錄」頁面顯示所有查詢記錄
3. WHEN User 開啟歷史紀錄 THEN THE System SHALL 依時間倒序顯示最近 100 筆紀錄
4. WHEN User 點擊歷史紀錄項目 THEN THE System SHALL 顯示該次查詢的完整結果
5. THE System SHALL 在歷史紀錄中標示 Risk_Level 顏色標籤
6. WHEN User 查詢相同號碼或內容 THEN THE System SHALL 提示「您曾在 X 天前查詢過此內容」

### Requirement 10: 無障礙設計

**User Story:** 作為有視力或操作困難的長輩使用者，我想要 App 介面簡單易用，這樣我就能獨立完成查詢操作。

#### Acceptance Criteria

1. THE System SHALL 使用至少 18pt 作為預設字體大小
2. THE System SHALL 提供字體大小調整功能（小、中、大、特大）
3. THE System SHALL 確保所有可點擊按鈕至少 48x48 dp 大小
4. THE System SHALL 在按鈕之間保持至少 8dp 間距
5. THE System SHALL 使用簡單明確的圖示搭配文字標籤
6. THE System SHALL 避免使用複雜的手勢操作（如雙擊、長按、滑動）
7. WHEN User 點擊任何按鈕 THEN THE System SHALL 提供明確的視覺或觸覺回饋

### Requirement 11: 離線基本功能

**User Story:** 作為在網路訊號不佳地區的使用者，我想要在沒有網路時仍能使用基本的詐騙判斷功能。

#### Acceptance Criteria

1. THE System SHALL 在本地儲存常見詐騙關鍵字資料庫
2. WHEN 裝置無網路連線 THEN THE System SHALL 使用本地資料庫進行基本分析
3. WHEN 使用離線模式 THEN THE System SHALL 明確標示「離線模式，結果僅供參考」
4. WHEN 裝置恢復網路連線 THEN THE System SHALL 自動更新本地詐騙關鍵字資料庫
5. THE System SHALL 每週至少更新一次本地資料庫
6. WHEN 離線模式無法判斷 THEN THE System SHALL 建議 User 在有網路時重新查詢

### Requirement 12: 隱私保護

**User Story:** 作為重視隱私的使用者，我想要確保我上傳的訊息和個人資料受到保護，不會被濫用。

#### Acceptance Criteria

1. WHEN User 上傳 Screenshot THEN THE System SHALL 在本地處理 OCR，不上傳原始圖片至伺服器
2. WHEN System 需要進行 AI 分析 THEN THE System SHALL 僅上傳提取的文字內容，不包含個人識別資訊
3. THE System SHALL 在傳輸資料時使用 HTTPS 加密
4. THE System SHALL 在本地儲存的資料使用加密保護
5. THE System SHALL 提供「清除所有歷史紀錄」功能
6. WHEN User 清除歷史紀錄 THEN THE System SHALL 永久刪除所有本地儲存的查詢資料
7. THE System SHALL 在首次啟動時顯示隱私政策並要求 User 同意
