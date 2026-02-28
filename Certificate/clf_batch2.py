
CLF_BATCH2 = [
  {
    "id":59,"exam":"CLF",
    "question":"Which CloudFront component is used to distribute content to users across the globe?",
    "question_zh":"CloudFront 的哪個元件用於向全球使用者分發內容？",
    "options":{
      "A":{"en":"Amazon Regions","zh":"AWS 區域"},
      "B":{"en":"Amazon VPC","zh":"Amazon VPC"},
      "C":{"en":"Amazon Edge Locations","zh":"Amazon 邊緣站點"},
      "D":{"en":"Amazon Availability Zones","zh":"Amazon 可用區域"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ AWS Regions 是包含多個 AZ 的地理區域，是基礎設施的骨幹，但 CloudFront 的快取分發依靠的是 Edge Locations，而不是 Region 本身。",
      "B":"✗ Amazon VPC 是虛擬私有網路服務，用於隔離和管理 AWS 資源，與 CloudFront 的內容分發機制無關。",
      "C":"✓ 正確 — CloudFront 透過遍布全球的數百個 Edge Locations（邊緣站點）快取並分發內容，讓使用者從最近的節點取得資料，大幅降低延遲。",
      "D":"✗ Availability Zones 提供區域內的高可用性與容錯能力，但它們是 Region 內的邏輯單元，不是 CloudFront 的分發網路。"
    }
  },
  {
    "id":60,"exam":"CLF",
    "question":"You need to reduce costs of a large fleet of always-running EC2 instances that each serves a single user-initiated process. What managed service could help?",
    "question_zh":"您需要降低大批持續運行的 EC2 執行個體成本，這些執行個體各自服務一個由使用者觸發的單次流程。哪種託管服務可以幫助降低成本？",
    "options":{
      "A":{"en":"AWS Lambda","zh":"AWS Lambda"},
      "B":{"en":"Amazon CloudFront","zh":"Amazon CloudFront"},
      "C":{"en":"Amazon Kinesis","zh":"Amazon Kinesis"},
      "D":{"en":"AWS CloudFormation","zh":"AWS CloudFormation"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — AWS Lambda 是無伺服器運算服務，僅在函數被呼叫時才執行並計費（毫秒計費）。將每次使用者觸發的流程改為 Lambda 函數，可徹底消除「24 小時待機 EC2」的閒置費用。",
      "B":"✗ CloudFront 是 CDN（內容傳遞網路），用於加速靜態/動態內容交付，不能執行應用程式邏輯或替代運算執行個體。",
      "C":"✗ Amazon Kinesis 是即時資料串流服務，用於收集和處理大量串流資料，不是通用運算替代方案。",
      "D":"✗ AWS CloudFormation 是基礎設施即程式碼服務，用於自動佈建資源，不能減少正在執行的 EC2 數量。"
    }
  },
  {
    "id":61,"exam":"CLF",
    "question":"Which of the following is a serverless compute service in AWS?",
    "question_zh":"下列哪項是 AWS 的無伺服器運算服務？",
    "options":{
      "A":{"en":"AWS OpsWorks","zh":"AWS OpsWorks"},
      "B":{"en":"Amazon EC2","zh":"Amazon EC2"},
      "C":{"en":"AWS Config","zh":"AWS Config"},
      "D":{"en":"AWS Lambda","zh":"AWS Lambda"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ AWS OpsWorks 是配置管理服務（基於 Chef/Puppet），用於自動化伺服器設定，需要管理底層 EC2 執行個體，不是無伺服器。",
      "B":"✗ Amazon EC2 是虛擬伺服器服務，您需要選擇、佈建並管理執行個體，是有伺服器（server-based）的服務。",
      "C":"✗ AWS Config 追蹤 AWS 資源的配置變更和合規性，是管理/稽核工具，不是運算服務。",
      "D":"✓ 正確 — AWS Lambda 是無伺服器（serverless）運算服務。您只需上傳程式碼，AWS 自動管理伺服器、擴展和維護。只在程式碼執行時計費，無需佈建或管理任何伺服器。"
    }
  },
  {
    "id":62,"exam":"CLF",
    "question":"Which of the following is a benefit of running an application across two Availability Zones?",
    "question_zh":"跨兩個可用區域執行應用程式的主要優點是什麼？",
    "options":{
      "A":{"en":"Performance is improved over running in a single Availability Zone","zh":"效能比單一可用區域更好"},
      "B":{"en":"It is more secure than running in a single Availability Zone","zh":"比在單一可用區域執行更安全"},
      "C":{"en":"It significantly reduces the total cost of ownership","zh":"大幅降低擁有總成本"},
      "D":{"en":"It increases the availability of an application compared to running in a single Availability Zone","zh":"與在單一可用區域執行相比，提高了應用程式的可用性"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 跨 AZ 不一定能提升效能，反而因為網路跳轉可能略增延遲。效能取決於應用程式架構，不是 AZ 數量。",
      "B":"✗ 跨 AZ 主要解決的是可用性問題（硬體故障、資料中心停電），不是安全性問題。安全性由 IAM、安全群組等控制。",
      "C":"✗ 跨兩個 AZ 通常會增加成本（需要在兩個 AZ 中運行資源），不會顯著降低 TCO。",
      "D":"✓ 正確 — 跨多個 AZ 是 AWS 高可用性設計的核心原則。若一個 AZ 發生故障（停電、硬體問題），另一個 AZ 的資源可以繼續服務，避免單點故障，提高應用程式可用性。"
    }
  },
  {
    "id":63,"exam":"CLF",
    "question":"Which AWS service helps developers quickly deploy resources using different programming languages such as .NET and Java?",
    "question_zh":"哪個 AWS 服務幫助開發人員快速部署支援 .NET 和 Java 等多種程式語言的資源？",
    "options":{
      "A":{"en":"AWS Elastic Beanstalk","zh":"AWS Elastic Beanstalk"},
      "B":{"en":"Amazon SQS","zh":"Amazon SQS"},
      "C":{"en":"Amazon EC2","zh":"Amazon EC2"},
      "D":{"en":"AWS CloudFormation","zh":"AWS CloudFormation"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — AWS Elastic Beanstalk 支援多種語言和平台（Node.js、Python、Ruby、Go、.NET、Java 等），開發人員只需上傳程式碼，Beanstalk 自動處理部署、負載平衡、擴展和監控。",
      "B":"✗ Amazon SQS（Simple Queue Service）是訊息佇列服務，用於解耦應用程式元件，不是應用程式部署服務。",
      "C":"✗ Amazon EC2 提供虛擬伺服器，開發人員需要手動設定環境、安裝執行環境和部署應用程式，不是快速部署工具。",
      "D":"✗ AWS CloudFormation 是基礎設施即程式碼服務，用 YAML/JSON 定義整個雲端基礎設施，而非針對應用程式部署和語言支援的服務。"
    }
  },
  {
    "id":64,"exam":"CLF",
    "question":"When granting permissions via AWS IAM, which principle should be applied?",
    "question_zh":"透過 AWS IAM 授予權限時，應套用哪項原則？",
    "options":{
      "A":{"en":"Principle of lower privilege","zh":"較低權限原則"},
      "B":{"en":"Principle of greatest privilege","zh":"最大權限原則"},
      "C":{"en":"Principle of most privilege","zh":"最多權限原則"},
      "D":{"en":"Principle of least privilege","zh":"最小權限原則"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 「較低權限」不是標準術語。正確術語是「最小權限 (least privilege)」，代表的是精確的最小必要權限。",
      "B":"✗ 「最大權限」是安全反模式。給予過多權限會擴大攻擊面，一旦帳號遭入侵，損失將最大化。",
      "C":"✗ 「最多權限」同 B，是安全反模式。AWS 明確建議避免廣泛授予管理員權限。",
      "D":"✓ 正確 — 最小權限原則（Principle of Least Privilege）是 IAM 的核心安全最佳實務：每個使用者、角色、服務只獲得完成任務所需的最低限度權限，不多給任何額外存取。"
    }
  },
  {
    "id":65,"exam":"CLF",
    "question":"Which networking component can be used to host EC2 resources in the AWS Cloud?",
    "question_zh":"哪個網路元件可用於在 AWS 雲端中托管 EC2 資源？",
    "options":{
      "A":{"en":"Amazon VPC","zh":"Amazon VPC"},
      "B":{"en":"AWS Trusted Advisor","zh":"AWS Trusted Advisor"},
      "C":{"en":"AWS Auto Scaling","zh":"AWS Auto Scaling"},
      "D":{"en":"AWS Elastic Load Balancer","zh":"AWS Elastic Load Balancer"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon VPC（Virtual Private Cloud）是在 AWS 中定義虛擬網路的服務。所有 EC2 執行個體必須在某個 VPC 的子網路（Subnet）中啟動，VPC 提供網路隔離、路由控制和安全邊界。",
      "B":"✗ AWS Trusted Advisor 是提供最佳實務建議的工具（成本、安全性、效能等），不是網路元件。",
      "C":"✗ AWS Auto Scaling 自動調整 EC2 執行個體數量以應對負載變化，是容量管理服務，不是用來「托管」EC2 的網路元件。",
      "D":"✗ Elastic Load Balancer 在多個 EC2 執行個體間分配流量，提高可用性，但它是流量分配服務，不是托管 EC2 的網路基礎元件。"
    }
  },
  {
    "id":66,"exam":"CLF",
    "question":"Which feature is normally present in ALL AWS Support plans?",
    "question_zh":"哪個功能在所有 AWS 支援計劃中都提供？",
    "options":{
      "A":{"en":"Access to all features in AWS Trusted Advisor","zh":"存取 Trusted Advisor 的所有功能"},
      "B":{"en":"A Technical Account Manager (TAM)","zh":"技術客戶經理 (TAM)"},
      "C":{"en":"A dedicated support person","zh":"專屬支援人員"},
      "D":{"en":"24/7 access to customer service for account and billing questions","zh":"全天候存取客戶服務以處理帳戶和帳單問題"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 完整的 Trusted Advisor 檢查（所有類別）僅在 Business 和 Enterprise 支援計劃中提供。Basic 和 Developer 只能存取部分核心安全和服務限制檢查。",
      "B":"✗ Technical Account Manager (TAM) 僅在 Enterprise 支援計劃（月費最高）中提供，作為指定的技術聯絡人。",
      "C":"✗ 專屬支援人員同樣只在較高階的計劃（Business 及以上）提供，Basic 計劃沒有。",
      "D":"✓ 正確 — 所有 AWS 支援計劃（包含免費的 Basic 計劃）都包含全天候 24/7 客戶服務，可存取線上資源、文件，以及帳戶和帳單問題的支援。"
    }
  },
  {
    "id":67,"exam":"CLF",
    "question":"Your project requires hosting a set of servers for a short period of 3 months. Which EC2 instance type is most cost effective?",
    "question_zh":"您的專案需要在短短 3 個月內托管一組伺服器，哪種 EC2 執行個體類型最具成本效益？",
    "options":{
      "A":{"en":"On-Demand Instances","zh":"隨需執行個體"},
      "B":{"en":"No Upfront Reserved Instances","zh":"無預付款預留執行個體"},
      "C":{"en":"Spot Instances","zh":"Spot 執行個體"},
      "D":{"en":"Partial Upfront Reserved Instances","zh":"部分預付款預留執行個體"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ On-Demand 不需承諾，彈性高，但每小時費率是最高的選項之一。對於 3 個月的短期需求，不是最便宜的方案（若工作負載可承受中斷）。",
      "B":"✗ Reserved Instances 需要 1 年或 3 年的承諾期，遠超 3 個月需求，違約等同於損失費用。",
      "C":"✓ 正確 — Spot Instances 利用 AWS 閒置容量，可提供高達 90% 的折扣。若工作負載可以容忍偶爾中斷（Spot 被回收時），是短期最便宜的選項。考試情境預設工作負載可容忍中斷時，Spot 是成本最低答案。",
      "D":"✗ 部分預付款 Reserved Instances 同樣需要 1-3 年承諾，不適合 3 個月短期需求。"
    }
  },
  {
    "id":68,"exam":"CLF",
    "question":"Which tool can display the distribution of AWS spending?",
    "question_zh":"哪個工具可以顯示 AWS 支出的分佈情況？",
    "options":{
      "A":{"en":"AWS Organizations","zh":"AWS Organizations"},
      "B":{"en":"AWS Cost Explorer","zh":"AWS Cost Explorer"},
      "C":{"en":"AWS Trusted Advisor","zh":"AWS Trusted Advisor"},
      "D":{"en":"Amazon DevPay","zh":"Amazon DevPay"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ AWS Organizations 管理多帳戶結構和合併帳單，但它本身不是視覺化支出分佈的工具。",
      "B":"✓ 正確 — AWS Cost Explorer 提供互動式圖表，讓您視覺化並分析 AWS 支出的分佈（按服務、區域、帳戶、標籤等維度），並可預測未來費用趨勢。",
      "C":"✗ AWS Trusted Advisor 提供成本最佳化建議（如指出未使用的資源），但不是用來顯示支出分佈的視覺化工具。",
      "D":"✗ Amazon DevPay 是過去的計費服務（已停用），用於第三方應用程式的計費管理，現在不再使用。"
    }
  },
  {
    "id":69,"exam":"CLF",
    "question":"You created an S3 bucket 'ytmProfilePictures' in us-east-2 with static website hosting enabled and a folder 'images/' at the root. What is the correct URL format to access these images?",
    "question_zh":"您在 us-east-2 建立了名為 ytmProfilePictures 的 S3 儲存桶，啟用了靜態網站托管並在根目錄建立了 images/ 資料夾。存取圖片的正確 URL 格式是什麼？",
    "options":{
      "A":{"en":"https://ytmProfilePictures.s3-website.us-east-2.amazonaws.com/images","zh":"（儲存桶名稱 → s3-website → 區域格式）"},
      "B":{"en":"https://s3-us-east-2.amazonaws.com/ytmProfilePictures/images","zh":"（區域 → s3 → 儲存桶名稱格式）"},
      "C":{"en":"https://s3-website-us-east-2.ytmProfilePictures.amazonaws.com/images","zh":"（s3-website-區域 → 儲存桶名稱格式）"},
      "D":{"en":"https://s3-website-us-east-2.amazonaws.com/ytmProfilePictures/images","zh":"（s3-website-區域 → 儲存桶在路徑格式）"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — S3 靜態網站托管的 URL 格式為：{bucket-name}.s3-website.{region}.amazonaws.com（虛擬托管格式）。儲存桶名稱是子網域的一部分。",
      "B":"✗ 這是 S3 REST API 的路徑樣式 URL（非網站托管格式）：s3.{region}.amazonaws.com/{bucket-name}/object，用於 API 呼叫，不是網站 URL。",
      "C":"✗ URL 格式錯誤：s3-website-{region} 後面接的是 amazonaws.com，不是儲存桶名稱作為子網域。",
      "D":"✗ 這個格式把儲存桶名稱放在路徑中，而非作為子網域，不符合 S3 靜態網站托管的 URL 格式規範。"
    }
  },
  {
    "id":70,"exam":"CLF",
    "question":"Which AWS services allow the customer to retain FULL administrative privileges of the underlying virtual infrastructure?",
    "question_zh":"哪項 AWS 服務允許客戶保留對底層虛擬基礎設施的完整管理權限？",
    "options":{
      "A":{"en":"Amazon S3","zh":"Amazon S3"},
      "B":{"en":"AWS Lambda","zh":"AWS Lambda"},
      "C":{"en":"Amazon DynamoDB","zh":"Amazon DynamoDB"},
      "D":{"en":"Amazon EC2","zh":"Amazon EC2"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ Amazon S3 是完全託管的物件儲存服務。您管理物件、儲存桶政策和存取控制，但完全無法存取底層伺服器或作業系統。",
      "B":"✗ AWS Lambda 是無伺服器服務，AWS 完全管理底層基礎設施。客戶只能存取函數程式碼，無法控制作業系統、網路或伺服器配置。",
      "C":"✗ Amazon DynamoDB 是完全託管的 NoSQL 資料庫。AWS 管理所有底層伺服器、儲存和網路，客戶只管理資料表和資料。",
      "D":"✓ 正確 — Amazon EC2 提供虛擬伺服器，客戶擁有作業系統層（OS）以上的完整管理權限：可以 SSH 進入、安裝任何軟體、配置網路介面、管理使用者帳號等。這是 IaaS 模型的核心特性。"
    }
  },
  {
    "id":71,"exam":"CLF",
    "question":"Which storage option is best for storing archive data at the lowest cost?",
    "question_zh":"哪種儲存選項最適合以最低成本儲存封存資料？",
    "options":{
      "A":{"en":"Amazon S3 Glacier","zh":"Amazon S3 Glacier"},
      "B":{"en":"Amazon S3 Standard","zh":"Amazon S3 標準"},
      "C":{"en":"Amazon EBS","zh":"Amazon EBS"},
      "D":{"en":"AWS Storage Gateway","zh":"AWS Storage Gateway"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon S3 Glacier（包括 Glacier Deep Archive）是專為長期封存設計的低成本儲存服務。Glacier Deep Archive 每 GB 費用可低至 $0.00099/月，是所有 AWS 儲存選項中最便宜的，適合需要保存多年但幾乎不存取的資料。",
      "B":"✗ Amazon S3 Standard 適合頻繁存取的資料，每 GB 費用遠高於 Glacier，不適合封存。",
      "C":"✗ Amazon EBS 是 EC2 的區塊儲存，成本高且主要用途是為執行中的執行個體提供持久儲存，不是封存解決方案。",
      "D":"✗ AWS Storage Gateway 是混合雲儲存閘道服務，讓本地應用程式連接雲端儲存，不是專門的封存服務，成本也較 Glacier 高。"
    }
  },
]
