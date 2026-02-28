
AIF_BATCH2 = [
  {
    "id":116,"exam":"AIF",
    "question":"A company has petabytes of unlabeled customer data. The company wants to classify its customers into tiers to advertise and promote its products. Which methodology should the company use?",
    "question_zh":"一家公司有 PB 級的未標記客戶資料，想將客戶分為不同層級以進行廣告和促銷。應使用哪種方法？",
    "options":{
      "A":{"en":"Supervised learning","zh":"監督式學習"},
      "B":{"en":"Unsupervised learning","zh":"非監督式學習"},
      "C":{"en":"Reinforcement learning","zh":"強化學習"},
      "D":{"en":"Reinforcement learning from human feedback (RLHF)","zh":"來自人類回饋的強化學習 (RLHF)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 監督式學習需要標記資料（每筆資料都有正確答案標籤），但題目明確說明資料是「未標記」的。",
      "B":"✓ 正確 — 非監督式學習（如 K-Means 分群）不需要標記資料，能自動從 PB 級資料中發現隱藏的客戶分群模式，適合將客戶分成有意義的層級。",
      "C":"✗ 強化學習透過獎懲機制訓練代理採取行動，適合決策問題（如遊戲、機器人控制），不適合客戶分群。",
      "D":"✗ RLHF 是一種訓練 LLM 的技術，需要人類回饋，與未標記資料的客戶分群無關。"
    }
  },
  {
    "id":117,"exam":"AIF",
    "question":"An AI practitioner is writing a report about trained ML models to provide transparency and explainability to company stakeholders. The company uses ML models to make quarterly forecasts. What should the AI practitioner include in the report?",
    "question_zh":"AI 從業者正在撰寫有關已訓練 ML 模型的報告，以向公司利益相關者提供透明度和可解釋性。應在報告中包含什麼？",
    "options":{
      "A":{"en":"Code for model training","zh":"模型訓練程式碼"},
      "B":{"en":"Partial dependence plots (PDPs)","zh":"偏依賴圖 (PDPs)"},
      "C":{"en":"Sample data for training","zh":"訓練用的樣本資料"},
      "D":{"en":"Model convergence tables","zh":"模型收斂表"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 訓練程式碼是技術細節，利益相關者通常不是工程師，無法從程式碼中理解模型的決策邏輯。",
      "B":"✓ 正確 — 偏依賴圖（PDP）直觀地顯示每個特徵對模型預測的邊際影響，是 XAI（可解釋 AI）的核心工具，讓非技術利益相關者能理解「哪些因素影響了預測結果及影響程度」。",
      "C":"✗ 訓練樣本資料不能說明模型為何做出特定預測，不符合可解釋性需求。",
      "D":"✗ 收斂表顯示訓練過程中 loss 的變化，是技術指標，不能向業務利益相關者解釋模型決策。"
    }
  },
  {
    "id":118,"exam":"AIF",
    "question":"A company is building an application that needs to generate synthetic data based on existing data. Which type of model can the company use?",
    "question_zh":"一家公司正在建立一個需要根據現有資料生成合成資料的應用程式。公司可以使用哪種類型的模型？",
    "options":{
      "A":{"en":"Generative adversarial network (GAN)","zh":"生成對抗網路 (GAN)"},
      "B":{"en":"XGBoost","zh":"XGBoost"},
      "C":{"en":"Residual neural network","zh":"殘差神經網路 (ResNet)"},
      "D":{"en":"WaveNet","zh":"WaveNet"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — GAN 由生成器（Generator）和判別器（Discriminator）相互對抗訓練，生成器學習生成與真實資料分布相同的合成資料。GAN 廣泛用於生成逼真的圖片、影片、表格資料等合成資料。",
      "B":"✗ XGBoost 是梯度提升樹演算法，用於分類和迴歸預測任務，不能生成合成資料。",
      "C":"✗ 殘差神經網路（ResNet）主要用於圖像分類和特徵提取，不是生成模型。",
      "D":"✗ WaveNet 是 Google 開發的波形生成模型，專注於音訊（語音）合成，不是通用合成資料生成工具。"
    }
  },
  {
    "id":119,"exam":"AIF",
    "question":"A company is using domain-specific models and wants to avoid creating new models from scratch. The company wants to adapt pre-trained models for new, related tasks. Which ML strategy meets these requirements?",
    "question_zh":"一家公司使用特定領域模型，希望避免從頭建立新模型，想要調整預訓練模型以用於新的相關任務。哪種 ML 策略符合需求？",
    "options":{
      "A":{"en":"Increase the number of epochs","zh":"增加訓練輪數（epochs）"},
      "B":{"en":"Use transfer learning","zh":"使用遷移學習"},
      "C":{"en":"Decrease the number of epochs","zh":"減少訓練輪數（epochs）"},
      "D":{"en":"Use unsupervised learning","zh":"使用非監督式學習"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 增加 epoch 只是讓現有模型多訓練幾輪，不涉及將預訓練知識遷移到新任務。",
      "B":"✓ 正確 — 遷移學習（Transfer Learning）將在大型資料集上預訓練的模型知識遷移到新的相關任務。例如，用 ImageNet 預訓練的 ResNet 進行醫療影像分類，或用 BERT 進行特定領域 NLP 任務，無需從頭訓練，節省大量時間和資源。",
      "C":"✗ 減少 epoch 只影響訓練時間，不是知識遷移策略。",
      "D":"✗ 非監督式學習從無標記資料中發現模式，不是利用現有預訓練模型的技術。"
    }
  },
  {
    "id":120,"exam":"AIF",
    "question":"A company built a deep learning model for object detection and deployed it to production. Which AI process occurs when the model analyzes a new image to identify objects?",
    "question_zh":"一家公司建立了用於物件偵測的深度學習模型並部署到生產環境。當模型分析新圖片以識別物件時，發生了哪個 AI 程序？",
    "options":{
      "A":{"en":"Training","zh":"訓練 (Training)"},
      "B":{"en":"Inference","zh":"推論 (Inference)"},
      "C":{"en":"Model deployment","zh":"模型部署 (Model deployment)"},
      "D":{"en":"Bias correction","zh":"偏差修正 (Bias correction)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 訓練是使用標記資料調整模型參數的過程，發生在部署「之前」。",
      "B":"✓ 正確 — 推論（Inference）是模型部署後，使用已訓練完成的模型對新輸入（新圖片）進行預測/識別的過程。這是模型「使用」的階段，而非「學習」的階段。",
      "C":"✗ 模型部署是將訓練好的模型放到可對外提供服務的環境，是一次性的操作，不是每次分析圖片時都發生的程序。",
      "D":"✗ 偏差修正是針對模型偏見的後處理步驟，不是分析新圖片的正常推論流程。"
    }
  },
  {
    "id":121,"exam":"AIF",
    "question":"A company wants to use language models on edge devices for inference with the lowest latency possible. Which solution meets these requirements?",
    "question_zh":"一家公司想在邊緣裝置上使用語言模型進行推論，且延遲必須盡可能低。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Deploy optimized small language models (SLMs) on edge devices","zh":"在邊緣裝置上部署最佳化的小型語言模型 (SLM)"},
      "B":{"en":"Deploy optimized large language models (LLMs) on edge devices","zh":"在邊緣裝置上部署最佳化的大型語言模型 (LLM)"},
      "C":{"en":"Incorporate a centralized small language model (SLM) API for asynchronous communication with edge devices","zh":"採用集中式 SLM API 與邊緣裝置進行非同步通訊"},
      "D":{"en":"Incorporate a centralized large language model (LLM) API for asynchronous communication with edge devices","zh":"採用集中式 LLM API 與邊緣裝置進行非同步通訊"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 在邊緣裝置本地部署最佳化的 SLM（如量化、蒸餾後的小模型），推論在裝置上直接執行，無需網路往返，延遲最低。LLM 太大無法在邊緣裝置上有效執行。",
      "B":"✗ LLM 參數量龐大（數十億至數千億），邊緣裝置的記憶體和運算能力無法有效執行，部署不切實際。",
      "C":"✗ 集中式 API 即使用 SLM，仍需要網路通訊，增加網路延遲，不能達到「最低延遲」的要求。",
      "D":"✗ 集中式 LLM API + 非同步通訊，兩個缺點疊加（大模型 + 網路延遲），延遲最高。"
    }
  },
  {
    "id":122,"exam":"AIF",
    "question":"A company developed a model to predict item prices. The model performed well on training data but performance decreased significantly in production. What should the company do to mitigate this problem?",
    "question_zh":"一家公司開發了預測商品價格的模型，訓練資料表現良好，但部署到生產環境後效能大幅下降。公司應如何緩解此問題？",
    "options":{
      "A":{"en":"Reduce the volume of data used in training","zh":"減少訓練資料量"},
      "B":{"en":"Add hyperparameters to the model","zh":"為模型增加超參數"},
      "C":{"en":"Increase the volume of data used in training","zh":"增加訓練資料量"},
      "D":{"en":"Increase the model training time","zh":"增加模型訓練時間"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 減少訓練資料只會讓過擬合問題更嚴重，使模型更難泛化到生產資料。",
      "B":"✗ 增加超參數可能增加模型複雜度，進一步加劇過擬合。",
      "C":"✓ 正確 — 訓練好、生產差是「過擬合（Overfitting）」的典型症狀：模型記住了訓練資料的細節而非通用模式。增加訓練資料量讓模型接觸更多樣化的例子，改善泛化能力，是最有效的緩解方式。",
      "D":"✗ 增加訓練時間在資料不足的情況下只會讓模型更過擬合，不能解決根本問題。"
    }
  },
  {
    "id":123,"exam":"AIF",
    "question":"A company is using an LLM from Amazon Bedrock for intent detection in a chatbot. The company wants to use few-shot learning to improve intent detection accuracy. Which additional data does the company need?",
    "question_zh":"一家公司使用 Amazon Bedrock 的 LLM 在聊天機器人中進行意圖偵測，想使用少量示例學習提升準確率。公司需要哪些額外資料？",
    "options":{
      "A":{"en":"Pairs of chatbot responses and correct user intents","zh":"聊天機器人回應與正確使用者意圖的配對"},
      "B":{"en":"Pairs of user messages and correct chatbot responses","zh":"使用者訊息與正確聊天機器人回應的配對"},
      "C":{"en":"Pairs of user messages and correct user intents","zh":"使用者訊息與正確使用者意圖的配對"},
      "D":{"en":"Pairs of user intents and correct chatbot responses","zh":"使用者意圖與正確聊天機器人回應的配對"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 任務是「意圖偵測」（輸入：使用者訊息 → 輸出：意圖），聊天機器人回應不是此任務的輸入。",
      "B":"✗ 此配對訓練的是「回應生成」任務，不是意圖偵測。",
      "C":"✓ 正確 — 少量示例（Few-shot）學習的格式是：「輸入 → 正確輸出」的範例對。意圖偵測任務的輸入是使用者訊息，輸出是對應的意圖（如 order_pizza、check_status），因此需要「使用者訊息 + 正確意圖」的配對。",
      "D":"✗ 此配對是反向的，以意圖作為輸入並非意圖偵測的任務定義。"
    }
  },
  {
    "id":124,"exam":"AIF",
    "question":"A company is training a foundation model (FM) and wants to increase the accuracy of the model up to a specific acceptance level. Which solution will meet these requirements?",
    "question_zh":"一家公司正在訓練基礎模型，想將模型準確率提升到特定的接受水準。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Decrease the batch size","zh":"減少批次大小 (batch size)"},
      "B":{"en":"Increase the epochs","zh":"增加訓練輪數 (epochs)"},
      "C":{"en":"Decrease the epochs","zh":"減少訓練輪數 (epochs)"},
      "D":{"en":"Increase the temperature parameter","zh":"增加溫度 (temperature) 參數"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 減少 batch size 影響梯度估計的穩定性，不直接提升模型準確率，且可能使訓練更慢。",
      "B":"✓ 正確 — 增加 epoch（訓練輪數）讓模型多次遍歷訓練資料，持續調整權重以改善學習，通常能提升準確率（直到收斂或過擬合）。",
      "C":"✗ 減少 epoch 會導致欠擬合（Underfitting），模型還沒充分學習資料模式就停止訓練，準確率更低。",
      "D":"✗ Temperature 是推論參數，控制輸出的隨機程度，不影響訓練準確率。"
    }
  },
  {
    "id":125,"exam":"AIF",
    "question":"Which type of AI model makes numeric predictions?",
    "question_zh":"哪種類型的 AI 模型進行數值預測？",
    "options":{
      "A":{"en":"Diffusion","zh":"擴散模型 (Diffusion)"},
      "B":{"en":"Regression","zh":"迴歸 (Regression)"},
      "C":{"en":"Transformer","zh":"Transformer"},
      "D":{"en":"Multi-modal","zh":"多模態 (Multi-modal)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 擴散模型（Diffusion Models）是生成模型，用於生成圖像、音訊等，不做數值預測。",
      "B":"✓ 正確 — 迴歸（Regression）模型的輸出是連續的數值（如房價、溫度、銷售量），是專門用於數值預測的 ML 模型類型。",
      "C":"✗ Transformer 是神經網路架構，廣泛用於 NLP 和視覺任務，但不是「做數值預測」的特定模型類型。",
      "D":"✗ 多模態模型可處理多種輸入（文字、圖片、音訊），是能力描述而非預測類型。"
    }
  },
  {
    "id":126,"exam":"AIF",
    "question":"An ecommerce company receives multiple gigabytes of customer data daily and uses it to train an ML model to forecast future product demand. The company needs a solution to perform inferences once each day. Which inference type meets these requirements?",
    "question_zh":"一家電商公司每天收到數 GB 的客戶資料，用於訓練 ML 模型預測未來產品需求，需要每天執行一次推論。哪種推論類型符合需求？",
    "options":{
      "A":{"en":"Batch inference","zh":"批次推論 (Batch inference)"},
      "B":{"en":"Asynchronous inference","zh":"非同步推論 (Asynchronous inference)"},
      "C":{"en":"Real-time inference","zh":"即時推論 (Real-time inference)"},
      "D":{"en":"Serverless inference","zh":"無伺服器推論 (Serverless inference)"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 批次推論（Batch Inference）適合定期（每天、每週）對大量資料執行推論，一次處理整批資料後輸出結果，完全符合「每天一次、大量資料」的需求模式，成本最優化。",
      "B":"✗ 非同步推論適合大型輸入（最高 1GB）且需要近即時但非同步回應，適合單筆請求，不是定期批次處理的最佳選擇。",
      "C":"✗ 即時推論適合低延遲即時請求（毫秒級），不適合每天一次的大批量定期處理。",
      "D":"✗ 無伺服器推論適合流量不規則且較低的工作負載，對每天 GB 級資料的批次推論不是最佳選擇。"
    }
  },
  {
    "id":127,"exam":"AIF",
    "question":"A company manually reviews all submitted resumes in PDF format. As the company grows, the volume of resumes will exceed review capacity. The company needs an automated system to convert PDF resumes into plain text for additional processing. Which AWS service meets this requirement?",
    "question_zh":"一家公司手動審查所有以 PDF 格式提交的履歷，隨著公司成長，履歷量將超過審查能力。需要自動化系統將 PDF 履歷轉換為純文字。哪個 AWS 服務符合需求？",
    "options":{
      "A":{"en":"Amazon Textract","zh":"Amazon Textract"},
      "B":{"en":"Amazon Personalize","zh":"Amazon Personalize"},
      "C":{"en":"Amazon Lex","zh":"Amazon Lex"},
      "D":{"en":"Amazon Transcribe","zh":"Amazon Transcribe"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon Textract 是文件文字提取服務，可自動從 PDF、掃描文件和圖片中提取文字、表格和表單資料，完全符合「PDF 轉純文字」的需求。",
      "B":"✗ Amazon Personalize 是個人化推薦服務，不處理文件內容提取。",
      "C":"✗ Amazon Lex 是建立對話式聊天機器人的服務，不用於文件文字提取。",
      "D":"✗ Amazon Transcribe 是語音轉文字（STT）服務，處理音訊輸入，不處理 PDF 文件。"
    }
  },
  {
    "id":128,"exam":"AIF",
    "question":"A company is building a contact center application and wants to analyze and extract key information from the audio of customer calls. Which solution meets these requirements?",
    "question_zh":"一家公司正在建立聯絡中心應用程式，想從客戶通話音訊中分析和提取關鍵資訊。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Build a conversational chatbot by using Amazon Lex","zh":"使用 Amazon Lex 建立對話式聊天機器人"},
      "B":{"en":"Transcribe call recordings by using Amazon Transcribe","zh":"使用 Amazon Transcribe 轉錄通話錄音"},
      "C":{"en":"Extract information from call recordings by using Amazon SageMaker Model Monitor","zh":"使用 Amazon SageMaker Model Monitor 從通話錄音中提取資訊"},
      "D":{"en":"Create classification labels by using Amazon Comprehend","zh":"使用 Amazon Comprehend 建立分類標籤"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Lex 建立對話式介面，不用於分析現有通話錄音的音訊內容。",
      "B":"✓ 正確 — Amazon Transcribe 將音訊轉為文字（STT），支援通話錄音轉錄。轉錄後的文字可進一步用 Comprehend 提取關鍵資訊、分析情感等，是聯絡中心分析的標準 AWS 解決方案。",
      "C":"✗ SageMaker Model Monitor 監控 ML 模型的資料漂移和效能，不是音訊內容提取工具。",
      "D":"✗ Amazon Comprehend 分析文字，但無法直接處理音訊，需要先用 Transcribe 轉錄後才能使用 Comprehend。"
    }
  },
  {
    "id":129,"exam":"AIF",
    "question":"An ecommerce company wants to build a solution to determine customer sentiments based on written customer reviews. Which AWS services meet these requirements? (Select TWO)",
    "question_zh":"一家電商公司想建立根據書面客戶評論判斷客戶情感的解決方案。哪些 AWS 服務符合需求？（選2項）",
    "options":{
      "A":{"en":"Amazon Lex","zh":"Amazon Lex"},
      "B":{"en":"Amazon Comprehend","zh":"Amazon Comprehend"},
      "C":{"en":"Amazon Polly","zh":"Amazon Polly"},
      "D":{"en":"Amazon Bedrock","zh":"Amazon Bedrock"},
      "E":{"en":"Amazon Rekognition","zh":"Amazon Rekognition"}
    },
    "correct":["B","D"],"multi":True,
    "explanations":{
      "A":"✗ Amazon Lex 建立對話介面（聊天機器人），不做情感分析。",
      "B":"✓ 正確 — Amazon Comprehend 內建情感分析 API，可直接判斷文字為正面、負面、中立或混合情感，是文字情感分析的原生 AWS 服務。",
      "C":"✗ Amazon Polly 是文字轉語音（TTS）服務，不分析文字內容。",
      "D":"✓ 正確 — Amazon Bedrock 的基礎模型（如 Claude、Titan）具備強大的 NLP 能力，可透過提示工程進行情感分析，適合需要更複雜理解或自訂分析的場景。",
      "E":"✗ Amazon Rekognition 分析圖像和影片（如人臉識別、物件偵測），不處理文字情感。"
    }
  },
  {
    "id":130,"exam":"AIF",
    "question":"A company has thousands of customer support interactions per day and wants to analyze these interactions to identify frequently asked questions and develop insights. Which AWS service can the company use?",
    "question_zh":"一家公司每天有數千個客戶支援互動，想分析這些互動以識別常見問題並獲得見解。可以使用哪個 AWS 服務？",
    "options":{
      "A":{"en":"Amazon Lex","zh":"Amazon Lex"},
      "B":{"en":"Amazon Comprehend","zh":"Amazon Comprehend"},
      "C":{"en":"Amazon Transcribe","zh":"Amazon Transcribe"},
      "D":{"en":"Amazon Translate","zh":"Amazon Translate"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Lex 建立聊天機器人，不用於分析已有的互動文字資料。",
      "B":"✓ 正確 — Amazon Comprehend 提供主題建模（Topic Modeling）、關鍵詞提取、情感分析等功能，可從大量文字互動中識別常見主題（常見問題）和洞察，是文字分析的核心服務。",
      "C":"✗ Amazon Transcribe 將語音轉為文字，若互動是音訊可先用它轉錄，但直接分析文字互動應用 Comprehend。",
      "D":"✗ Amazon Translate 提供語言翻譯，不用於分析內容或識別常見問題。"
    }
  },
  {
    "id":131,"exam":"AIF",
    "question":"Which feature of Amazon OpenSearch Service gives companies the ability to build vector database applications?",
    "question_zh":"Amazon OpenSearch Service 的哪個功能讓公司能夠建立向量資料庫應用程式？",
    "options":{
      "A":{"en":"Integration with Amazon S3 for object storage","zh":"與 Amazon S3 整合以進行物件儲存"},
      "B":{"en":"Support for geospatial indexing and queries","zh":"支援地理空間索引和查詢"},
      "C":{"en":"Scalable index management and nearest neighbor search capability","zh":"可擴展的索引管理和最近鄰搜尋功能"},
      "D":{"en":"Ability to perform real-time analysis on streaming data","zh":"對串流資料執行即時分析的能力"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ S3 整合是儲存功能，不是向量資料庫的核心能力。",
      "B":"✗ 地理空間索引用於位置資料查詢，不是向量相似度搜尋。",
      "C":"✓ 正確 — OpenSearch 的 k-NN（k-Nearest Neighbor）外掛提供向量索引和近似最近鄰（ANN）搜尋，這是向量資料庫的核心功能：儲存高維度 embedding 向量，並快速找到語義最相似的向量，常用於 RAG 應用的語義搜尋。",
      "D":"✗ 即時串流分析是 OpenSearch Dashboards 的功能，不是向量資料庫能力。"
    }
  },
  {
    "id":132,"exam":"AIF",
    "question":"An animation company wants to provide subtitles for its content. Which AWS service meets this requirement?",
    "question_zh":"一家動畫公司想為其內容提供字幕。哪個 AWS 服務符合此需求？",
    "options":{
      "A":{"en":"Amazon Comprehend","zh":"Amazon Comprehend"},
      "B":{"en":"Amazon Polly","zh":"Amazon Polly"},
      "C":{"en":"Amazon Transcribe","zh":"Amazon Transcribe"},
      "D":{"en":"Amazon Translate","zh":"Amazon Translate"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Comprehend 分析文字的語義（情感、主題等），不能從音訊生成字幕。",
      "B":"✗ Amazon Polly 是文字轉語音（TTS），將文字轉為音訊，功能與字幕需求相反。",
      "C":"✓ 正確 — Amazon Transcribe 是語音轉文字（STT）服務，可將動畫中的對話音訊自動轉為文字，並輸出帶時間戳記的字幕檔（如 SRT 格式），是自動生成字幕的標準解決方案。",
      "D":"✗ Amazon Translate 提供語言翻譯，可在字幕生成後用於多語言翻譯，但本身不能從音訊生成字幕。"
    }
  },
  {
    "id":133,"exam":"AIF",
    "question":"A customer service team is developing an application to analyze customer feedback and automatically classify it into categories: product quality, customer service, and delivery experience. Which AI concept does this scenario present?",
    "question_zh":"客戶服務團隊正在開發一個分析客戶回饋並自動將其分類為「產品品質」、「客戶服務」和「交貨體驗」的應用程式。此場景呈現哪個 AI 概念？",
    "options":{
      "A":{"en":"Computer vision","zh":"電腦視覺 (Computer Vision)"},
      "B":{"en":"Natural language processing (NLP)","zh":"自然語言處理 (NLP)"},
      "C":{"en":"Recommendation systems","zh":"推薦系統 (Recommendation Systems)"},
      "D":{"en":"Fraud detection","zh":"欺詐偵測 (Fraud Detection)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 電腦視覺處理圖片和影片的分析，此場景的輸入是文字（客戶回饋），不是視覺內容。",
      "B":"✓ 正確 — 分析文字並將其分類是 NLP 的核心任務之一（文字分類/Text Classification）。理解客戶書面回饋的語義並歸類到對應主題，正是 NLP 和情感分析的典型應用。",
      "C":"✗ 推薦系統根據使用者行為推薦商品或內容（如 Netflix 推薦），與文字分類不同。",
      "D":"✗ 欺詐偵測識別異常交易或可疑活動，不是文字內容分類。"
    }
  },
  {
    "id":134,"exam":"AIF",
    "question":"A financial company wants to flag all credit card activity as possibly fraudulent or non-fraudulent based on transaction data. Which type of ML model meets these requirements?",
    "question_zh":"一家金融公司想根據交易資料將所有信用卡活動標記為可能欺詐或非欺詐。哪種 ML 模型類型符合需求？",
    "options":{
      "A":{"en":"Regression","zh":"迴歸 (Regression)"},
      "B":{"en":"Diffusion","zh":"擴散模型 (Diffusion)"},
      "C":{"en":"Binary classification","zh":"二元分類 (Binary classification)"},
      "D":{"en":"Multi-class classification","zh":"多類別分類 (Multi-class classification)"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 迴歸預測連續數值（如欺詐風險分數），不做二選一的標記判斷。",
      "B":"✗ 擴散模型是生成模型，用於圖像生成等，不做欺詐分類。",
      "C":"✓ 正確 — 二元分類（Binary Classification）的輸出只有兩個類別：欺詐（1）或非欺詐（0），完全符合「標記為欺詐或非欺詐」的需求。典型演算法包括邏輯迴歸、XGBoost、神經網路等。",
      "D":"✗ 多類別分類輸出三個或以上的類別，此場景只需要兩個類別，不需要多類別分類。"
    }
  },
  {
    "id":135,"exam":"AIF",
    "question":"A manufacturing company wants to create product descriptions in multiple languages. Which AWS service will automate this task?",
    "question_zh":"一家製造公司想以多種語言建立產品描述。哪個 AWS 服務可以自動化此任務？",
    "options":{
      "A":{"en":"Amazon Translate","zh":"Amazon Translate"},
      "B":{"en":"Amazon Transcribe","zh":"Amazon Transcribe"},
      "C":{"en":"Amazon Kendra","zh":"Amazon Kendra"},
      "D":{"en":"Amazon Polly","zh":"Amazon Polly"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon Translate 是神經網路機器翻譯服務，可將文字（如產品描述）自動翻譯成 75+ 種語言，支援即時和批次翻譯，完全符合多語言產品描述的需求。",
      "B":"✗ Amazon Transcribe 是語音轉文字服務，不做語言翻譯。",
      "C":"✗ Amazon Kendra 是智慧企業搜尋服務，不做語言翻譯。",
      "D":"✗ Amazon Polly 是文字轉語音（TTS），可將文字轉為語音輸出，但不翻譯語言。"
    }
  },
  {
    "id":136,"exam":"AIF",
    "question":"A company wants to find groups for its customers based on their demographics and buying patterns. Which algorithm should the company use?",
    "question_zh":"一家公司想根據客戶的人口統計資料和購買模式找出客戶群組。應使用哪種演算法？",
    "options":{
      "A":{"en":"K-nearest neighbors (k-NN)","zh":"K 近鄰演算法 (k-NN)"},
      "B":{"en":"K-means","zh":"K-均值演算法 (K-means)"},
      "C":{"en":"Decision tree","zh":"決策樹 (Decision tree)"},
      "D":{"en":"Support vector machine","zh":"支援向量機 (SVM)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ k-NN 是監督式學習的分類演算法，根據最近的 k 個已標記樣本預測類別，需要預先標記的訓練資料。",
      "B":"✓ 正確 — K-means 是非監督式分群演算法，無需標記資料，將資料點依相似度自動分為 K 個群集，是根據人口統計和購買行為進行客戶分群的標準方法。",
      "C":"✗ 決策樹是監督式分類/迴歸演算法，需要標記資料，不用於發現未知群組。",
      "D":"✗ SVM 是監督式分類演算法，需要標記訓練資料，不適合無標記的客戶分群任務。"
    }
  },
  {
    "id":137,"exam":"AIF",
    "question":"A company wants to develop an educational game where users answer probability questions. Which solution meets these requirements with the LEAST operational overhead?",
    "question_zh":"一家公司想開發一個使用者回答概率問題的教育遊戲。哪個解決方案以最少的操作負擔符合需求？",
    "options":{
      "A":{"en":"Use supervised learning to create a regression model that will predict probability","zh":"使用監督式學習建立預測概率的迴歸模型"},
      "B":{"en":"Use reinforcement learning to train a model to return the probability","zh":"使用強化學習訓練模型返回概率"},
      "C":{"en":"Use code that will calculate probability by using simple rules and computations","zh":"使用程式碼透過簡單規則和計算來計算概率"},
      "D":{"en":"Use unsupervised learning to create a model that will estimate probability density","zh":"使用非監督式學習建立估計概率密度的模型"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 為確定性數學計算建立 ML 模型是過度工程化，需要資料收集、訓練、評估，操作負擔遠高於必要。",
      "B":"✗ 強化學習適合序列決策問題（如遊戲 AI），為基礎概率計算建立 RL 模型更是嚴重過度設計。",
      "C":"✓ 正確 — 概率是確定性數學計算（如從罐子中取球：P = 目標數量 / 總數量）。使用簡單程式碼計算是最直接、最低負擔的方法，不需要任何 ML 模型。這是「不要過度使用 AI」原則的體現。",
      "D":"✗ 概率密度估計是統計 ML 技術，針對本題的簡單確定性計算是完全不必要的複雜度。"
    }
  },
  {
    "id":138,"exam":"AIF",
    "question":"An AI practitioner is building a model to generate images of humans in various professions. The AI practitioner discovered that the input data is biased and that specific attributes affect image generation and create bias. Which technique will solve this problem?",
    "question_zh":"AI 從業者正在建立一個生成各種職業人類圖像的模型，發現輸入資料有偏見，特定屬性影響圖像生成並造成偏見。哪種技術可以解決此問題？",
    "options":{
      "A":{"en":"Data augmentation for imbalanced classes","zh":"針對不平衡類別的資料擴充"},
      "B":{"en":"Model monitoring for class distribution","zh":"用於類別分布的模型監控"},
      "C":{"en":"Retrieval Augmented Generation (RAG)","zh":"檢索增強生成 (RAG)"},
      "D":{"en":"Watermark detection for images","zh":"圖像浮水印偵測"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 資料增廣（Data Augmentation）可為代表性不足的類別（如特定職業中少數群體的圖像）生成更多樣本，平衡資料集中各群組的代表性，從根本上減少訓練資料偏見。",
      "B":"✗ 模型監控追蹤已部署模型的效能，是事後偵測工具，不能在訓練前解決資料偏見。",
      "C":"✗ RAG 用於讓 LLM 檢索外部知識以豐富回應，不是處理圖像生成偏見的技術。",
      "D":"✗ 浮水印偵測用於識別 AI 生成的圖像，不是消除訓練資料偏見的方法。"
    }
  },
  {
    "id":139,"exam":"AIF",
    "question":"A food service company wants to collect a dataset to predict customer food preferences. The company wants to ensure that the food preferences of all demographics are included in the data. Which dataset characteristic does this scenario present?",
    "question_zh":"一家食品服務公司想收集資料集來預測客戶食物偏好，想確保所有人口族群的食物偏好都包含在資料中。此場景呈現哪個資料集特性？",
    "options":{
      "A":{"en":"Accuracy","zh":"準確性 (Accuracy)"},
      "B":{"en":"Diversity","zh":"多樣性 (Diversity)"},
      "C":{"en":"Recency bias","zh":"近期偏見 (Recency bias)"},
      "D":{"en":"Reliability","zh":"可靠性 (Reliability)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 準確性指資料反映真實情況的程度，與確保「所有人口族群代表性」的目標不同。",
      "B":"✓ 正確 — 多樣性（Diversity）是指資料集包含廣泛且有代表性的樣本，涵蓋不同年齡、性別、文化背景等人口族群。確保所有族群的偏好都被包含，正是追求資料集多樣性的實踐，可防止模型對特定族群產生偏見。",
      "C":"✗ 近期偏見是指過度強調近期資料而忽視歷史趨勢，與族群代表性無關。",
      "D":"✗ 可靠性指資料來源的一致性和可信度，不是族群多樣性的描述。"
    }
  },
  {
    "id":140,"exam":"AIF",
    "question":"A financial company is developing a fraud detection system. Employees will evaluate flagged fraud cases. The company wants to minimize the time employees spend reviewing flagged cases that are NOT actually fraudulent. Which evaluation metric meets these requirements?",
    "question_zh":"一家金融公司正在開發欺詐偵測系統，員工將評估被標記的欺詐案例。公司想最小化員工審查「實際上並非欺詐」的標記案例所花費的時間。哪個評估指標符合需求？",
    "options":{
      "A":{"en":"Recall","zh":"召回率 (Recall)"},
      "B":{"en":"Accuracy","zh":"準確率 (Accuracy)"},
      "C":{"en":"Precision","zh":"精確率 (Precision)"},
      "D":{"en":"Lift chart","zh":"提升圖 (Lift chart)"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 召回率（Recall = TP / (TP+FN)）衡量「所有真實欺詐中被找到的比例」，最小化漏報（False Negative），不是減少誤報（False Positive）。",
      "B":"✗ 準確率是整體正確率，在不平衡資料集（欺詐案例少）中可能失真，且不能直接反映誤報問題。",
      "C":"✓ 正確 — 精確率（Precision = TP / (TP+FP)）衡量「被標記為欺詐中真正是欺詐的比例」。精確率高代表誤報（False Positive，非欺詐被標記為欺詐）少，員工審查的案例中大多數真的是欺詐，最小化無效審查時間。",
      "D":"✗ 提升圖評估模型相對於隨機選擇的效能，不是直接最小化誤報的指標。"
    }
  },
  {
    "id":141,"exam":"AIF",
    "question":"Which technique can a company use to lower bias and toxicity in generative AI applications during the post-processing ML lifecycle?",
    "question_zh":"在後處理 ML 生命週期中，公司可以使用哪種技術降低生成式 AI 應用程式中的偏見和毒性？",
    "options":{
      "A":{"en":"Human-in-the-loop","zh":"人在迴路中 (Human-in-the-loop)"},
      "B":{"en":"Data augmentation","zh":"資料擴充 (Data augmentation)"},
      "C":{"en":"Feature engineering","zh":"特徵工程 (Feature engineering)"},
      "D":{"en":"Adversarial training","zh":"對抗訓練 (Adversarial training)"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Human-in-the-loop（HITL）在後處理階段讓人類審查和修正 AI 輸出，直接攔截有偏見或有毒的回應。這是 Amazon A2I（Augmented AI）等服務的核心概念，也是 RLHF 的基礎，有效降低有害輸出。",
      "B":"✗ 資料擴充是訓練前的資料準備技術，不是後處理階段的工具。",
      "C":"✗ 特徵工程是訓練前優化輸入特徵的技術，屬於預處理步驟。",
      "D":"✗ 對抗訓練透過對抗樣本提升模型魯棒性，是訓練階段的技術，不是後處理。"
    }
  },
  {
    "id":142,"exam":"AIF",
    "question":"A company uses Amazon SageMaker in production with large input data up to 1 GB and processing times up to 1 hour. The company needs near real-time latency. Which SageMaker inference option meets these requirements?",
    "question_zh":"一家公司在生產環境中使用 Amazon SageMaker，輸入資料最高達 1 GB，處理時間最長 1 小時，需要近即時延遲。哪個 SageMaker 推論選項符合需求？",
    "options":{
      "A":{"en":"Real-time inference","zh":"即時推論 (Real-time inference)"},
      "B":{"en":"Serverless inference","zh":"無伺服器推論 (Serverless inference)"},
      "C":{"en":"Asynchronous inference","zh":"非同步推論 (Asynchronous inference)"},
      "D":{"en":"Batch transform","zh":"批次轉換 (Batch transform)"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 即時推論有 60 秒的 invocation 超時限制，無法處理長達 1 小時的請求；且通常用於小型、低延遲的即時請求。",
      "B":"✗ 無伺服器推論適合低頻、輕量的工作負載，不支援大型（1GB）輸入或長時間處理。",
      "C":"✓ 正確 — 非同步推論（Asynchronous Inference）專為大型負載設計：支援最高 1 GB 輸入、最長 1 小時處理時間，以佇列方式處理請求並在完成後通知，實現近即時（Near Real-time）的大型請求處理，完全符合所有條件。",
      "D":"✗ 批次轉換是離線批次處理，適合定期大量資料，不提供近即時的回應。"
    }
  },
  {
    "id":143,"exam":"AIF",
    "question":"A company wants to build an ML model using Amazon SageMaker. The company needs to share and manage variables for model development across multiple teams. Which SageMaker feature meets these requirements?",
    "question_zh":"一家公司想使用 Amazon SageMaker 建立 ML 模型，需要跨多個團隊共享和管理模型開發的變數。哪個 SageMaker 功能符合需求？",
    "options":{
      "A":{"en":"Amazon SageMaker Feature Store","zh":"Amazon SageMaker Feature Store"},
      "B":{"en":"Amazon SageMaker Data Wrangler","zh":"Amazon SageMaker Data Wrangler"},
      "C":{"en":"Amazon SageMaker Clarify","zh":"Amazon SageMaker Clarify"},
      "D":{"en":"Amazon SageMaker Model Cards","zh":"Amazon SageMaker Model Cards"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon SageMaker Feature Store 是集中式特徵儲存庫，讓不同團隊可以發現、共享和重用 ML 特徵（Feature），確保跨團隊使用一致的特徵定義，避免重複計算。",
      "B":"✗ SageMaker Data Wrangler 是資料準備和轉換工具，不是跨團隊特徵共享平台。",
      "C":"✗ SageMaker Clarify 用於偵測模型偏見和提供可解釋性，不是特徵管理工具。",
      "D":"✗ SageMaker Model Cards 記錄模型的詳細資訊（用途、效能、限制），是模型文件工具，不是特徵共享平台。"
    }
  },
]
