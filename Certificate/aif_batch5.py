AIF_BATCH5 = [
    {
        "id": 231,
        "question": "A company has fine-tuned an LLM to predict customer churn. The company wants to evaluate model performance considering both precision and recall. Which metric should the company use?",
        "zh_question": "一家公司微調了 LLM 來預測客戶流失。公司希望同時考慮精確率和召回率來評估模型效能。公司應使用哪個指標？",
        "options": {
            "A": "BLEU score",
            "B": "ROUGE score",
            "C": "F1 score",
            "D": "Perplexity"
        },
        "zh_options": {
            "A": "BLEU 分數",
            "B": "ROUGE 分數",
            "C": "F1 分數",
            "D": "困惑度"
        },
        "answer": "C",
        "explanation": "F1 score is the harmonic mean of precision and recall, making it the ideal metric when both are important. For churn prediction, missing churners (low recall) and false alarms (low precision) both have business costs.",
        "zh_explanation": "F1 分數是精確率和召回率的調和平均數，是同時需要兩者時的理想指標。在流失預測中，漏掉流失客戶（低召回率）和誤報（低精確率）都有業務成本。",
        "category": "AIF",
        "option_explanations": {
            "A": "BLEU 分數用於翻譯品質評估，不適合分類問題。",
            "B": "ROUGE 分數用於文字摘要評估，不適合分類問題。",
            "C": "正確。F1 分數平衡精確率和召回率，適合需要兩者兼顧的分類任務。",
            "D": "困惑度是語言模型的文字生成指標，不適合分類評估。"
        }
    },
    {
        "id": 232,
        "question": "A company uses a BLEU score to evaluate its translation model. The data scientist explains that BLEU measures relative translation quality. What does this mean?",
        "zh_question": "一家公司使用 BLEU 分數來評估其翻譯模型。資料科學家解釋說 BLEU 衡量相對翻譯品質。這是什麼意思？",
        "options": {
            "A": "BLEU measures the absolute correctness of each word",
            "B": "BLEU compares the translation against reference translations rather than measuring absolute correctness",
            "C": "BLEU only works for specific language pairs",
            "D": "BLEU requires human evaluators to score translations"
        },
        "zh_options": {
            "A": "BLEU 衡量每個詞的絕對正確性",
            "B": "BLEU 將翻譯與參考翻譯進行比較，而不是衡量絕對正確性",
            "C": "BLEU 只適用於特定語言對",
            "D": "BLEU 需要人工評估員對翻譯評分"
        },
        "answer": "B",
        "explanation": "BLEU is a relative metric that compares n-gram overlap between the generated translation and one or more human reference translations. A high BLEU means the output is similar to references, not that it is perfectly correct.",
        "zh_explanation": "BLEU 是一個相對指標，比較生成翻譯與一個或多個人工參考翻譯之間的 n-gram 重疊度。高 BLEU 意味著輸出與參考相似，而不是絕對正確。",
        "category": "AIF",
        "option_explanations": {
            "A": "BLEU 不衡量每個詞的絕對正確性，而是整體 n-gram 重疊。",
            "B": "正確。BLEU 通過與參考翻譯比較來評估品質，是相對而非絕對指標。",
            "C": "BLEU 可用於任何語言對，不限於特定語言。",
            "D": "BLEU 是自動指標，不需要人工評估員。"
        }
    },
    {
        "id": 233,
        "question": "A company has built a creative writing AI application. The company wants to evaluate the semantic similarity between the AI's output and reference texts, even when the AI uses different words or creative spelling. Which metric is MOST appropriate?",
        "zh_question": "一家公司建立了一個創意寫作 AI 應用程式。公司希望評估 AI 輸出與參考文字之間的語意相似性，即使 AI 使用不同的詞語或創意拼寫。哪個指標最合適？",
        "options": {
            "A": "BLEU score",
            "B": "BERTScore",
            "C": "Accuracy",
            "D": "Precision"
        },
        "zh_options": {
            "A": "BLEU 分數",
            "B": "BERTScore",
            "C": "準確率",
            "D": "精確率"
        },
        "answer": "B",
        "explanation": "BERTScore uses contextual embeddings from BERT to compute semantic similarity between generated and reference text. Unlike BLEU, it captures meaning even when different words are used, making it ideal for creative writing evaluation.",
        "zh_explanation": "BERTScore 使用 BERT 的上下文嵌入來計算生成文字與參考文字之間的語意相似性。與 BLEU 不同，它即使在使用不同詞語時也能捕捉含義，非常適合創意寫作評估。",
        "category": "AIF",
        "option_explanations": {
            "A": "BLEU 基於精確的 n-gram 匹配，無法處理創意用詞和語意相似性。",
            "B": "正確。BERTScore 衡量語意相似性，不要求詞語完全匹配，適合創意文字評估。",
            "C": "準確率用於分類任務，不適合評估創意文字品質。",
            "D": "精確率用於分類任務，不適合語意相似性評估。"
        }
    },
    {
        "id": 234,
        "question": "A data scientist is evaluating a binary classification model for customer churn prediction. The data scientist wants a single metric that balances both the model's precision and recall. Which metric should the data scientist use?",
        "zh_question": "一位資料科學家正在評估用於客戶流失預測的二元分類模型。資料科學家希望使用能夠平衡模型精確率和召回率的單一指標。資料科學家應使用哪個指標？",
        "options": {
            "A": "F1 score",
            "B": "BLEU score",
            "C": "Perplexity",
            "D": "ROUGE-L"
        },
        "zh_options": {
            "A": "F1 分數",
            "B": "BLEU 分數",
            "C": "困惑度",
            "D": "ROUGE-L"
        },
        "answer": "A",
        "explanation": "F1 score (harmonic mean of precision and recall) is the standard single metric that balances precision and recall for binary classification tasks. It penalizes models that sacrifice one for the other.",
        "zh_explanation": "F1 分數（精確率和召回率的調和平均數）是平衡二元分類任務精確率和召回率的標準單一指標。它懲罰以犧牲其中一個來提高另一個的模型。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。F1 分數是平衡精確率和召回率的標準指標。",
            "B": "BLEU 用於翻譯評估，不適合分類任務。",
            "C": "困惑度衡量語言模型的不確定性，不適合分類評估。",
            "D": "ROUGE-L 用於摘要評估，不適合分類任務。"
        }
    },
    {
        "id": 235,
        "question": "A data scientist is evaluating a classification model. The data scientist wants to know the proportion of all predictions that the model got correct. Which metric should the data scientist use?",
        "zh_question": "一位資料科學家正在評估分類模型。資料科學家希望了解模型所有預測中正確的比例。資料科學家應使用哪個指標？",
        "options": {
            "A": "Accuracy",
            "B": "BLEU score",
            "C": "Perplexity",
            "D": "ROUGE score"
        },
        "zh_options": {
            "A": "準確率",
            "B": "BLEU 分數",
            "C": "困惑度",
            "D": "ROUGE 分數"
        },
        "answer": "A",
        "explanation": "Accuracy = (correctly classified instances) / (total instances). It measures the proportion of predictions that are correct across all classes, making it the most intuitive overall performance metric.",
        "zh_explanation": "準確率 = 正確分類的實例 / 總實例數。它衡量所有類別中正確預測的比例，是最直觀的整體效能指標。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。準確率 = 正確預測數 / 總預測數，直接衡量預測正確比例。",
            "B": "BLEU 用於翻譯品質評估，不是分類指標。",
            "C": "困惑度衡量語言模型預測的不確定性，不是分類正確率指標。",
            "D": "ROUGE 用於摘要評估，不是分類指標。"
        }
    },
    {
        "id": 236,
        "question": "A company has deployed a customer segmentation model using Amazon SageMaker. The company is concerned about model bias and wants to monitor for data and model quality changes over time. Which AWS service should the company use?",
        "zh_question": "一家公司已使用 Amazon SageMaker 部署了客戶細分模型。公司擔心模型偏差，並希望監控資料和模型品質隨時間的變化。公司應使用哪個 AWS 服務？",
        "options": {
            "A": "Amazon SageMaker Model Monitor",
            "B": "Amazon SageMaker Training",
            "C": "Amazon Bedrock Guardrails",
            "D": "Amazon CloudWatch only"
        },
        "zh_options": {
            "A": "Amazon SageMaker Model Monitor",
            "B": "Amazon SageMaker 訓練",
            "C": "Amazon Bedrock Guardrails",
            "D": "僅 Amazon CloudWatch"
        },
        "answer": "A",
        "explanation": "Amazon SageMaker Model Monitor provides continuous monitoring for data drift, model quality, bias drift, and feature attribution drift. It's specifically designed to detect quality changes in production models over time.",
        "zh_explanation": "Amazon SageMaker Model Monitor 提供對資料漂移、模型品質、偏差漂移和特徵歸因漂移的持續監控。它專門設計用於偵測生產模型隨時間的品質變化。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。SageMaker Model Monitor 專門監控生產模型的資料品質、模型品質和偏差漂移。",
            "B": "SageMaker 訓練用於模型訓練，不用於生產監控。",
            "C": "Bedrock Guardrails 用於 Bedrock 模型的內容過濾，不監控 SageMaker 模型漂移。",
            "D": "CloudWatch 可監控基礎設施指標，但缺少專業的 ML 模型品質監控功能。"
        }
    },
    {
        "id": 237,
        "question": "A company wants to proactively detect when their deployed ML model's predictions start to degrade in quality due to changes in the input data. Which AWS service addresses this requirement?",
        "zh_question": "一家公司希望主動偵測其已部署 ML 模型的預測因輸入資料的變化而開始品質下降的情況。哪個 AWS 服務滿足此需求？",
        "options": {
            "A": "AWS Lambda for scheduled evaluations",
            "B": "Amazon SageMaker Experiments",
            "C": "Amazon SageMaker Clarify",
            "D": "Amazon SageMaker Model Monitor"
        },
        "zh_options": {
            "A": "AWS Lambda 用於定期評估",
            "B": "Amazon SageMaker Experiments",
            "C": "Amazon SageMaker Clarify",
            "D": "Amazon SageMaker Model Monitor"
        },
        "answer": "D",
        "explanation": "Amazon SageMaker Model Monitor automatically monitors endpoints for data drift and model quality degradation. It compares current data statistics against a baseline and alerts when significant drift is detected.",
        "zh_explanation": "Amazon SageMaker Model Monitor 自動監控端點的資料漂移和模型品質下降。它將當前資料統計資訊與基準進行比較，並在偵測到顯著漂移時發出警報。",
        "category": "AIF",
        "option_explanations": {
            "A": "Lambda 可用於自定義評估，但缺少開箱即用的 ML 模型漂移偵測功能。",
            "B": "SageMaker Experiments 用於追蹤和比較實驗，不用於生產監控。",
            "C": "SageMaker Clarify 用於偏差分析和可解釋性，不專門監控模型品質下降。",
            "D": "正確。SageMaker Model Monitor 是專為偵測生產環境模型品質下降設計的服務。"
        }
    },
    {
        "id": 238,
        "question": "A company has fine-tuned two different foundation models for content moderation. The company wants to compare the models' toxicity detection capabilities automatically. Which approach should the company use?",
        "zh_question": "一家公司對兩個不同的基礎模型進行了微調以用於內容審核。公司希望自動比較模型的毒性偵測能力。公司應使用哪種方法？",
        "options": {
            "A": "Manual human evaluation of random samples",
            "B": "Use Amazon Bedrock Model Evaluation with toxicity as the evaluation criterion",
            "C": "Compare training loss curves only",
            "D": "Deploy both models and track user complaints"
        },
        "zh_options": {
            "A": "對隨機樣本進行人工評估",
            "B": "使用 Amazon Bedrock Model Evaluation，以毒性作為評估標準",
            "C": "僅比較訓練損失曲線",
            "D": "部署兩個模型並追蹤使用者投訴"
        },
        "answer": "B",
        "explanation": "Amazon Bedrock Model Evaluation provides automated evaluation capabilities including toxicity detection. It allows systematic comparison of multiple models against specific criteria like toxicity, quality, and safety.",
        "zh_explanation": "Amazon Bedrock Model Evaluation 提供自動化評估功能，包括毒性偵測。它允許根據毒性、品質和安全性等特定標準系統化地比較多個模型。",
        "category": "AIF",
        "option_explanations": {
            "A": "人工評估耗時且難以規模化，不如自動評估高效。",
            "B": "正確。Bedrock Model Evaluation 提供自動化毒性評估，可系統比較多個模型。",
            "C": "訓練損失只反映訓練過程，不能直接比較毒性偵測能力。",
            "D": "部署後追蹤投訴有延遲且可能造成用戶傷害，不是比較模型的好方法。"
        }
    },
    {
        "id": 239,
        "question": "A company wants to use Amazon Bedrock Guardrails to filter inappropriate content in their customer-facing AI application. Which TWO content categories can be filtered using Bedrock Guardrails? (Choose TWO)",
        "zh_question": "一家公司希望使用 Amazon Bedrock Guardrails 過濾其面向客戶的 AI 應用程式中的不當內容。哪兩個內容類別可以使用 Bedrock Guardrails 過濾？（選擇兩個）",
        "options": {
            "A": "Hate speech",
            "B": "Competitor product mentions",
            "C": "Violence",
            "D": "Technical jargon",
            "E": "Long responses"
        },
        "zh_options": {
            "A": "仇恨言論",
            "B": "競爭對手產品提及",
            "C": "暴力",
            "D": "技術術語",
            "E": "長篇回應"
        },
        "answer": "AC",
        "explanation": "Amazon Bedrock Guardrails can filter harmful content categories including hate speech, violence, sexual content, insults, and misconduct. Hate speech (A) and violence (C) are both standard filterable content categories.",
        "zh_explanation": "Amazon Bedrock Guardrails 可以過濾有害內容類別，包括仇恨言論、暴力、性內容、侮辱和不當行為。仇恨言論（A）和暴力（C）都是標準的可過濾內容類別。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。仇恨言論是 Bedrock Guardrails 支援過濾的標準有害內容類別。",
            "B": "競爭對手提及可用「拒絕主題」功能處理，但不是預設的有害內容類別。",
            "C": "正確。暴力內容是 Bedrock Guardrails 支援過濾的標準有害內容類別。",
            "D": "技術術語不是有害內容，Guardrails 不過濾此類內容。",
            "E": "回應長度不是有害內容，Guardrails 不基於長度過濾。"
        }
    },
    {
        "id": 240,
        "question": "A company wants to use Amazon Bedrock Guardrails to prevent their AI assistant from discussing political topics. Which Bedrock Guardrails feature should the company use?",
        "zh_question": "一家公司希望使用 Amazon Bedrock Guardrails 阻止其 AI 助理討論政治話題。公司應使用哪個 Bedrock Guardrails 功能？",
        "options": {
            "A": "Content filters for harmful categories",
            "B": "Denied topics",
            "C": "Word filters",
            "D": "Sensitive information filters"
        },
        "zh_options": {
            "A": "有害類別的內容過濾器",
            "B": "拒絕主題",
            "C": "詞語過濾器",
            "D": "敏感資訊過濾器"
        },
        "answer": "B",
        "explanation": "The 'Denied topics' feature in Bedrock Guardrails allows companies to define specific topics that the AI should not discuss. Political topics can be configured as a denied topic, causing the model to refuse such discussions.",
        "zh_explanation": "Bedrock Guardrails 中的「拒絕主題」功能允許公司定義 AI 不應討論的特定主題。可以將政治主題配置為拒絕主題，使模型拒絕此類討論。",
        "category": "AIF",
        "option_explanations": {
            "A": "內容過濾器用於過濾仇恨、暴力等有害內容，不用於特定主題限制。",
            "B": "正確。拒絕主題功能允許定義 AI 不應討論的特定話題，如政治話題。",
            "C": "詞語過濾器針對特定詞彙，不能有效阻止整個主題的討論。",
            "D": "敏感資訊過濾器用於 PII 等敏感個人資訊，不用於主題限制。"
        }
    },
    {
        "id": 241,
        "question": "A company is developing an AI model to screen job resumes. A data scientist discovers that the training dataset contains mostly resumes from male candidates. Which responsible AI principle is MOST at risk?",
        "zh_question": "一家公司正在開發一個 AI 模型來篩選求職履歷。一位資料科學家發現訓練資料集主要包含男性候選人的履歷。哪個負責任 AI 原則面臨最大風險？",
        "options": {
            "A": "Fairness",
            "B": "Explainability",
            "C": "Privacy",
            "D": "Performance"
        },
        "zh_options": {
            "A": "公平性",
            "B": "可解釋性",
            "C": "隱私",
            "D": "效能"
        },
        "answer": "A",
        "explanation": "A dataset with mostly male resumes will cause the model to be biased against female candidates, violating the fairness principle. The model may unfairly discriminate based on gender due to the imbalanced training data.",
        "zh_explanation": "以男性履歷為主的資料集將導致模型對女性候選人存在偏見，違反公平性原則。由於訓練資料不平衡，模型可能基於性別進行不公平歧視。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。不平衡的訓練資料（以男性為主）會使模型對女性候選人產生不公平偏見。",
            "B": "可解釋性關注理解模型決策，不是此場景的主要風險。",
            "C": "隱私關注個人資料保護，不是此場景的主要風險。",
            "D": "效能是模型準確性問題，不是此場景的核心倫理風險。"
        }
    },
    {
        "id": 242,
        "question": "A healthcare company is building an AI application using Amazon Bedrock. The company needs to ensure patient PII is never included in AI responses and that content is appropriate for medical use. Which combination of services should the company use?",
        "zh_question": "一家醫療公司正在使用 Amazon Bedrock 構建 AI 應用程式。公司需要確保 AI 回應中絕不包含患者 PII，並且內容適合醫療使用。公司應使用哪種服務組合？",
        "options": {
            "A": "Amazon Rekognition and Amazon Textract",
            "B": "Amazon SageMaker and AWS Lambda",
            "C": "Amazon Bedrock Guardrails with PII and content filters",
            "D": "Amazon Macie and AWS Shield"
        },
        "zh_options": {
            "A": "Amazon Rekognition 和 Amazon Textract",
            "B": "Amazon SageMaker 和 AWS Lambda",
            "C": "帶有 PII 和內容過濾器的 Amazon Bedrock Guardrails",
            "D": "Amazon Macie 和 AWS Shield"
        },
        "answer": "C",
        "explanation": "Amazon Bedrock Guardrails with PII filtering (sensitive information filters) and content filters provides comprehensive protection: it blocks PII from appearing in responses and filters inappropriate content for medical contexts.",
        "zh_explanation": "帶有 PII 過濾（敏感資訊過濾器）和內容過濾器的 Amazon Bedrock Guardrails 提供全面保護：阻止 PII 出現在回應中，並過濾不適合醫療情境的內容。",
        "category": "AIF",
        "option_explanations": {
            "A": "Rekognition 用於圖像分析，Textract 用於文字擷取，不用於 AI 回應過濾。",
            "B": "SageMaker 和 Lambda 是通用服務，需要自定義實施 PII 保護。",
            "C": "正確。Bedrock Guardrails 的 PII 過濾和內容過濾直接解決醫療 AI 的安全需求。",
            "D": "Macie 用於發現 S3 中的 PII，Shield 用於 DDoS 防護，都不用於 AI 回應過濾。"
        }
    },
    {
        "id": 243,
        "question": "A company is concerned about their LLM providing inaccurate information that is not grounded in factual sources. Which Amazon Bedrock feature helps prevent hallucinations by grounding responses in verified information?",
        "zh_question": "一家公司擔心其 LLM 提供未基於事實來源的不準確資訊。哪個 Amazon Bedrock 功能通過將回應建立在已驗證資訊上來幫助防止幻覺？",
        "options": {
            "A": "Bedrock Fine-tuning",
            "B": "Bedrock Guardrails with grounding checks",
            "C": "Bedrock Model Evaluation",
            "D": "Bedrock Agents"
        },
        "zh_options": {
            "A": "Bedrock 微調",
            "B": "帶有基礎檢查的 Bedrock Guardrails",
            "C": "Bedrock Model Evaluation",
            "D": "Bedrock Agents"
        },
        "answer": "B",
        "explanation": "Amazon Bedrock Guardrails includes a grounding check feature that verifies whether the model's responses are grounded in the provided context/source documents, helping to prevent hallucinations.",
        "zh_explanation": "Amazon Bedrock Guardrails 包含基礎檢查功能，驗證模型的回應是否建立在提供的上下文/來源文件上，有助於防止幻覺。",
        "category": "AIF",
        "option_explanations": {
            "A": "微調改善模型行為，但不能即時驗證回應是否有事實依據。",
            "B": "正確。Guardrails 的基礎檢查功能驗證回應是否基於事實來源，防止幻覺。",
            "C": "Model Evaluation 用於評估模型效能，不用於即時防止幻覺。",
            "D": "Agents 用於任務自動化，不專門防止幻覺。"
        }
    },
    {
        "id": 244,
        "question": "A company is building a mobile application that uses ML to recognize objects. The company wants to ensure the model works fairly across different demographics. Which action should the company take?",
        "zh_question": "一家公司正在構建使用 ML 識別物體的行動應用程式。公司希望確保模型在不同人口群體中公平運作。公司應採取什麼行動？",
        "options": {
            "A": "Use a diverse dataset that represents different demographics",
            "B": "Train the model only on the most common demographic",
            "C": "Use the highest-performing model regardless of fairness",
            "D": "Skip fairness testing to reduce development time"
        },
        "zh_options": {
            "A": "使用代表不同人口群體的多樣化資料集",
            "B": "僅在最常見的人口群體上訓練模型",
            "C": "不考慮公平性，使用效能最高的模型",
            "D": "跳過公平性測試以減少開發時間"
        },
        "answer": "A",
        "explanation": "Using a diverse dataset that represents different demographics ensures the model is trained on balanced data, preventing it from performing well for some groups while failing for others. This is a fundamental fairness practice.",
        "zh_explanation": "使用代表不同人口群體的多樣化資料集確保模型在平衡資料上訓練，防止模型對某些群體效果好而對其他群體效果差。這是基本的公平性實踐。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。多樣化且代表各人口群體的資料集是確保模型公平性的基礎。",
            "B": "僅在最常見群體上訓練會對少數群體產生偏見，違反公平性。",
            "C": "忽略公平性可能導致對某些群體的歧視性輸出，是不負責任的做法。",
            "D": "跳過公平性測試會導致部署有偏見的模型，可能造成真實傷害。"
        }
    },
    {
        "id": 245,
        "question": "A student submits an essay that was entirely written by an AI writing tool without disclosing this to the teacher. Which responsible AI concern does this situation BEST represent?",
        "zh_question": "一名學生提交了一篇完全由 AI 寫作工具撰寫的文章，而沒有向老師披露這一事實。這種情況最能代表哪個負責任 AI 的問題？",
        "options": {
            "A": "Privacy violation",
            "B": "Security breach",
            "C": "Plagiarism and intellectual dishonesty",
            "D": "Model hallucination"
        },
        "zh_options": {
            "A": "隱私侵犯",
            "B": "安全漏洞",
            "C": "剽竊和學術不誠實",
            "D": "模型幻覺"
        },
        "answer": "C",
        "explanation": "Submitting AI-generated content as one's own work without disclosure is a form of plagiarism and academic dishonesty. This is a key responsible AI concern: transparency about AI-generated content and appropriate attribution.",
        "zh_explanation": "在未披露的情況下將 AI 生成的內容作為自己的作品提交是一種剽竊和學術不誠實行為。這是負責任 AI 的關鍵問題：對 AI 生成內容的透明度和適當歸因。",
        "category": "AIF",
        "option_explanations": {
            "A": "此場景不涉及個人資料的不當收集或使用，不是隱私侵犯。",
            "B": "此場景不涉及系統入侵或資料洩露，不是安全漏洞。",
            "C": "正確。未披露使用 AI 寫作是剽竊和學術不誠實，是核心的負責任 AI 問題。",
            "D": "幻覺是指 AI 生成不實資訊，不是此場景的核心問題。"
        }
    },
    {
        "id": 246,
        "question": "A company is implementing responsible AI practices for their LLM application. Which TWO practices should the company prioritize to ensure responsible AI? (Choose TWO)",
        "zh_question": "一家公司正在為其 LLM 應用程式實施負責任 AI 實踐。公司應優先採用哪兩種實踐以確保負責任 AI？（選擇兩個）",
        "options": {
            "A": "Regularly measure fairness metrics across different demographic groups",
            "B": "Maximize model accuracy regardless of fairness concerns",
            "C": "Identify and mitigate potential biases in training data",
            "D": "Use the largest available model for all tasks",
            "E": "Prioritize speed of deployment over safety testing"
        },
        "zh_options": {
            "A": "定期衡量不同人口群體的公平性指標",
            "B": "不考慮公平性問題，最大化模型準確性",
            "C": "識別並緩解訓練資料中的潛在偏見",
            "D": "對所有任務使用最大的可用模型",
            "E": "優先考慮部署速度而非安全性測試"
        },
        "answer": "AC",
        "explanation": "Responsible AI requires: A) Regularly measuring fairness metrics to detect disparate performance across groups, and C) Identifying and mitigating biases in training data before they propagate to model outputs.",
        "zh_explanation": "負責任 AI 需要：A) 定期衡量公平性指標以偵測群體間的效能差異，以及 C) 在偏見傳播到模型輸出之前識別並緩解訓練資料中的偏見。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。定期測量公平性指標是偵測和解決模型偏見的關鍵實踐。",
            "B": "僅追求準確性而忽略公平性會導致對某些群體的歧視性輸出。",
            "C": "正確。識別並緩解訓練資料偏見是防止模型偏見的根本方法。",
            "D": "模型大小與負責任 AI 無直接關係，且大型模型也可能有偏見。",
            "E": "跳過安全測試以求快速部署是不負責任的，可能導致有害輸出。"
        }
    },
    {
        "id": 247,
        "question": "A company is using AI to classify images of eyewear for their e-commerce platform. The company wants to ensure the accuracy of the AI's decisions. Which responsible AI practice should the company implement?",
        "zh_question": "一家公司正在使用 AI 為其電子商務平台對眼鏡圖像進行分類。公司希望確保 AI 決策的準確性。公司應實施哪種負責任 AI 實踐？",
        "options": {
            "A": "Implement human-in-the-loop review for low-confidence predictions",
            "B": "Deploy the model without any human oversight",
            "C": "Use the model's outputs directly without validation",
            "D": "Increase model complexity to reduce all errors"
        },
        "zh_options": {
            "A": "對低信心預測實施人機協作審查",
            "B": "在沒有任何人工監督的情況下部署模型",
            "C": "直接使用模型輸出而不進行驗證",
            "D": "增加模型複雜度以減少所有錯誤"
        },
        "answer": "A",
        "explanation": "Human-in-the-loop (HITL) review for low-confidence predictions ensures that uncertain AI decisions are reviewed by humans before taking effect. This combines AI efficiency with human oversight for improved accuracy and responsibility.",
        "zh_explanation": "對低信心預測的人機協作（HITL）審查確保不確定的 AI 決策在生效前由人工審查。這結合了 AI 效率和人工監督，提高準確性和責任性。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。人機協作對低信心預測進行人工審查，在效率和準確性間取得平衡。",
            "B": "沒有人工監督的部署對於高風險決策是不負責任的。",
            "C": "不驗證直接使用模型輸出可能傳播錯誤，不負責任。",
            "D": "更複雜的模型不一定減少所有錯誤，且可解釋性更差。"
        }
    },
    {
        "id": 248,
        "question": "A loan company is deploying an ML model for credit decisions and wants to minimize bias. Which TWO actions should the company take? (Choose TWO)",
        "zh_question": "一家貸款公司正在部署用於信貸決策的 ML 模型，並希望最小化偏見。公司應採取哪兩個行動？（選擇兩個）",
        "options": {
            "A": "Detect and address class imbalances in training data",
            "B": "Use only historical approval data without any adjustments",
            "C": "Regularly evaluate model behavior across demographic groups",
            "D": "Maximize model accuracy on the majority group only",
            "E": "Deploy the model without bias testing"
        },
        "zh_options": {
            "A": "偵測並解決訓練資料中的類別不平衡問題",
            "B": "僅使用歷史核准資料而不進行任何調整",
            "C": "定期評估各人口群體的模型行為",
            "D": "僅最大化多數群體的模型準確性",
            "E": "在沒有偏見測試的情況下部署模型"
        },
        "answer": "AC",
        "explanation": "To minimize bias in credit decisions: A) Detect and fix class imbalances in training data (historical bias can perpetuate discrimination), and C) Regularly evaluate model performance across demographic groups to identify disparate impact.",
        "zh_explanation": "為最小化信貸決策中的偏見：A) 偵測並修正訓練資料中的類別不平衡（歷史偏見可能延續歧視），以及 C) 定期評估各人口群體的模型效能以識別不同影響。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。解決類別不平衡防止模型對歷史上被歧視的群體產生偏見。",
            "B": "未調整的歷史資料可能包含歷史歧視模式，直接使用會延續偏見。",
            "C": "正確。定期跨群體評估可及時發現並糾正不公平的差異化影響。",
            "D": "僅最大化多數群體效能會忽視少數群體，加重歧視。",
            "E": "沒有偏見測試就部署是不負責任的，可能導致違法的歧視性決策。"
        }
    },
    {
        "id": 249,
        "question": "A company wants to prevent their AI chatbot from generating harmful or inappropriate content for users. Which approach is MOST appropriate?",
        "zh_question": "一家公司希望防止其 AI 聊天機器人為使用者生成有害或不當內容。哪種方法最合適？",
        "options": {
            "A": "Increase the model temperature for better responses",
            "B": "Implement content filtering and safety guardrails",
            "C": "Use a smaller model to reduce capabilities",
            "D": "Remove all system prompts"
        },
        "zh_options": {
            "A": "增加模型溫度以獲得更好的回應",
            "B": "實施內容過濾和安全護欄",
            "C": "使用更小的模型以降低能力",
            "D": "刪除所有系統提示"
        },
        "answer": "B",
        "explanation": "Content filtering and safety guardrails (like Amazon Bedrock Guardrails) are the standard approach for preventing harmful content generation. They filter both inputs and outputs to block inappropriate content.",
        "zh_explanation": "內容過濾和安全護欄（如 Amazon Bedrock Guardrails）是防止生成有害內容的標準方法。它們過濾輸入和輸出以阻止不當內容。",
        "category": "AIF",
        "option_explanations": {
            "A": "增加溫度使輸出更隨機，可能增加有害內容的可能性。",
            "B": "正確。內容過濾和安全護欄是防止有害輸出的最直接有效方法。",
            "C": "更小的模型能力更弱，不一定更安全，且犧牲了實用性。",
            "D": "刪除系統提示移除了重要的安全指令，使模型更容易產生有害內容。"
        }
    },
    {
        "id": 250,
        "question": "A healthcare company is deploying an AI model that makes treatment recommendations. The company wants to ensure responsible AI practices. Which safeguard should the company implement?",
        "zh_question": "一家醫療公司正在部署一個提供治療建議的 AI 模型。公司希望確保負責任的 AI 實踐。公司應實施哪種保護措施？",
        "options": {
            "A": "Implement guardrails to flag recommendations for medical professional review",
            "B": "Allow the AI to make final treatment decisions autonomously",
            "C": "Use the model with maximum temperature for diverse recommendations",
            "D": "Remove all safety checks to improve response speed"
        },
        "zh_options": {
            "A": "實施護欄以標記建議供醫療專業人員審查",
            "B": "允許 AI 自主做出最終治療決策",
            "C": "使用最高溫度模型以獲得多樣化的建議",
            "D": "刪除所有安全檢查以提高回應速度"
        },
        "answer": "A",
        "explanation": "For high-stakes medical decisions, implementing guardrails that flag AI recommendations for mandatory review by qualified medical professionals is essential. AI should support, not replace, medical judgment.",
        "zh_explanation": "對於高風險的醫療決策，實施護欄將 AI 建議標記供合格醫療專業人員強制審查至關重要。AI 應支援而非取代醫療判斷。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。醫療建議必須由專業人員審查，護欄確保人工監督的合規性。",
            "B": "讓 AI 自主做出最終治療決策是危險的，可能導致患者受到傷害。",
            "C": "最高溫度增加隨機性，不適合需要一致性和準確性的醫療建議。",
            "D": "在高風險醫療應用中刪除安全檢查是嚴重的不負責任行為。"
        }
    },
    {
        "id": 251,
        "question": "A company is using Amazon Bedrock to build an AI application and wants to prevent the model from generating discriminatory content. Which feature should the company use?",
        "zh_question": "一家公司正在使用 Amazon Bedrock 構建 AI 應用程式，希望防止模型生成歧視性內容。公司應使用哪個功能？",
        "options": {
            "A": "Amazon Bedrock Model Evaluation",
            "B": "Amazon Bedrock Guardrails with hate speech filters",
            "C": "Amazon Bedrock Fine-tuning",
            "D": "Amazon Bedrock Knowledge Bases"
        },
        "zh_options": {
            "A": "Amazon Bedrock Model Evaluation",
            "B": "帶有仇恨言論過濾器的 Amazon Bedrock Guardrails",
            "C": "Amazon Bedrock 微調",
            "D": "Amazon Bedrock Knowledge Bases"
        },
        "answer": "B",
        "explanation": "Amazon Bedrock Guardrails with hate speech and harmful content filters blocks discriminatory and offensive content from being generated or returned to users. This is the direct tool for preventing discriminatory outputs.",
        "zh_explanation": "帶有仇恨言論和有害內容過濾器的 Amazon Bedrock Guardrails 阻止歧視性和冒犯性內容被生成或返回給使用者。這是防止歧視性輸出的直接工具。",
        "category": "AIF",
        "option_explanations": {
            "A": "Model Evaluation 評估模型效能，不即時阻止歧視性內容。",
            "B": "正確。Guardrails 的仇恨言論過濾器直接阻止歧視性內容的生成。",
            "C": "微調改善模型行為，但不能即時阻止所有歧視性輸出。",
            "D": "Knowledge Bases 提供資訊檢索功能，不用於內容過濾。"
        }
    },
    {
        "id": 252,
        "question": "A company is developing an AI recruiting tool and wants to implement responsible AI principles. Which TWO principles should the company prioritize? (Choose TWO)",
        "zh_question": "一家公司正在開發 AI 招募工具，希望實施負責任 AI 原則。公司應優先考慮哪兩個原則？（選擇兩個）",
        "options": {
            "A": "Fairness: ensure the tool evaluates all candidates equitably",
            "B": "Speed: maximize processing time regardless of bias",
            "C": "Exclusion: optimize for the historically successful demographic",
            "D": "Capability: use the largest available model",
            "E": "Transparency: be able to explain the tool's decisions"
        },
        "zh_options": {
            "A": "公平性：確保工具公平評估所有候選人",
            "B": "速度：不考慮偏見，最大化處理速度",
            "C": "排他性：針對歷史上成功的人口群體進行優化",
            "D": "能力：使用最大的可用模型",
            "E": "透明度：能夠解釋工具的決策"
        },
        "answer": "AE",
        "explanation": "Responsible AI for recruiting requires: A) Fairness - ensuring equitable evaluation regardless of demographic characteristics, and E) Transparency/Explainability - being able to explain hiring decisions to candidates and regulators.",
        "zh_explanation": "招募中的負責任 AI 需要：A) 公平性——確保不考慮人口特徵的公平評估，以及 E) 透明度/可解釋性——能夠向候選人和監管機構解釋錄用決策。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。公平性確保 AI 招募工具對所有候選人提供公平機會。",
            "B": "以速度換取公平性是不負責任的，可能導致歧視性結果。",
            "C": "針對歷史成功群體優化會延續歷史歧視，違反公平性原則。",
            "D": "模型大小與負責任 AI 原則無直接關係。",
            "E": "正確。透明度使候選人了解評估依據，也使公司可以審計決策的公平性。"
        }
    },
    {
        "id": 253,
        "question": "A company is building a recommendation system and wants to ensure the model does not have unintended biases. Which action is MOST important for building an unbiased model?",
        "zh_question": "一家公司正在建立推薦系統，希望確保模型不存在意外偏見。建立無偏見模型最重要的行動是什麼？",
        "options": {
            "A": "Maximize training data size without considering diversity",
            "B": "Use the most complex model architecture available",
            "C": "Curate a diverse and representative training dataset",
            "D": "Skip data preprocessing to save time"
        },
        "zh_options": {
            "A": "在不考慮多樣性的情況下最大化訓練資料大小",
            "B": "使用最複雜的模型架構",
            "C": "策劃多樣化且具有代表性的訓練資料集",
            "D": "跳過資料預處理以節省時間"
        },
        "answer": "C",
        "explanation": "A diverse and representative training dataset is the foundation of an unbiased model. If training data reflects diverse perspectives and groups proportionally, the model is less likely to develop systematic biases.",
        "zh_explanation": "多樣化且具有代表性的訓練資料集是無偏見模型的基礎。如果訓練資料按比例反映不同的觀點和群體，模型就不太可能形成系統性偏見。",
        "category": "AIF",
        "option_explanations": {
            "A": "大量但不多樣化的資料可能放大偏見，而非減少偏見。",
            "B": "模型複雜度與偏見無直接關係，複雜模型也可能學習偏見。",
            "C": "正確。多樣化且具有代表性的訓練資料是防止模型偏見的最根本方法。",
            "D": "跳過資料預處理可能保留資料中的噪音和偏見，增加模型偏見風險。"
        }
    },
    {
        "id": 254,
        "question": "A company wants to fine-tune a foundation model using customer data. The company is concerned about data privacy and wants to ensure compliance. Which action should the company take FIRST?",
        "zh_question": "一家公司希望使用客戶資料微調基礎模型。公司擔心資料隱私並希望確保合規性。公司首先應採取什麼行動？",
        "options": {
            "A": "Immediately upload all customer data to the model provider",
            "B": "Remove or anonymize PII from the fine-tuning dataset",
            "C": "Use the raw customer data without any modifications",
            "D": "Share customer data with third-party model providers"
        },
        "zh_options": {
            "A": "立即將所有客戶資料上傳給模型提供商",
            "B": "從微調資料集中刪除或匿名化 PII",
            "C": "直接使用原始客戶資料而不作任何修改",
            "D": "與第三方模型提供商分享客戶資料"
        },
        "answer": "B",
        "explanation": "Before using customer data for fine-tuning, the FIRST step is to remove or anonymize personally identifiable information (PII). This protects customer privacy, ensures regulatory compliance (GDPR, CCPA), and prevents PII from being embedded in the model.",
        "zh_explanation": "在使用客戶資料進行微調之前，第一步是刪除或匿名化個人身份資訊（PII）。這保護客戶隱私，確保監管合規性（GDPR、CCPA），並防止 PII 被嵌入模型。",
        "category": "AIF",
        "option_explanations": {
            "A": "未先處理 PII 就上傳客戶資料可能違反隱私法規。",
            "B": "正確。首先移除或匿名化 PII 是使用客戶資料前的必要合規步驟。",
            "C": "使用未修改的原始客戶資料（含 PII）可能違反隱私法規。",
            "D": "與第三方分享含 PII 的客戶資料通常違反資料保護法規。"
        }
    },
    {
        "id": 255,
        "question": "A data scientist wants to understand which features most influence a model's predictions and detect any bias in the model. Which AWS service provides this functionality?",
        "zh_question": "一位資料科學家希望了解哪些特徵對模型預測影響最大，並偵測模型中的任何偏見。哪個 AWS 服務提供此功能？",
        "options": {
            "A": "Amazon SageMaker Training",
            "B": "Amazon Bedrock Knowledge Bases",
            "C": "Amazon SageMaker Model Monitor",
            "D": "Amazon SageMaker Clarify"
        },
        "zh_options": {
            "A": "Amazon SageMaker 訓練",
            "B": "Amazon Bedrock Knowledge Bases",
            "C": "Amazon SageMaker Model Monitor",
            "D": "Amazon SageMaker Clarify"
        },
        "answer": "D",
        "explanation": "Amazon SageMaker Clarify provides bias detection and explainability features. It identifies which features contribute most to predictions (feature importance) and detects pre-training and post-training bias in ML models.",
        "zh_explanation": "Amazon SageMaker Clarify 提供偏見偵測和可解釋性功能。它識別哪些特徵對預測貢獻最大（特徵重要性），並偵測 ML 模型中的訓練前和訓練後偏見。",
        "category": "AIF",
        "option_explanations": {
            "A": "SageMaker 訓練用於訓練模型，不提供偏見偵測或可解釋性分析。",
            "B": "Knowledge Bases 用於 RAG 知識管理，不提供偏見偵測。",
            "C": "Model Monitor 監控生產模型的漂移，但 Clarify 更專注於偏見和可解釋性。",
            "D": "正確。SageMaker Clarify 提供特徵重要性分析和偏見偵測功能。"
        }
    },
    {
        "id": 256,
        "question": "A company wants to create a mechanism for their ML team to document and audit their machine learning models. Which AWS service should the company use?",
        "zh_question": "一家公司希望為其 ML 團隊建立記錄和審計機器學習模型的機制。公司應使用哪個 AWS 服務？",
        "options": {
            "A": "Amazon SageMaker Experiments",
            "B": "Amazon SageMaker Autopilot",
            "C": "Amazon SageMaker Model Cards",
            "D": "Amazon SageMaker Clarify"
        },
        "zh_options": {
            "A": "Amazon SageMaker Experiments",
            "B": "Amazon SageMaker Autopilot",
            "C": "Amazon SageMaker Model Cards",
            "D": "Amazon SageMaker Clarify"
        },
        "answer": "C",
        "explanation": "Amazon SageMaker Model Cards provides a standardized framework for documenting ML models, including model details, intended use, training data, evaluation results, and ethical considerations. It serves as the official documentation and audit trail.",
        "zh_explanation": "Amazon SageMaker Model Cards 提供記錄 ML 模型的標準化框架，包括模型詳情、預期用途、訓練資料、評估結果和倫理考量。它作為官方文件和審計追蹤。",
        "category": "AIF",
        "option_explanations": {
            "A": "SageMaker Experiments 追蹤實驗參數和指標，不是完整的模型文件和審計工具。",
            "B": "SageMaker Autopilot 自動化 ML 流程，不用於模型文件和審計。",
            "C": "正確。Model Cards 提供標準化的模型文件框架，適合記錄和審計。",
            "D": "SageMaker Clarify 專注於偏見偵測和可解釋性，不是完整的文件和審計機制。"
        }
    },
    {
        "id": 257,
        "question": "A social media company uses AI to make content recommendations. Users want to understand why they are seeing certain recommendations. Which responsible AI principle should the company focus on?",
        "zh_question": "一家社交媒體公司使用 AI 進行內容推薦。使用者希望了解為什麼會看到某些推薦。公司應關注哪個負責任 AI 原則？",
        "options": {
            "A": "Privacy",
            "B": "Explainability",
            "C": "Security",
            "D": "Scalability"
        },
        "zh_options": {
            "A": "隱私",
            "B": "可解釋性",
            "C": "安全性",
            "D": "可擴展性"
        },
        "answer": "B",
        "explanation": "Explainability (also called interpretability) is the responsible AI principle about making AI decisions understandable to users. Providing explanations for content recommendations helps users trust and understand the AI system.",
        "zh_explanation": "可解釋性（也稱為可解讀性）是關於使 AI 決策對使用者可理解的負責任 AI 原則。提供內容推薦的解釋幫助使用者信任和理解 AI 系統。",
        "category": "AIF",
        "option_explanations": {
            "A": "隱私關注個人資料保護，不是關於解釋推薦決策的原則。",
            "B": "正確。可解釋性確保使用者能夠理解 AI 為何做出特定推薦決策。",
            "C": "安全性關注系統保護，不是關於向使用者解釋 AI 決策的原則。",
            "D": "可擴展性是技術特性，不是負責任 AI 的核心原則。"
        }
    },
    {
        "id": 258,
        "question": "A company has a dataset for training a loan approval model. A data scientist wants to measure the imbalance between approved and denied loan applications in the dataset. Which metric should the data scientist use?",
        "zh_question": "一家公司有用於訓練貸款核准模型的資料集。一位資料科學家希望衡量資料集中核准和拒絕貸款申請之間的不平衡程度。資料科學家應使用哪個指標？",
        "options": {
            "A": "BLEU score",
            "B": "F1 score",
            "C": "Model perplexity",
            "D": "Class imbalance ratio"
        },
        "zh_options": {
            "A": "BLEU 分數",
            "B": "F1 分數",
            "C": "模型困惑度",
            "D": "類別不平衡比率"
        },
        "answer": "D",
        "explanation": "Class imbalance ratio measures the proportion of samples in each class. For loan data, it quantifies the ratio of approved vs. denied applications, helping identify if one class is significantly overrepresented.",
        "zh_explanation": "類別不平衡比率衡量每個類別的樣本比例。對於貸款資料，它量化核准與拒絕申請的比率，幫助識別某個類別是否被顯著過度代表。",
        "category": "AIF",
        "option_explanations": {
            "A": "BLEU 分數用於文字生成評估，不是資料集平衡性指標。",
            "B": "F1 分數評估分類模型效能，不直接衡量資料集的類別不平衡。",
            "C": "困惑度是語言模型指標，不用於衡量資料集類別分佈。",
            "D": "正確。類別不平衡比率直接衡量各類別樣本數量的不平衡程度。"
        }
    },
    {
        "id": 259,
        "question": "A data scientist is choosing between a simple logistic regression model and a complex deep learning model for a credit scoring application. The stakeholders require that the model's decisions must be explainable to regulators. How does model complexity affect explainability?",
        "zh_question": "一位資料科學家正在為信用評分應用程式選擇簡單邏輯回歸模型和複雜深度學習模型之間的選擇。利害關係人要求模型的決策必須能向監管機構解釋。模型複雜度如何影響可解釋性？",
        "options": {
            "A": "Higher complexity generally reduces model explainability",
            "B": "Higher complexity always improves explainability",
            "C": "Model complexity has no effect on explainability",
            "D": "Only deep learning models can be explained"
        },
        "zh_options": {
            "A": "更高的複雜度通常降低模型的可解釋性",
            "B": "更高的複雜度總是提高可解釋性",
            "C": "模型複雜度對可解釋性沒有影響",
            "D": "只有深度學習模型可以被解釋"
        },
        "answer": "A",
        "explanation": "There is generally a trade-off between model complexity and explainability. Simple models (logistic regression, decision trees) are inherently interpretable, while complex models (deep neural networks) are 'black boxes' that are harder to explain.",
        "zh_explanation": "模型複雜度和可解釋性之間通常存在權衡。簡單模型（邏輯回歸、決策樹）本質上是可解讀的，而複雜模型（深度神經網路）是難以解釋的「黑盒」。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。模型越複雜，其內部決策過程越難以解釋（黑盒問題）。",
            "B": "更高的複雜度通常使模型更難解釋，而非更容易。",
            "C": "複雜度對可解釋性有直接影響，這是 AI 倫理的核心權衡之一。",
            "D": "恰恰相反，深度學習模型通常是最難解釋的模型類型。"
        }
    },
    {
        "id": 260,
        "question": "A company's AI customer service agent provides answers to product questions. To increase customer trust, the company wants the agent to cite the sources of its answers. Which responsible AI principle does this BEST represent?",
        "zh_question": "一家公司的 AI 客戶服務代理回答產品問題。為了增加客戶信任，公司希望代理引用其答案的來源。這最能代表哪個負責任 AI 原則？",
        "options": {
            "A": "Privacy",
            "B": "Transparency and explainability",
            "C": "Security",
            "D": "Performance optimization"
        },
        "zh_options": {
            "A": "隱私",
            "B": "透明度和可解釋性",
            "C": "安全性",
            "D": "效能最佳化"
        },
        "answer": "B",
        "explanation": "Citing sources demonstrates transparency (being open about where information comes from) and explainability (helping users understand why the AI gave a certain answer). This builds trust by making the AI's knowledge base visible.",
        "zh_explanation": "引用來源展示了透明度（公開資訊來源）和可解釋性（幫助使用者理解 AI 為何給出某個答案）。這通過使 AI 的知識庫可見來建立信任。",
        "category": "AIF",
        "option_explanations": {
            "A": "隱私關注個人資料保護，不是關於引用來源增加信任的原則。",
            "B": "正確。引用來源是透明度和可解釋性的體現，讓使用者了解 AI 答案的依據。",
            "C": "安全性關注系統保護，不是關於引用來源的原則。",
            "D": "效能最佳化是技術指標，與引用來源增加信任無關。"
        }
    },
    {
        "id": 261,
        "question": "A hospital is using an AI system to recommend treatments. Doctors want to understand how the AI arrives at its recommendations to make informed decisions. Which responsible AI principle is MOST relevant?",
        "zh_question": "一家醫院正在使用 AI 系統推薦治療方案。醫生希望了解 AI 如何得出其建議以做出明智的決策。哪個負責任 AI 原則最相關？",
        "options": {
            "A": "Explainability",
            "B": "Scalability",
            "C": "Efficiency",
            "D": "Cost optimization"
        },
        "zh_options": {
            "A": "可解釋性",
            "B": "可擴展性",
            "C": "效率",
            "D": "成本最佳化"
        },
        "answer": "A",
        "explanation": "Explainability is critical for medical AI systems. Doctors need to understand the reasoning behind AI recommendations to critically evaluate them, catch potential errors, and take responsibility for final decisions.",
        "zh_explanation": "可解釋性對於醫療 AI 系統至關重要。醫生需要理解 AI 建議背後的推理，以批判性地評估它們、發現潛在錯誤，並對最終決策負責。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。醫療 AI 必須具備可解釋性，使醫生能夠理解和評估 AI 建議。",
            "B": "可擴展性是技術特性，在此場景中不是最相關的負責任 AI 原則。",
            "C": "效率雖重要，但不是醫生理解 AI 建議的核心原則。",
            "D": "成本最佳化是業務考量，不是此場景的核心負責任 AI 原則。"
        }
    },
    {
        "id": 262,
        "question": "Multiple research institutes want to share and collaborate on their ML models while maintaining consistent documentation standards. Which AWS service enables this cross-institutional collaboration with standardized model documentation?",
        "zh_question": "多個研究機構希望在保持一致文件標準的同時共享和協作其 ML 模型。哪個 AWS 服務能夠通過標準化模型文件實現跨機構協作？",
        "options": {
            "A": "Amazon SageMaker Pipelines",
            "B": "Amazon SageMaker Experiments",
            "C": "Amazon SageMaker Model Cards",
            "D": "Amazon SageMaker Feature Store"
        },
        "zh_options": {
            "A": "Amazon SageMaker Pipelines",
            "B": "Amazon SageMaker Experiments",
            "C": "Amazon SageMaker Model Cards",
            "D": "Amazon SageMaker Feature Store"
        },
        "answer": "C",
        "explanation": "Amazon SageMaker Model Cards provides a standardized format for documenting ML models that can be shared across teams and organizations. This common documentation standard facilitates collaboration and knowledge sharing.",
        "zh_explanation": "Amazon SageMaker Model Cards 提供可在團隊和組織之間共享的標準化 ML 模型文件格式。這種通用文件標準促進了協作和知識共享。",
        "category": "AIF",
        "option_explanations": {
            "A": "SageMaker Pipelines 自動化 ML 工作流，不提供跨機構模型文件共享。",
            "B": "SageMaker Experiments 追蹤實驗，不是標準化的跨機構文件工具。",
            "C": "正確。Model Cards 提供標準化文件格式，適合跨機構的模型文件共享和協作。",
            "D": "Feature Store 管理特徵，不用於模型文件和協作。"
        }
    },
    {
        "id": 263,
        "question": "A company's ML team wants to ensure all their models have consistent documentation that includes model details, training information, and evaluation results. What is a PRIMARY benefit of using Amazon SageMaker Model Cards?",
        "zh_question": "一家公司的 ML 團隊希望確保所有模型都有一致的文件，包括模型詳情、訓練資訊和評估結果。使用 Amazon SageMaker Model Cards 的主要好處是什麼？",
        "options": {
            "A": "It automatically trains better models",
            "B": "It standardizes and centralizes model documentation",
            "C": "It reduces model inference costs",
            "D": "It improves model accuracy automatically"
        },
        "zh_options": {
            "A": "它自動訓練更好的模型",
            "B": "它標準化並集中管理模型文件",
            "C": "它降低了模型推論成本",
            "D": "它自動提高模型準確性"
        },
        "answer": "B",
        "explanation": "The PRIMARY benefit of SageMaker Model Cards is standardizing and centralizing model documentation. It provides a consistent framework for capturing model details, intended use, limitations, and evaluation metrics across all models.",
        "zh_explanation": "SageMaker Model Cards 的主要好處是標準化並集中管理模型文件。它提供一致的框架，用於記錄所有模型的模型詳情、預期用途、限制和評估指標。",
        "category": "AIF",
        "option_explanations": {
            "A": "Model Cards 是文件工具，不會自動訓練或改善模型。",
            "B": "正確。Model Cards 的核心價值是提供標準化的模型文件框架。",
            "C": "Model Cards 是文件服務，不影響推論成本。",
            "D": "Model Cards 記錄模型性能，但不會自動提高準確性。"
        }
    },
    {
        "id": 264,
        "question": "A company is using Amazon Bedrock to build an AI application that needs to access encrypted data stored in Amazon S3. Which permission should the foundation model's execution role have?",
        "zh_question": "一家公司正在使用 Amazon Bedrock 構建需要存取 Amazon S3 中加密資料的 AI 應用程式。基礎模型的執行角色應具有哪個權限？",
        "options": {
            "A": "IAM role with permission to decrypt the S3 data using AWS KMS",
            "B": "Root account access to all S3 buckets",
            "C": "Public read access to the S3 bucket",
            "D": "Only S3 GetObject permission without KMS access"
        },
        "zh_options": {
            "A": "具有使用 AWS KMS 解密 S3 資料權限的 IAM 角色",
            "B": "對所有 S3 儲存桶的根帳戶存取",
            "C": "對 S3 儲存桶的公開讀取存取",
            "D": "僅 S3 GetObject 權限而沒有 KMS 存取"
        },
        "answer": "A",
        "explanation": "To access encrypted S3 data, the execution role needs both S3 read permissions AND AWS KMS decryption permissions. An IAM role with these specific permissions follows the principle of least privilege while enabling the required access.",
        "zh_explanation": "要存取加密的 S3 資料，執行角色需要 S3 讀取權限和 AWS KMS 解密權限。具有這些特定權限的 IAM 角色在遵循最小權限原則的同時實現所需存取。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。需要 IAM 角色同時具有 S3 存取和 KMS 解密權限才能存取加密資料。",
            "B": "根帳戶存取違反最小權限原則，是安全風險。",
            "C": "公開讀取存取不適合包含加密敏感資料的 S3 儲存桶。",
            "D": "沒有 KMS 存取權限，GetObject 無法解密 KMS 加密的資料。"
        }
    },
    {
        "id": 265,
        "question": "A company has compliance requirements that prohibit their ML models from accessing the internet. Which Amazon SageMaker feature should the company use to train models in an isolated environment?",
        "zh_question": "一家公司有合規要求，禁止其 ML 模型存取網際網路。公司應使用哪個 Amazon SageMaker 功能在隔離環境中訓練模型？",
        "options": {
            "A": "SageMaker Autopilot for automated training",
            "B": "SageMaker network isolation mode",
            "C": "SageMaker Experiments for tracking",
            "D": "SageMaker Model Cards for documentation"
        },
        "zh_options": {
            "A": "用於自動化訓練的 SageMaker Autopilot",
            "B": "SageMaker 網路隔離模式",
            "C": "用於追蹤的 SageMaker Experiments",
            "D": "用於文件記錄的 SageMaker Model Cards"
        },
        "answer": "B",
        "explanation": "SageMaker network isolation mode runs training jobs in a network-isolated environment where the container cannot make any outbound network connections to the internet. This satisfies compliance requirements for internet-restricted training.",
        "zh_explanation": "SageMaker 網路隔離模式在網路隔離環境中運行訓練工作，容器無法建立任何到網際網路的出站網路連接。這滿足了禁止網際網路存取的合規要求。",
        "category": "AIF",
        "option_explanations": {
            "A": "Autopilot 自動化 ML 流程，不提供網路隔離的合規功能。",
            "B": "正確。SageMaker 網路隔離模式確保訓練環境無法存取網際網路，滿足合規要求。",
            "C": "Experiments 追蹤實驗指標，不提供網路隔離功能。",
            "D": "Model Cards 用於模型文件，不提供網路隔離功能。"
        }
    },
    {
        "id": 266,
        "question": "A company wants to use Amazon SageMaker JumpStart to deploy foundation models and needs to meet compliance requirements. Which TWO compliance capabilities does SageMaker JumpStart provide? (Choose TWO)",
        "zh_question": "一家公司希望使用 Amazon SageMaker JumpStart 部署基礎模型，並需要滿足合規要求。SageMaker JumpStart 提供哪兩個合規能力？（選擇兩個）",
        "options": {
            "A": "Automatic model accuracy improvement",
            "B": "Threat detection through AWS security services integration",
            "C": "Data protection through encryption",
            "D": "Automatic bias elimination",
            "E": "Free unlimited model training"
        },
        "zh_options": {
            "A": "自動模型準確性改善",
            "B": "通過 AWS 安全服務整合進行威脅偵測",
            "C": "通過加密保護資料",
            "D": "自動偏見消除",
            "E": "免費無限制模型訓練"
        },
        "answer": "BC",
        "explanation": "SageMaker JumpStart compliance capabilities include: B) Integration with AWS security services (GuardDuty, Security Hub) for threat detection, and C) Data protection through encryption at rest and in transit using AWS KMS.",
        "zh_explanation": "SageMaker JumpStart 的合規能力包括：B) 與 AWS 安全服務（GuardDuty、Security Hub）整合進行威脅偵測，以及 C) 通過使用 AWS KMS 的靜態和傳輸加密保護資料。",
        "category": "AIF",
        "option_explanations": {
            "A": "JumpStart 不自動改善模型準確性，準確性取決於訓練和資料。",
            "B": "正確。JumpStart 整合 AWS 安全服務提供威脅偵測能力。",
            "C": "正確。JumpStart 支援 KMS 加密，提供資料保護合規能力。",
            "D": "JumpStart 不會自動消除偏見，偏見需要透過資料和評估來解決。",
            "E": "JumpStart 使用有相關成本，不提供免費無限制訓練。"
        }
    },
    {
        "id": 267,
        "question": "A security researcher is testing an AI system's vulnerabilities. The researcher attempts to make the AI bypass its safety guidelines by framing requests in clever ways. Which security technique is the researcher testing?",
        "zh_question": "一位安全研究人員正在測試 AI 系統的漏洞。研究人員試圖通過以巧妙的方式構建請求來使 AI 繞過其安全指南。研究人員正在測試哪種安全技術？",
        "options": {
            "A": "Data poisoning",
            "B": "Model inversion attack",
            "C": "SQL injection",
            "D": "Jailbreaking"
        },
        "zh_options": {
            "A": "資料投毒",
            "B": "模型反轉攻擊",
            "C": "SQL 注入",
            "D": "越獄"
        },
        "answer": "D",
        "explanation": "Jailbreaking refers to techniques used to make AI models bypass their safety guidelines and restrictions. Attackers craft clever prompts to trick the model into producing content it would normally refuse.",
        "zh_explanation": "越獄是指用於使 AI 模型繞過其安全指南和限制的技術。攻擊者構造巧妙的提示，誘使模型產生通常會拒絕的內容。",
        "category": "AIF",
        "option_explanations": {
            "A": "資料投毒是在訓練資料中植入惡意樣本，影響模型學習，不是此場景描述的技術。",
            "B": "模型反轉攻擊試圖從模型輸出重建訓練資料，不是此場景描述的技術。",
            "C": "SQL 注入是針對資料庫的攻擊，不是針對 AI 模型的技術。",
            "D": "正確。越獄是通過巧妙的提示讓 AI 繞過安全限制的技術。"
        }
    },
    {
        "id": 268,
        "question": "A company is using Amazon Bedrock for their AI application. The company asks about their security responsibilities. What is the customer's responsibility when using Amazon Bedrock?",
        "zh_question": "一家公司正在使用 Amazon Bedrock 用於其 AI 應用程式。公司詢問其安全責任。使用 Amazon Bedrock 時，客戶的責任是什麼？",
        "options": {
            "A": "Managing the physical security of data centers",
            "B": "Patching the underlying hardware infrastructure",
            "C": "Protecting data in transit and at rest for their applications",
            "D": "Managing the Bedrock service infrastructure"
        },
        "zh_options": {
            "A": "管理資料中心的物理安全",
            "B": "修補底層硬體基礎設施",
            "C": "保護其應用程式的傳輸中和靜態資料",
            "D": "管理 Bedrock 服務基礎設施"
        },
        "answer": "C",
        "explanation": "Under the AWS Shared Responsibility Model, customers are responsible for security 'in' the cloud: protecting their data in transit and at rest, managing access controls, and configuring security settings for their applications.",
        "zh_explanation": "根據 AWS 共同責任模型，客戶負責雲端「中」的安全：保護傳輸中和靜態的資料、管理存取控制，以及為其應用程式配置安全設定。",
        "category": "AIF",
        "option_explanations": {
            "A": "物理資料中心安全是 AWS 的責任（雲端「的」安全）。",
            "B": "底層硬體修補是 AWS 的責任，不是客戶的責任。",
            "C": "正確。客戶負責其應用程式資料的加密（傳輸中和靜態）及存取控制。",
            "D": "Bedrock 服務基礎設施由 AWS 管理，不是客戶的責任。"
        }
    },
    {
        "id": 269,
        "question": "A company discovers that their fine-tuned model may have memorized confidential customer data from the training dataset. What is the BEST course of action?",
        "zh_question": "一家公司發現其微調模型可能已記憶了訓練資料集中的機密客戶資料。最佳處理方式是什麼？",
        "options": {
            "A": "Delete the model and retrain with properly sanitized data",
            "B": "Continue using the model but add a disclaimer",
            "C": "Increase the model's temperature to hide the memorized data",
            "D": "Share the discovery only with senior management"
        },
        "zh_options": {
            "A": "刪除模型並使用適當清理的資料重新訓練",
            "B": "繼續使用模型但添加免責聲明",
            "C": "增加模型溫度以隱藏記憶的資料",
            "D": "僅與高層管理人員分享這一發現"
        },
        "answer": "A",
        "explanation": "If a model has memorized confidential data, the BEST action is to delete the compromised model and retrain using properly sanitized training data (with PII removed/anonymized). Continuing to use the model risks data leakage.",
        "zh_explanation": "如果模型已記憶了機密資料，最佳做法是刪除受損的模型，並使用適當清理的訓練資料（已刪除/匿名化 PII）重新訓練。繼續使用該模型有資料洩露風險。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。刪除受損模型並用清理後的資料重新訓練是保護客戶資料的正確做法。",
            "B": "僅添加免責聲明不能解決模型可能洩露機密資料的根本問題。",
            "C": "增加溫度不會消除模型記憶的資料，只是增加輸出的隨機性。",
            "D": "資料洩露風險需要採取行動，不只是內部報告，可能還需要通知受影響的客戶。"
        }
    },
    {
        "id": 270,
        "question": "A hospital needs to deploy an AI system and must ensure that all patient data remains within a specific geographic region due to regulatory requirements. Which AWS capability addresses this requirement?",
        "zh_question": "一家醫院需要部署 AI 系統，並必須確保所有患者資料因監管要求而保留在特定地理區域內。哪個 AWS 能力解決了這個需求？",
        "options": {
            "A": "AWS Regions and data residency controls",
            "B": "AWS CloudFront for global distribution",
            "C": "AWS Auto Scaling for performance",
            "D": "AWS Cost Explorer for cost management"
        },
        "zh_options": {
            "A": "AWS 區域和資料駐留控制",
            "B": "用於全球分發的 AWS CloudFront",
            "C": "用於效能的 AWS Auto Scaling",
            "D": "用於成本管理的 AWS Cost Explorer"
        },
        "answer": "A",
        "explanation": "AWS Regions allow customers to choose where their data is stored geographically. Data residency controls ensure data remains within specific regions to comply with regulations like GDPR, HIPAA, and local data sovereignty laws.",
        "zh_explanation": "AWS 區域允許客戶選擇其資料的地理儲存位置。資料駐留控制確保資料保留在特定區域內，以遵守 GDPR、HIPAA 和當地資料主權法律等法規。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。AWS 區域和資料駐留控制確保資料保留在指定的地理區域，滿足監管要求。",
            "B": "CloudFront 是 CDN，用於全球內容分發，與資料駐留要求相反。",
            "C": "Auto Scaling 用於調整運算資源，不解決資料地理駐留問題。",
            "D": "Cost Explorer 用於成本分析，與資料駐留合規無關。"
        }
    },
    {
        "id": 271,
        "question": "A company is evaluating different AI deployment approaches. According to the AWS Security Scoping Matrix for generative AI, which approach requires the MOST customer ownership of security?",
        "zh_question": "一家公司正在評估不同的 AI 部署方法。根據 AWS 生成式 AI 安全範圍矩陣，哪種方法需要最多的客戶安全所有權？",
        "options": {
            "A": "Using a fully managed SaaS AI service",
            "B": "Using Amazon Bedrock with managed models",
            "C": "Fine-tuning a managed model via API",
            "D": "Building and training your own model from scratch on AWS infrastructure"
        },
        "zh_options": {
            "A": "使用完全託管的 SaaS AI 服務",
            "B": "使用 Amazon Bedrock 的託管模型",
            "C": "通過 API 微調託管模型",
            "D": "在 AWS 基礎設施上從頭構建和訓練自己的模型"
        },
        "answer": "D",
        "explanation": "Building your own model from scratch on AWS infrastructure requires the MOST customer security ownership. The customer is responsible for the infrastructure, model code, training pipeline, data security, and deployment security.",
        "zh_explanation": "在 AWS 基礎設施上從頭構建自己的模型需要最多的客戶安全所有權。客戶負責基礎設施、模型代碼、訓練管道、資料安全和部署安全。",
        "category": "AIF",
        "option_explanations": {
            "A": "完全託管的 SaaS AI 服務由服務提供商承擔大部分安全責任，客戶所有權最少。",
            "B": "使用 Bedrock 託管模型，AWS 管理模型基礎設施，客戶安全責任適中。",
            "C": "微調託管模型需要一些額外的客戶安全責任（訓練資料），但比從頭構建少。",
            "D": "正確。從頭構建自己的模型需要最多的客戶安全所有權，包括所有層面。"
        }
    },
    {
        "id": 272,
        "question": "A company wants to maintain an audit trail of all requests made to their Amazon Bedrock foundation models for compliance purposes. Which action should the company take?",
        "zh_question": "一家公司希望為合規目的維護所有對其 Amazon Bedrock 基礎模型的請求審計追蹤。公司應採取什麼行動？",
        "options": {
            "A": "Enable AWS CloudTrail for all API calls",
            "B": "Enable invocation logging in Amazon Bedrock",
            "C": "Use Amazon Inspector for security assessment",
            "D": "Deploy an API Gateway with logging"
        },
        "zh_options": {
            "A": "為所有 API 呼叫啟用 AWS CloudTrail",
            "B": "在 Amazon Bedrock 中啟用呼叫日誌記錄",
            "C": "使用 Amazon Inspector 進行安全評估",
            "D": "部署帶有日誌記錄的 API Gateway"
        },
        "answer": "B",
        "explanation": "Amazon Bedrock invocation logging captures the complete audit trail of model invocations, including inputs and outputs. This provides detailed records for compliance, security analysis, and auditing purposes.",
        "zh_explanation": "Amazon Bedrock 呼叫日誌記錄捕獲模型呼叫的完整審計追蹤，包括輸入和輸出。這為合規、安全分析和審計目的提供詳細記錄。",
        "category": "AIF",
        "option_explanations": {
            "A": "CloudTrail 記錄 AWS API 呼叫，但不記錄 Bedrock 模型的具體輸入/輸出內容。",
            "B": "正確。Bedrock 呼叫日誌記錄捕獲模型請求的完整詳情，包括輸入和輸出。",
            "C": "Inspector 用於安全漏洞評估，不提供 Bedrock 呼叫的審計追蹤。",
            "D": "API Gateway 日誌記錄 API 呼叫，但不記錄 Bedrock 模型的具體輸入/輸出。"
        }
    },
    {
        "id": 273,
        "question": "A company needs to access AWS compliance reports and certifications (such as SOC 2 and ISO 27001) to satisfy auditor requests. Which AWS service should the company use?",
        "zh_question": "一家公司需要存取 AWS 合規報告和認證（如 SOC 2 和 ISO 27001）以滿足審計員請求。公司應使用哪個 AWS 服務？",
        "options": {
            "A": "Amazon GuardDuty",
            "B": "AWS Artifact",
            "C": "AWS Config",
            "D": "Amazon Inspector"
        },
        "zh_options": {
            "A": "Amazon GuardDuty",
            "B": "AWS Artifact",
            "C": "AWS Config",
            "D": "Amazon Inspector"
        },
        "answer": "B",
        "explanation": "AWS Artifact is the central repository for AWS compliance reports, certifications, and agreements. It provides on-demand access to AWS's SOC reports, ISO certifications, PCI DSS reports, and other compliance documents.",
        "zh_explanation": "AWS Artifact 是 AWS 合規報告、認證和協議的中央存儲庫。它提供對 AWS 的 SOC 報告、ISO 認證、PCI DSS 報告和其他合規文件的按需存取。",
        "category": "AIF",
        "option_explanations": {
            "A": "GuardDuty 是威脅偵測服務，不提供合規報告和認證文件。",
            "B": "正確。AWS Artifact 是獲取 AWS 合規報告、SOC 認證等文件的官方服務。",
            "C": "AWS Config 追蹤資源配置變更，不提供合規認證文件。",
            "D": "Inspector 評估安全漏洞，不提供合規報告和認證文件。"
        }
    },
    {
        "id": 274,
        "question": "A company wants to implement continuous compliance monitoring for their AWS environment hosting AI workloads. Which TWO AWS services should the company use? (Choose TWO)",
        "zh_question": "一家公司希望對其托管 AI 工作負載的 AWS 環境實施持續合規監控。公司應使用哪兩個 AWS 服務？（選擇兩個）",
        "options": {
            "A": "AWS Audit Manager",
            "B": "AWS Config",
            "C": "Amazon SageMaker Training",
            "D": "Amazon Bedrock Knowledge Bases",
            "E": "Amazon Comprehend"
        },
        "zh_options": {
            "A": "AWS Audit Manager",
            "B": "AWS Config",
            "C": "Amazon SageMaker 訓練",
            "D": "Amazon Bedrock Knowledge Bases",
            "E": "Amazon Comprehend"
        },
        "answer": "AB",
        "explanation": "A) AWS Audit Manager automates audit evidence collection and continuous compliance assessment against frameworks like GDPR, HIPAA, and SOC. B) AWS Config continuously monitors and records resource configurations, assessing compliance against rules.",
        "zh_explanation": "A) AWS Audit Manager 自動化審計證據收集和針對 GDPR、HIPAA、SOC 等框架的持續合規評估。B) AWS Config 持續監控並記錄資源配置，根據規則評估合規性。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。AWS Audit Manager 提供持續合規評估和自動化審計證據收集。",
            "B": "正確。AWS Config 持續監控資源配置合規性，是持續合規監控的核心服務。",
            "C": "SageMaker 訓練用於模型訓練，不用於合規監控。",
            "D": "Knowledge Bases 用於 RAG，不用於合規監控。",
            "E": "Comprehend 是自然語言處理服務，不用於合規監控。"
        }
    },
    {
        "id": 275,
        "question": "A company wants to establish governance over their ML models throughout the entire model lifecycle. Which AWS service provides model governance and reporting capabilities?",
        "zh_question": "一家公司希望在整個模型生命週期中建立對其 ML 模型的治理。哪個 AWS 服務提供模型治理和報告功能？",
        "options": {
            "A": "Amazon SageMaker Model Cards",
            "B": "Amazon Bedrock Knowledge Bases",
            "C": "Amazon SageMaker Training",
            "D": "Amazon CloudWatch"
        },
        "zh_options": {
            "A": "Amazon SageMaker Model Cards",
            "B": "Amazon Bedrock Knowledge Bases",
            "C": "Amazon SageMaker 訓練",
            "D": "Amazon CloudWatch"
        },
        "answer": "A",
        "explanation": "Amazon SageMaker Model Cards provides model governance through standardized documentation of model details, intended use, training data, evaluation results, and ethical considerations. It supports the full model lifecycle governance.",
        "zh_explanation": "Amazon SageMaker Model Cards 通過標準化記錄模型詳情、預期用途、訓練資料、評估結果和倫理考量提供模型治理。它支持完整的模型生命週期治理。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。SageMaker Model Cards 提供模型治理框架，涵蓋整個模型生命週期的文件和報告。",
            "B": "Knowledge Bases 用於 RAG，不提供模型治理功能。",
            "C": "SageMaker 訓練執行模型訓練，不提供治理和報告功能。",
            "D": "CloudWatch 監控基礎設施和應用程式指標，不提供 ML 模型治理。"
        }
    },
    {
        "id": 276,
        "question": "A company wants to restrict which Amazon Bedrock foundation models different teams in the organization can access. Which approach should the company use?",
        "zh_question": "一家公司希望限制組織中不同團隊可以存取的 Amazon Bedrock 基礎模型。公司應使用哪種方法？",
        "options": {
            "A": "Create IAM policies that restrict access to specific Bedrock model ARNs",
            "B": "Change the model's API endpoint for each team",
            "C": "Use different AWS accounts with no cross-account access",
            "D": "Ask team members to self-regulate their model usage"
        },
        "zh_options": {
            "A": "建立限制存取特定 Bedrock 模型 ARN 的 IAM 策略",
            "B": "為每個團隊更改模型的 API 端點",
            "C": "使用沒有跨帳戶存取的不同 AWS 帳戶",
            "D": "請團隊成員自我規範其模型使用"
        },
        "answer": "A",
        "explanation": "IAM policies can restrict access to specific Amazon Bedrock model ARNs, allowing fine-grained control over which teams can use which models. This follows the principle of least privilege for model access control.",
        "zh_explanation": "IAM 策略可以限制對特定 Amazon Bedrock 模型 ARN 的存取，允許對哪些團隊可以使用哪些模型進行精細控制。這遵循模型存取控制的最小權限原則。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。IAM 策略通過指定允許/拒絕的模型 ARN 來精細控制模型存取權限。",
            "B": "更改 API 端點不是有效的存取控制機制。",
            "C": "使用不同帳戶過於嚴格，阻止了合法的跨團隊協作，且管理複雜。",
            "D": "依靠自我規範不是可靠的存取控制機制，缺乏技術執行力。"
        }
    },
    {
        "id": 277,
        "question": "A company is evaluating Amazon Bedrock for their AI application and is concerned about data privacy. What is Amazon Bedrock's data privacy policy regarding customer data?",
        "zh_question": "一家公司正在評估 Amazon Bedrock 用於其 AI 應用程式，並擔心資料隱私。Amazon Bedrock 關於客戶資料的資料隱私政策是什麼？",
        "options": {
            "A": "Customer data is used to improve all Bedrock foundation models",
            "B": "Customer data is shared with the original model providers",
            "C": "Customer data is not used to train the base foundation models without explicit consent",
            "D": "All customer data is permanently retained by AWS"
        },
        "zh_options": {
            "A": "客戶資料用於改善所有 Bedrock 基礎模型",
            "B": "客戶資料與原始模型提供商共享",
            "C": "未經明確同意，客戶資料不用於訓練基礎基礎模型",
            "D": "所有客戶資料由 AWS 永久保留"
        },
        "answer": "C",
        "explanation": "Amazon Bedrock does not use customer inputs/outputs to train the base foundation models without customer consent. Customer data is treated as private and is not shared with third-party model providers.",
        "zh_explanation": "Amazon Bedrock 在未獲得客戶同意的情況下不使用客戶的輸入/輸出來訓練基礎模型。客戶資料被視為私有，不與第三方模型提供商共享。",
        "category": "AIF",
        "option_explanations": {
            "A": "Bedrock 不會使用客戶資料來改善基礎模型，除非客戶明確同意。",
            "B": "Bedrock 不與原始模型提供商共享客戶資料，保護客戶隱私。",
            "C": "正確。Bedrock 的隱私政策明確表示未經同意不使用客戶資料訓練模型。",
            "D": "Bedrock 不永久保留客戶資料，有明確的資料保留政策。"
        }
    },
    {
        "id": 278,
        "question": "A developer is aware of prompt injection attacks. Which prompt engineering risk does prompt injection PRIMARILY represent?",
        "zh_question": "一位開發人員了解提示注入攻擊。提示注入主要代表哪種提示工程風險？",
        "options": {
            "A": "Model hallucination",
            "B": "Malicious instructions embedded in user inputs overriding system instructions",
            "C": "High token usage costs",
            "D": "Poor response quality"
        },
        "zh_options": {
            "A": "模型幻覺",
            "B": "嵌入使用者輸入中的惡意指令覆蓋系統指令",
            "C": "高 token 使用成本",
            "D": "回應品質差"
        },
        "answer": "B",
        "explanation": "Prompt injection is when malicious instructions are embedded in user inputs (or retrieved content) that override or hijack the system prompt's instructions, causing the model to follow the attacker's commands instead.",
        "zh_explanation": "提示注入是指惡意指令嵌入使用者輸入（或檢索的內容）中，覆蓋或劫持系統提示的指令，導致模型遵循攻擊者的命令而非原始指令。",
        "category": "AIF",
        "option_explanations": {
            "A": "幻覺是模型生成不實資訊，不是提示注入攻擊的定義。",
            "B": "正確。提示注入的核心是惡意指令覆蓋系統指令，讓 AI 執行攻擊者的意圖。",
            "C": "高 token 成本是使用效率問題，不是提示注入的定義。",
            "D": "回應品質差是一般性問題，不是提示注入的特定定義。"
        }
    },
    {
        "id": 279,
        "question": "A company is building an AI application on AWS and wants to understand their security responsibilities. Which controls does the customer FULLY inherit from AWS with no additional customer action required?",
        "zh_question": "一家公司正在 AWS 上構建 AI 應用程式，並希望了解其安全責任。客戶從 AWS 完全繼承哪些控制措施，無需客戶採取額外行動？",
        "options": {
            "A": "Data encryption settings",
            "B": "IAM user management",
            "C": "Physical and environmental controls",
            "D": "Application security testing"
        },
        "zh_options": {
            "A": "資料加密設定",
            "B": "IAM 使用者管理",
            "C": "物理和環境控制",
            "D": "應用程式安全測試"
        },
        "answer": "C",
        "explanation": "Under the AWS Shared Responsibility Model, physical and environmental controls (data center security, facility access, hardware maintenance) are FULLY managed by AWS. Customers inherit these controls completely with no action required.",
        "zh_explanation": "根據 AWS 共同責任模型，物理和環境控制（資料中心安全、設施存取、硬體維護）完全由 AWS 管理。客戶完全繼承這些控制措施，無需採取任何行動。",
        "category": "AIF",
        "option_explanations": {
            "A": "資料加密設定是客戶的責任，需要客戶配置和管理。",
            "B": "IAM 使用者管理完全是客戶的責任，AWS 不管理客戶的使用者帳戶。",
            "C": "正確。物理和環境控制（如資料中心安全）完全由 AWS 負責，客戶自動繼承。",
            "D": "應用程式安全測試是客戶的責任，AWS 不為客戶應用程式執行安全測試。"
        }
    },
    {
        "id": 280,
        "question": "An independent software vendor (ISV) needs to receive notifications about AWS compliance changes that may affect their certification status. Which AWS service provides this functionality?",
        "zh_question": "一家獨立軟體供應商（ISV）需要接收可能影響其認證狀態的 AWS 合規變更通知。哪個 AWS 服務提供此功能？",
        "options": {
            "A": "Amazon GuardDuty for threat detection",
            "B": "AWS Artifact for compliance notifications and agreements",
            "C": "Amazon Inspector for vulnerability assessments",
            "D": "AWS Security Hub for security posture"
        },
        "zh_options": {
            "A": "Amazon GuardDuty 用於威脅偵測",
            "B": "AWS Artifact 用於合規通知和協議",
            "C": "Amazon Inspector 用於漏洞評估",
            "D": "AWS Security Hub 用於安全態勢"
        },
        "answer": "B",
        "explanation": "AWS Artifact provides access to AWS compliance reports and also manages compliance agreements and notifications. ISVs can use Artifact to track AWS compliance changes and access updated certifications.",
        "zh_explanation": "AWS Artifact 提供對 AWS 合規報告的存取，也管理合規協議和通知。ISV 可以使用 Artifact 追蹤 AWS 合規變更並存取更新的認證。",
        "category": "AIF",
        "option_explanations": {
            "A": "GuardDuty 偵測安全威脅，不提供合規認證狀態通知。",
            "B": "正確。AWS Artifact 是 AWS 合規文件和通知的中央服務，適合 ISV 追蹤合規變更。",
            "C": "Inspector 評估安全漏洞，不提供合規認證狀態通知。",
            "D": "Security Hub 提供整合安全態勢視圖，但不專門提供合規認證通知。"
        }
    },
    {
        "id": 281,
        "question": "A company is concerned about attacks where malicious content in retrieved documents could manipulate their RAG-based AI system. Which type of vulnerability does this represent?",
        "zh_question": "一家公司擔心檢索文件中的惡意內容可能操縱其基於 RAG 的 AI 系統。這代表哪種類型的漏洞？",
        "options": {
            "A": "Data poisoning attack",
            "B": "Prompt injection via retrieved content",
            "C": "Model inversion attack",
            "D": "Denial of service attack"
        },
        "zh_options": {
            "A": "資料投毒攻擊",
            "B": "通過檢索內容進行的提示注入",
            "C": "模型反轉攻擊",
            "D": "拒絕服務攻擊"
        },
        "answer": "B",
        "explanation": "When malicious instructions are embedded in documents that a RAG system retrieves and includes in prompts, it's called indirect prompt injection. The retrieved content acts as a vector for injecting malicious instructions into the AI.",
        "zh_explanation": "當惡意指令嵌入 RAG 系統檢索並包含在提示中的文件時，稱為間接提示注入。檢索的內容充當向 AI 注入惡意指令的載體。",
        "category": "AIF",
        "option_explanations": {
            "A": "資料投毒是通過污染訓練資料影響模型學習，不是此場景描述的攻擊。",
            "B": "正確。通過檢索文件注入惡意指令是間接提示注入（Prompt Injection），是 RAG 系統的主要安全風險。",
            "C": "模型反轉攻擊試圖從模型輸出重建訓練資料，不是此場景。",
            "D": "拒絕服務攻擊旨在使系統不可用，不是通過惡意內容操縱 AI 輸出。"
        }
    },
    {
        "id": 282,
        "question": "A company's board of directors is implementing an AI governance framework. Which characteristic is MOST important for an effective AI governance framework?",
        "zh_question": "一家公司的董事會正在實施 AI 治理框架。對於有效的 AI 治理框架，哪個特性最重要？",
        "options": {
            "A": "It should be created once and never updated",
            "B": "It should only be applied to externally-facing AI systems",
            "C": "It should focus solely on technical metrics",
            "D": "It should define clear accountability and responsibility for AI decisions"
        },
        "zh_options": {
            "A": "應該創建一次，永不更新",
            "B": "應該只適用於面向外部的 AI 系統",
            "C": "應該只關注技術指標",
            "D": "應該為 AI 決策定義明確的責任和問責制"
        },
        "answer": "D",
        "explanation": "An effective AI governance framework MUST define clear accountability structures: who is responsible for AI decisions, who oversees AI systems, and who is accountable when AI causes harm. This is the foundation of responsible AI governance.",
        "zh_explanation": "有效的 AI 治理框架必須定義明確的責任結構：誰負責 AI 決策、誰監督 AI 系統、以及當 AI 造成傷害時誰承擔責任。這是負責任 AI 治理的基礎。",
        "category": "AIF",
        "option_explanations": {
            "A": "AI 治理框架需要隨著技術和監管環境的變化而定期更新。",
            "B": "治理框架應適用於所有 AI 系統，包括內部使用的系統。",
            "C": "僅關注技術指標忽略了倫理、法律和社會影響等重要方面。",
            "D": "正確。明確的責任和問責制是 AI 治理框架最重要的特性。"
        }
    },
    {
        "id": 283,
        "question": "A company wants to connect their Amazon Bedrock workloads to their VPC resources without routing traffic through the public internet. Which AWS service should the company use?",
        "zh_question": "一家公司希望將其 Amazon Bedrock 工作負載連接到其 VPC 資源，而不通過公共網際網路路由流量。公司應使用哪個 AWS 服務？",
        "options": {
            "A": "AWS PrivateLink",
            "B": "Amazon CloudFront",
            "C": "AWS Direct Connect only",
            "D": "Amazon Route 53"
        },
        "zh_options": {
            "A": "AWS PrivateLink",
            "B": "Amazon CloudFront",
            "C": "僅 AWS Direct Connect",
            "D": "Amazon Route 53"
        },
        "answer": "A",
        "explanation": "AWS PrivateLink enables private connectivity between VPCs and AWS services (including Bedrock) without routing traffic through the public internet. Traffic remains within the AWS network, enhancing security.",
        "zh_explanation": "AWS PrivateLink 在 VPC 和 AWS 服務（包括 Bedrock）之間實現私有連接，流量不通過公共網際網路路由。流量保留在 AWS 網路內，增強安全性。",
        "category": "AIF",
        "option_explanations": {
            "A": "正確。AWS PrivateLink 允許 VPC 到 AWS 服務的私有連接，不通過公共網際網路。",
            "B": "CloudFront 是 CDN，用於公共內容分發，不提供私有 VPC 到服務的連接。",
            "C": "Direct Connect 連接本地資料中心到 AWS，不是 VPC 到 AWS 服務的私有連接方案。",
            "D": "Route 53 是 DNS 服務，不提供私有網路連接。"
        }
    },
    {
        "id": 284,
        "question": "A multinational company is deploying an AI system across multiple countries. The company needs to ensure compliance with local AI regulations in each country. Which governance approach is MOST appropriate?",
        "zh_question": "一家跨國公司正在多個國家部署 AI 系統。公司需要確保在每個國家遵守當地的 AI 法規。哪種治理方法最合適？",
        "options": {
            "A": "Apply only the home country's regulations globally",
            "B": "Ignore local regulations in favor of efficiency",
            "C": "Apply the same model globally regardless of local laws",
            "D": "Assess and comply with local AI laws and regulations in each jurisdiction"
        },
        "zh_options": {
            "A": "在全球範圍內只應用本國法規",
            "B": "為了效率而忽視當地法規",
            "C": "無論當地法律如何，在全球應用相同的模型",
            "D": "在每個司法管轄區評估並遵守當地 AI 法律法規"
        },
        "answer": "D",
        "explanation": "For multinational deployments, companies must assess and comply with local AI regulations in each jurisdiction (e.g., EU AI Act, China AI regulations, US state laws). A one-size-fits-all approach risks non-compliance and legal consequences.",
        "zh_explanation": "對於跨國部署，公司必須在每個司法管轄區評估並遵守當地 AI 法規（如歐盟 AI 法案、中國 AI 法規、美國州法律）。一刀切的方法面臨不合規和法律後果的風險。",
        "category": "AIF",
        "option_explanations": {
            "A": "只應用本國法規在其他國家可能不符合當地法律要求。",
            "B": "忽視當地法規可能導致法律責任、罰款和業務暫停。",
            "C": "忽略當地法律應用統一模型可能在某些司法管轄區非法。",
            "D": "正確。跨國部署必須在每個國家評估並遵守當地的 AI 法律法規。"
        }
    },
]
