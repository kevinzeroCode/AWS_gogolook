CLF_BATCH5 = [
  {
    "id": 129, "exam": "CLF",
    "question": "What are the advantages of cloud computing over computing on-premises? (Select the best answer.)",
    "question_zh": "雲端運算相較於本地端運算有哪些優勢？（選擇最佳答案）",
    "options": {
      "A": {"en": "Avoid large capital purchases", "zh": "避免大型資本採購"},
      "B": {"en": "Use on-demand capacity", "zh": "使用按需容量"},
      "C": {"en": "Go global in minutes", "zh": "幾分鐘內實現全球部署"},
      "D": {"en": "Increase speed and agility", "zh": "提高速度和靈活性"},
      "E": {"en": "All of the above", "zh": "以上皆是"}
    },
    "correct": ["E"], "multi": False,
    "explanations": {
      "A": "✓ 雲端以訂閱/按量計費取代大型資本採購，將 CapEx 轉為 OpEx，這是雲端優勢之一。",
      "B": "✓ 雲端提供彈性容量，可根據需求即時擴大或縮小，無需預先購買，這也是優勢之一。",
      "C": "✓ AWS 全球基礎設施讓你只需幾分鐘即可在多個區域部署應用程式，這也是優勢之一。",
      "D": "✓ 雲端讓開發者能快速試驗和部署，大幅提高創新速度和業務靈活性，這也是優勢之一。",
      "E": "✓ 正確。選項 A、B、C、D 全部都是雲端運算的核心優勢，因此「以上皆是」是正確答案。"
    }
  },
  {
    "id": 130, "exam": "CLF",
    "question": "What is the pricing model that enables AWS customers to pay for resources on an as-needed basis?",
    "question_zh": "哪種定價模型讓 AWS 客戶能夠按需付費使用資源？",
    "options": {
      "A": {"en": "Pay as you go", "zh": "隨用隨付"},
      "B": {"en": "Pay as you decommission", "zh": "隨停隨付"},
      "C": {"en": "Pay as you buy", "zh": "隨買隨付"},
      "D": {"en": "Pay as you reserve", "zh": "隨訂隨付"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確 — Pay as you go（隨用隨付）是 AWS 的核心定價模型，只需為實際使用的資源付費，沒有前期費用或長期承諾。",
      "B": "✗ 「隨停隨付」不是 AWS 定價模型；雖然停止資源後就停止計費，但這不是定價模型的名稱。",
      "C": "✗ 「隨買隨付」不是標準術語；AWS 不要求你「買」資源，而是租用/按使用量付費。",
      "D": "✗ Reserved（預留）實例確實是 AWS 的一種選項，但它是預先承諾換取折扣的模型，不是「按需付費」模型。"
    }
  },
  {
    "id": 131, "exam": "CLF",
    "question": "Which of these is NOT a cloud deployment model?",
    "question_zh": "下列哪項不是雲端部署模型？",
    "options": {
      "A": {"en": "System administration as a service", "zh": "系統管理即服務"},
      "B": {"en": "Software as a service (SaaS)", "zh": "軟體即服務（SaaS）"},
      "C": {"en": "Infrastructure as a service (IaaS)", "zh": "基礎設施即服務（IaaS）"},
      "D": {"en": "Platform as a service (PaaS)", "zh": "平台即服務（PaaS）"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確（即非雲端部署模型）。「系統管理即服務」是虛構的概念，不屬於標準雲端服務模型。",
      "B": "✗ SaaS（軟體即服務）是真實的雲端服務模型，如 Gmail、Microsoft 365、Salesforce 等。",
      "C": "✗ IaaS（基礎設施即服務）是真實的雲端服務模型，如 Amazon EC2、Amazon S3。",
      "D": "✗ PaaS（平台即服務）是真實的雲端服務模型，如 AWS Elastic Beanstalk、Google App Engine。"
    }
  },
  {
    "id": 132, "exam": "CLF",
    "question": "True or False? AWS owns and maintains the network-connected hardware required for application services, while you provision and use what you need.",
    "question_zh": "對或錯？AWS 擁有並維護應用程式服務所需的網路連接硬體，而你則按需配置和使用。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確。這正確描述了雲端運算的本質：AWS 負責實體硬體的所有權和維護，客戶只需通過 AWS 主控台或 API 按需配置和使用資源，無需管理實體設備。",
      "B": "✗ 此陳述是正確的，所以答案是「真」而非「假」。"
    }
  },
  {
    "id": 133, "exam": "CLF",
    "question": "Which of the following are NOT benefits of AWS Cloud computing? (Choose two.)",
    "question_zh": "下列哪些不是 AWS 雲端運算的好處？（選擇兩個）",
    "options": {
      "A": {"en": "Temporary and disposable resources", "zh": "臨時性和可拋棄式資源"},
      "B": {"en": "High availability", "zh": "高可用性"},
      "C": {"en": "Multiple procurement cycles", "zh": "多個採購週期"},
      "D": {"en": "High latency", "zh": "高延遲"},
      "E": {"en": "Fault-tolerant databases", "zh": "容錯資料庫"}
    },
    "correct": ["C", "D"], "multi": True,
    "explanations": {
      "A": "✗ 臨時性和可拋棄式資源是雲端優勢——可以輕鬆啟動、測試後刪除資源，降低實驗成本和風險。",
      "B": "✗ 高可用性是雲端的核心優勢，AWS 提供多可用區部署確保服務持續可用。",
      "C": "✓ 正確（非好處）。多個採購週期是傳統 IT 的痛點；雲端消除了繁瑣的硬體採購流程。",
      "D": "✓ 正確（非好處）。高延遲是需要避免的問題；AWS 全球基礎設施旨在降低而非增加延遲。",
      "E": "✗ 容錯資料庫（如 Amazon RDS Multi-AZ）是雲端提供的重要優勢，可確保資料庫高可用性和資料持久性。"
    }
  },
  {
    "id": 134, "exam": "CLF",
    "question": "Which of the following is a compute service?",
    "question_zh": "下列哪項是運算服務？",
    "options": {
      "A": {"en": "Amazon S3", "zh": "Amazon S3"},
      "B": {"en": "Amazon CloudFront", "zh": "Amazon CloudFront"},
      "C": {"en": "Amazon Redshift", "zh": "Amazon Redshift"},
      "D": {"en": "Amazon VPC", "zh": "Amazon VPC"},
      "E": {"en": "Amazon EC2", "zh": "Amazon EC2"}
    },
    "correct": ["E"], "multi": False,
    "explanations": {
      "A": "✗ Amazon S3 是物件儲存服務（Simple Storage Service），不是運算服務。",
      "B": "✗ Amazon CloudFront 是內容傳遞網路（CDN）服務，負責靜態/動態內容加速分發，不是運算服務。",
      "C": "✗ Amazon Redshift 是資料倉儲/分析服務，用於大規模資料分析，不是通用運算服務。",
      "D": "✗ Amazon VPC（Virtual Private Cloud）是網路/虛擬私有雲服務，不是運算服務。",
      "E": "✓ 正確 — Amazon EC2（Elastic Compute Cloud）是 AWS 的核心運算服務，提供可調整大小的虛擬伺服器（實例）。"
    }
  },
  {
    "id": 135, "exam": "CLF",
    "question": "True or False? Cloud computing provides a simple way to access servers, storage, databases, and a broad set of application services over the internet. You own the network-connected hardware required for these services and Amazon Web Services provisions what you need.",
    "question_zh": "對或錯？雲端運算提供了一種通過網際網路存取伺服器、儲存、資料庫和廣泛應用服務的簡便方式。你擁有這些服務所需的網路連接硬體，而 Amazon Web Services 負責配置你所需的內容。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ 此陳述是錯的，因為它顛倒了角色——陳述說「你」擁有硬體，但實際上是 AWS 擁有硬體。",
      "B": "✓ 正確 — 此陳述是錯的（False）。正確說法應該是：AWS 擁有並維護網路連接硬體，而「你」（客戶）配置和使用所需的資源，而非相反。"
    }
  },
  {
    "id": 136, "exam": "CLF",
    "question": "Which of these are ways to access AWS core services? (Choose three.)",
    "question_zh": "下列哪些是存取 AWS 核心服務的方式？（選擇三個）",
    "options": {
      "A": {"en": "AWS Command Line Interface (AWS CLI)", "zh": "AWS 命令列介面（AWS CLI）"},
      "B": {"en": "Technical support calls", "zh": "技術支援電話"},
      "C": {"en": "Software Development Kits (SDKs)", "zh": "軟體開發工具包（SDK）"},
      "D": {"en": "AWS Marketplace", "zh": "AWS Marketplace"},
      "E": {"en": "AWS Management Console", "zh": "AWS 管理主控台"}
    },
    "correct": ["A", "C", "E"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — AWS CLI 讓使用者從終端命令列管理 AWS 服務，適合自動化腳本和批次操作。",
      "B": "✗ 技術支援電話是聯絡 AWS Support 的方式，不是直接存取和管理 AWS 服務的程式化方式。",
      "C": "✓ 正確 — SDK（如 Python boto3、Java SDK、Node.js SDK）讓開發者以程式碼方式呼叫 AWS API 管理服務。",
      "D": "✗ AWS Marketplace 是購買、部署第三方軟體和解決方案的市集，不是存取核心 AWS 服務的方式。",
      "E": "✓ 正確 — AWS 管理主控台是基於瀏覽器的圖形介面，讓使用者以點選方式管理所有 AWS 服務。"
    }
  },
  {
    "id": 137, "exam": "CLF",
    "question": "For certain services like Amazon EC2 and Amazon RDS, you can invest in reserved capacity. What options are available for Reserved Instances? (Choose three.)",
    "question_zh": "對於 Amazon EC2 和 Amazon RDS 等特定服務，你可以投資預留容量。預留實例有哪些付款選項？（選擇三個）",
    "options": {
      "A": {"en": "PURI (Partial Upfront Reserved Instance)", "zh": "PURI（部分前期預留實例）"},
      "B": {"en": "MURI (Monthly Upfront Reserved Instance)", "zh": "MURI（每月前期預留實例）"},
      "C": {"en": "DURI (Daily Upfront Reserved Instance)", "zh": "DURI（每日前期預留實例）"},
      "D": {"en": "AURI (All Upfront Reserved Instance)", "zh": "AURI（全額前期預留實例）"},
      "E": {"en": "NURI (No Upfront Reserved Instance)", "zh": "NURI（無前期費用預留實例）"}
    },
    "correct": ["A", "D", "E"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — PURI（Partial Upfront）：預付部分費用，其餘按月付，折扣介於 AURI 和 NURI 之間。",
      "B": "✗ MURI 不是 AWS 預留實例的有效選項，此縮寫不存在於 AWS 定價選項中。",
      "C": "✗ DURI 不是 AWS 預留實例的有效選項，此縮寫不存在於 AWS 定價選項中。",
      "D": "✓ 正確 — AURI（All Upfront）：一次性支付全部費用，提供最大折扣（可比按需價格節省高達 75%）。",
      "E": "✓ 正確 — NURI（No Upfront）：無需前期付款，以稍高的每月費率付費，但仍比按需（On-Demand）價格便宜。"
    }
  },
  {
    "id": 138, "exam": "CLF",
    "question": "Where can a customer go to get more details about Amazon EC2 billing activity that took place 3 months ago?",
    "question_zh": "客戶可以去哪裡獲取 3 個月前發生的 Amazon EC2 計費活動的詳細資訊？",
    "options": {
      "A": {"en": "Amazon EC2 dashboard", "zh": "Amazon EC2 儀表板"},
      "B": {"en": "AWS Cost Explorer", "zh": "AWS Cost Explorer"},
      "C": {"en": "AWS Trusted Advisor dashboard", "zh": "AWS Trusted Advisor 儀表板"},
      "D": {"en": "AWS CloudTrail logs stored in Amazon S3", "zh": "儲存在 Amazon S3 中的 AWS CloudTrail 日誌"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ EC2 儀表板顯示當前資源狀態（運行中的實例等），不提供歷史計費分析功能。",
      "B": "✓ 正確 — AWS Cost Explorer 專門用於可視化和分析歷史 AWS 費用，支援查詢過去 13 個月的計費資料，可按服務、區域、標籤等維度分析。",
      "C": "✗ AWS Trusted Advisor 提供最佳實踐建議（安全、成本節省、效能、容錯、服務限制），不是查看歷史計費記錄的工具。",
      "D": "✗ CloudTrail 記錄 AWS API 呼叫和操作日誌（誰做了什麼），不是計費詳情查詢工具。"
    }
  },
  {
    "id": 139, "exam": "CLF",
    "question": "True or false? To receive the discounted rate associated with Reserved Instances, you must make a full, upfront payment for the term of the agreement.",
    "question_zh": "對或錯？要獲得預留實例相關的折扣費率，你必須為協議期限預先全額付款。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ 此陳述不正確。全額前期付款（AURI）只是三種付款選項之一，不是獲得折扣的唯一方式。",
      "B": "✓ 正確（False）— 預留實例有三種付款選項：AURI（全額前期，最大折扣）、PURI（部分前期）、NURI（無前期）。你不必全額預付也能獲得折扣，只是折扣幅度不同。"
    }
  },
  {
    "id": 140, "exam": "CLF",
    "question": "There is no charge for which of the following? (Choose two.)",
    "question_zh": "下列哪些項目不收費？（選擇兩個）",
    "options": {
      "A": {"en": "Compute", "zh": "運算"},
      "B": {"en": "Storage", "zh": "儲存"},
      "C": {"en": "Inbound data transfer (with some exceptions)", "zh": "入站資料傳輸（有些例外）"},
      "D": {"en": "Outbound data transfer", "zh": "出站資料傳輸"},
      "E": {"en": "Data transfer between services within the same AWS Region", "zh": "同一 AWS 區域內服務之間的資料傳輸"}
    },
    "correct": ["C", "E"], "multi": True,
    "explanations": {
      "A": "✗ 運算（EC2 等）按使用時間和實例類型收費，不是免費的。",
      "B": "✗ 儲存（S3、EBS 等）按儲存量、存取次數和請求次數收費，不是免費的。",
      "C": "✓ 正確 — 入站資料傳輸（從網際網路流入 AWS）在大多數情況下不收費，AWS 鼓勵資料流入其平台。",
      "D": "✗ 出站資料傳輸（從 AWS 流出到網際網路）按 GB 收費，費用因區域和流量大小而異。",
      "E": "✓ 正確 — 同一 AWS 區域內 AWS 服務之間的資料傳輸不收費（例如同區域 EC2 到 S3、Lambda 到 DynamoDB）。"
    }
  },
  {
    "id": 141, "exam": "CLF",
    "question": "What are the four support plans offered by AWS Support?",
    "question_zh": "AWS Support 提供哪四種支援計劃？",
    "options": {
      "A": {"en": "Basic, Developer, Business, Enterprise", "zh": "基本、開發者、商業、企業"},
      "B": {"en": "Basic, Startup, Business, Enterprise", "zh": "基本、新創、商業、企業"},
      "C": {"en": "Free, Bronze, Silver, Gold", "zh": "免費、銅級、銀級、金級"},
      "D": {"en": "All support is free", "zh": "所有支援都是免費的"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確 — AWS 四個支援計劃：Basic（免費，僅文件/論壇/健康通知）、Developer（工作時間 email 支援）、Business（24/7 電話/聊天，TAM 存取）、Enterprise（15 分鐘回應，專屬 TAM）。",
      "B": "✗ 「Startup（新創）」不是 AWS 支援計劃的名稱，正確的第二層是「Developer（開發者）」。",
      "C": "✗ AWS 支援計劃不使用金屬等級命名（銅/銀/金），這是其他廠商的常見命名方式。",
      "D": "✗ 只有 Basic 計劃是免費的；Developer、Business 和 Enterprise 計劃都需要按月付費（費用按照 AWS 月費的百分比計算）。"
    }
  },
  {
    "id": 142, "exam": "CLF",
    "question": "As AWS grows, the cost of doing business is reduced and savings are passed back to the customer with lower pricing. What is this optimization called?",
    "question_zh": "隨著 AWS 的增長，業務成本降低，節省的費用以更低的定價回饋給客戶。這種優化叫什麼？",
    "options": {
      "A": {"en": "EC2 Right Sizing", "zh": "EC2 右型調整"},
      "B": {"en": "Expenditure awareness", "zh": "支出感知"},
      "C": {"en": "Economies of scale", "zh": "規模經濟"},
      "D": {"en": "Matching supply and demand", "zh": "供需匹配"}
    },
    "correct": ["C"], "multi": False,
    "explanations": {
      "A": "✗ EC2 Right Sizing 是指調整 EC2 實例大小以匹配實際工作負載需求，是一種成本優化技術，但不是描述 AWS 業務成長帶來降價的術語。",
      "B": "✗ 支出感知（Expenditure awareness）是 AWS Well-Architected 成本優化支柱的原則之一，指了解自己的花費情況，不是此概念。",
      "C": "✓ 正確 — 規模經濟（Economies of scale）：AWS 服務的客戶越多，每單位運營成本越低，AWS 將節省的費用以更低的價格回饋客戶（AWS 已累計降價超過 100 次）。",
      "D": "✗ 供需匹配（Matching supply and demand）是指根據實際需求彈性調整資源容量，是另一個 AWS 雲端優勢概念，不是此問題的答案。"
    }
  },
  {
    "id": 143, "exam": "CLF",
    "question": "True or false? AWS offers a variety of services at no charge such as Amazon VPC, AWS IAM, Consolidated Billing, AWS Elastic Beanstalk, automatic scaling, AWS OpsWorks, and AWS CloudFormation. However, you might be charged for other AWS services that you use in conjunction with these services.",
    "question_zh": "對或錯？AWS 提供多種免費服務，例如 Amazon VPC、AWS IAM、合併帳單、Elastic Beanstalk、自動擴縮、OpsWorks 和 CloudFormation。但是，與這些服務搭配使用的其他 AWS 服務可能需要收費。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["A"], "multi": False,
    "explanations": {
      "A": "✓ 正確 — VPC、IAM、CloudFormation 等服務本身不收費，但它們管理或創建的底層資源（如 CloudFormation 啟動的 EC2 實例、Elastic Beanstalk 使用的 RDS 資料庫）仍按標準費率計費。",
      "B": "✗ 此陳述是正確的，所以答案是「真」而非「假」。"
    }
  },
  {
    "id": 144, "exam": "CLF",
    "question": "When are free data transfers applicable across AWS? (Choose two.)",
    "question_zh": "AWS 中何時適用免費資料傳輸？（選擇兩個）",
    "options": {
      "A": {"en": "Free inbound data transfer across all AWS services in all Regions", "zh": "所有區域所有 AWS 服務的免費入站資料傳輸"},
      "B": {"en": "Free outbound data transfer across all AWS services in all Regions", "zh": "所有區域所有 AWS 服務的免費出站資料傳輸"},
      "C": {"en": "Free inbound data transfer for Amazon EC2 instances", "zh": "Amazon EC2 實例的免費入站資料傳輸"},
      "D": {"en": "Free outbound data transfer between AWS services within the same Region", "zh": "同一區域內 AWS 服務之間的免費出站資料傳輸"}
    },
    "correct": ["A", "C"], "multi": True,
    "explanations": {
      "A": "✓ 正確 — 入站資料傳輸（從網際網路流入 AWS）在所有服務和所有區域均免費，AWS 歡迎資料進入其平台。",
      "B": "✗ 出站資料傳輸（從 AWS 傳輸到網際網路）需要按 GB 付費，是 AWS 主要的資料傳輸費用來源之一。",
      "C": "✓ 正確 — 流入 Amazon EC2 實例的入站資料傳輸是免費的，這是選項 A 一般規則的具體體現。",
      "D": "✗ 雖然同區域服務之間的資料傳輸通常免費，但此選項將其描述為「出站」資料傳輸，在語義和分類上容易混淆，不是最準確的表述。"
    }
  },
  {
    "id": 145, "exam": "CLF",
    "question": "True or False? Unlimited services are available with the AWS Free Tier to new AWS customers for 12 months following their AWS sign-up date.",
    "question_zh": "對或錯？AWS 免費方案在新 AWS 客戶登記後的 12 個月內提供無限制的服務。",
    "options": {
      "A": {"en": "True", "zh": "對"},
      "B": {"en": "False", "zh": "錯"}
    },
    "correct": ["B"], "multi": False,
    "explanations": {
      "A": "✗ 此陳述不正確。AWS 免費方案有明確的使用限制，不是無限制的。",
      "B": "✓ 正確（False）— AWS 免費方案有嚴格的使用限制，例如：EC2 t2.micro 每月僅 750 小時、S3 僅 5GB 儲存、Lambda 每月 100 萬次請求等。超出限制將按標準費率計費，「無限制」的說法是錯誤的。"
    }
  },
]
