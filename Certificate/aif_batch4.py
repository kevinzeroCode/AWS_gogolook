AIF_BATCH4 = [
    {
        "id": 182,
        "question": "What does context window refer to in the context of large language models (LLMs)?",
        "zh_question": "在大型語言模型（LLM）中，上下文視窗（context window）是指什麼？",
        "options": {
            "A": "The maximum number of parameters the model can have",
            "B": "The amount of memory the model requires to run",
            "C": "How much information can fit in a single prompt",
            "D": "The number of layers in the neural network"
        },
        "zh_options": {
            "A": "模型可擁有的最大參數數量",
            "B": "模型運行所需的記憶體量",
            "C": "單一提示中可容納的資訊量",
            "D": "神經網路中的層數"
        },
        "answer": "C",
        "explanation": "Context window refers to how much information (text/tokens) can fit in a single prompt sent to the LLM. It determines how much text the model can 'see' and process at once.",
        "zh_explanation": "上下文視窗指的是單一提示中可容納的資訊（文字/tokens）量，決定模型一次能「看到」並處理多少文字。",
        "category": "AIF",
        "option_explanations": {
            "A": "參數數量是模型大小，與上下文視窗無關。",
            "B": "記憶體需求是運算資源問題，非上下文視窗定義。",
            "C": "正確。上下文視窗決定單次提示可包含的資訊量。",
            "D": "神經網路層數是模型架構，與上下文視窗無關。"
        }
    },
    {
        "id": 183,
        "question": "A company wants to use a foundation model (FM) to classify customer support tickets. The company has labeled data that includes customer support tickets and their associated categories. Which fine-tuning strategy should the company use?",
        "zh_question": "一家公司想使用基礎模型（FM）對客戶支援票券進行分類。該公司擁有包含客戶支援票券及其相關類別的標記資料。公司應使用哪種微調策略？",
        "options": {
            "A": "Instruction-based fine-tuning with prompt and completion fields",
            "B": "Continued pre-training with unlabeled ticket data",
            "C": "RLHF with human preference rankings",
            "D": "Domain adaptation with raw ticket text only"
        },
        "zh_options": {
            "A": "使用提示和完成欄位進行指令式微調",
            "B": "使用未標記票券資料進行持續預訓練",
            "C": "使用人工偏好排名進行 RLHF",
            "D": "僅使用原始票券文字進行領域適應"
        },
        "answer": "A",
        "explanation": "Instruction-based fine-tuning with prompt (ticket text) and completion (category) pairs is ideal when you have labeled data mapping inputs to outputs. This directly trains the model for the classification task.",
        "zh_explanation": "當有標記資料（輸入→輸出對應）時，使用提示（票券文字）和完成（類別）配對的指令式微調最為理想，可直接訓練模型完成分類任務。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。有標記資料時使用指令式微調（prompt+completion）最有效。",
            "B": "持續預訓練使用未標記資料，不適合已有標記資料的分類任務。",
            "C": "RLHF 需要人工偏好排名，程序複雜，不適合此場景。",
            "D": "領域適應僅使用原始文字，無法利用已有的標記類別資訊。"
        }
    },
    {
        "id": 184,
        "question": "A company is building an application that will answer questions about products. The company needs a solution that is MOST cost-effective and that can handle rapidly changing questions and answers. Which solution meets these requirements?",
        "zh_question": "一家公司正在構建一個能夠回答產品問題的應用程式。公司需要一個最具成本效益且能處理快速變化問題和答案的解決方案。哪個解決方案符合這些要求？",
        "options": {
            "A": "Fine-tune the model on the product questions and answers",
            "B": "Use continued pre-training on product documentation",
            "C": "Implement RLHF with product-specific feedback",
            "D": "Use RAG to retrieve relevant product information dynamically"
        },
        "zh_options": {
            "A": "在產品問答上微調模型",
            "B": "在產品文件上進行持續預訓練",
            "C": "使用產品特定回饋實施 RLHF",
            "D": "使用 RAG 動態擷取相關產品資訊"
        },
        "answer": "D",
        "explanation": "RAG (Retrieval-Augmented Generation) is MOST cost-effective for rapidly changing Q&A because it doesn't require retraining. The knowledge base can be updated without model changes, making it ideal for dynamic product information.",
        "zh_explanation": "RAG（檢索增強生成）對於快速變化的問答最具成本效益，因為不需要重新訓練模型。知識庫可以在不更改模型的情況下更新，非常適合動態產品資訊。",
        "category": "AIF",
        "option_explanations": {
            "A": "微調每次資訊變更都需重新訓練，成本高昂。",
            "B": "持續預訓練同樣需要重新訓練，不適合頻繁變更。",
            "C": "RLHF 程序複雜且昂貴，不適合此需求。",
            "D": "正確。RAG 可動態更新知識庫，無需重訓模型，最具成本效益。"
        }
    },
    {
        "id": 185,
        "question": "A company is deploying a machine learning model for real-time predictions. Which model characteristic is MOST important for this use case?",
        "zh_question": "一家公司正在部署機器學習模型進行即時預測。對於此使用案例，哪個模型特性最重要？",
        "options": {
            "A": "High accuracy on training data",
            "B": "Large number of parameters",
            "C": "Fast inference speed",
            "D": "Low training cost"
        },
        "zh_options": {
            "A": "在訓練資料上的高準確率",
            "B": "大量的參數數量",
            "C": "快速的推論速度",
            "D": "低訓練成本"
        },
        "answer": "C",
        "explanation": "For real-time predictions, inference speed is MOST critical. The model must respond quickly enough to meet real-time latency requirements, even if this means sacrificing some accuracy.",
        "zh_explanation": "對於即時預測，推論速度最為關鍵。模型必須足夠快速地回應，以滿足即時延遲要求，即使這意味著犧牲一些準確性。",
        "category": "AIF",
        "option_explanations": {
            "A": "訓練資料準確率重要，但即時場景更優先考量推論速度。",
            "B": "大量參數通常使推論更慢，不利於即時預測。",
            "C": "正確。即時預測最需要快速的推論速度以滿足延遲需求。",
            "D": "低訓練成本是一次性考量，對即時預測運作影響不大。"
        }
    },
    {
        "id": 186,
        "question": "A company wants to build an LLM chatbot that can answer questions using the company's internal policies. The company wants to minimize retraining costs as policies change frequently. Which solution should the company use?",
        "zh_question": "一家公司想建立一個可以使用公司內部政策回答問題的 LLM 聊天機器人。隨著政策頻繁變更，公司希望最小化重新訓練成本。公司應使用哪個解決方案？",
        "options": {
            "A": "Fine-tune the model monthly when policies update",
            "B": "Use RLHF to incorporate policy feedback",
            "C": "Implement RAG with the policies stored in a knowledge base",
            "D": "Use prompt engineering to include all policies in every prompt"
        },
        "zh_options": {
            "A": "每當政策更新時每月微調模型",
            "B": "使用 RLHF 納入政策回饋",
            "C": "使用 RAG，將政策儲存在知識庫中",
            "D": "使用提示工程在每個提示中包含所有政策"
        },
        "answer": "C",
        "explanation": "RAG with a knowledge base allows policies to be updated without retraining the model. When policies change, only the knowledge base needs updating, making it the most cost-effective solution for frequently changing content.",
        "zh_explanation": "使用知識庫的 RAG 允許在不重新訓練模型的情況下更新政策。當政策變更時，只需更新知識庫，是處理頻繁變更內容最具成本效益的解決方案。",
        "category": "AIF",
        "option_explanations": {
            "A": "每月重新訓練成本高昂，且訓練與部署有時間差。",
            "B": "RLHF 無法直接更新政策資訊，不適合此場景。",
            "C": "正確。RAG 知識庫可隨時更新政策，無需重訓模型。",
            "D": "將所有政策放入提示會超出上下文視窗限制，不切實際。"
        }
    },
    {
        "id": 187,
        "question": "A company is implementing an offline batch processing pipeline for RAG. Which TWO components should be included in this offline pipeline? (Choose TWO)",
        "zh_question": "一家公司正在為 RAG 實施離線批次處理管道。離線管道中應包含哪兩個元件？（選擇兩個）",
        "options": {
            "A": "Create content embeddings for documents",
            "B": "Generate responses to user queries",
            "C": "Build and maintain the search index",
            "D": "Send responses back to users",
            "E": "Authenticate user requests"
        },
        "zh_options": {
            "A": "為文件建立內容嵌入",
            "B": "產生使用者查詢的回應",
            "C": "建立並維護搜尋索引",
            "D": "將回應傳送回使用者",
            "E": "驗證使用者請求"
        },
        "answer": "AC",
        "explanation": "The offline (preprocessing) pipeline for RAG involves: A) Creating embeddings for documents (vectorizing content), and C) Building the search index (storing vectors for retrieval). These happen before any user queries.",
        "zh_explanation": "RAG 的離線（預處理）管道包括：A) 為文件建立嵌入（向量化內容），以及 C) 建立搜尋索引（儲存向量以供檢索）。這些在使用者查詢之前發生。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。離線管道需要預先為文件建立向量嵌入。",
            "B": "產生回應是線上（即時）管道的工作，不在離線批次中。",
            "C": "正確。建立並維護搜尋索引是離線預處理的核心工作。",
            "D": "傳送回應給使用者是線上管道的最後步驟。",
            "E": "使用者驗證是線上請求處理的一部分。"
        }
    },
    {
        "id": 188,
        "question": "A company wants to build a chatbot that can answer questions about their rapidly changing product inventory. The company needs the chatbot to have access to the most current inventory data. Which solution should the company use?",
        "zh_question": "一家公司想建立一個可以回答其快速變化產品庫存問題的聊天機器人。公司需要聊天機器人能夠存取最新的庫存資料。公司應使用哪個解決方案？",
        "options": {
            "A": "Fine-tune the LLM daily with new inventory data",
            "B": "Use prompt engineering to include inventory in system prompts",
            "C": "Implement RAG with a database containing current inventory",
            "D": "Use RLHF to teach the model current inventory information"
        },
        "zh_options": {
            "A": "每天使用新庫存資料微調 LLM",
            "B": "使用提示工程在系統提示中包含庫存",
            "C": "使用包含當前庫存的資料庫實施 RAG",
            "D": "使用 RLHF 教導模型當前庫存資訊"
        },
        "answer": "C",
        "explanation": "RAG with a current inventory database allows real-time access to the latest inventory data without retraining. The model retrieves fresh data at query time, making it ideal for rapidly changing information.",
        "zh_explanation": "使用當前庫存資料庫的 RAG 允許即時存取最新庫存資料，無需重新訓練。模型在查詢時擷取最新資料，非常適合快速變化的資訊。",
        "category": "AIF",
        "option_explanations": {
            "A": "每天微調成本高且耗時，且模型仍會有資料時效落差。",
            "B": "庫存資料量大，放入系統提示會超出上下文限制。",
            "C": "正確。RAG 可即時查詢最新庫存資料庫，無需重訓模型。",
            "D": "RLHF 無法有效傳達即時庫存資料，不適合此場景。"
        }
    },
    {
        "id": 189,
        "question": "A company is implementing a RAG system and wants to improve the contextual relevancy of retrieved content. Which RAG technique should the company use?",
        "zh_question": "一家公司正在實施 RAG 系統，希望提高擷取內容的上下文相關性。公司應使用哪種 RAG 技術？",
        "options": {
            "A": "Increase the number of retrieved documents",
            "B": "Use a larger embedding model",
            "C": "Implement appropriate chunking strategies",
            "D": "Reduce the vector database size"
        },
        "zh_options": {
            "A": "增加擷取的文件數量",
            "B": "使用更大的嵌入模型",
            "C": "實施適當的分塊策略",
            "D": "縮小向量資料庫大小"
        },
        "answer": "C",
        "explanation": "Chunking strategies significantly impact contextual relevancy in RAG. Proper chunking ensures that retrieved text segments contain coherent, contextually complete information, improving response quality.",
        "zh_explanation": "分塊策略對 RAG 中的上下文相關性有重大影響。適當的分塊確保擷取的文字片段包含連貫、完整的上下文資訊，從而提高回應品質。",
        "category": "AIF",
        "option_explanations": {
            "A": "增加擷取文件數量可能引入不相關內容，降低品質。",
            "B": "更大的嵌入模型有幫助，但分塊策略更直接影響上下文完整性。",
            "C": "正確。適當的分塊策略確保每個片段包含完整的上下文資訊。",
            "D": "縮小向量資料庫會減少可用知識，降低回應品質。"
        }
    },
    {
        "id": 190,
        "question": "What is the main advantage of using RAG for NLP tasks?",
        "zh_question": "在 NLP 任務中使用 RAG 的主要優勢是什麼？",
        "options": {
            "A": "It enables the model to access and use external knowledge sources",
            "B": "It reduces the model size significantly",
            "C": "It eliminates the need for any training data",
            "D": "It makes the model run faster during inference"
        },
        "zh_options": {
            "A": "它使模型能夠存取和使用外部知識來源",
            "B": "它顯著縮小了模型大小",
            "C": "它消除了對任何訓練資料的需求",
            "D": "它使模型在推論期間運行更快"
        },
        "answer": "A",
        "explanation": "The main advantage of RAG is enabling the model to access external knowledge sources (documents, databases) at query time, allowing it to answer questions with up-to-date information beyond its training data.",
        "zh_explanation": "RAG 的主要優勢是使模型在查詢時能夠存取外部知識來源（文件、資料庫），從而能夠使用超出訓練資料範圍的最新資訊回答問題。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。RAG 的核心優勢是讓模型能夠動態存取外部知識來源。",
            "B": "RAG 不會縮小模型大小，反而增加了檢索元件。",
            "C": "RAG 仍需基礎模型的訓練，不能消除訓練資料需求。",
            "D": "RAG 增加了檢索步驟，通常使推論時間更長而非更短。"
        }
    },
    {
        "id": 191,
        "question": "A developer is building an application that uses an LLM to summarize books. The application fails when processing long books. What is the MOST likely cause of this failure?",
        "zh_question": "一位開發人員正在構建一個使用 LLM 摘要書籍的應用程式。處理長書籍時應用程式失敗。此失敗最可能的原因是什麼？",
        "options": {
            "A": "The model does not have enough parameters",
            "B": "The training data did not include books",
            "C": "The model requires GPU acceleration",
            "D": "The input tokens exceed the model's context window size"
        },
        "zh_options": {
            "A": "模型沒有足夠的參數",
            "B": "訓練資料不包含書籍",
            "C": "模型需要 GPU 加速",
            "D": "輸入 tokens 超過了模型的上下文視窗大小"
        },
        "answer": "D",
        "explanation": "When an LLM fails on long documents, the MOST likely cause is that the input exceeds the model's context window limit (maximum tokens). Long books contain far more tokens than most LLMs can process in a single prompt.",
        "zh_explanation": "當 LLM 在長文件上失敗時，最可能的原因是輸入超過了模型的上下文視窗限制（最大 tokens 數）。長書籍包含的 tokens 遠超過大多數 LLM 在單一提示中能處理的數量。",
        "category": "AIF",
        "option_explanations": {
            "A": "參數數量不足不會直接導致長文件處理失敗。",
            "B": "大型語言模型通常已在大量文字資料（包括書籍）上訓練。",
            "C": "GPU 不足會導致速度慢，但不會造成處理失敗（功能層面）。",
            "D": "正確。長書籍的 tokens 超過模型上下文視窗是最常見的失敗原因。"
        }
    },
    {
        "id": 192,
        "question": "What does the Top K parameter control in text generation models?",
        "zh_question": "在文字生成模型中，Top K 參數控制什麼？",
        "options": {
            "A": "The maximum length of the generated text",
            "B": "The number of highest probability tokens to consider for next token selection",
            "C": "The temperature of the sampling process",
            "D": "The number of training epochs"
        },
        "zh_options": {
            "A": "生成文字的最大長度",
            "B": "選擇下一個 token 時考慮的最高機率 tokens 數量",
            "C": "採樣過程的溫度",
            "D": "訓練輪次的數量"
        },
        "answer": "B",
        "explanation": "Top K limits token sampling to the K highest probability tokens at each step. For example, Top K=50 means only the 50 most likely next tokens are considered, controlling output diversity and randomness.",
        "zh_explanation": "Top K 限制每步的 token 採樣只考慮 K 個最高機率的 tokens。例如 Top K=50 表示只考慮最可能的 50 個下一個 tokens，從而控制輸出的多樣性和隨機性。",
        "category": "AIF",
        "option_explanations": {
            "A": "最大長度由 max_tokens 或 max_length 參數控制。",
            "B": "正確。Top K 決定採樣時考慮的最高機率 token 候選數量。",
            "C": "溫度由獨立的 temperature 參數控制。",
            "D": "訓練輪次與 Top K 推論參數無關。"
        }
    },
    {
        "id": 193,
        "question": "A data scientist wants to generate more diverse and creative outputs from a language model. Which action should the data scientist take?",
        "zh_question": "一位資料科學家希望從語言模型生成更多樣化和創造性的輸出。資料科學家應採取什麼行動？",
        "options": {
            "A": "Increase the temperature parameter",
            "B": "Decrease the top K parameter",
            "C": "Reduce the max tokens setting",
            "D": "Lower the top P threshold"
        },
        "zh_options": {
            "A": "增加溫度參數",
            "B": "降低 Top K 參數",
            "C": "減少最大 tokens 設定",
            "D": "降低 Top P 閾值"
        },
        "answer": "A",
        "explanation": "Increasing temperature makes the probability distribution more uniform, allowing the model to sample from a wider range of tokens. Higher temperature = more creative and diverse outputs.",
        "zh_explanation": "增加溫度使概率分佈更均勻，允許模型從更廣泛的 tokens 範圍採樣。更高的溫度 = 更有創意和多樣化的輸出。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。增加溫度使輸出更隨機、多樣化和富有創意。",
            "B": "降低 Top K 會限制選擇範圍，使輸出更保守，不更多樣。",
            "C": "減少最大 tokens 只影響輸出長度，不影響創意程度。",
            "D": "降低 Top P 閾值會限制採樣範圍，減少多樣性。"
        }
    },
    {
        "id": 194,
        "question": "A company wants to create an HR policy chatbot. The company wants to reduce hallucinations and ensure responses are based on the company's HR documentation. Which solution should the company use?",
        "zh_question": "一家公司想創建一個 HR 政策聊天機器人。公司希望減少幻覺並確保回應基於公司的 HR 文件。公司應使用哪個解決方案？",
        "options": {
            "A": "Implement RAG with the HR documents stored in a vector database",
            "B": "Fine-tune the model on all employee conversations",
            "C": "Increase the model temperature to improve accuracy",
            "D": "Use prompt engineering to list all HR policies"
        },
        "zh_options": {
            "A": "使用儲存在向量資料庫中的 HR 文件實施 RAG",
            "B": "在所有員工對話上微調模型",
            "C": "增加模型溫度以提高準確性",
            "D": "使用提示工程列出所有 HR 政策"
        },
        "answer": "A",
        "explanation": "RAG with HR documents in a vector database grounds the model's responses in actual company documentation, significantly reducing hallucinations. Retrieved documents provide factual context for each response.",
        "zh_explanation": "使用向量資料庫中 HR 文件的 RAG 將模型回應建立在實際公司文件上，大幅減少幻覺。擷取的文件為每個回應提供事實依據。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。RAG 讓模型回應有文件依據，有效減少幻覺。",
            "B": "在員工對話上微調可能引入不準確資訊，不能確保政策準確性。",
            "C": "增加溫度會使輸出更隨機，增加而非減少幻覺。",
            "D": "所有 HR 政策可能超出上下文視窗，且無法動態更新。"
        }
    },
    {
        "id": 195,
        "question": "A company wants to prevent its LLM-based application from being manipulated by malicious users through adversarial inputs. Which solution should the company implement?",
        "zh_question": "一家公司希望防止其基於 LLM 的應用程式被惡意使用者通過對抗性輸入操縱。公司應實施哪個解決方案？",
        "options": {
            "A": "Implement a prompt template that uses adversarial prompting techniques",
            "B": "Increase the model's temperature parameter",
            "C": "Remove all system prompts from the application",
            "D": "Allow users to modify the system prompt directly"
        },
        "zh_options": {
            "A": "實施使用對抗性提示技術的提示模板",
            "B": "增加模型的溫度參數",
            "C": "從應用程式中刪除所有系統提示",
            "D": "允許使用者直接修改系統提示"
        },
        "answer": "A",
        "explanation": "Implementing a robust prompt template that uses adversarial prompting techniques (such as input validation, instruction boundaries, and injection detection) helps protect against prompt injection and manipulation attacks.",
        "zh_explanation": "實施使用對抗性提示技術（如輸入驗證、指令邊界和注入檢測）的穩健提示模板，有助於防範提示注入和操縱攻擊。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。穩健的提示模板包含防禦性技術可防止對抗性操縱。",
            "B": "增加溫度會增加隨機性，不能防止操縱攻擊。",
            "C": "刪除系統提示反而讓模型更容易被操縱，降低安全性。",
            "D": "允許使用者修改系統提示是嚴重的安全漏洞。"
        }
    },
    {
        "id": 196,
        "question": "A data scientist is working with Stable Diffusion to generate images. The data scientist wants to make the generated images more specific to the provided description. Which parameter should the data scientist adjust?",
        "zh_question": "一位資料科學家正在使用 Stable Diffusion 生成圖像。資料科學家希望使生成的圖像對所提供的描述更具體。資料科學家應調整哪個參數？",
        "options": {
            "A": "Increase the number of diffusion steps",
            "B": "Decrease the negative prompt weight",
            "C": "Increase the CFG (Classifier-Free Guidance) scale",
            "D": "Reduce the image resolution"
        },
        "zh_options": {
            "A": "增加擴散步驟數",
            "B": "降低負面提示權重",
            "C": "增加 CFG（無分類器引導）比例",
            "D": "降低圖像解析度"
        },
        "answer": "C",
        "explanation": "The CFG (Classifier-Free Guidance) scale controls how closely the image follows the text prompt. Higher CFG = image adheres more strictly to the description. Lower CFG = more creative/random but less specific.",
        "zh_explanation": "CFG（無分類器引導）比例控制圖像與文字提示的貼近程度。更高的 CFG = 圖像更嚴格地遵循描述。更低的 CFG = 更有創意/隨機但更不具體。",
        "category": "AIF",
        "option_explanations": {
            "A": "增加擴散步驟可提高品質，但不直接控制描述的具體性。",
            "B": "負面提示權重用於避免某些元素，不直接提高描述具體性。",
            "C": "正確。提高 CFG 比例使圖像更緊密地遵循提示描述。",
            "D": "降低解析度只影響圖像大小，不影響描述具體性。"
        }
    },
    {
        "id": 197,
        "question": "A data scientist is building a sentiment analysis model and wants to ensure the model produces consistent results for the same input. Which action should the data scientist take?",
        "zh_question": "一位資料科學家正在構建情感分析模型，希望確保模型對相同輸入產生一致的結果。資料科學家應採取什麼行動？",
        "options": {
            "A": "Decrease the model temperature",
            "B": "Increase the top K parameter",
            "C": "Add more training examples",
            "D": "Use a larger foundation model"
        },
        "zh_options": {
            "A": "降低模型溫度",
            "B": "增加 Top K 參數",
            "C": "增加更多訓練範例",
            "D": "使用更大的基礎模型"
        },
        "answer": "A",
        "explanation": "Decreasing temperature makes the model more deterministic, producing more consistent and predictable outputs for the same input. For sentiment analysis where accuracy and consistency matter, lower temperature is preferred.",
        "zh_explanation": "降低溫度使模型更具確定性，對相同輸入產生更一致、可預測的輸出。對於準確性和一致性很重要的情感分析，較低的溫度是首選。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。較低的溫度使模型輸出更確定性，對相同輸入產生更一致的結果。",
            "B": "增加 Top K 會增加採樣範圍，使輸出更多樣（不更一致）。",
            "C": "更多訓練範例改善準確性，但不直接確保一致性輸出。",
            "D": "更大的模型不一定產生更一致的輸出。"
        }
    },
    {
        "id": 198,
        "question": "A developer wants to build a question-answering system that always gives the same answer for identical questions. Which configuration should the developer use?",
        "zh_question": "一位開發人員想構建一個對相同問題總是給出相同答案的問答系統。開發人員應使用哪種配置？",
        "options": {
            "A": "Set temperature to 0 for deterministic responses",
            "B": "Set temperature to 1 for balanced responses",
            "C": "Set temperature to 2 for creative responses",
            "D": "Use random sampling without temperature control"
        },
        "zh_options": {
            "A": "將溫度設定為 0 以獲得確定性回應",
            "B": "將溫度設定為 1 以獲得平衡回應",
            "C": "將溫度設定為 2 以獲得創意回應",
            "D": "在沒有溫度控制的情況下使用隨機採樣"
        },
        "answer": "A",
        "explanation": "Temperature of 0 makes the model always select the highest probability token, resulting in deterministic/greedy decoding. This means identical inputs will always produce identical outputs.",
        "zh_explanation": "溫度為 0 使模型始終選擇最高機率的 token，產生確定性/貪婪解碼。這意味著相同的輸入將始終產生相同的輸出。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。溫度為 0 = 確定性輸出，相同問題總是得到相同答案。",
            "B": "溫度為 1 是預設值，仍有隨機性，不能保證相同輸出。",
            "C": "溫度為 2 會產生更隨機的輸出，不適合需要一致性的場景。",
            "D": "隨機採樣無溫度控制會產生高度不一致的輸出。"
        }
    },
    {
        "id": 199,
        "question": "A company is building a chatbot that uses Amazon Bedrock and needs to provide responses based on the company's proprietary data. Which Amazon Bedrock feature should the company use to give the model access to company-specific context?",
        "zh_question": "一家公司正在建立使用 Amazon Bedrock 的聊天機器人，需要根據公司的專有資料提供回應。公司應使用哪個 Amazon Bedrock 功能來讓模型存取公司特定的上下文？",
        "options": {
            "A": "Amazon Bedrock Knowledge Bases",
            "B": "Amazon Bedrock Model Evaluation",
            "C": "Amazon Bedrock Guardrails",
            "D": "Amazon Bedrock Fine-tuning"
        },
        "zh_options": {
            "A": "Amazon Bedrock Knowledge Bases",
            "B": "Amazon Bedrock Model Evaluation",
            "C": "Amazon Bedrock Guardrails",
            "D": "Amazon Bedrock 微調"
        },
        "answer": "A",
        "explanation": "Amazon Bedrock Knowledge Bases implements RAG, allowing the model to retrieve and use company-specific documents stored in a vector database. This gives the model access to proprietary context without retraining.",
        "zh_explanation": "Amazon Bedrock Knowledge Bases 實施 RAG，允許模型擷取並使用儲存在向量資料庫中的公司特定文件。這使模型無需重新訓練即可存取專有上下文。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。Bedrock Knowledge Bases 實現 RAG，提供公司專有資料存取。",
            "B": "Model Evaluation 用於評估模型效能，不用於資料存取。",
            "C": "Guardrails 用於內容過濾和安全防護，不提供知識存取。",
            "D": "微調改變模型參數，成本更高且不適合頻繁更新的資料。"
        }
    },
    {
        "id": 200,
        "question": "A company needs to build an airline customer service chatbot using an LLM. The company wants to implement this solution with the LEAST operational effort. Which approach should the company use?",
        "zh_question": "一家公司需要使用 LLM 建立航空公司客戶服務聊天機器人。公司希望以最少的操作工作量實施此解決方案。公司應使用哪種方法？",
        "options": {
            "A": "Build a custom RAG pipeline from scratch with self-managed vector database",
            "B": "Use Amazon Bedrock Agents with Knowledge Bases for RAG",
            "C": "Deploy a custom transformer model on EC2 instances",
            "D": "Fine-tune an open-source LLM with airline-specific data"
        },
        "zh_options": {
            "A": "使用自管理向量資料庫從頭建立自訂 RAG 管道",
            "B": "使用 Amazon Bedrock Agents 和 Knowledge Bases 進行 RAG",
            "C": "在 EC2 執行個體上部署自訂 transformer 模型",
            "D": "使用航空公司特定資料微調開源 LLM"
        },
        "answer": "B",
        "explanation": "Amazon Bedrock Agents with Knowledge Bases provides a fully managed RAG solution with minimal operational overhead. It handles infrastructure, retrieval, and orchestration automatically, requiring the LEAST effort.",
        "zh_explanation": "Amazon Bedrock Agents 與 Knowledge Bases 提供完全託管的 RAG 解決方案，操作開銷最小。它自動處理基礎設施、檢索和編排，需要最少的工作量。",
        "category": "AIF",
        "option_explanations": {
            "A": "從頭建立 RAG 管道需要大量工程工作和維護。",
            "B": "正確。Bedrock Agents + Knowledge Bases 是完全託管的解決方案，操作工作量最少。",
            "C": "在 EC2 上部署自訂模型需要管理基礎設施，工作量大。",
            "D": "微調開源 LLM 需要資料準備、訓練和部署，工作量大。"
        }
    },
    {
        "id": 201,
        "question": "A developer has an LLM that generates responses that are too long and use complex language. The developer wants the LLM to generate shorter, more specific responses. Which approach should the developer use?",
        "zh_question": "一位開發人員有一個 LLM，它生成太長且使用複雜語言的回應。開發人員希望 LLM 生成更短、更具體的回應。開發人員應使用哪種方法？",
        "options": {
            "A": "Adjust the prompt to specify the desired output length and language style",
            "B": "Increase the model temperature to generate more concise outputs",
            "C": "Use a smaller language model instead",
            "D": "Add more training examples of long responses"
        },
        "zh_options": {
            "A": "調整提示以指定所需的輸出長度和語言風格",
            "B": "增加模型溫度以生成更簡潔的輸出",
            "C": "改用更小的語言模型",
            "D": "增加更多長回應的訓練範例"
        },
        "answer": "A",
        "explanation": "Adjusting the prompt to explicitly specify desired output length (e.g., 'in 2-3 sentences') and language style (e.g., 'use simple language') is the most direct and effective prompt engineering approach.",
        "zh_explanation": "調整提示以明確指定所需的輸出長度（例如「用 2-3 句話」）和語言風格（例如「使用簡單語言」）是最直接有效的提示工程方法。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。在提示中明確指定長度和語言風格是最有效的方法。",
            "B": "增加溫度增加隨機性，不能保證更短或更具體的輸出。",
            "C": "更小的模型可能能力不足，不是解決輸出格式問題的最佳方法。",
            "D": "增加長回應的訓練範例會使模型生成更長而非更短的回應。"
        }
    },
    {
        "id": 202,
        "question": "A company wants to use a foundation model to classify customer reviews as positive or negative. The company needs high accuracy with minimal effort. Which prompting technique should the company use?",
        "zh_question": "一家公司希望使用基礎模型將客戶評論分類為正面或負面。公司需要以最少的工作量實現高準確性。公司應使用哪種提示技術？",
        "options": {
            "A": "Zero-shot prompting",
            "B": "Chain-of-thought prompting",
            "C": "Few-shot prompting with positive and negative examples",
            "D": "ReAct prompting"
        },
        "zh_options": {
            "A": "零樣本提示",
            "B": "思維鏈提示",
            "C": "使用正負面範例的少樣本提示",
            "D": "ReAct 提示"
        },
        "answer": "C",
        "explanation": "Few-shot prompting with examples of positive and negative sentiment classifications helps the model understand the exact output format and classification criteria expected, improving accuracy over zero-shot.",
        "zh_explanation": "使用正負面情感分類範例的少樣本提示幫助模型理解預期的確切輸出格式和分類標準，比零樣本提示具有更高的準確性。",
        "category": "AIF",
        "option_explanations": {
            "A": "零樣本提示不提供範例，準確性通常低於少樣本提示。",
            "B": "思維鏈提示用於需要推理步驟的問題，分類任務不需要。",
            "C": "正確。少樣本提示通過提供範例，使模型更好地理解分類任務。",
            "D": "ReAct 結合推理和行動，對簡單分類任務過於複雜。"
        }
    },
    {
        "id": 203,
        "question": "A marketing team wants to use a foundation model to generate product descriptions in a specific style. The team has several example descriptions. Which prompting technique requires the LEAST effort to implement while matching the style?",
        "zh_question": "行銷團隊希望使用基礎模型以特定風格生成產品描述。團隊有幾個範例描述。哪種提示技術在匹配風格的同時需要最少的實施工作量？",
        "options": {
            "A": "Few-shot prompting using the example descriptions",
            "B": "Fine-tune the model on the example descriptions",
            "C": "Use RLHF with the marketing team as reviewers",
            "D": "Zero-shot prompting with detailed style instructions"
        },
        "zh_options": {
            "A": "使用範例描述進行少樣本提示",
            "B": "在範例描述上微調模型",
            "C": "以行銷團隊作為審閱者使用 RLHF",
            "D": "使用詳細風格說明進行零樣本提示"
        },
        "answer": "A",
        "explanation": "Few-shot prompting with the existing example descriptions requires LEAST effort - just include the examples in the prompt. Fine-tuning requires more examples, training time, and cost. RLHF is even more complex.",
        "zh_explanation": "使用現有範例描述的少樣本提示需要最少工作量——只需在提示中包含範例。微調需要更多範例、訓練時間和成本。RLHF 更為複雜。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。少樣本提示直接使用現有範例，實施工作量最少。",
            "B": "微調需要準備資料、訓練和部署，工作量遠大於提示工程。",
            "C": "RLHF 需要收集人工偏好資料，是最複雜且耗時的方法。",
            "D": "詳細風格說明可能不如直接範例有效，且需要精心撰寫說明。"
        }
    },
    {
        "id": 204,
        "question": "A company wants to use a foundation model to generate marketing content that aligns with the company's brand voice. Which prompt engineering practice is MOST effective for ensuring brand voice alignment?",
        "zh_question": "一家公司希望使用基礎模型生成符合公司品牌聲音的行銷內容。哪種提示工程實踐最有效地確保品牌聲音對齊？",
        "options": {
            "A": "Use high temperature settings for creative outputs",
            "B": "Include only the content topic with no other instructions",
            "C": "Include brand voice guidelines and examples in the prompt",
            "D": "Use zero-shot prompting for maximum flexibility"
        },
        "zh_options": {
            "A": "使用高溫度設定以獲得創意輸出",
            "B": "只包含內容主題而不包含其他說明",
            "C": "在提示中包含品牌聲音指南和範例",
            "D": "使用零樣本提示以獲得最大靈活性"
        },
        "answer": "C",
        "explanation": "Including brand voice guidelines (tone, style, vocabulary) and examples in the prompt gives the model clear constraints and patterns to follow, ensuring alignment with the company's specific brand voice.",
        "zh_explanation": "在提示中包含品牌聲音指南（語調、風格、詞彙）和範例為模型提供明確的限制和模式，確保與公司特定品牌聲音的對齊。",
        "category": "AIF",
        "option_explanations": {
            "A": "高溫度增加創意但可能偏離品牌聲音，不利於一致性。",
            "B": "只有主題而無指南，模型無法了解品牌特定要求。",
            "C": "正確。在提示中包含品牌指南和範例是確保品牌對齊的最有效方法。",
            "D": "零樣本提示靈活但無法保證品牌聲音一致性。"
        }
    },
    {
        "id": 205,
        "question": "A developer is building a system to generate product descriptions. The system must generate different types of descriptions based on product categories. Which prompt structure should the developer use?",
        "zh_question": "一位開發人員正在建立一個生成產品描述的系統。系統必須根據產品類別生成不同類型的描述。開發人員應使用哪種提示結構？",
        "options": {
            "A": "Use a single generic prompt for all product categories",
            "B": "Use a separate prompt template for each product category",
            "C": "Randomly select from multiple prompts for each request",
            "D": "Use only the product name without any instructions"
        },
        "zh_options": {
            "A": "對所有產品類別使用單一通用提示",
            "B": "對每個產品類別使用單獨的提示模板",
            "C": "對每個請求隨機從多個提示中選擇",
            "D": "只使用產品名稱而不包含任何說明"
        },
        "answer": "B",
        "explanation": "Using separate prompt templates for each product category allows tailored instructions and examples specific to each category (electronics, clothing, food, etc.), resulting in more appropriate and higher-quality descriptions.",
        "zh_explanation": "對每個產品類別使用單獨的提示模板，可針對每個類別（電子產品、服裝、食品等）定制說明和範例，從而產生更適合、品質更高的描述。",
        "category": "AIF",
        "option_explanations": {
            "A": "通用提示無法針對各類別的特殊需求，輸出品質較差。",
            "B": "正確。各類別的專用模板可包含針對性的說明和範例，提高品質。",
            "C": "隨機選擇提示會導致不一致和不可預測的輸出。",
            "D": "只有產品名稱沒有足夠的上下文，無法生成高品質描述。"
        }
    },
    {
        "id": 206,
        "question": "A developer is using a text-to-image model and wants to prevent the model from generating images that contain unrelated or unwanted elements. Which technique should the developer use?",
        "zh_question": "一位開發人員正在使用文字轉圖像模型，希望防止模型生成包含不相關或不需要元素的圖像。開發人員應使用哪種技術？",
        "options": {
            "A": "Increase the CFG scale parameter",
            "B": "Use negative prompts to specify unwanted elements",
            "C": "Reduce the number of diffusion steps",
            "D": "Increase the image resolution"
        },
        "zh_options": {
            "A": "增加 CFG 比例參數",
            "B": "使用負面提示指定不需要的元素",
            "C": "減少擴散步驟數",
            "D": "增加圖像解析度"
        },
        "answer": "B",
        "explanation": "Negative prompts explicitly tell the text-to-image model what elements to avoid or exclude from the generated image. This is the standard technique for preventing unwanted elements in AI image generation.",
        "zh_explanation": "負面提示明確告訴文字轉圖像模型在生成的圖像中要避免或排除哪些元素。這是防止 AI 圖像生成中出現不需要元素的標準技術。",
        "category": "AIF",
        "option_explanations": {
            "A": "增加 CFG 使圖像更貼近正面提示，但不直接排除特定元素。",
            "B": "正確。負面提示專門用於指定不希望出現在圖像中的元素。",
            "C": "減少擴散步驟降低圖像品質，不能防止特定元素出現。",
            "D": "增加解析度只影響圖像大小，不影響內容元素。"
        }
    },
    {
        "id": 207,
        "question": "A company is implementing adversarial prompting techniques in their LLM application. What is the PRIMARY purpose of adversarial prompting in this context?",
        "zh_question": "一家公司正在其 LLM 應用程式中實施對抗性提示技術。在此情境下，對抗性提示的主要目的是什麼？",
        "options": {
            "A": "To protect the application against prompt injection attacks",
            "B": "To increase the creativity of the model's outputs",
            "C": "To reduce the cost of API calls",
            "D": "To improve the model's performance on standard benchmarks"
        },
        "zh_options": {
            "A": "保護應用程式免受提示注入攻擊",
            "B": "增加模型輸出的創意性",
            "C": "降低 API 呼叫成本",
            "D": "提高模型在標準基準上的效能"
        },
        "answer": "A",
        "explanation": "Adversarial prompting techniques (such as defensive instructions and injection detection in system prompts) are primarily used to protect LLM applications from prompt injection and manipulation attacks.",
        "zh_explanation": "對抗性提示技術（如系統提示中的防禦性指令和注入檢測）主要用於保護 LLM 應用程式免受提示注入和操縱攻擊。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。對抗性提示的主要目的是防禦性的，保護免受提示注入攻擊。",
            "B": "增加創意性通常通過提高溫度實現，不是對抗性提示的目的。",
            "C": "對抗性提示與 API 成本無直接關係。",
            "D": "對抗性提示關注安全性，不直接改善基準效能。"
        }
    },
    {
        "id": 208,
        "question": "A developer wants to improve an LLM's ability to generate step-by-step assembly instructions for complex products. Which prompting technique should the developer use?",
        "zh_question": "一位開發人員希望提高 LLM 生成複雜產品逐步組裝說明的能力。開發人員應使用哪種提示技術？",
        "options": {
            "A": "Zero-shot prompting with a detailed product description",
            "B": "Chain-of-thought prompting with step-by-step reasoning examples",
            "C": "ReAct prompting for tool use",
            "D": "Negative prompting to avoid incorrect steps"
        },
        "zh_options": {
            "A": "使用詳細產品描述進行零樣本提示",
            "B": "使用逐步推理範例進行思維鏈提示",
            "C": "用於工具使用的 ReAct 提示",
            "D": "負面提示以避免不正確的步驟"
        },
        "answer": "B",
        "explanation": "Chain-of-thought (CoT) prompting with step-by-step examples teaches the model to break down complex tasks into logical sequential steps, which is ideal for generating assembly instructions.",
        "zh_explanation": "帶有逐步範例的思維鏈（CoT）提示教導模型將複雜任務分解為邏輯順序步驟，非常適合生成組裝說明。",
        "category": "AIF",
        "option_explanations": {
            "A": "零樣本提示不提供步驟結構範例，對複雜的序列任務效果有限。",
            "B": "正確。思維鏈提示通過範例教導模型進行逐步推理，適合組裝說明。",
            "C": "ReAct 結合推理和外部工具使用，對純文字說明生成過於複雜。",
            "D": "負面提示用於圖像生成，不直接適用於文字指令生成。"
        }
    },
    {
        "id": 209,
        "question": "A company wants to improve the accuracy of a foundation model for domain-specific tasks. The company needs the MOST cost-effective approach. Which solution should the company use?",
        "zh_question": "一家公司希望提高基礎模型在特定領域任務上的準確性。公司需要最具成本效益的方法。公司應使用哪個解決方案？",
        "options": {
            "A": "Continued pre-training with domain-specific data",
            "B": "RLHF with domain experts",
            "C": "Full fine-tuning of all model parameters",
            "D": "Optimize prompts with domain-specific context and examples"
        },
        "zh_options": {
            "A": "使用特定領域資料進行持續預訓練",
            "B": "使用領域專家進行 RLHF",
            "C": "對所有模型參數進行完整微調",
            "D": "使用特定領域上下文和範例優化提示"
        },
        "answer": "D",
        "explanation": "Prompt engineering (optimizing prompts with domain context and few-shot examples) is the MOST cost-effective approach as it requires no model training, just crafting effective prompts. Training methods (pre-training, RLHF, fine-tuning) all involve significant computational costs.",
        "zh_explanation": "提示工程（使用領域上下文和少樣本範例優化提示）是最具成本效益的方法，因為不需要模型訓練，只需撰寫有效的提示。所有訓練方法（預訓練、RLHF、微調）都涉及大量計算成本。",
        "category": "AIF",
        "option_explanations": {
            "A": "持續預訓練需要大量資料和計算資源，成本高。",
            "B": "RLHF 需要人工標注和迭代訓練，成本最高。",
            "C": "完整微調需要計算資源和訓練基礎設施，成本可觀。",
            "D": "正確。提示工程不需要訓練，是最具成本效益的提高準確性方法。"
        }
    },
    {
        "id": 210,
        "question": "A developer wants the LLM to generate responses in a specific format. The developer provides examples of the desired format in the prompt. Which prompting technique is the developer using?",
        "zh_question": "一位開發人員希望 LLM 以特定格式生成回應。開發人員在提示中提供了所需格式的範例。開發人員正在使用哪種提示技術？",
        "options": {
            "A": "Zero-shot prompting",
            "B": "Chain-of-thought prompting",
            "C": "Retrieval-augmented generation",
            "D": "Few-shot prompting"
        },
        "zh_options": {
            "A": "零樣本提示",
            "B": "思維鏈提示",
            "C": "檢索增強生成",
            "D": "少樣本提示"
        },
        "answer": "D",
        "explanation": "Few-shot prompting involves providing examples (shots) in the prompt to demonstrate the desired input-output format. The model learns the pattern from the examples and applies it to new inputs.",
        "zh_explanation": "少樣本提示涉及在提示中提供範例（shots）來演示所需的輸入-輸出格式。模型從範例中學習模式並將其應用於新的輸入。",
        "category": "AIF",
        "option_explanations": {
            "A": "零樣本提示不提供範例，只有任務描述。",
            "B": "思維鏈提示提供推理過程範例，重點在邏輯步驟而非格式。",
            "C": "RAG 從外部來源擷取資訊，不是基於範例的提示技術。",
            "D": "正確。在提示中提供格式範例正是少樣本提示的定義。"
        }
    },
    {
        "id": 211,
        "question": "A developer is building a chatbot that needs to check product inventory, look up order status, and answer customer questions. Which prompting technique is MOST appropriate for this multi-step task?",
        "zh_question": "一位開發人員正在建立一個需要檢查產品庫存、查詢訂單狀態並回答客戶問題的聊天機器人。哪種提示技術最適合這個多步驟任務？",
        "options": {
            "A": "Zero-shot prompting",
            "B": "Few-shot prompting",
            "C": "Chain-of-thought prompting",
            "D": "ReAct prompting"
        },
        "zh_options": {
            "A": "零樣本提示",
            "B": "少樣本提示",
            "C": "思維鏈提示",
            "D": "ReAct 提示"
        },
        "answer": "D",
        "explanation": "ReAct (Reasoning + Acting) prompting is ideal for tasks that require the model to reason about what to do AND take actions (like calling tools/APIs to check inventory or order status). It combines reasoning with external tool use.",
        "zh_explanation": "ReAct（推理+行動）提示非常適合需要模型進行推理並採取行動（如呼叫工具/API 檢查庫存或訂單狀態）的任務。它結合了推理和外部工具使用。",
        "category": "AIF",
        "option_explanations": {
            "A": "零樣本提示無法處理需要外部工具呼叫的多步驟任務。",
            "B": "少樣本提示提供範例，但不支援與外部工具的互動。",
            "C": "思維鏈提示提供推理，但不支援採取行動（工具呼叫）。",
            "D": "正確。ReAct 結合推理和行動，適合需要呼叫外部工具的複雜任務。"
        }
    },
    {
        "id": 212,
        "question": "A developer is using Amazon Bedrock Agents and finds that the agent is not performing as expected. The developer wants to improve the agent's accuracy. Which action should the developer take?",
        "zh_question": "一位開發人員正在使用 Amazon Bedrock Agents，發現 agent 的表現不如預期。開發人員希望提高 agent 的準確性。開發人員應採取什麼行動？",
        "options": {
            "A": "Modify the agent's advanced prompts to provide clearer instructions",
            "B": "Increase the model temperature for more diverse outputs",
            "C": "Switch to a smaller, faster model",
            "D": "Remove the agent's system prompt entirely"
        },
        "zh_options": {
            "A": "修改 agent 的進階提示以提供更清晰的說明",
            "B": "增加模型溫度以獲得更多樣化的輸出",
            "C": "切換到更小、更快的模型",
            "D": "完全刪除 agent 的系統提示"
        },
        "answer": "A",
        "explanation": "Modifying the agent's advanced prompts (system prompt, orchestration prompt, etc.) to provide clearer instructions is the most direct way to improve agent accuracy without changing the underlying model or architecture.",
        "zh_explanation": "修改 agent 的進階提示（系統提示、編排提示等）以提供更清晰的說明，是在不更改底層模型或架構的情況下提高 agent 準確性的最直接方法。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。優化進階提示提供更清晰的指令，直接改善 agent 準確性。",
            "B": "增加溫度使輸出更隨機，通常降低而非提高準確性。",
            "C": "切換到更小的模型通常降低能力和準確性。",
            "D": "刪除系統提示會移除重要指令，使 agent 更難以正確執行。"
        }
    },
    {
        "id": 213,
        "question": "A developer is working on an AI application that needs to handle complex, multi-step tasks where the output of one step becomes the input of the next. Which prompting approach is MOST suitable?",
        "zh_question": "一位開發人員正在開發一個 AI 應用程式，需要處理複雜的多步驟任務，其中一個步驟的輸出成為下一個步驟的輸入。哪種提示方法最合適？",
        "options": {
            "A": "Zero-shot prompting for simplicity",
            "B": "Prompt chaining to pass outputs as inputs",
            "C": "Few-shot prompting with complex examples",
            "D": "Increasing temperature for more complete answers"
        },
        "zh_options": {
            "A": "零樣本提示以求簡單",
            "B": "提示鏈接將輸出作為輸入傳遞",
            "C": "使用複雜範例進行少樣本提示",
            "D": "增加溫度以獲得更完整的答案"
        },
        "answer": "B",
        "explanation": "Prompt chaining connects multiple LLM calls where each step's output feeds into the next prompt. This is designed for complex sequential tasks where breaking the problem into steps improves accuracy and traceability.",
        "zh_explanation": "提示鏈接連接多個 LLM 呼叫，其中每個步驟的輸出成為下一個提示的輸入。這專為複雜的順序任務設計，將問題分解為步驟可提高準確性和可追蹤性。",
        "category": "AIF",
        "option_explanations": {
            "A": "零樣本提示無法處理需要多步驟依序執行的複雜任務。",
            "B": "正確。提示鏈接專為多步驟任務設計，前一步驟輸出作為後一步驟輸入。",
            "C": "少樣本提示提供範例，但不支援步驟間的資料流動。",
            "D": "增加溫度與多步驟任務處理能力無關。"
        }
    },
    {
        "id": 214,
        "question": "A company is using an LLM API and wants to reduce its monthly costs. The company has determined that reducing the number of tokens in requests would help. Which action should the company take?",
        "zh_question": "一家公司正在使用 LLM API，希望降低每月成本。公司確定減少請求中的 tokens 數量會有所幫助。公司應採取什麼行動？",
        "options": {
            "A": "Increase the temperature parameter",
            "B": "Decrease the number of tokens in the prompt",
            "C": "Use larger foundation models",
            "D": "Add more context to each prompt"
        },
        "zh_options": {
            "A": "增加溫度參數",
            "B": "減少提示中的 tokens 數量",
            "C": "使用更大的基礎模型",
            "D": "在每個提示中增加更多上下文"
        },
        "answer": "B",
        "explanation": "LLM API costs are directly tied to token usage (input + output tokens). Decreasing the number of tokens in prompts (more concise instructions, fewer examples) directly reduces API costs.",
        "zh_explanation": "LLM API 成本直接與 token 使用量（輸入 + 輸出 tokens）相關。減少提示中的 tokens 數量（更簡潔的指令、更少的範例）直接降低 API 成本。",
        "category": "AIF",
        "option_explanations": {
            "A": "溫度參數影響輸出多樣性，不影響 tokens 消耗量。",
            "B": "正確。減少提示中的 tokens 直接降低 API 使用成本。",
            "C": "更大的基礎模型通常有更高的每 token 費率，增加而非降低成本。",
            "D": "增加更多上下文會增加 tokens 數量，提高而非降低成本。"
        }
    },
    {
        "id": 215,
        "question": "A company has a large collection of PDF product manuals and wants to build a system where customers can ask questions about products and get accurate answers. Which solution should the company use?",
        "zh_question": "一家公司擁有大量 PDF 產品手冊，希望建立一個客戶可以詢問產品問題並獲得準確答案的系統。公司應使用哪個解決方案？",
        "options": {
            "A": "Fine-tune an LLM on all product manual text",
            "B": "Create a traditional keyword search system",
            "C": "Use RLHF with customer service representatives",
            "D": "Use Amazon Bedrock Knowledge Bases to implement RAG with the PDF manuals"
        },
        "zh_options": {
            "A": "在所有產品手冊文字上微調 LLM",
            "B": "建立傳統關鍵字搜尋系統",
            "C": "與客戶服務代表使用 RLHF",
            "D": "使用 Amazon Bedrock Knowledge Bases 對 PDF 手冊實施 RAG"
        },
        "answer": "D",
        "explanation": "Amazon Bedrock Knowledge Bases with RAG can ingest PDF manuals, create vector embeddings, and retrieve relevant content to answer customer questions accurately. This is more maintainable than fine-tuning and more capable than keyword search.",
        "zh_explanation": "Amazon Bedrock Knowledge Bases 搭配 RAG 可以讀取 PDF 手冊，建立向量嵌入，並擷取相關內容準確回答客戶問題。這比微調更易維護，比關鍵字搜尋更有能力。",
        "category": "AIF",
        "option_explanations": {
            "A": "微調 LLM 成本高，且當手冊更新時需要重新訓練。",
            "B": "關鍵字搜尋無法理解語義，對複雜問題效果差。",
            "C": "RLHF 需要大量人工參與，不適合產品問答系統。",
            "D": "正確。Bedrock Knowledge Bases + RAG 是處理 PDF 手冊問答的最佳解決方案。"
        }
    },
    {
        "id": 216,
        "question": "A developer is building a conversational AI application that needs to remember previous exchanges in the conversation. Which approach should the developer use to maintain conversation context?",
        "zh_question": "一位開發人員正在建立一個需要記住之前對話交流的對話式 AI 應用程式。開發人員應使用哪種方法來維護對話上下文？",
        "options": {
            "A": "Store conversation history in a separate database and never include it in prompts",
            "B": "Include previous conversation messages in the prompt context",
            "C": "Use a higher temperature to improve memory",
            "D": "Increase the model's parameter count"
        },
        "zh_options": {
            "A": "將對話歷史儲存在單獨的資料庫中，永遠不要包含在提示中",
            "B": "在提示上下文中包含之前的對話訊息",
            "C": "使用更高的溫度來改善記憶",
            "D": "增加模型的參數數量"
        },
        "answer": "B",
        "explanation": "LLMs are stateless and don't inherently remember previous conversations. To maintain conversation context, developers must include the conversation history (previous messages) in the prompt for each new request.",
        "zh_explanation": "LLM 是無狀態的，本質上不記得之前的對話。為維護對話上下文，開發人員必須在每個新請求的提示中包含對話歷史（之前的訊息）。",
        "category": "AIF",
        "option_explanations": {
            "A": "只儲存但不在提示中包含對話歷史，模型仍無法存取之前的對話。",
            "B": "正確。將之前的對話訊息包含在提示中是維護對話上下文的標準方法。",
            "C": "溫度控制隨機性，與記憶能力無關。",
            "D": "增加參數數量不會讓模型記住之前的對話。"
        }
    },
    {
        "id": 217,
        "question": "A data scientist wants to customize a foundation model using ongoing pre-training. What is a KEY benefit of this approach?",
        "zh_question": "一位資料科學家想使用持續預訓練來自定義基礎模型。這種方法的主要好處是什麼？",
        "options": {
            "A": "It reduces the model's context window size",
            "B": "It allows the model to learn domain-specific terminology and knowledge",
            "C": "It eliminates the need for any labeled data",
            "D": "It makes the model run faster during inference"
        },
        "zh_options": {
            "A": "它縮小了模型的上下文視窗大小",
            "B": "它允許模型學習特定領域的術語和知識",
            "C": "它消除了對任何標記資料的需求",
            "D": "它使模型在推論期間運行更快"
        },
        "answer": "B",
        "explanation": "Ongoing pre-training (also called continued pre-training or domain-adaptive pre-training) allows the model to learn domain-specific vocabulary, terminology, and knowledge from unlabeled domain text, adapting the model's base knowledge.",
        "zh_explanation": "持續預訓練（也稱為領域自適應預訓練）允許模型從未標記的領域文字中學習特定領域的詞彙、術語和知識，調整模型的基礎知識。",
        "category": "AIF",
        "option_explanations": {
            "A": "持續預訓練不會縮小上下文視窗，通常不影響此參數。",
            "B": "正確。持續預訓練使模型從領域文字中學習特定術語和知識。",
            "C": "持續預訓練使用未標記資料，但微調仍需要標記資料用於其他任務。",
            "D": "持續預訓練通常不會使推論更快，模型大小通常保持不變。"
        }
    },
    {
        "id": 218,
        "question": "A company wants to use a pre-trained foundation model for a specific business task. The company needs the model to follow specific output formats and styles. What is a PRIMARY benefit of fine-tuning the foundation model?",
        "zh_question": "一家公司想使用預訓練的基礎模型來完成特定的業務任務。公司需要模型遵循特定的輸出格式和風格。微調基礎模型的主要好處是什麼？",
        "options": {
            "A": "It reduces the model's size significantly",
            "B": "It eliminates the need for a GPU",
            "C": "It allows the model to access real-time internet data",
            "D": "It adapts the model to produce outputs in the required format and style"
        },
        "zh_options": {
            "A": "它顯著縮小了模型大小",
            "B": "它消除了對 GPU 的需求",
            "C": "它允許模型存取即時網際網路資料",
            "D": "它使模型能夠以所需格式和風格產生輸出"
        },
        "answer": "D",
        "explanation": "Fine-tuning adapts a pre-trained model to specific tasks, formats, and styles by training on task-specific labeled data. This teaches the model to consistently produce outputs matching the required format and style.",
        "zh_explanation": "微調通過在特定任務標記資料上訓練，將預訓練模型調整為特定任務、格式和風格。這教導模型一致地產生符合所需格式和風格的輸出。",
        "category": "AIF",
        "option_explanations": {
            "A": "微調通常不會縮小模型大小，LoRA 等技術是例外。",
            "B": "微調通常需要 GPU，不能消除 GPU 需求。",
            "C": "微調改變模型參數，不提供即時網際網路存取能力。",
            "D": "正確。微調使模型學習特定的輸出格式和風格。"
        }
    },
    {
        "id": 219,
        "question": "A company wants to fine-tune a model using Amazon Bedrock to make a customer service chatbot respond in the company's specific tone. What input does the company need to provide for this fine-tuning job?",
        "zh_question": "一家公司想使用 Amazon Bedrock 微調模型，使客戶服務聊天機器人以公司特定的語氣回應。公司需要為此微調工作提供什麼輸入？",
        "options": {
            "A": "Unlabeled customer service transcripts",
            "B": "A description of the desired tone in natural language",
            "C": "Competitor chatbot conversation logs",
            "D": "Labeled training data with prompts and desired completions in the required tone"
        },
        "zh_options": {
            "A": "未標記的客戶服務記錄",
            "B": "用自然語言描述所需語氣",
            "C": "競爭對手聊天機器人的對話日誌",
            "D": "帶有提示和所需語氣完成內容的標記訓練資料"
        },
        "answer": "D",
        "explanation": "For instruction fine-tuning (teaching specific tone/style), you need labeled training data pairs: prompts (customer questions) and completions (responses in the desired tone). This teaches the model through examples.",
        "zh_explanation": "對於指令微調（教導特定語氣/風格），需要標記訓練資料對：提示（客戶問題）和完成（所需語氣的回應）。這通過範例教導模型。",
        "category": "AIF",
        "option_explanations": {
            "A": "未標記記錄用於持續預訓練，不適用於教導特定語氣的微調。",
            "B": "自然語言描述可用於系統提示，但不足以作為微調訓練資料。",
            "C": "競爭對手的對話日誌可能不符合公司特定語氣要求。",
            "D": "正確。帶有所需語氣回應的標記提示-完成對是微調的必要輸入。"
        }
    },
    {
        "id": 220,
        "question": "A company is deploying a specialized AI assistant for medical professionals. The company wants the model to use correct medical terminology. Which approach is MOST appropriate?",
        "zh_question": "一家公司正在為醫療專業人員部署專業 AI 助理。公司希望模型使用正確的醫學術語。哪種方法最合適？",
        "options": {
            "A": "Zero-shot prompting with medical terminology requests",
            "B": "Fine-tune the model on medical literature and documentation",
            "C": "Increase the model temperature to 2.0",
            "D": "Use a general-purpose model without customization"
        },
        "zh_options": {
            "A": "使用醫學術語請求進行零樣本提示",
            "B": "在醫學文獻和文件上微調模型",
            "C": "將模型溫度增加到 2.0",
            "D": "使用未自定義的通用模型"
        },
        "answer": "B",
        "explanation": "Fine-tuning on medical literature and documentation teaches the model domain-specific terminology, clinical context, and appropriate professional language. This is more effective than prompt engineering for specialized vocabulary.",
        "zh_explanation": "在醫學文獻和文件上進行微調教導模型特定領域的術語、臨床上下文和適當的專業語言。對於專業詞彙，這比提示工程更有效。",
        "category": "AIF",
        "option_explanations": {
            "A": "零樣本提示對醫學術語的掌握有限，基礎模型可能缺乏深度醫學知識。",
            "B": "正確。在醫學資料上微調使模型深度學習醫學術語和知識。",
            "C": "增加溫度使輸出更隨機，不會改善術語準確性。",
            "D": "通用模型的醫學術語知識有限，不適合醫療專業場景。"
        }
    },
    {
        "id": 221,
        "question": "A developer is preparing training data for instruction-based fine-tuning. Which data format should the developer use?",
        "zh_question": "一位開發人員正在為基於指令的微調準備訓練資料。開發人員應使用哪種資料格式？",
        "options": {
            "A": "Raw text documents without any structure",
            "B": "Image-label pairs for computer vision tasks",
            "C": "Question and answer pairs with instructions",
            "D": "Numerical feature vectors"
        },
        "zh_options": {
            "A": "沒有任何結構的原始文字文件",
            "B": "用於電腦視覺任務的圖像-標籤對",
            "C": "帶有指令的問題和答案對",
            "D": "數值特徵向量"
        },
        "answer": "C",
        "explanation": "Instruction-based fine-tuning requires structured prompt-completion pairs: an instruction/question (prompt) and the correct response (completion). This format teaches the model to follow instructions and produce appropriate outputs.",
        "zh_explanation": "基於指令的微調需要結構化的提示-完成對：指令/問題（提示）和正確回應（完成）。這種格式教導模型遵循指令並產生適當的輸出。",
        "category": "AIF",
        "option_explanations": {
            "A": "原始文字文件用於持續預訓練，不適合指令式微調。",
            "B": "圖像-標籤對適用於電腦視覺分類任務，不適合語言指令微調。",
            "C": "正確。問答對格式是指令式微調的標準輸入格式。",
            "D": "數值特徵向量是傳統機器學習的輸入格式，不適合語言模型微調。"
        }
    },
    {
        "id": 222,
        "question": "A machine learning team needs to evaluate the runtime efficiency of their deployed LLM. Which metric should the team use?",
        "zh_question": "機器學習團隊需要評估其已部署 LLM 的運行時效率。團隊應使用哪個指標？",
        "options": {
            "A": "BLEU score",
            "B": "F1 score",
            "C": "Average response time (latency)",
            "D": "Training loss"
        },
        "zh_options": {
            "A": "BLEU 分數",
            "B": "F1 分數",
            "C": "平均回應時間（延遲）",
            "D": "訓練損失"
        },
        "answer": "C",
        "explanation": "Average response time (latency) measures how quickly the model responds to requests, which is the primary metric for runtime efficiency. Lower latency indicates better runtime performance.",
        "zh_explanation": "平均回應時間（延遲）衡量模型回應請求的速度，是運行時效率的主要指標。較低的延遲表示更好的運行時效能。",
        "category": "AIF",
        "option_explanations": {
            "A": "BLEU 分數評估文字生成品質（主要用於翻譯），不評估效率。",
            "B": "F1 分數評估分類準確性，不評估運行時效率。",
            "C": "正確。平均回應時間/延遲是衡量運行時效率的核心指標。",
            "D": "訓練損失在訓練時使用，不反映已部署模型的運行效率。"
        }
    },
    {
        "id": 223,
        "question": "A company has deployed an LLM-based customer service chatbot to handle customer calls. The company wants to measure whether the chatbot is achieving its business objective of reducing customer service costs. Which business metric should the company track?",
        "zh_question": "一家公司已部署基於 LLM 的客戶服務聊天機器人來處理客戶來電。公司希望衡量聊天機器人是否實現了降低客戶服務成本的業務目標。公司應追蹤哪個業務指標？",
        "options": {
            "A": "Model perplexity score",
            "B": "Average call duration",
            "C": "BLEU score for response quality",
            "D": "Training data size"
        },
        "zh_options": {
            "A": "模型困惑度分數",
            "B": "平均通話時長",
            "C": "回應品質的 BLEU 分數",
            "D": "訓練資料大小"
        },
        "answer": "B",
        "explanation": "Average call duration is a direct business metric: shorter calls mean the chatbot resolves issues more efficiently, reducing operational costs (agent time, infrastructure). It directly measures cost reduction effectiveness.",
        "zh_explanation": "平均通話時長是直接的業務指標：通話時間越短意味著聊天機器人更有效地解決問題，從而降低運營成本（代理時間、基礎設施）。它直接衡量降低成本的效果。",
        "category": "AIF",
        "option_explanations": {
            "A": "困惑度是模型品質指標，不直接反映業務成本節省。",
            "B": "正確。平均通話時長直接反映客戶服務效率和成本節省。",
            "C": "BLEU 分數評估文字品質，不直接反映業務目標達成情況。",
            "D": "訓練資料大小是模型開發因素，不是業務效能指標。"
        }
    },
    {
        "id": 224,
        "question": "A data scientist has built an image classification model and needs to evaluate its performance. The data scientist wants to understand the number of correct and incorrect predictions for each class. Which evaluation tool should the data scientist use?",
        "zh_question": "一位資料科學家構建了一個圖像分類模型，需要評估其效能。資料科學家希望了解每個類別的正確和錯誤預測數量。資料科學家應使用哪種評估工具？",
        "options": {
            "A": "Confusion matrix",
            "B": "BLEU score",
            "C": "Perplexity",
            "D": "ROUGE score"
        },
        "zh_options": {
            "A": "混淆矩陣",
            "B": "BLEU 分數",
            "C": "困惑度",
            "D": "ROUGE 分數"
        },
        "answer": "A",
        "explanation": "A confusion matrix shows the counts of true positives, true negatives, false positives, and false negatives for each class, allowing detailed analysis of correct and incorrect predictions by category.",
        "zh_explanation": "混淆矩陣顯示每個類別的真陽性、真陰性、假陽性和假陰性的計數，允許對每個類別的正確和錯誤預測進行詳細分析。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。混淆矩陣展示每個類別的預測分佈，包括正確和錯誤分類。",
            "B": "BLEU 分數用於評估文字生成品質（翻譯），不適用於圖像分類。",
            "C": "困惑度衡量語言模型的預測不確定性，不適用於圖像分類。",
            "D": "ROUGE 分數評估文字摘要品質，不適用於圖像分類。"
        }
    },
    {
        "id": 225,
        "question": "A machine learning team has built a translation model and wants to evaluate the quality of its translations. Which metric should the team use?",
        "zh_question": "一個機器學習團隊構建了一個翻譯模型，希望評估其翻譯品質。團隊應使用哪個指標？",
        "options": {
            "A": "BLEU score",
            "B": "F1 score",
            "C": "Accuracy",
            "D": "Precision"
        },
        "zh_options": {
            "A": "BLEU 分數",
            "B": "F1 分數",
            "C": "準確率",
            "D": "精確率"
        },
        "answer": "A",
        "explanation": "BLEU (Bilingual Evaluation Understudy) is the standard metric for evaluating machine translation quality. It measures n-gram overlap between the generated translation and reference translations.",
        "zh_explanation": "BLEU（雙語評估替代）是評估機器翻譯品質的標準指標。它衡量生成翻譯與參考翻譯之間的 n-gram 重疊度。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。BLEU 是評估機器翻譯品質的標準指標，衡量 n-gram 重疊。",
            "B": "F1 分數用於分類任務，不適合評估翻譯品質。",
            "C": "準確率用於分類任務，不適合評估翻譯的連續品質。",
            "D": "精確率用於分類任務，不是翻譯品質的合適指標。"
        }
    },
    {
        "id": 226,
        "question": "A company has fine-tuned an LLM for customer service and wants to evaluate how well the model balances correctly identifying customer issues and avoiding false alarms. Which metric should the company use?",
        "zh_question": "一家公司對 LLM 進行了微調用於客戶服務，希望評估模型在正確識別客戶問題和避免誤報之間的平衡情況。公司應使用哪個指標？",
        "options": {
            "A": "BLEU score",
            "B": "Accuracy",
            "C": "F1 score",
            "D": "Perplexity"
        },
        "zh_options": {
            "A": "BLEU 分數",
            "B": "準確率",
            "C": "F1 分數",
            "D": "困惑度"
        },
        "answer": "C",
        "explanation": "F1 score balances precision (avoiding false alarms) and recall (correctly identifying issues). It's ideal when you need to evaluate both the model's ability to find true positives and avoid false positives.",
        "zh_explanation": "F1 分數平衡精確率（避免誤報）和召回率（正確識別問題）。當需要評估模型找到真陽性和避免假陽性的能力時，它是理想選擇。",
        "category": "AIF",
        "option_explanations": {
            "A": "BLEU 分數用於翻譯品質評估，不適合分類平衡評估。",
            "B": "準確率在類別不平衡時可能誤導，不能單獨評估精確率和召回率的平衡。",
            "C": "正確。F1 分數是精確率和召回率的調和平均，衡量兩者的平衡。",
            "D": "困惑度是語言模型的生成品質指標，不適合分類評估。"
        }
    },
    {
        "id": 227,
        "question": "A company has built an AI application that summarizes customer feedback. Which metric should the company use to evaluate the quality of the summaries?",
        "zh_question": "一家公司構建了一個摘要客戶回饋的 AI 應用程式。公司應使用哪個指標來評估摘要的品質？",
        "options": {
            "A": "Confusion matrix",
            "B": "BLEU or ROUGE score",
            "C": "Mean squared error",
            "D": "Area under the ROC curve"
        },
        "zh_options": {
            "A": "混淆矩陣",
            "B": "BLEU 或 ROUGE 分數",
            "C": "均方誤差",
            "D": "ROC 曲線下面積"
        },
        "answer": "B",
        "explanation": "BLEU and ROUGE are standard metrics for evaluating text generation tasks like summarization. ROUGE is particularly designed for summarization evaluation, measuring n-gram overlap between generated and reference summaries.",
        "zh_explanation": "BLEU 和 ROUGE 是評估文字生成任務（如摘要）的標準指標。ROUGE 特別為摘要評估設計，衡量生成摘要和參考摘要之間的 n-gram 重疊度。",
        "category": "AIF",
        "option_explanations": {
            "A": "混淆矩陣用於分類任務，不適合文字摘要評估。",
            "B": "正確。BLEU/ROUGE 是文字生成和摘要任務的標準評估指標。",
            "C": "均方誤差用於回歸問題，不適合評估文字品質。",
            "D": "AUC-ROC 用於二元分類評估，不適合文字摘要品質評估。"
        }
    },
    {
        "id": 228,
        "question": "At which stage of the generative AI application lifecycle does model evaluation typically occur?",
        "zh_question": "在生成式 AI 應用程式生命週期的哪個階段通常會進行模型評估？",
        "options": {
            "A": "During initial data collection",
            "B": "Before selecting the foundation model",
            "C": "During model pre-training",
            "D": "After fine-tuning and before deployment"
        },
        "zh_options": {
            "A": "在初始資料收集期間",
            "B": "在選擇基礎模型之前",
            "C": "在模型預訓練期間",
            "D": "在微調之後、部署之前"
        },
        "answer": "D",
        "explanation": "Model evaluation typically occurs after fine-tuning (to assess how well the customization worked) and before deployment (to ensure the model meets requirements before going live). This is a critical quality gate in the ML lifecycle.",
        "zh_explanation": "模型評估通常在微調之後（評估自定義效果）和部署之前（確保模型在上線前符合要求）進行。這是 ML 生命週期中的關鍵品質把關點。",
        "category": "AIF",
        "option_explanations": {
            "A": "資料收集是前期準備階段，模型尚未存在，無法評估。",
            "B": "選擇基礎模型前進行的是需求分析，不是模型評估。",
            "C": "預訓練期間有訓練指標監控，但正式評估在訓練後進行。",
            "D": "正確。微調後、部署前是模型評估的標準時間點。"
        }
    },
    {
        "id": 229,
        "question": "A data scientist needs to evaluate a binary classification model. The data scientist wants a metric that considers both false positives and false negatives. Which metric should the data scientist use?",
        "zh_question": "一位資料科學家需要評估二元分類模型。資料科學家希望使用同時考慮假陽性和假陰性的指標。資料科學家應使用哪個指標？",
        "options": {
            "A": "F1 score",
            "B": "BLEU score",
            "C": "Perplexity",
            "D": "ROUGE score"
        },
        "zh_options": {
            "A": "F1 分數",
            "B": "BLEU 分數",
            "C": "困惑度",
            "D": "ROUGE 分數"
        },
        "answer": "A",
        "explanation": "F1 score is the harmonic mean of precision and recall. Precision accounts for false positives (predicted positive but actually negative), while recall accounts for false negatives (actually positive but predicted negative).",
        "zh_explanation": "F1 分數是精確率和召回率的調和平均數。精確率考慮假陽性（預測為正但實際為負），而召回率考慮假陰性（實際為正但預測為負）。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。F1 分數通過精確率和召回率同時考慮假陽性和假陰性。",
            "B": "BLEU 分數用於文字生成評估，不適合二元分類。",
            "C": "困惑度是語言模型的生成指標，不適合分類評估。",
            "D": "ROUGE 分數用於文字摘要評估，不適合二元分類。"
        }
    },
    {
        "id": 230,
        "question": "A company has deployed a machine learning model in production and wants to detect when the model's performance degrades due to changes in input data distribution. Which AWS service should the company use?",
        "zh_question": "一家公司已在生產環境中部署了機器學習模型，希望在輸入資料分佈變化導致模型效能下降時進行偵測。公司應使用哪個 AWS 服務？",
        "options": {
            "A": "Amazon SageMaker Training Job",
            "B": "Amazon Bedrock Knowledge Bases",
            "C": "Amazon SageMaker Clarify",
            "D": "Amazon SageMaker Model Monitor"
        },
        "zh_options": {
            "A": "Amazon SageMaker 訓練工作",
            "B": "Amazon Bedrock Knowledge Bases",
            "C": "Amazon SageMaker Clarify",
            "D": "Amazon SageMaker Model Monitor"
        },
        "answer": "D",
        "explanation": "Amazon SageMaker Model Monitor continuously monitors deployed models for data drift, model quality drift, and bias drift. It alerts when model performance degrades due to changes in input data distribution.",
        "zh_explanation": "Amazon SageMaker Model Monitor 持續監控已部署模型的資料漂移、模型品質漂移和偏差漂移。當輸入資料分佈變化導致模型效能下降時發出警報。",
        "category": "AIF",
        "option_explanations": {
            "A": "SageMaker 訓練工作用於訓練模型，不用於監控生產模型。",
            "B": "Bedrock Knowledge Bases 實施 RAG，不用於模型效能監控。",
            "C": "SageMaker Clarify 用於偏差偵測和可解釋性，不專門監控資料漂移。",
            "D": "正確。SageMaker Model Monitor 專門用於偵測生產環境中的模型效能下降和資料漂移。"
        }
    },
]
