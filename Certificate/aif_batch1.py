
AIF_BATCH1 = [
  {
    "id":101,"exam":"AIF",
    "question":"Which ML technique uses training data that is labeled with the correct output values?",
    "question_zh":"哪種機器學習技術使用標記了正確輸出值的訓練資料？",
    "options":{
      "A":{"en":"Supervised learning","zh":"監督式學習"},
      "B":{"en":"Unsupervised learning","zh":"非監督式學習"},
      "C":{"en":"Reinforcement learning","zh":"強化學習"},
      "D":{"en":"Transfer learning","zh":"遷移學習"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 監督式學習（Supervised Learning）使用含有正確答案標籤的訓練資料（如「這封郵件是垃圾郵件」）訓練模型，使其學會將輸入映射到正確輸出。",
      "B":"✗ 非監督式學習不使用標籤，而是從資料中自行發現隱藏模式（如分群、降維）。",
      "C":"✗ 強化學習透過與環境互動，以獎勵/懲罰訊號學習最佳決策，不使用預先標記的資料集。",
      "D":"✗ 遷移學習是將預訓練模型的知識應用到新任務，是訓練策略而非資料標記方法。"
    }
  },
  {
    "id":102,"exam":"AIF",
    "question":"An education provider wants to automatically change the style of a generative AI model response depending on the age range of the user asking the question. Which solution meets these requirements with the LEAST implementation effort?",
    "question_zh":"教育供應商希望根據提問使用者的年齡範圍，自動調整生成式 AI 模型回應的風格，哪個解決方案以最少的實作工作量達成此需求？",
    "options":{
      "A":{"en":"Fine-tune the model using additional training data representative of the various age ranges","zh":"使用代表各年齡層的額外訓練資料對模型進行微調"},
      "B":{"en":"Add a role description to the prompt context that instructs the model of the age range that the response should target","zh":"在提示語境中加入角色描述，指示模型回應應針對的年齡層"},
      "C":{"en":"Use chain-of-thought reasoning to deduce the correct style and complexity","zh":"使用思維鏈推理來推導正確的風格和複雜度"},
      "D":{"en":"Summarize the response text depending on the age of the user","zh":"根據使用者年齡對回應文字進行摘要"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 微調需要準備各年齡層的代表性資料集並執行訓練，實作工作量很高，不符合「最少工作量」的要求。",
      "B":"✓ 正確 — 在提示的系統或上下文部分加入角色說明（如「請用適合8歲兒童的語言回答」）是最快速的方式，只需修改提示即可，無需任何訓練或額外基礎設施。",
      "C":"✗ 思維鏈（Chain-of-Thought）提示需要設計複雜的推理步驟，工作量比直接加入角色描述高。",
      "D":"✗ 摘要只是縮短回應長度，不能改變語言風格或複雜度以適應不同年齡層。"
    }
  },
  {
    "id":103,"exam":"AIF",
    "question":"A company wants to make a chatbot to help customers solve technical problems without human intervention. The chatbot uses a foundation model (FM) and needs to produce responses that adhere to company tone. Which solution meets these requirements?",
    "question_zh":"一家公司想建立一個聊天機器人協助客戶解決技術問題，需要使用基礎模型並產生符合公司語調的回應。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Set a low limit on the number of tokens the FM can produce","zh":"設定 FM 可產生的 token 數量上限"},
      "B":{"en":"Use batch inferencing to process detailed responses","zh":"使用批次推論處理詳細回應"},
      "C":{"en":"Experiment and refine the prompt until the FM produces the desired responses","zh":"實驗並反覆修改提示，直到 FM 產生所需回應"},
      "D":{"en":"Define a higher number for the temperature parameter","zh":"為溫度參數設定更高的值"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 限制 token 數量只影響回應長度，不能控制語調或風格。",
      "B":"✗ 批次推論（Batch Inferencing）適合離線大量處理，不是即時聊天場景，也無法控制語調。",
      "C":"✓ 正確 — 提示工程（Prompt Engineering）透過反覆實驗和優化系統提示（System Prompt），明確指定公司語調要求，是讓 FM 遵循特定風格最直接且成本最低的方法。",
      "D":"✗ 溫度越高，輸出越隨機和創意，反而會讓回應更不一致、更難保持穩定的公司語調。"
    }
  },
  {
    "id":104,"exam":"AIF",
    "question":"A company is implementing the Amazon Titan FM via Amazon Bedrock. The company needs to supplement the model with relevant data from the company's private data sources. Which solution will meet this requirement?",
    "question_zh":"一家公司正在透過 Amazon Bedrock 實作 Amazon Titan 基礎模型，需要以公司私有資料來源的相關資料補充模型。哪個解決方案符合此需求？",
    "options":{
      "A":{"en":"Use a different FM","zh":"使用不同的基礎模型"},
      "B":{"en":"Choose a lower temperature value","zh":"選擇較低的溫度值"},
      "C":{"en":"Create an Amazon Bedrock knowledge base","zh":"建立 Amazon Bedrock 知識庫"},
      "D":{"en":"Enable model invocation logging","zh":"啟用模型調用日誌"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 更換 FM 無法解決使用私有資料的問題，任何 FM 都不會自動知道公司的私有資料。",
      "B":"✗ 溫度值影響輸出的隨機性，與補充私有資料完全無關。",
      "C":"✓ 正確 — Amazon Bedrock Knowledge Base 實作 RAG（檢索增強生成）架構：將私有資料（如 S3 文件）向量化並儲存，在推論時自動檢索相關內容注入提示，讓 FM 回答私有資料的問題。",
      "D":"✗ 模型調用日誌記錄請求和回應，用於監控和審計，不能讓模型存取私有資料。"
    }
  },
  {
    "id":105,"exam":"AIF",
    "question":"An ecommerce company wants to group customers based on their purchase history and preferences to personalize the user experience. Which ML technique should the company use?",
    "question_zh":"一家電商公司想根據客戶的購買歷史和偏好將客戶分組，以個人化使用者體驗。應使用哪種 ML 技術？",
    "options":{
      "A":{"en":"Classification","zh":"分類 (Classification)"},
      "B":{"en":"Clustering","zh":"分群 (Clustering)"},
      "C":{"en":"Regression","zh":"迴歸 (Regression)"},
      "D":{"en":"Content generation","zh":"內容生成 (Content Generation)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 分類需要預先定義好的類別標籤（如「高價值客戶」、「流失風險客戶」），且需要標記資料訓練；此場景沒有預定義分組。",
      "B":"✓ 正確 — 分群（Clustering）是非監督式學習，無需預先定義類別，自動將相似客戶聚集在一起（如 K-Means），非常適合根據購買行為發現自然的客群細分。",
      "C":"✗ 迴歸預測連續數值（如下一次購買金額），不是用來分組客戶的技術。",
      "D":"✗ 內容生成是生成式 AI 的能力（如生成產品描述），不是分析/分組客戶資料的技術。"
    }
  },
  {
    "id":106,"exam":"AIF",
    "question":"Which term describes the numerical representations of real-world objects and concepts that AI and NLP models use to improve understanding of textual information?",
    "question_zh":"哪個術語描述 AI 和 NLP 模型用來提升對文字資訊理解的真實世界物件和概念的數值表示？",
    "options":{
      "A":{"en":"Embeddings","zh":"嵌入向量 (Embeddings)"},
      "B":{"en":"Tokens","zh":"Token"},
      "C":{"en":"Models","zh":"模型 (Models)"},
      "D":{"en":"Binaries","zh":"二進位 (Binaries)"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Embeddings（嵌入向量）是將詞語、句子或文件轉換為高維度數值向量，語義相近的概念在向量空間中距離更近，讓模型能理解語義關係（如「國王」-「男」+「女」≈「女王」）。",
      "B":"✗ Token 是文字的基本分割單位（詞或子詞），是文字的分割結果，不是數值表示本身。",
      "C":"✗ Model 是整個 AI 系統，不是表示概念的數值格式。",
      "D":"✗ Binary 是二進位數據格式，不是 AI/NLP 中語義表示的術語。"
    }
  },
  {
    "id":107,"exam":"AIF",
    "question":"A company deploying a generative AI system for marketing copy has established policies to ensure the AI system does not generate harmful or discriminatory content. Which principle of responsible AI does the company demonstrate?",
    "question_zh":"一家公司部署用於行銷文案的生成式 AI 系統，並制定政策確保 AI 不生成有害或歧視性內容。公司展示了哪個負責任 AI 原則？",
    "options":{
      "A":{"en":"Fairness","zh":"公平性 (Fairness)"},
      "B":{"en":"Explainability","zh":"可解釋性 (Explainability)"},
      "C":{"en":"Governance","zh":"治理 (Governance)"},
      "D":{"en":"Transparency","zh":"透明度 (Transparency)"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 公平性（Fairness）確保 AI 對所有群體不帶偏見地平等對待；雖然與歧視內容有關聯，但政策和制度框架更屬於「治理」範疇。",
      "B":"✗ 可解釋性（Explainability）是讓使用者理解 AI 如何做出決策，不是建立政策防止有害輸出。",
      "C":"✓ 正確 — 治理（Governance）是指建立政策、流程和控制機制，確保 AI 系統的負責任使用。制定內容政策來防止有害或歧視性輸出，正是 AI 治理的核心實踐。",
      "D":"✗ 透明度（Transparency）是公開 AI 系統的運作方式，讓外部人員了解其決策邏輯，不是內部政策控制。"
    }
  },
  {
    "id":108,"exam":"AIF",
    "question":"A social media company wants to use a large language model (LLM) for content moderation. The company wants to evaluate the LLM outputs for bias and potential discrimination. Which data source should the company use with the LEAST administrative effort?",
    "question_zh":"一家社群媒體公司想使用 LLM 進行內容審核，並評估 LLM 輸出是否存在偏見和歧視。以最少管理工作量應使用哪個資料來源？",
    "options":{
      "A":{"en":"User-generated content","zh":"使用者生成的內容"},
      "B":{"en":"Moderation logs","zh":"審核日誌"},
      "C":{"en":"Content moderation guidelines","zh":"內容審核指南"},
      "D":{"en":"Benchmark datasets","zh":"基準資料集"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 使用者生成內容需要大量標記和清理工作，管理工作量高，且隱私和版權問題複雜。",
      "B":"✗ 審核日誌是歷史記錄，範圍有限，不一定包含評估偏見所需的多樣化測試案例。",
      "C":"✗ 內容審核指南是文字政策文件，不是可直接用於評估 AI 輸出的測試資料集。",
      "D":"✓ 正確 — 基準資料集（Benchmark Datasets）是預先設計好用於評估 AI 偏見和公平性的標準化資料集（如 WinoBias、BBQ 等），無需從頭建立，管理工作量最少，可直接用於評估。"
    }
  },
  {
    "id":109,"exam":"AIF",
    "question":"A company wants to identify harmful language in social media comments using an ML model. The company will NOT use labeled data to train the model. Which strategy should the company use?",
    "question_zh":"一家公司想使用 ML 模型識別社群媒體評論中的有害語言，且不會使用標記資料訓練模型。應使用哪種策略？",
    "options":{
      "A":{"en":"Use Amazon Rekognition moderation","zh":"使用 Amazon Rekognition 審核"},
      "B":{"en":"Use Amazon Comprehend toxicity detection","zh":"使用 Amazon Comprehend 毒性偵測"},
      "C":{"en":"Use Amazon SageMaker built-in algorithms to train the model","zh":"使用 Amazon SageMaker 內建演算法訓練模型"},
      "D":{"en":"Use Amazon Polly to monitor comments","zh":"使用 Amazon Polly 監控評論"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Rekognition 的審核功能用於圖片和影片中的不適當視覺內容，不是文字毒性分析工具。",
      "B":"✓ 正確 — Amazon Comprehend 提供預建的毒性偵測（Toxicity Detection）API，無需訓練任何模型，直接偵測文字中的有害語言（仇恨言論、騷擾等），完全符合「不使用標記資料訓練」的要求。",
      "C":"✗ SageMaker 內建演算法需要準備並標記訓練資料，違反了「不使用標記資料」的限制。",
      "D":"✗ Amazon Polly 是文字轉語音（TTS）服務，無法分析文字內容或偵測有害語言。"
    }
  },
  {
    "id":110,"exam":"AIF",
    "question":"A research company built a chatbot using an FM from Amazon Bedrock to search research papers. The FM is performing poorly because of complex scientific terms. How can the company improve performance?",
    "question_zh":"一家研究公司使用 Amazon Bedrock 的 FM 建立聊天機器人，用於搜尋研究論文，但因複雜科學術語而表現不佳。如何改善效能？",
    "options":{
      "A":{"en":"Use few-shot prompting to define how the FM can answer the questions","zh":"使用少量示例提示定義 FM 如何回答問題"},
      "B":{"en":"Use domain adaptation fine-tuning to adapt the FM to complex scientific terms","zh":"使用領域適應微調使 FM 適應複雜科學術語"},
      "C":{"en":"Change the FM inference parameters","zh":"更改 FM 推論參數"},
      "D":{"en":"Clean the research paper data to remove complex scientific terms","zh":"清理研究論文資料，移除複雜科學術語"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Few-shot prompting 提供幾個範例引導模型輸出格式，但無法讓模型真正理解它不認識的專業術語。",
      "B":"✓ 正確 — 領域適應微調（Domain Adaptation Fine-tuning）在特定領域語料（如科學論文）上繼續訓練 FM，使其內化專業術語的語義，從根本解決對複雜科學詞彙的理解不足問題。",
      "C":"✗ 推論參數（如 temperature、top-p）影響輸出的隨機性，不能提升模型對未知術語的理解能力。",
      "D":"✗ 移除複雜術語會破壞研究論文的核心內容，造成資訊損失，反而使搜尋品質更差。"
    }
  },
  {
    "id":111,"exam":"AIF",
    "question":"A company has developed custom computer vision models and needs a user-friendly interface for data labeling to minimize model mistakes on new real-world data. Which AWS service meets these requirements?",
    "question_zh":"一家公司已開發自訂電腦視覺模型，需要一個使用者友善的資料標記介面，以最小化模型在新真實世界資料上的錯誤。哪個 AWS 服務符合需求？",
    "options":{
      "A":{"en":"Amazon SageMaker Ground Truth","zh":"Amazon SageMaker Ground Truth"},
      "B":{"en":"Amazon SageMaker Canvas","zh":"Amazon SageMaker Canvas"},
      "C":{"en":"Amazon Bedrock playground","zh":"Amazon Bedrock 遊樂場"},
      "D":{"en":"Amazon Bedrock Agents","zh":"Amazon Bedrock Agents"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon SageMaker Ground Truth 提供資料標記的完整解決方案：圖形化標記介面（支援影像邊界框、語義分割等）、自動資料飛輪（Active Learning）讓模型持續從新資料學習，以及人工審核工作流程，完全符合電腦視覺資料標記需求。",
      "B":"✗ SageMaker Canvas 是無程式碼 ML 模型建置工具，不是資料標記平台。",
      "C":"✗ Bedrock Playground 是用於快速測試基礎模型提示的互動介面，不是資料標記工具。",
      "D":"✗ Bedrock Agents 用於建立多步驟 AI 代理，不是資料標記服務。"
    }
  },
  {
    "id":112,"exam":"AIF",
    "question":"Which strategy will determine if a foundation model (FM) effectively meets business objectives?",
    "question_zh":"哪種策略可以判斷基礎模型是否有效達成業務目標？",
    "options":{
      "A":{"en":"Evaluate the model's performance on benchmark datasets","zh":"在基準資料集上評估模型效能"},
      "B":{"en":"Analyze the model's architecture and hyperparameters","zh":"分析模型架構和超參數"},
      "C":{"en":"Assess the model's alignment with specific use cases","zh":"評估模型與特定使用案例的對齊程度"},
      "D":{"en":"Measure the computational resources required for model deployment","zh":"衡量模型部署所需的運算資源"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 基準資料集評估提供通用效能指標（如 MMLU、HumanEval），但不一定反映企業的具體業務場景表現。",
      "B":"✗ 分析架構和超參數是技術層面的理解，無法直接回答「是否達成業務目標」的問題。",
      "C":"✓ 正確 — 評估模型與特定業務使用案例的對齊程度——使用真實業務資料、業務指標（如客戶滿意度、任務完成率）評估——才是判斷 FM 是否真正達成業務目標的最直接方法。",
      "D":"✗ 運算資源衡量的是部署效率和成本，不是業務有效性。"
    }
  },
  {
    "id":113,"exam":"AIF",
    "question":"A company needs to choose a model from Amazon Bedrock for internal use. The company must identify a model that generates responses in a style that employees prefer. What should the company do?",
    "question_zh":"一家公司需要從 Amazon Bedrock 選擇一個內部使用的模型，必須找出能以員工偏好的風格生成回應的模型。公司應怎麼做？",
    "options":{
      "A":{"en":"Evaluate the models by using built-in prompt datasets","zh":"使用內建提示資料集評估模型"},
      "B":{"en":"Evaluate the models by using a human workforce and custom prompt datasets","zh":"使用人力工作隊和自訂提示資料集評估模型"},
      "C":{"en":"Use public model leaderboards to identify the model","zh":"使用公開模型排行榜識別模型"},
      "D":{"en":"Use the model InvocationLatency runtime metrics in Amazon CloudWatch","zh":"在 Amazon CloudWatch 中使用模型調用延遲執行時間指標"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 內建提示資料集是通用評估集，不反映公司員工的具體使用場景和偏好風格。",
      "B":"✓ 正確 — 讓員工（人力工作隊）使用公司實際工作場景的自訂提示對多個模型進行評估，直接衡量員工對不同模型回應風格的偏好，是最準確的選擇依據。",
      "C":"✗ 公開排行榜根據標準基準評分，不代表員工的主觀偏好或公司特定使用案例的表現。",
      "D":"✗ InvocationLatency 衡量回應速度，不衡量回應品質或員工偏好的風格。"
    }
  },
  {
    "id":114,"exam":"AIF",
    "question":"A company wants to develop an LLM application using Amazon Bedrock and customer data uploaded to Amazon S3. The company's security policy states that each team can access data for only their own customers. Which solution meets these requirements?",
    "question_zh":"一家公司想使用 Amazon Bedrock 和 S3 上的客戶資料開發 LLM 應用，安全政策規定每個團隊只能存取自己客戶的資料。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Create an Amazon Bedrock custom service role for each team that has access to only the team's customer data","zh":"為每個團隊建立只能存取該團隊客戶資料的 Amazon Bedrock 自訂服務角色"},
      "B":{"en":"Create a custom service role with Amazon S3 access. Ask teams to specify the customer name on each Bedrock request","zh":"建立有 S3 存取權限的自訂服務角色，請團隊在每個 Bedrock 請求中指定客戶名稱"},
      "C":{"en":"Redact personal data in Amazon S3. Update the S3 bucket policy to allow team access to customer data","zh":"在 S3 中編輯個人資料，更新 S3 儲存貯體政策允許團隊存取客戶資料"},
      "D":{"en":"Create one Amazon Bedrock role with full S3 access. Create IAM roles for each team that have access to only each team's customer folders","zh":"建立一個具有完整 S3 存取權限的 Bedrock 角色，為每個團隊建立只能存取該團隊客戶資料夾的 IAM 角色"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 為每個團隊建立獨立的 Bedrock 服務角色，每個角色的 IAM 政策限制只能存取對應的 S3 路徑，實作最小權限原則，確保各團隊資料的嚴格隔離。",
      "B":"✗ 依賴請求者「自行指定」客戶名稱是不安全的設計——任何人都可以指定其他客戶的名稱，沒有真正的存取控制。",
      "C":"✗ 編輯個人資料會破壞資料的可用性；S3 儲存貯體政策可以限制存取，但此選項描述不夠精確，且與 A 相比不是最佳做法。",
      "D":"✗ Bedrock 角色具有完整 S3 存取權限違反最小權限原則；即使 IAM 角色限制了人員存取，底層 Bedrock 調用仍有過高的 S3 存取範圍。"
    }
  },
  {
    "id":115,"exam":"AIF",
    "question":"Which ML technique ensures data compliance and privacy when training AI models on AWS?",
    "question_zh":"哪種 ML 技術在 AWS 上訓練 AI 模型時確保資料合規和隱私？",
    "options":{
      "A":{"en":"Reinforcement learning","zh":"強化學習"},
      "B":{"en":"Transfer learning","zh":"遷移學習"},
      "C":{"en":"Federated learning","zh":"聯邦學習"},
      "D":{"en":"Unsupervised learning","zh":"非監督式學習"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 強化學習透過獎懲機制訓練代理，與資料隱私保護無直接關係。",
      "B":"✗ 遷移學習將預訓練模型的知識應用到新任務，是效率優化策略，不專注於資料隱私。",
      "C":"✓ 正確 — 聯邦學習（Federated Learning）允許多個客戶端在本地資料上訓練模型，只將模型更新（梯度）而非原始資料傳送到中央伺服器，確保敏感資料永不離開本地環境，是隱私保護 ML 的核心技術。",
      "D":"✗ 非監督式學習發現資料中的隱藏模式，不是隱私保護的訓練方法。"
    }
  },
]
