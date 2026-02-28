
CLF_BATCH4 = [
  {
    "id":100,"exam":"CLF",
    "question":"Which of the following is a benefit of Amazon EC2 over physical servers?",
    "question_zh":"相較於實體伺服器，Amazon EC2 的優勢是什麼？",
    "options":{
      "A":{"en":"Automated backup","zh":"自動備份"},
      "B":{"en":"Root/administrator access","zh":"Root/管理員存取權"},
      "C":{"en":"The ability to choose hardware vendors","zh":"能夠選擇硬體廠商"},
      "D":{"en":"Paying only for what you use","zh":"只為實際使用量付費"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ EC2 不會自動備份，備份需要自行設定（如 AWS Backup 或 EBS Snapshot）。實體伺服器和雲端都不會主動幫你備份。",
      "B":"✗ Root/admin 存取是 EC2 和實體伺服器都具備的功能，不是 EC2 相對於實體伺服器的差異化優勢。",
      "C":"✗ 在 AWS 上無法選擇硬體廠商，這是實體伺服器才有的能力（雲端抽象化了底層硬體）。",
      "D":"✓ 正確 — EC2 按隨需（On-Demand）模式按秒/分計費，用多少付多少。實體伺服器需要預購、無論使用率高低都要支付全額成本，EC2 的彈性計費是核心優勢之一。"
    }
  },
  {
    "id":101,"exam":"CLF",
    "question":"Which AWS networking service enables a company to create a virtual network within AWS?",
    "question_zh":"哪個 AWS 網路服務讓公司能在 AWS 內建立虛擬網路？",
    "options":{
      "A":{"en":"AWS Direct Connect","zh":"AWS Direct Connect"},
      "B":{"en":"Amazon VPC","zh":"Amazon VPC"},
      "C":{"en":"AWS Config","zh":"AWS Config"},
      "D":{"en":"Amazon Route 53","zh":"Amazon Route 53"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Direct Connect 提供從企業資料中心到 AWS 的專用實體連線，不是 AWS 內部的虛擬網路。",
      "B":"✓ 正確 — Amazon VPC（Virtual Private Cloud）讓您在 AWS 中定義邏輯隔離的虛擬網路，包含子網路、路由表、安全群組和網路 ACL，完全控制網路環境。",
      "C":"✗ Config 追蹤資源配置合規性，不是網路服務。",
      "D":"✗ Route 53 是 DNS 和流量路由服務，不負責建立虛擬網路。"
    }
  },
  {
    "id":102,"exam":"CLF",
    "question":"Which of the following can be used as an additional layer of security when logging into the AWS Console, beyond username and password?",
    "question_zh":"除了使用者名稱和密碼之外，下列哪項可作為登入 AWS Console 的額外安全層？",
    "options":{
      "A":{"en":"Secondary user name","zh":"次要使用者名稱"},
      "B":{"en":"Secondary password","zh":"次要密碼"},
      "C":{"en":"Root access privileges","zh":"Root 存取權限"},
      "D":{"en":"Multi-Factor Authentication (MFA)","zh":"多因素驗證 (MFA)"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 次要使用者名稱仍屬於「知識因素」（Something you know），不能構成真正的多因素驗證。",
      "B":"✗ 次要密碼同樣是知識因素，只是增加複雜度，不是真正的第二驗證因素。",
      "C":"✗ Root 存取是帳號最高權限，與登入安全層無關，且不應用於日常操作。",
      "D":"✓ 正確 — MFA 加入第二因素（如 Authenticator App 的 TOTP 代碼或硬體金鑰），即使密碼外洩，攻擊者也無法登入，是 AWS 強烈建議的安全措施。"
    }
  },
  {
    "id":103,"exam":"CLF",
    "question":"Which of the following is NOT a feature of an edge location?",
    "question_zh":"下列哪項不是 Edge Location（邊緣站點）的功能？",
    "options":{
      "A":{"en":"Used in conjunction with the CloudFront service","zh":"與 CloudFront 服務配合使用"},
      "B":{"en":"Distribute content to users","zh":"向使用者分發內容"},
      "C":{"en":"Distribute load across multiple resources","zh":"將負載分散到多個資源"},
      "D":{"en":"Cache common responses","zh":"快取常用回應"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗（是功能）— Edge Location 是 CloudFront 的核心節點，CloudFront 利用它在全球分發內容。",
      "B":"✗（是功能）— Edge Location 的主要目的就是就近向全球使用者分發快取內容。",
      "C":"✓ 正確（非功能）— 負載分散是 Elastic Load Balancer (ELB) 的職責，Edge Location 不負責將請求分配到多個後端資源。",
      "D":"✗（是功能）— Edge Location 會快取 CloudFront 分發的靜態和動態內容，減少回源請求。"
    }
  },
  {
    "id":104,"exam":"CLF",
    "question":"Which is the secure way of using AWS API to call AWS services from EC2 instances?",
    "question_zh":"從 EC2 執行個體呼叫 AWS 服務 API 的安全方式是什麼？",
    "options":{
      "A":{"en":"IAM Users","zh":"IAM 使用者"},
      "B":{"en":"IAM Roles","zh":"IAM 角色"},
      "C":{"en":"IAM Policies","zh":"IAM 政策"},
      "D":{"en":"IAM Groups","zh":"IAM 群組"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 將 IAM 使用者的存取金鑰硬寫在 EC2 程式碼或設定檔中是安全反模式，一旦金鑰洩漏風險極大，AWS 強烈不建議此做法。",
      "B":"✓ 正確 — 將 IAM Role 附加到 EC2 執行個體，應用程式透過 Instance Metadata Service 動態取得臨時憑證，無需在程式碼中存放任何靜態金鑰，是最安全的最佳實踐。",
      "C":"✗ IAM Policy 定義允許或拒絕的操作，但它附加在角色/使用者上，本身不是呼叫 API 的機制。",
      "D":"✗ IAM Group 用於管理使用者集合，不是給 EC2 執行個體賦予 API 呼叫能力的方式。"
    }
  },
  {
    "id":105,"exam":"CLF",
    "question":"In AWS billing, which option can be used to ensure costs can be reduced if you have multiple accounts?",
    "question_zh":"在 AWS 帳單中，擁有多個帳號時，哪個選項可用於降低成本？",
    "options":{
      "A":{"en":"Combined billing","zh":"合併帳單"},
      "B":{"en":"It is not possible to reduce costs with multiple accounts","zh":"多個帳號無法降低成本"},
      "C":{"en":"Consolidated billing","zh":"整合帳單（Consolidated Billing）"},
      "D":{"en":"Costs are automatically reduced for multiple accounts by AWS","zh":"AWS 自動為多個帳號降低成本"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 「Combined billing」不是 AWS 的正式術語，正確術語是 Consolidated Billing。",
      "B":"✗ 這是錯誤說法，整合帳單確實可以合併用量獲得批量折扣。",
      "C":"✓ 正確 — Consolidated Billing（整合帳單）將組織內所有帳號的用量合計，整體用量越高可獲得更多批量折扣（如 S3、EC2 等），節省成本。",
      "D":"✗ AWS 不會自動降低多帳號成本，需要客戶主動設定 Organizations 和整合帳單。"
    }
  },
  {
    "id":106,"exam":"CLF",
    "question":"Which of the below can be used to access AWS Services? (Choose 3)",
    "question_zh":"下列哪些可用於存取 AWS 服務？（選3項）",
    "options":{
      "A":{"en":"Amazon CloudWatch","zh":"Amazon CloudWatch"},
      "B":{"en":"Software Development Kits (SDK)","zh":"軟體開發套件 (SDK)"},
      "C":{"en":"AWS Availability Zones","zh":"AWS 可用區域"},
      "D":{"en":"AWS Management Console","zh":"AWS Management Console"},
      "E":{"en":"AWS Command Line Interface (AWS CLI)","zh":"AWS 命令列介面 (CLI)"}
    },
    "correct":["B","D","E"],"multi":True,
    "explanations":{
      "A":"✗ CloudWatch 是監控服務，本身不是存取 AWS 服務的入口或工具。",
      "B":"✓ 正確 — AWS SDK 提供各種程式語言（Python、Java、.NET 等）的函式庫，讓應用程式以程式化方式呼叫 AWS API。",
      "C":"✗ 可用區域是 AWS 基礎設施的物理概念，不是存取 AWS 服務的工具或介面。",
      "D":"✓ 正確 — AWS Management Console 是圖形化網頁介面，是最直觀的 AWS 服務存取方式。",
      "E":"✓ 正確 — AWS CLI 是命令列工具，透過終端機以指令方式管理 AWS 服務，適合腳本自動化。"
    }
  },
  {
    "id":107,"exam":"CLF",
    "question":"What are the three cloud deployment models? (Choose 3)",
    "question_zh":"雲端有哪三種部署模型？（選3項）",
    "options":{
      "A":{"en":"Hybrid cloud","zh":"混合雲"},
      "B":{"en":"Private cloud","zh":"私有雲"},
      "C":{"en":"Platform as a Service (PaaS)","zh":"平台即服務 (PaaS)"},
      "D":{"en":"Software as a Service (SaaS)","zh":"軟體即服務 (SaaS)"},
      "E":{"en":"All-in cloud (Public cloud)","zh":"全雲端（公有雲）"},
      "F":{"en":"Infrastructure as a Service (IaaS)","zh":"基礎設施即服務 (IaaS)"}
    },
    "correct":["A","B","E"],"multi":True,
    "explanations":{
      "A":"✓ 正確 — 混合雲（Hybrid）結合私有雲/本地端與公有雲，透過 Direct Connect 或 VPN 連接，是許多企業的過渡架構。",
      "B":"✓ 正確 — 私有雲（Private）在企業自有或租用的專屬設施上運行，完全掌控基礎設施。",
      "C":"✗ PaaS 是雲端服務模型（Service Model），不是部署模型。",
      "D":"✗ SaaS 是雲端服務模型（Service Model），不是部署模型。",
      "E":"✓ 正確 — 全雲端/公有雲（All-in cloud / Public cloud）完全使用雲端供應商的基礎設施，無本地端資源。",
      "F":"✗ IaaS 是雲端服務模型（Service Model），不是部署模型。"
    }
  },
  {
    "id":108,"exam":"CLF",
    "question":"Which of the following languages work on Lambda? (Choose two)",
    "question_zh":"下列哪些語言可在 Lambda 上運行？（選2項）",
    "options":{
      "A":{"en":"Scala","zh":"Scala"},
      "B":{"en":"C++","zh":"C++"},
      "C":{"en":"Python","zh":"Python"},
      "D":{"en":"Node.js","zh":"Node.js"}
    },
    "correct":["C","D"],"multi":True,
    "explanations":{
      "A":"✗ Lambda 原生不支援 Scala（可透過 Java runtime 間接使用，但不是原生支援語言）。",
      "B":"✗ Lambda 不支援 C++（可用 Lambda Runtime API 自訂，但不在標準支援清單）。",
      "C":"✓ 正確 — Python 是 Lambda 官方支援的執行環境之一，是最常用的 Lambda 語言之一。",
      "D":"✓ 正確 — Node.js 是 Lambda 官方支援的執行環境，適合事件驅動的輕量無伺服器函數。"
    }
  },
  {
    "id":109,"exam":"CLF",
    "question":"Which of the following provide capability for serverless websites? (Choose two)",
    "question_zh":"下列哪些服務提供無伺服器網站的能力？（選2項）",
    "options":{
      "A":{"en":"Lambda","zh":"AWS Lambda"},
      "B":{"en":"Route 53","zh":"Amazon Route 53"},
      "C":{"en":"S3","zh":"Amazon S3"},
      "D":{"en":"EC2","zh":"Amazon EC2"}
    },
    "correct":["A","C"],"multi":True,
    "explanations":{
      "A":"✓ 正確 — Lambda 提供無伺服器後端邏輯，結合 API Gateway 可建立完整的無伺服器 API 端點。",
      "B":"✗ Route 53 是 DNS 服務，可用於網站的域名解析，但本身不提供網站內容或後端邏輯。",
      "C":"✓ 正確 — S3 可託管靜態網站（HTML、CSS、JS），直接透過 URL 提供服務，不需要伺服器，是無伺服器前端的核心服務。",
      "D":"✗ EC2 是虛擬機器，需要管理伺服器，屬於有伺服器架構，不是無伺服器解決方案。"
    }
  },
  {
    "id":110,"exam":"CLF",
    "question":"Which are 2 ways that AWS allows you to link accounts? (Choose two)",
    "question_zh":"AWS 允許連結帳號的兩種方式是什麼？（選2項）",
    "options":{
      "A":{"en":"IAM","zh":"IAM"},
      "B":{"en":"Consolidated Billing","zh":"整合帳單"},
      "C":{"en":"AWS Organizations","zh":"AWS Organizations"},
      "D":{"en":"Cost Explorer","zh":"Cost Explorer"}
    },
    "correct":["B","C"],"multi":True,
    "explanations":{
      "A":"✗ IAM 管理帳號內的身分與存取權限，不是用來連結多個 AWS 帳號的服務。",
      "B":"✓ 正確 — Consolidated Billing（整合帳單）將多個帳號的費用合併為一張帳單，是帳號連結的帳單面向機制。",
      "C":"✓ 正確 — AWS Organizations 是管理多個 AWS 帳號的服務，可建立組織層級結構、套用服務控制政策（SCP），整合帳單也是其功能之一。",
      "D":"✗ Cost Explorer 分析帳單支出，不是連結帳號的機制。"
    }
  },
  {
    "id":111,"exam":"CLF",
    "question":"Which of the following does Elastic Beanstalk support? (Choose two)",
    "question_zh":"Elastic Beanstalk 支援下列哪些？（選2項）",
    "options":{
      "A":{"en":"Node.js","zh":"Node.js"},
      "B":{"en":"Scala","zh":"Scala"},
      "C":{"en":"C++","zh":"C++"},
      "D":{"en":"Docker","zh":"Docker"}
    },
    "correct":["A","D"],"multi":True,
    "explanations":{
      "A":"✓ 正確 — Elastic Beanstalk 原生支援 Node.js，可直接上傳 Node.js 應用程式，由 Beanstalk 管理環境。",
      "B":"✗ Scala 不在 Elastic Beanstalk 的原生支援平台清單中。",
      "C":"✗ C++ 不是 Elastic Beanstalk 支援的執行環境。",
      "D":"✓ 正確 — Elastic Beanstalk 支援 Docker，可部署任何容器化應用，提供最大靈活性。"
    }
  },
  {
    "id":112,"exam":"CLF",
    "question":"Which of the following security requirements are managed by AWS? (Choose 3)",
    "question_zh":"下列哪些安全要求是由 AWS 管理的？（選3項）",
    "options":{
      "A":{"en":"Hardware patching","zh":"硬體修補"},
      "B":{"en":"Physical security","zh":"實體安全"},
      "C":{"en":"Disk disposal","zh":"磁碟銷毀處理"},
      "D":{"en":"Password Policies","zh":"密碼政策"},
      "E":{"en":"User permissions","zh":"使用者權限"}
    },
    "correct":["A","B","C"],"multi":True,
    "explanations":{
      "A":"✓ 正確 — 底層硬體（伺服器、網路設備）的修補和更新是 AWS 的責任，客戶無法也不需要自行處理。",
      "B":"✓ 正確 — AWS 資料中心的實體安全（門禁、監控、防災）完全由 AWS 負責，客戶無需擔心。",
      "C":"✓ 正確 — 硬碟報廢後的安全銷毀（消磁、物理破壞）是 AWS 的責任，確保客戶資料不會洩漏。",
      "D":"✗ 密碼政策（IAM 密碼複雜度要求）是客戶的責任，客戶在 IAM 中自行設定。",
      "E":"✗ 使用者權限管理（IAM 角色、政策）是客戶的責任。"
    }
  },
  {
    "id":113,"exam":"CLF",
    "question":"When working on the costing for On-Demand EC2 instances, which of the following attributes determine the cost? (Choose 3)",
    "question_zh":"計算隨需 EC2 執行個體成本時，下列哪些屬性決定了費用？（選3項）",
    "options":{
      "A":{"en":"Edge location","zh":"邊緣站點"},
      "B":{"en":"Region","zh":"區域"},
      "C":{"en":"Instance Type","zh":"執行個體類型"},
      "D":{"en":"AMI Type","zh":"AMI 類型"}
    },
    "correct":["B","C","D"],"multi":True,
    "explanations":{
      "A":"✗ Edge Location 是 CloudFront 的節點，不是 EC2 的部署位置，與 EC2 定價無關。",
      "B":"✓ 正確 — EC2 的定價因區域而異（如 us-east-1 通常較便宜，ap-southeast-1 較貴），選擇不同 Region 會影響成本。",
      "C":"✓ 正確 — 執行個體類型（t3.micro vs m5.xlarge）直接決定 CPU、記憶體規格，是影響每小時費率最大的因素。",
      "D":"✓ 正確 — AMI 類型影響成本：例如使用 Windows AMI 比 Linux AMI 費用高（包含授權費），SQL Server AMI 費用更高。"
    }
  },
  {
    "id":114,"exam":"CLF",
    "question":"Which of the following provide centralized user management across your AWS resources? (Choose two)",
    "question_zh":"下列哪些提供跨 AWS 資源的集中式使用者管理？（選2項）",
    "options":{
      "A":{"en":"S3 SSE-C","zh":"S3 SSE-C 加密"},
      "B":{"en":"KMS","zh":"AWS KMS"},
      "C":{"en":"IAM","zh":"AWS IAM"},
      "D":{"en":"AWS Organizations","zh":"AWS Organizations"}
    },
    "correct":["C","D"],"multi":True,
    "explanations":{
      "A":"✗ S3 SSE-C 是 S3 客戶自管金鑰的伺服器端加密，與使用者管理無關。",
      "B":"✗ KMS 是金鑰管理服務，用於加密，不是使用者管理服務。",
      "C":"✓ 正確 — IAM 提供單一帳號內的集中式使用者、群組、角色和權限管理，是 AWS 身分管理的核心。",
      "D":"✓ 正確 — AWS Organizations 提供跨多個 AWS 帳號的集中管理，包含服務控制政策（SCP）和整合帳單，實現跨帳號的集中治理。"
    }
  },
  {
    "id":115,"exam":"CLF",
    "question":"What are the three models of cloud computing? (Choose 3)",
    "question_zh":"雲端運算有哪三種服務模型？（選3項）",
    "options":{
      "A":{"en":"All-in cloud","zh":"全雲端"},
      "B":{"en":"Infrastructure as a Service (IaaS)","zh":"基礎設施即服務 (IaaS)"},
      "C":{"en":"Private cloud","zh":"私有雲"},
      "D":{"en":"Platform as a Service (PaaS)","zh":"平台即服務 (PaaS)"},
      "E":{"en":"Hybrid cloud","zh":"混合雲"},
      "F":{"en":"Software as a Service (SaaS)","zh":"軟體即服務 (SaaS)"}
    },
    "correct":["B","D","F"],"multi":True,
    "explanations":{
      "A":"✗ 全雲端是雲端部署模型（Deployment Model），不是雲端服務模型（Service Model）。",
      "B":"✓ 正確 — IaaS 提供虛擬化基礎設施（運算、網路、儲存），客戶管理 OS 以上的層級，如 Amazon EC2。",
      "C":"✗ 私有雲是雲端部署模型，不是服務模型。",
      "D":"✓ 正確 — PaaS 提供完整開發平台，客戶只需管理應用程式和資料，如 AWS Elastic Beanstalk。",
      "E":"✗ 混合雲是雲端部署模型，不是服務模型。",
      "F":"✓ 正確 — SaaS 提供完整的軟體應用，客戶只需使用，如 Amazon Chime、Office 365。"
    }
  },
  {
    "id":116,"exam":"CLF",
    "question":"Under the shared responsibility model, which of the following is the customer responsible for?",
    "question_zh":"在共同責任模型下，下列哪項是客戶的責任？",
    "options":{
      "A":{"en":"Ensuring that disk drives are wiped after use","zh":"確保磁碟機使用後被清除"},
      "B":{"en":"Ensuring that firmware is updated on hardware devices","zh":"確保硬體裝置韌體更新"},
      "C":{"en":"Ensuring that data is encrypted at rest","zh":"確保靜態資料被加密"},
      "D":{"en":"Ensuring that network cables are category six or higher","zh":"確保網路線為六類或更高規格"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 磁碟清除（Disk Wiping）是 AWS 的責任；AWS 負責硬體的安全銷毀，符合 NIST 800-88 等標準。",
      "B":"✗ 硬體裝置韌體更新是 AWS 的責任，屬於底層基礎設施管理。",
      "C":"✓ 正確 — 資料加密（靜態加密 at-rest 和傳輸加密 in-transit）是客戶的責任。客戶決定是否啟用 S3 SSE、EBS 加密或 RDS 加密等功能。",
      "D":"✗ 實體網路基礎設施（纜線規格）的維護是 AWS 的責任，客戶無需也無法干預。"
    }
  },
  {
    "id":117,"exam":"CLF",
    "question":"Under the shared responsibility model, which of the following is the customer responsible for?",
    "question_zh":"在共同責任模型下，下列哪項是客戶的責任？",
    "options":{
      "A":{"en":"Cost allocation tags","zh":"成本分配標籤"},
      "B":{"en":"Consolidated billing","zh":"整合帳單"},
      "C":{"en":"AWS Budgets","zh":"AWS Budgets"},
      "D":{"en":"AWS Marketplace","zh":"AWS Marketplace"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 成本分配標籤雖然是客戶設定的，但較偏向成本管理工具，本題答案聚焦在成本控制責任。",
      "B":"✗ 整合帳單是 AWS Organizations 提供的功能，AWS 提供機制，客戶選擇使用。",
      "C":"✓ 正確 — AWS Budgets 由客戶設定和管理，用於追蹤和控制 AWS 支出，確保不超出預算是客戶的責任。客戶需主動設定預算閾值和警報。",
      "D":"✗ AWS Marketplace 是 AWS 提供的軟體市集，客戶在其中購買，但 Marketplace 本身由 AWS 維護。"
    }
  },
  {
    "id":118,"exam":"CLF",
    "question":"Which service stores objects, provides real-time access to those objects, and offers versioning and lifecycle capabilities?",
    "question_zh":"哪個服務儲存物件、提供即時存取，並提供版本控制和生命週期管理功能？",
    "options":{
      "A":{"en":"Amazon Glacier","zh":"Amazon S3 Glacier"},
      "B":{"en":"AWS Storage Gateway","zh":"AWS Storage Gateway"},
      "C":{"en":"Amazon S3","zh":"Amazon S3"},
      "D":{"en":"Amazon EBS","zh":"Amazon EBS"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Glacier 是封存儲存，不提供即時存取（需要數分鐘到數小時取回），且不提供版本控制功能。",
      "B":"✗ Storage Gateway 是混合雲儲存閘道，不提供版本控制或生命週期管理。",
      "C":"✓ 正確 — Amazon S3 提供：物件儲存、即時 URL 存取、版本控制（Version Control）防止誤刪、生命週期政策（自動轉移到 Glacier 或刪除舊版本），是功能最完整的物件儲存服務。",
      "D":"✗ EBS 是區塊儲存（磁碟），不是物件儲存，也沒有版本控制或生命週期管理功能。"
    }
  },
  {
    "id":119,"exam":"CLF",
    "question":"What AWS team assists customers with accelerating cloud adoption through paid engagements in specialty practice areas?",
    "question_zh":"哪個 AWS 團隊透過付費專業服務協助客戶加速雲端採用？",
    "options":{
      "A":{"en":"AWS Enterprise Support","zh":"AWS Enterprise 支援"},
      "B":{"en":"AWS Solutions Architects","zh":"AWS 解決方案架構師"},
      "C":{"en":"AWS Professional Services","zh":"AWS Professional Services"},
      "D":{"en":"AWS Account Managers","zh":"AWS 客戶經理"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Enterprise Support 是技術支援計劃（提供 TAM 等），不是專業顧問服務。",
      "B":"✗ AWS Solutions Architects 通常是免費為客戶提供架構建議的角色，不是付費顧問服務。",
      "C":"✓ 正確 — AWS Professional Services 是付費顧問團隊，提供雲端遷移、架構設計、安全、DevOps 等專業領域的深度顧問服務，協助客戶加速雲端採用。",
      "D":"✗ AWS Account Managers 負責客戶關係管理和帳號支援，不提供深度技術顧問服務。"
    }
  },
  {
    "id":120,"exam":"CLF",
    "question":"A customer wants to design and build a new workload on AWS Cloud but does not have the AWS-related technical expertise in-house. Which AWS program can help?",
    "question_zh":"客戶想在 AWS 雲端設計和建立新工作負載，但內部缺乏 AWS 技術專業知識，哪個 AWS 計劃可以協助？",
    "options":{
      "A":{"en":"AWS Partner Network Technology Partners","zh":"AWS 合作夥伴網路技術合作夥伴"},
      "B":{"en":"AWS Marketplace","zh":"AWS Marketplace"},
      "C":{"en":"AWS Partner Network Consulting Partners","zh":"AWS 合作夥伴網路諮詢合作夥伴"},
      "D":{"en":"AWS Service Catalog","zh":"AWS Service Catalog"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Technology Partners 提供軟體解決方案（ISV），不提供人力顧問服務。",
      "B":"✗ AWS Marketplace 是購買第三方軟體的市集，不提供技術顧問服務。",
      "C":"✓ 正確 — AWS Partner Network Consulting Partners 是通過 AWS 認證的系統整合商和顧問公司，可提供技術設計、建置和遷移服務，彌補客戶缺乏 AWS 技術能力的缺口。",
      "D":"✗ Service Catalog 用於管理和發布 IT 服務目錄，不是人力顧問服務。"
    }
  },
  {
    "id":121,"exam":"CLF",
    "question":"Distributing workloads across multiple Availability Zones supports which cloud architecture design principle?",
    "question_zh":"將工作負載分散到多個可用區域支援哪個雲端架構設計原則？",
    "options":{
      "A":{"en":"Implement automation","zh":"實作自動化"},
      "B":{"en":"Design for agility","zh":"為敏捷性設計"},
      "C":{"en":"Design for failure","zh":"為故障而設計"},
      "D":{"en":"Implement elasticity","zh":"實作彈性"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 實作自動化是指使用 CloudFormation、Auto Scaling 等工具自動化資源管理，與多 AZ 分佈的目的不同。",
      "B":"✗ 敏捷性是指快速部署和迭代的能力，不是多 AZ 部署的主要目的。",
      "C":"✓ 正確 — 「為故障而設計（Design for failure）」是 AWS Well-Architected 框架的核心原則：假設任何單一元件都可能故障，透過跨 AZ 部署確保即使一個 AZ 失效，服務仍能持續運行。",
      "D":"✗ 彈性是指根據需求動態調整資源數量（Auto Scaling），多 AZ 部署主要提供高可用性而非彈性。"
    }
  },
  {
    "id":122,"exam":"CLF",
    "question":"Which AWS services can host a Microsoft SQL Server database? (Choose two)",
    "question_zh":"哪些 AWS 服務可以託管 Microsoft SQL Server 資料庫？（選2項）",
    "options":{
      "A":{"en":"Amazon EC2","zh":"Amazon EC2"},
      "B":{"en":"Amazon Relational Database Service (Amazon RDS)","zh":"Amazon RDS"},
      "C":{"en":"Amazon Aurora","zh":"Amazon Aurora"},
      "D":{"en":"Amazon Redshift","zh":"Amazon Redshift"},
      "E":{"en":"Amazon S3","zh":"Amazon S3"}
    },
    "correct":["A","B"],"multi":True,
    "explanations":{
      "A":"✓ 正確 — 可在 EC2 上自行安裝和管理 SQL Server，使用 Windows Server AMI + SQL Server 授權，完全自主管理。",
      "B":"✓ 正確 — Amazon RDS 原生支援 Microsoft SQL Server，提供受管理的 SQL Server 服務（含自動備份、修補、高可用性），無需管理底層 OS。",
      "C":"✗ Aurora 相容 MySQL 和 PostgreSQL，不支援 Microsoft SQL Server。",
      "D":"✗ Redshift 是 OLAP 資料倉儲，不是 OLTP 關聯式資料庫，不用於運行 SQL Server。",
      "E":"✗ S3 是物件儲存，不能用來運行任何資料庫引擎。"
    }
  },
  {
    "id":123,"exam":"CLF",
    "question":"Which of the following inspects AWS environments to find opportunities that can save money for users and also improve system performance?",
    "question_zh":"下列哪項可檢查 AWS 環境，找出省錢機會並改善系統效能？",
    "options":{
      "A":{"en":"AWS Cost Explorer","zh":"AWS Cost Explorer"},
      "B":{"en":"AWS Trusted Advisor","zh":"AWS Trusted Advisor"},
      "C":{"en":"Consolidated billing","zh":"整合帳單"},
      "D":{"en":"Detailed billing","zh":"詳細帳單"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Cost Explorer 提供費用分析和視覺化，但不主動「檢查」環境並給出改善建議。",
      "B":"✓ 正確 — AWS Trusted Advisor 自動掃描您的 AWS 環境，提供五大類別建議：成本優化（找出閒置資源）、效能（識別瓶頸）、安全性、容錯能力和服務限制，同時改善省錢和效能。",
      "C":"✗ 整合帳單合併多帳號費用，不提供環境檢查或最佳化建議。",
      "D":"✗ 詳細帳單是費用明細報告，不提供最佳化建議。"
    }
  },
  {
    "id":124,"exam":"CLF",
    "question":"Which Amazon EC2 pricing model allows customers to use existing server-bound software licenses?",
    "question_zh":"哪種 Amazon EC2 定價模型允許客戶使用現有的伺服器綁定軟體授權？",
    "options":{
      "A":{"en":"Spot Instances","zh":"Spot 執行個體"},
      "B":{"en":"Reserved Instances","zh":"預留執行個體"},
      "C":{"en":"Dedicated Hosts","zh":"專用主機（Dedicated Hosts）"},
      "D":{"en":"On-Demand Instances","zh":"隨需執行個體"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Spot Instance 是競價實例，使用 AWS 閒置容量，可隨時被中斷，不適合綁定特定伺服器的授權。",
      "B":"✗ Reserved Instance 是預先承諾使用量換取折扣，但在虛擬化環境中，無法對應到特定實體伺服器，不支援 BYOL（自帶授權）的 per-socket 授權。",
      "C":"✓ 正確 — Dedicated Host 提供整台實體伺服器的獨家使用，您可以控制執行個體的放置，符合 Windows Server、SQL Server、Oracle 等按 socket 或核心計費的授權要求（BYOL）。",
      "D":"✗ On-Demand 按使用量計費，在共享或虛擬化環境中，不支援需要綁定特定實體伺服器的授權。"
    }
  },
  {
    "id":125,"exam":"CLF",
    "question":"Which AWS characteristics make AWS cost effective for a workload with dynamic user demand? (Choose two)",
    "question_zh":"哪些 AWS 特性讓具有動態使用者需求的工作負載在成本上具有效益？（選2項）",
    "options":{
      "A":{"en":"High availability","zh":"高可用性"},
      "B":{"en":"Shared security model","zh":"共同安全模型"},
      "C":{"en":"Elasticity","zh":"彈性 (Elasticity)"},
      "D":{"en":"Pay-as-you-go pricing","zh":"按用量付費定價"},
      "E":{"en":"Reliability","zh":"可靠性"}
    },
    "correct":["C","D"],"multi":True,
    "explanations":{
      "A":"✗ 高可用性確保服務不中斷，是可靠性指標，但不直接影響動態需求下的成本效益。",
      "B":"✗ 共同安全模型定義責任歸屬，與動態需求的成本無直接關係。",
      "C":"✓ 正確 — 彈性（Auto Scaling）讓資源隨需求自動增減，高峰期擴展、低谷期縮減，避免為峰值預購閒置資源。",
      "D":"✓ 正確 — 按用量付費確保只為實際使用的資源付費，動態需求下不需預付固定成本，直接節省低用量時期的費用。",
      "E":"✗ 可靠性確保系統正常運行，不直接影響成本效益。"
    }
  },
  {
    "id":126,"exam":"CLF",
    "question":"Which service enables risk auditing by continuously monitoring and logging account activity, including user actions in the AWS Management Console and AWS SDKs?",
    "question_zh":"哪個服務透過持續監控和記錄帳號活動（包括 AWS Console 和 SDK 的使用者操作）來實現風險稽核？",
    "options":{
      "A":{"en":"Amazon CloudWatch","zh":"Amazon CloudWatch"},
      "B":{"en":"AWS CloudTrail","zh":"AWS CloudTrail"},
      "C":{"en":"AWS Config","zh":"AWS Config"},
      "D":{"en":"AWS Health","zh":"AWS Health"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ CloudWatch 監控資源指標（CPU、記憶體）和應用程式日誌，不專門記錄帳號活動或 API 呼叫。",
      "B":"✓ 正確 — AWS CloudTrail 記錄所有 AWS API 呼叫（Console、CLI、SDK、其他服務），包含呼叫者身分、時間、來源 IP 等，是風險稽核和合規調查的核心工具。",
      "C":"✗ Config 追蹤資源配置的變更歷史，不記錄使用者的操作行為（如登入、呼叫 API）。",
      "D":"✗ AWS Health 提供 AWS 服務事件通知（如維護、服務中斷），不是帳號活動稽核工具。"
    }
  },
  {
    "id":127,"exam":"CLF",
    "question":"Which of the following are characteristics of Amazon S3? (Choose two)",
    "question_zh":"Amazon S3 的哪些特性是正確的？（選2項）",
    "options":{
      "A":{"en":"A global file system","zh":"全球檔案系統"},
      "B":{"en":"An object store","zh":"物件儲存"},
      "C":{"en":"A local file store","zh":"本地檔案儲存"},
      "D":{"en":"A network file system","zh":"網路檔案系統"},
      "E":{"en":"A durable storage system","zh":"高耐久性儲存系統"}
    },
    "correct":["B","E"],"multi":True,
    "explanations":{
      "A":"✗ S3 不是傳統的全球檔案系統（無法像 NFS 一樣掛載），它是物件儲存，以 HTTP API 存取。",
      "B":"✓ 正確 — Amazon S3 是物件儲存（Object Store），每個物件有唯一 Key，以 HTTP/S 方式存取，不是塊狀或檔案存取。",
      "C":"✗ S3 不是本地存取的檔案儲存，它是雲端物件儲存，需要透過 API 或 URL 存取。",
      "D":"✗ 網路檔案系統（NFS）是 Amazon EFS 的特性，S3 不是 NFS。",
      "E":"✓ 正確 — Amazon S3 提供 11 個 9（99.999999999%）的耐久性，資料自動跨多個 AZ 複寫，是業界最高的儲存耐久性標準。"
    }
  },
  {
    "id":128,"exam":"CLF",
    "question":"Which services can be used across hybrid AWS Cloud architectures? (Choose two)",
    "question_zh":"哪些服務可用於混合 AWS 雲端架構？（選2項）",
    "options":{
      "A":{"en":"Amazon Route 53","zh":"Amazon Route 53"},
      "B":{"en":"Virtual Private Gateway","zh":"虛擬私有閘道（Virtual Private Gateway）"},
      "C":{"en":"Classic Load Balancer","zh":"Classic Load Balancer"},
      "D":{"en":"Auto Scaling","zh":"Auto Scaling"},
      "E":{"en":"Amazon CloudWatch default metrics","zh":"Amazon CloudWatch 預設指標"}
    },
    "correct":["A","B"],"multi":True,
    "explanations":{
      "A":"✓ 正確 — Route 53 的 DNS 解析和健康檢查可同時指向雲端和本地端資源，支援混合架構的流量路由。",
      "B":"✓ 正確 — Virtual Private Gateway 是 VPC 的 VPN 端點，用於建立本地端資料中心與 AWS VPC 之間的 IPSec VPN 連線，是混合雲連接的核心元件。",
      "C":"✗ Classic Load Balancer 是 AWS 內部的負載平衡服務，只在 AWS VPC/EC2 內使用，不跨越本地端。",
      "D":"✗ Auto Scaling 在 AWS 雲端內自動調整 EC2 容量，不適用於本地端資源的混合管理。",
      "E":"✗ CloudWatch 預設指標監控 AWS 資源，不收集本地端伺服器的指標（需要安裝 CloudWatch Agent 才能監控本地端）。"
    }
  },
]
