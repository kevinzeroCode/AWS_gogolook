
AIF_BATCH3 = [
  {
    "id":144,"exam":"AIF",
    "question":"Which option is a use case for generative AI models?",
    "question_zh":"哪個選項是生成式 AI 模型的使用案例？",
    "options":{
      "A":{"en":"Improving network security by using intrusion detection systems","zh":"使用入侵偵測系統改善網路安全"},
      "B":{"en":"Creating photorealistic images from text descriptions for digital marketing","zh":"從文字描述為數位行銷建立逼真圖像"},
      "C":{"en":"Enhancing database performance by using optimized indexing","zh":"使用最佳化索引提升資料庫效能"},
      "D":{"en":"Analyzing financial data to forecast stock market trends","zh":"分析財務資料以預測股市趨勢"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 入侵偵測系統是判別式 ML 的應用（分類：正常/惡意流量），不是生成式 AI。",
      "B":"✓ 正確 — 從文字描述生成圖像（Text-to-Image）是生成式 AI 的核心能力，如 Stable Diffusion、DALL·E、Amazon Titan Image Generator，廣泛用於數位行銷素材製作。",
      "C":"✗ 資料庫索引最佳化是傳統資料庫工程技術，不需要生成式 AI。",
      "D":"✗ 股市趨勢預測是預測式 ML（迴歸/時間序列分析），不是生成式 AI。"
    }
  },
  {
    "id":145,"exam":"AIF",
    "question":"A company wants to use large language models (LLMs) to produce code from natural language code comments. Which LLM feature meets these requirements?",
    "question_zh":"一家公司想使用 LLM 從自然語言程式碼注解產生程式碼。哪個 LLM 功能符合需求？",
    "options":{
      "A":{"en":"Text summarization","zh":"文字摘要"},
      "B":{"en":"Text generation","zh":"文字生成"},
      "C":{"en":"Text completion","zh":"文字補全"},
      "D":{"en":"Text classification","zh":"文字分類"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 文字摘要是將長文字壓縮為短摘要，不是從注解生成程式碼。",
      "B":"✓ 正確 — 文字生成是 LLM 根據輸入（自然語言注解）產生全新內容（程式碼）的能力。從描述生成程式碼是文字生成任務，Amazon CodeWhisperer 和 GitHub Copilot 都基於此能力。",
      "C":"✗ 文字補全是在現有文字後繼續撰寫，而程式碼生成是從自然語言「轉換」成全新程式碼，更準確地屬於文字生成。",
      "D":"✗ 文字分類將文字歸類到預定義類別，不產生新的程式碼內容。"
    }
  },
  {
    "id":146,"exam":"AIF",
    "question":"An AI practitioner wants to design a search application that must handle queries containing both text and images. Which type of FM should be used to power this search application?",
    "question_zh":"AI 從業者想設計一個必須處理包含文字和圖片查詢的搜尋應用程式。應使用哪種類型的 FM？",
    "options":{
      "A":{"en":"Multi-modal embedding model","zh":"多模態嵌入模型"},
      "B":{"en":"Text embedding model","zh":"文字嵌入模型"},
      "C":{"en":"Multi-modal generation model","zh":"多模態生成模型"},
      "D":{"en":"Image generation model","zh":"圖像生成模型"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 多模態嵌入模型將文字和圖像都轉換為同一向量空間中的向量，使得文字查詢可以找到語義相關的圖像（或反之）。這是多模態搜尋的核心，如 Amazon Titan Multimodal Embeddings。",
      "B":"✗ 文字嵌入模型只能處理文字輸入，無法處理圖像查詢。",
      "C":"✗ 多模態生成模型用於生成內容（如根據文字生成圖像），不是搜尋/檢索用途。",
      "D":"✗ 圖像生成模型從文字描述生成圖像，不用於搜尋應用。"
    }
  },
  {
    "id":147,"exam":"AIF",
    "question":"What are tokens in the context of generative AI models?",
    "question_zh":"在生成式 AI 模型的上下文中，Token 是什麼？",
    "options":{
      "A":{"en":"Tokens are the basic units of input and output that a generative AI model operates on, representing words, subwords, or other linguistic units","zh":"Token 是生成式 AI 模型操作的輸入和輸出基本單位，代表詞語、子詞或其他語言單位"},
      "B":{"en":"Tokens are the mathematical representations of words or concepts used in generative AI models","zh":"Token 是生成式 AI 模型中使用的詞語或概念的數學表示"},
      "C":{"en":"Tokens are the pre-trained weights of a generative AI model that are fine-tuned for specific tasks","zh":"Token 是針對特定任務微調的生成式 AI 模型預訓練權重"},
      "D":{"en":"Tokens are the specific prompts or instructions given to a generative AI model to generate output","zh":"Token 是給予生成式 AI 模型以產生輸出的特定提示或指令"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Token 是 LLM 處理文字的基本單位：一個 token 大約等於 0.75 個英文單詞或 4 個字元。一個詞語可能被分成多個 token（如 \"tokenization\" = [\"token\",\"ization\"]）。模型的計費、上下文視窗限制都以 token 計算。",
      "B":"✗ 這描述的是 Embedding（嵌入向量），不是 Token。Token 是文字分割單位，Embedding 才是數學表示。",
      "C":"✗ 這描述的是模型權重（Weights），不是 Token。",
      "D":"✗ 這描述的是提示（Prompt）的概念，不是 Token 的定義。"
    }
  },
  {
    "id":148,"exam":"AIF",
    "question":"What is the purpose of vector embeddings in a large language model (LLM)?",
    "question_zh":"向量嵌入在大型語言模型 (LLM) 中的目的是什麼？",
    "options":{
      "A":{"en":"Splitting text into manageable pieces of data","zh":"將文字拆分為可管理的資料片段"},
      "B":{"en":"Grouping a set of characters to be treated as a single unit","zh":"將一組字元分組視為單一單位"},
      "C":{"en":"Providing the ability to mathematically compare texts","zh":"提供數學比較文字的能力"},
      "D":{"en":"Providing the count of every word in the input","zh":"提供輸入中每個單字的計數"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 這描述的是 Tokenization（分詞），不是向量嵌入。",
      "B":"✗ 這是 Token 的定義（將字元組合為語言單位），不是向量嵌入的目的。",
      "C":"✓ 正確 — 向量嵌入將文字轉換為數值向量後，可以用餘弦相似度等數學方法比較兩段文字的語義相似程度，是語義搜尋、RAG 檢索和推薦系統的基礎。相似語義的文字在向量空間中距離更近。",
      "D":"✗ 統計詞頻是 Bag-of-Words（詞袋模型）的概念，不是向量嵌入的目的。"
    }
  },
  {
    "id":149,"exam":"AIF",
    "question":"Which statement correctly describes embeddings in generative AI?",
    "question_zh":"哪個陳述正確描述了生成式 AI 中的嵌入（Embeddings）？",
    "options":{
      "A":{"en":"Embeddings represent data as high-dimensional vectors that capture semantic relationships","zh":"嵌入將資料表示為高維向量，捕捉語義關係"},
      "B":{"en":"Embeddings is a technique that searches data to find the most helpful information to answer natural language questions","zh":"嵌入是搜尋資料以找到最有用資訊來回答自然語言問題的技術"},
      "C":{"en":"Embeddings reduce hardware requirements by using a less precise data type for weights and activations","zh":"嵌入透過對權重和激活使用較低精度資料類型來降低硬體需求"},
      "D":{"en":"Embeddings provide the ability to store and retrieve data for generative AI applications","zh":"嵌入提供了為生成式 AI 應用程式儲存和擷取資料的能力"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 嵌入（Embeddings）將詞語、句子或文件轉換為高維度數值向量，語義相似的概念在向量空間中距離更近，這讓模型能理解和比較語義關係。",
      "B":"✗ 這描述的是 RAG（檢索增強生成）或語義搜尋，不是嵌入本身的定義。",
      "C":"✗ 這描述的是量化（Quantization）技術，如將 FP32 改為 INT8，降低硬體需求，與嵌入無關。",
      "D":"✗ 這描述的是向量資料庫（Vector Database）的功能，嵌入是轉換機制，向量資料庫才是儲存和檢索的系統。"
    }
  },
  {
    "id":150,"exam":"AIF",
    "question":"What is tokenization used for in natural language processing (NLP)?",
    "question_zh":"在自然語言處理 (NLP) 中，分詞（Tokenization）用於什麼？",
    "options":{
      "A":{"en":"To encrypt text data","zh":"加密文字資料"},
      "B":{"en":"To compress text files","zh":"壓縮文字檔案"},
      "C":{"en":"To break text into smaller units for processing","zh":"將文字分解為較小單位以進行處理"},
      "D":{"en":"To translate text between languages","zh":"在語言之間翻譯文字"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 文字加密是資安技術，與 NLP 分詞無關。",
      "B":"✗ 文字壓縮（如 gzip）是資料工程技術，不是 NLP 分詞的目的。",
      "C":"✓ 正確 — Tokenization 將原始文字分割為 token（詞、子詞或字元），是所有 NLP 模型的第一個處理步驟，讓模型可以對這些基本單位進行數學運算。",
      "D":"✗ 語言翻譯是 Amazon Translate 等服務的功能，不是分詞的用途。"
    }
  },
  {
    "id":151,"exam":"AIF",
    "question":"Which option is a characteristic of transformer-based language models?",
    "question_zh":"哪個選項是 Transformer 語言模型的特性？",
    "options":{
      "A":{"en":"Transformer-based language models use convolutional layers to apply filters across an input to capture local patterns","zh":"Transformer 語言模型使用卷積層在輸入上套用過濾器以捕捉局部模式"},
      "B":{"en":"Transformer-based language models can process only text data","zh":"Transformer 語言模型只能處理文字資料"},
      "C":{"en":"Transformer-based language models use self-attention mechanisms to capture contextual relationships","zh":"Transformer 語言模型使用自注意力機制捕捉上下文關係"},
      "D":{"en":"Transformer-based language models process data sequences one element at a time in cyclic iterations","zh":"Transformer 語言模型以循環迭代方式每次處理資料序列中的一個元素"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 這描述的是卷積神經網路（CNN）的特性，CNN 用局部過濾器提取特徵，不是 Transformer 的運作方式。",
      "B":"✗ Transformer 架構已擴展到多模態（圖像、音訊、影片），如 Vision Transformer（ViT）可處理圖像，不僅限於文字。",
      "C":"✓ 正確 — 自注意力機制（Self-Attention）是 Transformer 的核心創新，讓模型在處理每個 token 時能同時關注序列中所有其他 token，捕捉長距離依賴關係（如代名詞指代），是 LLM 優於 RNN 的關鍵。",
      "D":"✗ 這描述的是循環神經網路（RNN）的特性，RNN 按時間步驟順序處理，Transformer 可平行處理整個序列。"
    }
  },
  {
    "id":152,"exam":"AIF",
    "question":"Which option describes embeddings in the context of AI?",
    "question_zh":"哪個選項描述了 AI 上下文中的嵌入（Embeddings）？",
    "options":{
      "A":{"en":"A method for compressing large datasets","zh":"壓縮大型資料集的方法"},
      "B":{"en":"An encryption method for securing sensitive data","zh":"保護敏感資料的加密方法"},
      "C":{"en":"A method for visualizing high-dimensional data","zh":"視覺化高維資料的方法"},
      "D":{"en":"A numerical method for data representation in a reduced dimensionality space","zh":"在降維空間中進行資料表示的數值方法"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 嵌入是語義表示技術，不是資料壓縮技術（雖然降維有一定壓縮效果，但目的不同）。",
      "B":"✗ 嵌入與加密完全無關，嵌入向量不隱藏資訊，只轉換表示形式。",
      "C":"✗ t-SNE、PCA 是用於視覺化高維資料的技術，嵌入的主要目的是語義表示，不是視覺化。",
      "D":"✓ 正確 — 嵌入是將高維稀疏資料（如 one-hot 編碼的詞彙表）轉換為低維稠密的數值向量（降維空間）的方法，在保留語義關係的同時大幅減少維度。"
    }
  },
  {
    "id":153,"exam":"AIF",
    "question":"A company has terabytes of data and wants to build an AI-based application to generate SQL queries from input text. The employees have minimal technology experience. Which solution meets these requirements?",
    "question_zh":"一家公司有 TB 級資料，想建立 AI 應用程式從輸入文字生成 SQL 查詢，且員工技術經驗有限。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Generative pre-trained transformers (GPT)","zh":"生成式預訓練 Transformer (GPT)"},
      "B":{"en":"Residual neural network","zh":"殘差神經網路"},
      "C":{"en":"Support vector machine","zh":"支援向量機 (SVM)"},
      "D":{"en":"WaveNet","zh":"WaveNet"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — GPT 類型的生成式預訓練 Transformer 具備強大的自然語言理解和程式碼生成能力，可將自然語言描述（如「顯示過去30天的銷售額」）轉換為正確的 SQL 查詢，讓非技術員工也能查詢資料庫。",
      "B":"✗ 殘差神經網路（ResNet）主要用於電腦視覺任務，不適合文字到 SQL 的轉換。",
      "C":"✗ SVM 是分類演算法，不能生成 SQL 查詢或處理自然語言輸入。",
      "D":"✗ WaveNet 是音訊波形生成模型，不適合文字到 SQL 的轉換任務。"
    }
  },
  {
    "id":154,"exam":"AIF",
    "question":"A company's large language model (LLM) is experiencing hallucinations. How can the company decrease hallucinations?",
    "question_zh":"一家公司的 LLM 發生幻覺（Hallucination）。公司如何降低幻覺？",
    "options":{
      "A":{"en":"Set up Agents for Amazon Bedrock to supervise the model training","zh":"設定 Amazon Bedrock Agents 監督模型訓練"},
      "B":{"en":"Use data pre-processing and remove any data that causes hallucinations","zh":"使用資料預處理並移除導致幻覺的資料"},
      "C":{"en":"Decrease the temperature inference parameter for the model","zh":"降低模型的溫度推論參數"},
      "D":{"en":"Use a foundation model (FM) that is trained to not hallucinate","zh":"使用訓練為不產生幻覺的基礎模型"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Bedrock Agents 用於建立多步驟 AI 工作流程，不是控制模型幻覺的工具。",
      "B":"✗ 無法在預處理階段識別並移除「導致幻覺的資料」，幻覺是模型推論行為，不是特定訓練資料的直接結果。",
      "C":"✓ 正確 — 降低溫度（Temperature）使模型輸出更確定性（less random），選擇機率最高的詞語，減少模型「創造」不存在事實的傾向。低溫度讓模型更保守、更貼近已知知識，是降低幻覺最直接的推論參數調整。",
      "D":"✗ 目前沒有任何 FM 能完全保證不產生幻覺；這個選項在技術上不可行。"
    }
  },
  {
    "id":155,"exam":"AIF",
    "question":"An ecommerce company is using a generative AI chatbot to respond to customer inquiries. The company wants to measure the financial effect of the chatbot on its operations. Which metric should the company use?",
    "question_zh":"一家電商公司使用生成式 AI 聊天機器人回應客戶詢問，想衡量聊天機器人對其營運的財務影響。應使用哪個指標？",
    "options":{
      "A":{"en":"Number of customer inquiries handled","zh":"處理的客戶詢問數量"},
      "B":{"en":"Cost of training AI models","zh":"AI 模型的訓練成本"},
      "C":{"en":"Cost for each customer conversation","zh":"每次客戶對話的成本"},
      "D":{"en":"Average handled time (AHT)","zh":"平均處理時間 (AHT)"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 詢問數量是服務量指標，不是財務影響指標（數量多但成本也高不代表有財務效益）。",
      "B":"✗ 訓練成本是一次性沉沒成本，不反映日常營運的財務影響。",
      "C":"✓ 正確 — 每次對話成本（AI 成本 vs 人工成本）直接量化 AI 聊天機器人的財務效益：與人工客服相比節省多少成本，是衡量 AI 投資報酬率（ROI）的核心財務指標。",
      "D":"✗ AHT（平均處理時間）是效率指標，可間接影響成本，但不是直接的財務影響衡量指標。"
    }
  },
  {
    "id":156,"exam":"AIF",
    "question":"A software company wants to use AI to increase software development productivity. Which solution will meet these requirements?",
    "question_zh":"一家軟體公司想使用 AI 提升軟體開發生產力。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Use a binary classification model to generate code reviews","zh":"使用二元分類模型生成程式碼審查"},
      "B":{"en":"Install code recommendation software in the company's developer tools","zh":"在公司開發者工具中安裝程式碼推薦軟體"},
      "C":{"en":"Install a code forecasting tool to predict potential code issues","zh":"安裝程式碼預測工具來預測潛在程式碼問題"},
      "D":{"en":"Use a natural language processing (NLP) tool to generate code","zh":"使用自然語言處理 (NLP) 工具生成程式碼"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 二元分類模型不能生成有意義的程式碼審查，程式碼審查需要理解語意和上下文。",
      "B":"✓ 正確 — 程式碼推薦軟體（如 Amazon Q Developer / CodeWhisperer）整合在 IDE 中，即時推薦程式碼片段、自動補全函數，直接在開發者工作流程中提升生產力。",
      "C":"✗ 程式碼預測問題（如靜態分析工具）雖有幫助，但不是提升「生產力」最直接的方式。",
      "D":"✗ NLP 工具生成程式碼的描述太過籠統，且 B 選項（程式碼推薦）是更具體且更符合「安裝在開發工具中即用」的解決方案。"
    }
  },
  {
    "id":157,"exam":"AIF",
    "question":"A company wants to assess costs associated with using an LLM on Amazon Bedrock to generate inferences. Which factor will drive the inference costs?",
    "question_zh":"一家公司想評估使用 Amazon Bedrock 上的 LLM 生成推論的相關成本。哪個因素會驅動推論成本？",
    "options":{
      "A":{"en":"Number of tokens consumed","zh":"消耗的 token 數量"},
      "B":{"en":"Temperature value","zh":"溫度值"},
      "C":{"en":"Amount of data used to train the LLM","zh":"訓練 LLM 所用的資料量"},
      "D":{"en":"Total training time","zh":"總訓練時間"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon Bedrock 的推論（Inference）費用是按 token 計費：輸入 token 數量 + 輸出 token 數量。Prompt 越長、回應越詳細，消耗的 token 越多，成本越高。",
      "B":"✗ 溫度值影響輸出的隨機性，不影響帳單費用。",
      "C":"✗ 訓練資料量是訓練成本的因素；推論費用與訓練資料量無關。",
      "D":"✗ 訓練時間是訓練成本的因素；推論費用按 token 計算，與訓練時間無關。"
    }
  },
  {
    "id":158,"exam":"AIF",
    "question":"An AI practitioner is using an LLM to create marketing campaign content. The generated content sounds plausible and factual but is actually incorrect. Which problem is the LLM having?",
    "question_zh":"AI 從業者使用 LLM 建立行銷活動內容，生成的內容聽起來似乎合理且真實，但實際上是錯誤的。LLM 遇到了哪個問題？",
    "options":{
      "A":{"en":"Data leakage","zh":"資料洩漏"},
      "B":{"en":"Hallucination","zh":"幻覺 (Hallucination)"},
      "C":{"en":"Overfitting","zh":"過擬合 (Overfitting)"},
      "D":{"en":"Underfitting","zh":"欠擬合 (Underfitting)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 資料洩漏是指訓練過程中使用了不應使用的資料（如測試資料），或模型在輸出中洩露了敏感訓練資料，與生成看似合理但錯誤的內容不同。",
      "B":"✓ 正確 — LLM 幻覺（Hallucination）是指模型自信地生成聽起來合理但實際上不正確或無事實依據的內容。這是 LLM 的典型問題，特別在涉及具體事實、數據或引用時最危險。",
      "C":"✗ 過擬合是指模型在訓練資料上表現好但在新資料上表現差，不是描述生成錯誤內容的問題。",
      "D":"✗ 欠擬合是指模型過於簡單，連訓練資料都無法很好地學習，不是幻覺問題。"
    }
  },
  {
    "id":159,"exam":"AIF",
    "question":"Which strategy evaluates the accuracy of a foundation model (FM) used in image classification tasks?",
    "question_zh":"哪種策略可以評估用於圖像分類任務的基礎模型 (FM) 的準確率？",
    "options":{
      "A":{"en":"Calculate the total cost of resources used by the model","zh":"計算模型使用的資源總成本"},
      "B":{"en":"Measure the model's accuracy against a predefined benchmark dataset","zh":"根據預定義的基準資料集衡量模型準確率"},
      "C":{"en":"Count the number of layers in the neural network","zh":"計算神經網路的層數"},
      "D":{"en":"Assess the color accuracy of images processed by the model","zh":"評估模型處理的圖像的色彩準確率"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 資源成本衡量的是效率，不是準確率。",
      "B":"✓ 正確 — 使用標準化基準資料集（如 ImageNet 的 Top-1/Top-5 準確率）評估模型，是業界標準的模型準確率評估方法，允許不同模型間的客觀比較。",
      "C":"✗ 網路層數是架構特性，不等同於模型準確率（更深不代表更準確）。",
      "D":"✗ 色彩準確率是影像品質指標，與圖像分類的語義準確率無關。"
    }
  },
  {
    "id":160,"exam":"AIF",
    "question":"An education company is building an application where users can enter text or provide a picture of a question. The application responds with a written answer and an explanation. Which model type meets these requirements?",
    "question_zh":"一家教育公司正在建立一個應用程式，使用者可以輸入文字或提供問題的圖片，應用程式以書面答案和說明回應。哪種模型類型符合需求？",
    "options":{
      "A":{"en":"Computer vision model","zh":"電腦視覺模型"},
      "B":{"en":"Large multi-modal language model","zh":"大型多模態語言模型"},
      "C":{"en":"Diffusion model","zh":"擴散模型"},
      "D":{"en":"Text-to-speech model","zh":"文字轉語音模型"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 電腦視覺模型可識別圖像內容，但無法生成文字答案和說明。",
      "B":"✓ 正確 — 大型多模態語言模型（如 Claude 3、GPT-4V）可接受文字和圖像輸入，並生成文字輸出，完全符合「文字或圖片輸入 → 文字答案和說明輸出」的需求。",
      "C":"✗ 擴散模型（Diffusion Model）用於生成圖像（如 Stable Diffusion），不適合回答問題。",
      "D":"✗ 文字轉語音模型將文字轉為音訊，不處理圖像輸入也不生成文字答案。"
    }
  },
  {
    "id":161,"exam":"AIF",
    "question":"A financial company is using ML to help with some of the company's tasks. Which option is a use of generative AI models?",
    "question_zh":"一家金融公司使用 ML 協助公司的部分任務。哪個選項是生成式 AI 模型的使用？",
    "options":{
      "A":{"en":"Summarizing customer complaints","zh":"摘要客戶投訴"},
      "B":{"en":"Classifying customers based on product usage","zh":"根據產品使用情況對客戶進行分類"},
      "C":{"en":"Segmenting customers based on type of investments","zh":"根據投資類型對客戶進行細分"},
      "D":{"en":"Forecasting revenue for certain products","zh":"預測特定產品的收入"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 摘要（Summarization）是生成式 AI 的核心能力，LLM 理解客戶投訴文字後生成簡潔摘要，這是「生成新內容」的行為，屬於生成式 AI。",
      "B":"✗ 客戶分類是判別式 ML（分類算法），預測現有類別，不是生成新內容。",
      "C":"✗ 客戶分群是非監督式學習（分群算法），不是生成式 AI。",
      "D":"✗ 收入預測是預測式 ML（迴歸/時間序列），不是生成式 AI。"
    }
  },
  {
    "id":162,"exam":"AIF",
    "question":"A manufacturing company has an application that ingests consumer complaints and uses complex hard-coded logic to process them. The company wants to scale this logic across markets and product lines. Which advantage do generative AI models offer?",
    "question_zh":"一家製造公司的應用程式接收消費者投訴並使用複雜的硬編碼邏輯處理，想將此邏輯擴展到各市場和產品線。生成式 AI 模型提供哪個優勢？",
    "options":{
      "A":{"en":"Predictability of outputs","zh":"輸出的可預測性"},
      "B":{"en":"Adaptability","zh":"適應性 (Adaptability)"},
      "C":{"en":"Less sensitivity to changes in inputs","zh":"對輸入變化的敏感度較低"},
      "D":{"en":"Explainability","zh":"可解釋性 (Explainability)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 生成式 AI 的輸出具有一定隨機性（溫度影響），可預測性比硬編碼邏輯更低，不是其優勢。",
      "B":"✓ 正確 — 生成式 AI 的核心優勢是適應性：它能理解各種語言、格式和表達方式，無需為每個新市場或產品線修改程式碼。LLM 可自動適應不同語言、文化語境和產品術語，比硬編碼規則更靈活可擴展。",
      "C":"✗ 事實上，生成式 AI 對輸入變化（措辭、格式）更敏感，不同的表達方式可能給出不同輸出。",
      "D":"✗ 生成式 AI 通常比硬編碼邏輯可解釋性更低，不是此場景的主要優勢。"
    }
  },
  {
    "id":163,"exam":"AIF",
    "question":"A law firm wants to build an AI application that will read legal documents and extract key points from the documents. Which solution meets these requirements?",
    "question_zh":"一家律師事務所想建立 AI 應用程式，讀取法律文件並提取關鍵要點。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Build an automatic named entity recognition system","zh":"建立自動命名實體識別系統"},
      "B":{"en":"Create a recommendation engine","zh":"建立推薦引擎"},
      "C":{"en":"Develop a summarization chatbot","zh":"開發摘要聊天機器人"},
      "D":{"en":"Develop a multi-language translation system","zh":"開發多語言翻譯系統"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 命名實體識別（NER）提取人名、地點、組織等實體，功能較窄，無法全面提取法律文件的「關鍵要點」。",
      "B":"✗ 推薦引擎根據使用者偏好推薦內容，不用於文件摘要或要點提取。",
      "C":"✓ 正確 — 摘要聊天機器人（基於 LLM）可理解法律文件的複雜語義，提取關鍵論點、條款、義務等要點，並以簡潔格式呈現，是法律文件關鍵要點提取的最佳解決方案。",
      "D":"✗ 多語言翻譯解決語言障礙，不用於提取文件關鍵要點。"
    }
  },
  {
    "id":164,"exam":"AIF",
    "question":"A medical company is customizing a foundation model (FM) for diagnostic purposes. The company needs the model to be transparent and explainable to meet regulatory requirements. Which solution will meet these requirements?",
    "question_zh":"一家醫療公司正在自訂用於診斷目的的基礎模型，需要模型具有透明度和可解釋性以符合法規要求。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Configure security and compliance by using Amazon Inspector","zh":"使用 Amazon Inspector 配置安全性和合規性"},
      "B":{"en":"Generate simple metrics, reports, and examples by using Amazon SageMaker Clarify","zh":"使用 Amazon SageMaker Clarify 生成簡單指標、報告和範例"},
      "C":{"en":"Encrypt and secure training data by using Amazon Macie","zh":"使用 Amazon Macie 加密和保護訓練資料"},
      "D":{"en":"Gather more data and use Amazon Rekognition to add custom labels","zh":"收集更多資料並使用 Amazon Rekognition 添加自訂標籤"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Inspector 掃描 EC2 和容器的安全漏洞，與 AI 模型的透明度和可解釋性無關。",
      "B":"✓ 正確 — Amazon SageMaker Clarify 專門用於 AI 可解釋性和偏見偵測，可生成特徵重要性報告、偏差指標和決策說明，直接符合醫療法規對模型透明度和可解釋性的要求。",
      "C":"✗ Amazon Macie 使用 ML 識別和保護 S3 中的敏感資料（PII），不提供模型解釋功能。",
      "D":"✗ Rekognition 自訂標籤是電腦視覺標記工具，不是模型透明度解決方案。"
    }
  },
  {
    "id":165,"exam":"AIF",
    "question":"A company has documents with missing words due to a database error. The company wants an ML model that can suggest potential words to fill in the missing text. Which type of model meets this requirement?",
    "question_zh":"一家公司的文件因資料庫錯誤而遺失部分詞語，想要能建議潛在詞語填補遺失文字的 ML 模型。哪種類型的模型符合需求？",
    "options":{
      "A":{"en":"Topic modeling","zh":"主題建模"},
      "B":{"en":"Clustering models","zh":"分群模型"},
      "C":{"en":"Prescriptive ML models","zh":"規範性 ML 模型"},
      "D":{"en":"BERT-based models","zh":"基於 BERT 的模型"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 主題建模（如 LDA）識別文件中的主題分布，不用於填補遺失詞語。",
      "B":"✗ 分群模型將相似資料點聚集，不用於預測遺失詞語。",
      "C":"✗ 規範性 ML 提供最佳決策建議（如供應鏈優化），不是文字填補工具。",
      "D":"✓ 正確 — BERT（Bidirectional Encoder Representations from Transformers）是遮蔽語言模型（Masked Language Model），訓練方式就是預測文字中被遮蔽（遺失）的詞語，天然適合遺失詞語預測（Cloze task / 填空任務）。"
    }
  },
  {
    "id":166,"exam":"AIF",
    "question":"A company is making a chatbot using Amazon Lex and Amazon OpenSearch Service with private company data. The company needs to convert data into vector representation before storing it in a database. Which type of FM meets these requirements?",
    "question_zh":"一家公司使用 Amazon Lex 和 Amazon OpenSearch Service 建立聊天機器人，使用公司私有資料回答問題，需要在將資料儲存到資料庫之前將其轉換為向量表示。哪種類型的 FM 符合需求？",
    "options":{
      "A":{"en":"Text completion model","zh":"文字補全模型"},
      "B":{"en":"Instruction following model","zh":"指令遵循模型"},
      "C":{"en":"Text embeddings model","zh":"文字嵌入模型"},
      "D":{"en":"Image generation model","zh":"圖像生成模型"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 文字補全模型生成後續文字，不用於將資料轉換為向量表示。",
      "B":"✗ 指令遵循模型按照指令生成回應，不是向量化資料的工具。",
      "C":"✓ 正確 — 文字嵌入模型（Text Embeddings Model，如 Amazon Titan Text Embeddings）將文字轉換為高維向量，這些向量儲存在 OpenSearch 的向量索引中，供語義搜尋使用，是 RAG 架構的核心組件。",
      "D":"✗ 圖像生成模型生成圖像，不用於文字向量化。"
    }
  },
  {
    "id":167,"exam":"AIF",
    "question":"A data scientist has been running a SageMaker notebook instance for weeks. A new version of Jupyter Notebook and additional software updates have been released. The security team mandates use of the latest updates. How can the data scientist meet this requirement?",
    "question_zh":"資料科學家已執行 SageMaker 筆記本執行個體數週，新版 Jupyter Notebook 和軟體更新已發布，安全團隊要求使用最新更新。資料科學家如何滿足此需求？",
    "options":{
      "A":{"en":"Call the CreateNotebookInstanceLifecycleConfig API operation","zh":"呼叫 CreateNotebookInstanceLifecycleConfig API 操作"},
      "B":{"en":"Create a new SageMaker notebook instance and mount the Amazon EBS volume from the original instance","zh":"建立新的 SageMaker 筆記本執行個體並掛載原始執行個體的 EBS 磁碟區"},
      "C":{"en":"Stop and then restart the SageMaker notebook instance","zh":"停止然後重新啟動 SageMaker 筆記本執行個體"},
      "D":{"en":"Call the UpdateNotebookInstanceLifecycleConfig API operation","zh":"呼叫 UpdateNotebookInstanceLifecycleConfig API 操作"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ CreateNotebookInstanceLifecycleConfig 建立新的生命週期配置腳本，用於啟動時的初始設置，不是更新現有執行個體的方法。",
      "B":"✗ 建立新執行個體並遷移 EBS 比停止重啟複雜得多，且不必要。",
      "C":"✓ 正確 — 停止並重新啟動 SageMaker 筆記本執行個體時，它會從最新的 Amazon Linux AMI 啟動，自動套用 AWS 提供的最新 Jupyter 和安全更新，是最簡單快速的更新方式。",
      "D":"✗ UpdateNotebookInstanceLifecycleConfig 更新現有生命週期配置，不會立即更新已運行的執行個體的軟體。"
    }
  },
  {
    "id":168,"exam":"AIF",
    "question":"A company wants to use Amazon Q Developer to increase developer productivity and software development. What can Amazon Q Developer do to help?",
    "question_zh":"一家公司想使用 Amazon Q Developer 提升開發人員生產力和軟體開發。Amazon Q Developer 可以做什麼來協助？",
    "options":{
      "A":{"en":"Create software snippets, reference tracking, and open source license tracking","zh":"建立程式碼片段、參考追蹤和開源授權追蹤"},
      "B":{"en":"Run an application without provisioning or managing servers","zh":"在不佈建或管理伺服器的情況下執行應用程式"},
      "C":{"en":"Enable voice commands for coding and providing natural language search","zh":"啟用語音指令進行程式碼撰寫和自然語言搜尋"},
      "D":{"en":"Convert audio files to text documents by using ML models","zh":"使用 ML 模型將音訊檔案轉換為文字文件"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon Q Developer（原 CodeWhisperer）提供：AI 程式碼建議和片段生成、引用追蹤（識別程式碼來源）、開源授權掃描（避免授權風險），是直接提升開發生產力的 AI 程式設計助手。",
      "B":"✗ 無伺服器執行是 AWS Lambda 的功能，不是 Amazon Q Developer 的能力。",
      "C":"✗ 語音程式碼和自然語言搜尋不是 Amazon Q Developer 的核心功能描述。",
      "D":"✗ 音訊轉文字是 Amazon Transcribe 的功能，不是 Q Developer。"
    }
  },
  {
    "id":169,"exam":"AIF",
    "question":"A company has developed an ML model for image classification and wants to deploy it so that a web application can use it without managing any underlying infrastructure. Which solution meets these requirements?",
    "question_zh":"一家公司已開發圖像分類 ML 模型，想部署該模型供 Web 應用程式使用，且不需管理任何底層基礎設施。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Use Amazon SageMaker Serverless Inference to deploy the model","zh":"使用 Amazon SageMaker 無伺服器推論部署模型"},
      "B":{"en":"Use Amazon CloudFront to deploy the model","zh":"使用 Amazon CloudFront 部署模型"},
      "C":{"en":"Use Amazon API Gateway to host the model and serve predictions","zh":"使用 Amazon API Gateway 託管模型並提供預測"},
      "D":{"en":"Use AWS Batch to host the model and serve predictions","zh":"使用 AWS Batch 託管模型並提供預測"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — SageMaker Serverless Inference 是真正的無伺服器 ML 推論端點，AWS 自動管理底層基礎設施（容量、擴展），只需部署模型即可，無需任何伺服器管理，按實際推論請求計費。",
      "B":"✗ CloudFront 是 CDN 服務，用於快取和分發靜態/動態內容，不能部署和執行 ML 模型。",
      "C":"✗ API Gateway 是 API 管理服務，可以作為端點，但 ML 模型推論本身需要運算資源（如 SageMaker），API Gateway 本身不執行推論。",
      "D":"✗ AWS Batch 用於批次工作處理，不是為即時 Web 推論請求設計的服務。"
    }
  },
  {
    "id":170,"exam":"AIF",
    "question":"A company needs to build its own LLM based on only its private data. The company is concerned about the environmental effect of the training process. Which Amazon EC2 instance type has the LEAST environmental effect when training LLMs?",
    "question_zh":"一家公司需要基於私有資料建立自己的 LLM，並關注訓練過程的環境影響。哪種 Amazon EC2 執行個體類型在訓練 LLM 時環境影響最小？",
    "options":{
      "A":{"en":"Amazon EC2 C series","zh":"Amazon EC2 C 系列（運算最佳化）"},
      "B":{"en":"Amazon EC2 G series","zh":"Amazon EC2 G 系列（GPU 推論）"},
      "C":{"en":"Amazon EC2 P series","zh":"Amazon EC2 P 系列（GPU 訓練）"},
      "D":{"en":"Amazon EC2 Trn series","zh":"Amazon EC2 Trn 系列（Trainium）"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ C 系列是 CPU 最佳化執行個體，用於計算密集工作負載，不適合 LLM 訓練，效率更低。",
      "B":"✗ G 系列（NVIDIA GPU）主要為 ML 推論最佳化，不是 LLM 訓練的最佳選擇。",
      "C":"✗ P 系列（NVIDIA GPU）雖然是標準 LLM 訓練選擇，但 Trainium 專用晶片的能源效率更高。",
      "D":"✓ 正確 — Amazon EC2 Trn 系列使用 AWS 自訂的 Trainium 晶片，專為 ML 訓練設計，相比同等級 GPU 執行個體具有更高的能源效率（更高的 TFLOPS/Watt），在相同訓練任務下消耗更少電力，環境影響最小。"
    }
  },
  {
    "id":171,"exam":"AIF",
    "question":"A company wants to fine-tune a foundation model (FM) using AWS services. The company needs to ensure its data stays private, safe, and secure in the source AWS Region. Which combination of steps will meet these requirements MOST cost-effectively? (Choose TWO)",
    "question_zh":"一家公司想使用 AWS 服務微調基礎模型，需要確保資料在源 AWS 區域保持私密、安全。哪些步驟組合最具成本效益地符合需求？（選2項）",
    "options":{
      "A":{"en":"Host the model on premises by using AWS Outposts","zh":"使用 AWS Outposts 在本地端託管模型"},
      "B":{"en":"Use the Amazon Bedrock API","zh":"使用 Amazon Bedrock API"},
      "C":{"en":"Use AWS PrivateLink and a VPC","zh":"使用 AWS PrivateLink 和 VPC"},
      "D":{"en":"Host the Amazon Bedrock API on premises","zh":"在本地端託管 Amazon Bedrock API"},
      "E":{"en":"Use Amazon CloudWatch logs and metrics","zh":"使用 Amazon CloudWatch 日誌和指標"}
    },
    "correct":["B","C"],"multi":True,
    "explanations":{
      "A":"✗ AWS Outposts 將 AWS 服務延伸到本地端，成本非常高昂，不符合「最具成本效益」的要求。",
      "B":"✓ 正確 — Amazon Bedrock API 在 AWS 管理的基礎設施上執行微調，資料不離開 AWS，且 AWS 承諾不使用客戶資料訓練基礎模型，確保資料私密性，且是 Bedrock 標準定價，成本合理。",
      "C":"✓ 正確 — AWS PrivateLink 允許 VPC 與 Bedrock API 之間的私有連線，網路流量不經過公共網際網路，確保資料在傳輸過程中保持在 AWS 的私有網路內，符合資料留在源區域的要求。",
      "D":"✗ Bedrock 是雲端服務，無法在本地端託管，此選項不可行。",
      "E":"✗ CloudWatch 是監控服務，不提供資料隱私保護能力。"
    }
  },
  {
    "id":172,"exam":"AIF",
    "question":"A medical company wants to develop an AI application that can access structured patient records, extract relevant information, and generate concise summaries. Which solution meets these requirements?",
    "question_zh":"一家醫療公司想開發 AI 應用程式，可存取結構化患者記錄、提取相關資訊並生成簡潔摘要。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Use Amazon Comprehend Medical to extract relevant medical entities and relationships. Apply rule-based logic to structure and format summaries","zh":"使用 Amazon Comprehend Medical 提取相關醫療實體和關係，套用規則邏輯來結構化和格式化摘要"},
      "B":{"en":"Use Amazon Personalize to analyze patient engagement patterns. Integrate with a general purpose text summarization tool","zh":"使用 Amazon Personalize 分析患者參與模式，與通用文字摘要工具整合"},
      "C":{"en":"Use Amazon Textract to convert scanned documents into digital text. Design a keyword extraction system to generate summaries","zh":"使用 Amazon Textract 將掃描文件轉換為數位文字，設計關鍵字提取系統生成摘要"},
      "D":{"en":"Implement Amazon Kendra to provide a searchable index for medical records. Use a template-based system to format summaries","zh":"實作 Amazon Kendra 為醫療記錄提供可搜尋索引，使用基於範本的系統格式化摘要"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon Comprehend Medical 專為醫療 NLP 設計，可從結構化患者記錄中提取醫療實體（診斷、藥物、症狀、關係），搭配規則邏輯生成格式化摘要，是醫療資料提取和摘要的最佳 AWS 服務。",
      "B":"✗ Amazon Personalize 是個人化推薦服務，不用於醫療記錄提取或摘要。",
      "C":"✗ Amazon Textract 用於掃描文件的 OCR，題目說明是「結構化」患者記錄，不需要 OCR 轉換。",
      "D":"✗ Amazon Kendra 是企業搜尋服務，範本化摘要無法靈活處理患者記錄的多樣性。"
    }
  },
  {
    "id":173,"exam":"AIF",
    "question":"Which AWS Organizations feature can be used to track charges across multiple accounts and report the combined cost?",
    "question_zh":"哪個 AWS Organizations 功能可用於追蹤多個帳號的費用並報告合計成本？",
    "options":{
      "A":{"en":"Service control policies (SCPs)","zh":"服務控制政策 (SCPs)"},
      "B":{"en":"Cost Explorer","zh":"Cost Explorer"},
      "C":{"en":"Consolidated billing","zh":"整合帳單 (Consolidated billing)"},
      "D":{"en":"AWS Identity and Access Management (IAM)","zh":"AWS IAM"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ SCPs 限制組織帳號可使用的 AWS 服務和操作，是許可控制工具，不是費用追蹤。",
      "B":"✗ Cost Explorer 視覺化和分析費用，但它是分析工具，整合帳單才是「跨帳號合計費用」的功能。",
      "C":"✓ 正確 — AWS Organizations 的整合帳單（Consolidated Billing）將所有成員帳號的費用合併到管理帳號的單一帳單，可追蹤每個帳號的費用並查看組織總成本，並享有批量使用折扣。",
      "D":"✗ IAM 管理身分與存取權限，與費用追蹤無關。"
    }
  },
  {
    "id":174,"exam":"AIF",
    "question":"A company has created a custom model by fine-tuning an existing LLM from Amazon Bedrock. The company wants to deploy the model and handle a steady rate of requests each minute. Which solution meets these requirements MOST cost-effectively?",
    "question_zh":"一家公司透過微調 Amazon Bedrock 的 LLM 建立了自訂模型，想部署模型並處理每分鐘穩定的請求速率。哪個解決方案最具成本效益？",
    "options":{
      "A":{"en":"Deploy the model by using an Amazon EC2 compute optimized instance","zh":"使用 Amazon EC2 運算最佳化執行個體部署模型"},
      "B":{"en":"Use the model with on-demand throughput on Amazon Bedrock","zh":"在 Amazon Bedrock 上以隨需吞吐量使用模型"},
      "C":{"en":"Store the model in Amazon S3 and host by using AWS Lambda","zh":"在 Amazon S3 儲存模型並使用 AWS Lambda 託管"},
      "D":{"en":"Purchase Provisioned Throughput for the model on Amazon Bedrock","zh":"在 Amazon Bedrock 上為模型購買佈建吞吐量"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ EC2 執行個體需要自行管理基礎設施、模型服務框架，且計算最佳化執行個體不是 LLM 推論的最佳選擇。",
      "B":"✗ 隨需吞吐量按每個 token 計費，適合不可預測的流量；對穩定的請求速率，隨需費率通常高於佈建吞吐量。",
      "C":"✗ S3 + Lambda 的組合無法有效處理大型 LLM 推論，Lambda 有記憶體和超時限制，不適合 LLM 部署。",
      "D":"✓ 正確 — Provisioned Throughput（佈建吞吐量）以模型單位（Model Units）按小時計費，提供穩定的推論容量保證。對每分鐘穩定請求量的場景，比隨需計費更具成本效益，且支援自訂微調模型的部署。"
    }
  },
  {
    "id":175,"exam":"AIF",
    "question":"Which option is a benefit of using infrastructure as code (IaC) in machine learning operations (MLOps)?",
    "question_zh":"在機器學習操作 (MLOps) 中使用基礎設施即程式碼 (IaC) 的哪個選項是其效益？",
    "options":{
      "A":{"en":"IaC eliminates the need for hyperparameter tuning","zh":"IaC 消除了超參數調整的需求"},
      "B":{"en":"IaC always provisions powerful compute instances, contributing to more accurate models","zh":"IaC 總是佈建強大的運算執行個體，有助於更準確的模型"},
      "C":{"en":"IaC streamlines the deployment of scalable and consistent ML workloads in cloud environments","zh":"IaC 簡化了在雲端環境中部署可擴展且一致的 ML 工作負載"},
      "D":{"en":"IaC minimizes overall expenses by deploying only low-cost instances","zh":"IaC 透過僅部署低成本執行個體來最小化整體費用"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ IaC 管理基礎設施定義，與模型的超參數調整完全無關。",
      "B":"✗ IaC 佈建的執行個體類型由程式碼定義，不會「總是」選擇最強大的，這會增加成本。",
      "C":"✓ 正確 — IaC（如 AWS CloudFormation、Terraform）讓 ML 管道的基礎設施以程式碼方式版本控制和重現，確保不同環境（開發/測試/生產）的一致性，支援自動化部署和水平擴展，是 MLOps 的核心最佳實踐。",
      "D":"✗ IaC 的目標是一致性和可重現性，不是限制使用低成本執行個體（可能影響訓練效能）。"
    }
  },
  {
    "id":176,"exam":"AIF",
    "question":"A hospital wants to use a generative AI solution with speech-to-text functionality to help improve employee skills in dictating clinical notes. Which AWS service meets these requirements?",
    "question_zh":"一家醫院想使用具有語音轉文字功能的生成式 AI 解決方案，協助提升員工口述臨床筆記的技能。哪個 AWS 服務符合需求？",
    "options":{
      "A":{"en":"Amazon Q Developer","zh":"Amazon Q Developer"},
      "B":{"en":"Amazon Polly","zh":"Amazon Polly"},
      "C":{"en":"Amazon Rekognition","zh":"Amazon Rekognition"},
      "D":{"en":"AWS HealthScribe","zh":"AWS HealthScribe"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Q Developer 是 AI 程式設計助手，不是醫療語音轉文字服務。",
      "B":"✗ Amazon Polly 是文字轉語音（TTS），功能方向相反，不是語音轉文字。",
      "C":"✗ Amazon Rekognition 分析圖像和影片，不處理音訊或臨床筆記。",
      "D":"✓ 正確 — AWS HealthScribe 是專為醫療場景設計的語音轉文字 + 生成式 AI 服務，可自動轉錄醫患對話、生成臨床筆記摘要，並識別醫療術語，完全符合醫院口述臨床筆記的需求。"
    }
  },
  {
    "id":177,"exam":"AIF",
    "question":"A company is developing an editorial assistant using generative AI. During pilot, usage is low and performance is not a concern. The company cannot predict usage after full deployment and wants to minimize costs. Which solution meets these requirements?",
    "question_zh":"一家公司正在開發使用生成式 AI 的編輯助手，試驗期間使用量低，效能不是顧慮。公司無法預測完全部署後的使用量，且想最小化成本。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Use GPU-powered Amazon EC2 instances","zh":"使用 GPU 驅動的 Amazon EC2 執行個體"},
      "B":{"en":"Use Amazon Bedrock with Provisioned Throughput","zh":"使用具有佈建吞吐量的 Amazon Bedrock"},
      "C":{"en":"Use Amazon Bedrock with On-Demand Throughput","zh":"使用具有隨需吞吐量的 Amazon Bedrock"},
      "D":{"en":"Use Amazon SageMaker JumpStart","zh":"使用 Amazon SageMaker JumpStart"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ GPU EC2 執行個體需要持續付費（即使閒置），低使用量期間成本浪費大，且需要管理基礎設施。",
      "B":"✗ Provisioned Throughput 適合穩定可預測的高流量，按月承諾付費；無法預測使用量的情況下，佈建太多容量會浪費，佈建太少會限制效能。",
      "C":"✓ 正確 — On-Demand Throughput（隨需吞吐量）按實際使用的 token 計費，低使用量時費用低，使用量增加時自動擴展，無需預先承諾，完全符合「低使用量、無法預測、最小化成本」的需求。",
      "D":"✗ SageMaker JumpStart 部署模型需要 SageMaker 端點（持續收費），對低使用量的試驗期成本較高。"
    }
  },
  {
    "id":178,"exam":"AIF",
    "question":"A company wants to control employee access to publicly available foundation models (FMs). Which solution meets these requirements?",
    "question_zh":"一家公司想控制員工對公開可用基礎模型 (FM) 的存取。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Analyze cost and usage reports in AWS Cost Explorer","zh":"在 AWS Cost Explorer 中分析成本和用量報告"},
      "B":{"en":"Download AWS security and compliance documents from AWS Artifact","zh":"從 AWS Artifact 下載 AWS 安全性和合規文件"},
      "C":{"en":"Configure Amazon SageMaker JumpStart to restrict discoverable FMs","zh":"配置 Amazon SageMaker JumpStart 以限制可發現的 FM"},
      "D":{"en":"Build a hybrid search solution by using Amazon OpenSearch Service","zh":"使用 Amazon OpenSearch Service 建立混合搜尋解決方案"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Cost Explorer 分析費用支出，不控制員工對 FM 的存取。",
      "B":"✗ AWS Artifact 提供合規文件下載，不是存取控制工具。",
      "C":"✓ 正確 — Amazon SageMaker JumpStart 提供 FM 目錄，管理員可透過 IAM 政策和 JumpStart 設定控制哪些使用者或角色可以發現和使用哪些 FM，實現 FM 存取控制。",
      "D":"✗ OpenSearch 是搜尋和分析引擎，不是 FM 存取控制的工具。"
    }
  },
  {
    "id":179,"exam":"AIF",
    "question":"Which AWS service or feature can help an AI development team quickly deploy and consume a foundation model (FM) within the team's VPC?",
    "question_zh":"哪個 AWS 服務或功能可以幫助 AI 開發團隊在團隊的 VPC 內快速部署和使用基礎模型 (FM)？",
    "options":{
      "A":{"en":"Amazon Personalize","zh":"Amazon Personalize"},
      "B":{"en":"Amazon SageMaker JumpStart","zh":"Amazon SageMaker JumpStart"},
      "C":{"en":"PartyRock, an Amazon Bedrock Playground","zh":"PartyRock（Amazon Bedrock 遊樂場）"},
      "D":{"en":"Amazon SageMaker endpoints","zh":"Amazon SageMaker 端點"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Personalize 是個人化推薦服務，不是通用 FM 部署平台。",
      "B":"✓ 正確 — Amazon SageMaker JumpStart 提供 FM 目錄和一鍵部署功能，可以在 VPC 內的 SageMaker 環境中快速部署和使用各種基礎模型（如 Llama、Falcon），是在 VPC 內快速消費 FM 的最佳選擇。",
      "C":"✗ PartyRock 是公開的無程式碼 Bedrock 展示平台，不在 VPC 內運行，不適合企業內部部署。",
      "D":"✗ SageMaker 端點是模型服務端點，是部署後的產物，本身不是「快速部署和消費 FM」的服務入口。"
    }
  },
  {
    "id":180,"exam":"AIF",
    "question":"A company wants to create an application using Amazon Bedrock. The company has a limited budget and prefers flexibility without long-term commitment. Which Amazon Bedrock pricing model meets these requirements?",
    "question_zh":"一家公司想使用 Amazon Bedrock 建立應用程式，預算有限且偏好靈活性、不想長期承諾。哪種 Amazon Bedrock 定價模型符合需求？",
    "options":{
      "A":{"en":"On-Demand","zh":"隨需 (On-Demand)"},
      "B":{"en":"Model customization","zh":"模型自訂"},
      "C":{"en":"Provisioned Throughput","zh":"佈建吞吐量"},
      "D":{"en":"Spot Instance","zh":"Spot 執行個體"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — On-Demand 定價按實際消耗的 token 計費，無最低費用、無長期承諾，完全按用量付費，最適合預算有限且使用量不確定的場景。",
      "B":"✗ 模型自訂（微調）有額外的訓練成本和儲存費用，不是最節省的選項。",
      "C":"✗ Provisioned Throughput 需要按月承諾固定的模型單位費用，是長期承諾定價，不符合「無長期承諾」的要求。",
      "D":"✗ Amazon Bedrock 沒有 Spot Instance 定價模型，Spot 是 EC2 的概念。"
    }
  },
  {
    "id":181,"exam":"AIF",
    "question":"A pharmaceutical company wants to analyze user reviews of new medications and provide a concise overview for each medication. Which solution meets these requirements?",
    "question_zh":"一家製藥公司想分析新藥物的使用者評論並為每種藥物提供簡潔概述。哪個解決方案符合需求？",
    "options":{
      "A":{"en":"Create a time-series forecasting model to analyze medication reviews by using Amazon Personalize","zh":"使用 Amazon Personalize 建立時間序列預測模型分析藥物評論"},
      "B":{"en":"Create medication review summaries by using Amazon Bedrock large language models (LLMs)","zh":"使用 Amazon Bedrock 大型語言模型 (LLM) 建立藥物評論摘要"},
      "C":{"en":"Create a classification model that categorizes medications into different groups by using Amazon SageMaker","zh":"使用 Amazon SageMaker 建立將藥物分類為不同群組的分類模型"},
      "D":{"en":"Create medication review summaries by using Amazon Rekognition","zh":"使用 Amazon Rekognition 建立藥物評論摘要"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Personalize 是個人化推薦服務，不能分析文字評論或生成摘要。",
      "B":"✓ 正確 — Amazon Bedrock 的 LLM（如 Claude、Amazon Titan）具備強大的文字理解和摘要能力，可閱讀大量使用者評論並生成每種藥物的簡潔、有意義的概述，是文字摘要任務的最佳解決方案。",
      "C":"✗ 分類模型將藥物歸類，不能生成對人類有意義的文字摘要。",
      "D":"✗ Amazon Rekognition 分析圖像和影片，不能處理文字評論或生成摘要。"
    }
  },
]
