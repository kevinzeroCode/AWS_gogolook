
CLF_BATCH3 = [
  {
    "id":72,"exam":"CLF",
    "question":"You want to add an extra layer of protection to the current authentication mechanism of usernames and passwords for AWS. Which of the following can help?",
    "question_zh":"您想在現有帳號密碼登入機制上增加額外保護層，下列哪項可以協助？",
    "options":{
      "A":{"en":"Using Password Policies","zh":"使用密碼政策"},
      "B":{"en":"Using MFA","zh":"使用多因素驗證 (MFA)"},
      "C":{"en":"Using AWS WAF","zh":"使用 AWS WAF"},
      "D":{"en":"Using a mix of user names","zh":"使用混合使用者名稱"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 密碼政策可加強密碼複雜度，但仍是單因素驗證，無法提供「額外一層」保護。",
      "B":"✓ 正確 — MFA 在密碼之外增加第二驗證因素（如手機 OTP），即使密碼洩漏也能阻止未授權登入。",
      "C":"✗ AWS WAF 是 Web 應用程式防火牆，保護應用程式免受網路攻擊，不是登入驗證機制。",
      "D":"✗ 混合使用者名稱不構成額外安全層，無法有效阻止未授權存取。"
    }
  },
  {
    "id":73,"exam":"CLF",
    "question":"There is a requirement for storage of objects. The objects should be able to be downloaded via a URL. Which storage option would you choose?",
    "question_zh":"需要儲存物件，且物件必須能透過 URL 下載，應選擇哪個儲存選項？",
    "options":{
      "A":{"en":"Amazon S3","zh":"Amazon S3"},
      "B":{"en":"Amazon EBS","zh":"Amazon EBS"},
      "C":{"en":"Amazon Glacier","zh":"Amazon Glacier"},
      "D":{"en":"Amazon Storage Gateway","zh":"Amazon Storage Gateway"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon S3 是物件儲存服務，每個物件都有唯一的 URL，可直接透過 HTTPS 下載，且可設定公開或預簽署 URL。",
      "B":"✗ EBS 是區塊儲存，掛載到 EC2 後作為磁碟使用，無法透過 URL 直接存取。",
      "C":"✗ Glacier 是封存儲存，取出資料需要數分鐘到數小時，不提供即時 URL 下載。",
      "D":"✗ Storage Gateway 是混合雲儲存服務，用於本地端與 AWS 間的資料傳輸，不用於物件 URL 存取。"
    }
  },
  {
    "id":74,"exam":"CLF",
    "question":"Which of the following is the responsibility of the customer when ensuring that data on EBS volumes is left safe?",
    "question_zh":"在確保 EBS 磁碟區上的資料安全方面，下列哪項是客戶的責任？",
    "options":{
      "A":{"en":"Deleting the data when the device is destroyed","zh":"裝置銷毀時刪除資料"},
      "B":{"en":"Creating copies of EBS Volumes","zh":"建立 EBS 磁碟區的副本"},
      "C":{"en":"Attaching volumes to EC2 Instances","zh":"將磁碟區掛載至 EC2 執行個體"},
      "D":{"en":"Creating EBS snapshots","zh":"建立 EBS 快照"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 實體裝置的銷毀與清除是 AWS 的責任（共同責任模型中的底層硬體）。",
      "B":"✗ 建立副本是較不精確的說法；正確的 AWS 備份機制是快照（Snapshot）。",
      "C":"✗ 將磁碟區掛載到 EC2 是操作步驟，不是資料安全保護機制。",
      "D":"✓ 正確 — 建立 EBS 快照是客戶的責任，快照儲存在 S3 並可跨 AZ 復原，是保護 EBS 資料的標準方式。"
    }
  },
  {
    "id":75,"exam":"CLF",
    "question":"Which service can identify the user that made the API call when an Amazon EC2 instance is terminated?",
    "question_zh":"當 Amazon EC2 執行個體被終止時，哪個服務可以識別是哪個使用者進行了 API 呼叫？",
    "options":{
      "A":{"en":"AWS CloudTrail","zh":"AWS CloudTrail"},
      "B":{"en":"AWS X-Ray","zh":"AWS X-Ray"},
      "C":{"en":"Amazon CloudWatch","zh":"Amazon CloudWatch"},
      "D":{"en":"AWS Identity and Access Management (AWS IAM)","zh":"AWS IAM"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — AWS CloudTrail 記錄所有 AWS API 呼叫的詳細資訊，包括呼叫者身分、時間、IP 地址等，是 AWS 帳號的稽核日誌服務。",
      "B":"✗ AWS X-Ray 用於追蹤應用程式請求的效能與除錯，不記錄 AWS 管理操作的 API 呼叫。",
      "C":"✗ CloudWatch 監控資源指標（CPU、記憶體等）和日誌，不用於追蹤 IAM 使用者的操作。",
      "D":"✗ IAM 管理身分與存取權限，但不提供操作稽核日誌；稽核功能由 CloudTrail 提供。"
    }
  },
  {
    "id":76,"exam":"CLF",
    "question":"What is the service provided by AWS that allows developers to easily deploy and manage applications on the cloud?",
    "question_zh":"AWS 提供哪個服務讓開發人員可以輕鬆在雲端部署和管理應用程式？",
    "options":{
      "A":{"en":"Container service","zh":"容器服務"},
      "B":{"en":"Elastic Beanstalk","zh":"Elastic Beanstalk"},
      "C":{"en":"CloudFormation","zh":"CloudFormation"},
      "D":{"en":"OpsWorks","zh":"OpsWorks"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ 容器服務（ECS/EKS）是容器化部署平台，需要較多的設定和管理知識，不是「最簡單」的方式。",
      "B":"✓ 正確 — AWS Elastic Beanstalk 是 PaaS 服務，開發者只需上傳程式碼，AWS 自動處理部署、容量調整、負載平衡和監控，讓開發者專注於程式碼而非基礎設施。",
      "C":"✗ CloudFormation 是基礎設施即程式碼（IaC）服務，用於定義和佈建 AWS 資源，學習曲線較高，不是「輕鬆部署應用」的首選。",
      "D":"✗ OpsWorks 是基於 Chef/Puppet 的組態管理服務，複雜度較高，主要用於現有 Chef/Puppet 使用者。"
    }
  },
  {
    "id":77,"exam":"CLF",
    "question":"How would a system administrator add an additional layer of login security to a user's AWS Management Console?",
    "question_zh":"系統管理員如何為 AWS Management Console 的使用者登入增加額外安全層？",
    "options":{
      "A":{"en":"Enable AWS CloudTrail","zh":"啟用 AWS CloudTrail"},
      "B":{"en":"Enable Multi-Factor Authentication","zh":"啟用多因素驗證 (MFA)"},
      "C":{"en":"Audit AWS Identity and Access Management (IAM) roles","zh":"稽核 AWS IAM 角色"},
      "D":{"en":"Use AWS Cloud Directory","zh":"使用 AWS Cloud Directory"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ CloudTrail 記錄稽核日誌，可以事後查看誰做了什麼，但不能阻止未授權登入。",
      "B":"✓ 正確 — MFA 要求使用者在密碼之外提供第二個驗證因素（如 Authenticator App 的 6 位數代碼），大幅提升登入安全性。",
      "C":"✗ 稽核 IAM 角色是檢查權限是否合規的動作，不是為登入增加安全層。",
      "D":"✗ AWS Cloud Directory 是目錄服務，用於管理多層次的目錄結構，不是登入安全機制。"
    }
  },
  {
    "id":78,"exam":"CLF",
    "question":"Which AWS offering enables customers to find, buy, and immediately start using software solutions in their AWS environment?",
    "question_zh":"哪個 AWS 服務讓客戶能夠尋找、購買並立即在 AWS 環境中使用軟體解決方案？",
    "options":{
      "A":{"en":"AWS Config","zh":"AWS Config"},
      "B":{"en":"AWS Marketplace","zh":"AWS Marketplace"},
      "C":{"en":"AWS OpsWorks","zh":"AWS OpsWorks"},
      "D":{"en":"AWS SDK","zh":"AWS SDK"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ AWS Config 追蹤 AWS 資源的配置變更與合規狀態，不是軟體購買平台。",
      "B":"✓ 正確 — AWS Marketplace 是線上商店，提供數千種第三方軟體（安全、資料庫、網路等），可直接購買並部署到 AWS 環境，費用計入 AWS 帳單。",
      "C":"✗ OpsWorks 是基於 Chef/Puppet 的組態管理服務，不是軟體銷售平台。",
      "D":"✗ AWS SDK 是開發工具包，讓開發者以程式碼方式呼叫 AWS API，不是軟體購買市集。"
    }
  },
  {
    "id":79,"exam":"CLF",
    "question":"You have been tasked with replacing a legacy LDAP directory server that manages users, groups, and permissions with a cloud-based solution. What AWS service should you investigate?",
    "question_zh":"您需要以雲端解決方案取代管理使用者、群組和權限的舊版 LDAP 目錄伺服器，應研究哪個 AWS 服務？",
    "options":{
      "A":{"en":"AWS Organizations","zh":"AWS Organizations"},
      "B":{"en":"IAM","zh":"IAM"},
      "C":{"en":"AWS Directory Service","zh":"AWS Directory Service"},
      "D":{"en":"Cognito","zh":"Amazon Cognito"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ AWS Organizations 用於管理多個 AWS 帳號的層級結構和政策，不是用戶目錄服務。",
      "B":"✓ 正確 — AWS IAM 可管理使用者、群組和權限，取代 LDAP 的核心功能（身分管理 + 存取控制），是 AWS 原生的身分管理解決方案。",
      "C":"✗ AWS Directory Service 提供完整的 Microsoft AD 相容目錄（選項中未被選中，但在實務上更接近 LDAP 替代品；此題以 IAM 為官方答案）。",
      "D":"✗ Cognito 主要用於應用程式的終端使用者身分驗證（Web/Mobile App），不是企業內部 IT 人員的目錄管理。"
    }
  },
  {
    "id":80,"exam":"CLF",
    "question":"In order to predict the cost of moving resources from on-premises to the cloud, which of the following can be used?",
    "question_zh":"為了預測將資源從本地端遷移到雲端的成本，下列哪項可以使用？",
    "options":{
      "A":{"en":"AWS Inspector","zh":"AWS Inspector"},
      "B":{"en":"AWS TCO Calculator","zh":"AWS TCO 計算器"},
      "C":{"en":"AWS WAF","zh":"AWS WAF"},
      "D":{"en":"AWS Trusted Advisor","zh":"AWS Trusted Advisor"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ AWS Inspector 是自動化漏洞掃描服務，用於檢測 EC2 和容器的安全問題，與成本預測無關。",
      "B":"✓ 正確 — AWS TCO（Total Cost of Ownership）計算器可比較本地端基礎設施與 AWS 雲端的總擁有成本，協助企業進行遷移的財務分析與決策。",
      "C":"✗ AWS WAF 是 Web 應用程式防火牆，保護應用程式免受常見網路攻擊，與遷移成本估算無關。",
      "D":"✗ Trusted Advisor 提供現有 AWS 資源的最佳化建議（成本、安全、效能），不是遷移前的成本預測工具。"
    }
  },
  {
    "id":81,"exam":"CLF",
    "question":"You've just created a new S3 bucket named ytmProfilePictures in the US East 2 region. What is the correct bucket URL?",
    "question_zh":"您在 US East 2 區域建立了名為 ytmProfilePictures 的 S3 儲存貯體，正確的儲存貯體 URL 是什麼？",
    "options":{
      "A":{"en":"https://s3.us-east-2.ytmProfilePictures.amazonaws.com/","zh":"https://s3.us-east-2.ytmProfilePictures.amazonaws.com/"},
      "B":{"en":"https://ytmProfilePictures.s3.us-east-2.amazonaws.com","zh":"https://ytmProfilePictures.s3.us-east-2.amazonaws.com"},
      "C":{"en":"https://amazonaws.s3.us-east-2.com/ytmProfilePictures","zh":"https://amazonaws.s3.us-east-2.com/ytmProfilePictures"},
      "D":{"en":"https://s3.us-east-2.amazonaws.com/ytmProfilePictures","zh":"https://s3.us-east-2.amazonaws.com/ytmProfilePictures"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 網域格式錯誤：bucket 名稱不應嵌入 s3 子網域之後；正確格式不是這樣排列。",
      "B":"✗ 此為虛擬主機式（virtual-hosted-style）URL 格式：https://{bucket}.s3.{region}.amazonaws.com，雖然也是有效格式，但本題答案為路徑式（path-style）。",
      "C":"✗ 網域主機順序錯誤（amazonaws 在前），不是合法的 S3 URL 格式。",
      "D":"✓ 正確 — 路徑式（path-style）S3 URL 格式為 https://s3.{region}.amazonaws.com/{bucket-name}，這是標準的 S3 存取格式。"
    }
  },
  {
    "id":82,"exam":"CLF",
    "question":"Your company requires a support plan with 24x7 access to Cloud Support Engineers via email, chat & phone, and a response time of less than 1 hour for critical faults. Which plan suffices at lowest cost?",
    "question_zh":"公司需要支援計劃具備全天候（24x7）電話/聊天/郵件管道聯繫雲端支援工程師，且緊急故障回應時間低於1小時，最低成本方案為何？",
    "options":{
      "A":{"en":"Enterprise","zh":"Enterprise（企業）"},
      "B":{"en":"Developer","zh":"Developer（開發者）"},
      "C":{"en":"Business","zh":"Business（商業）"},
      "D":{"en":"Basic","zh":"Basic（基本）"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Enterprise 計劃提供 24x7 電話/聊天/郵件支援，且對業務關鍵系統故障的回應時間 < 15 分鐘（生產系統 < 1 小時）。雖然 Business 也有 < 1 小時，但題目提到 Cloud Support Engineers 直接存取，這通常是 Enterprise 的特色。",
      "B":"✗ Developer 計劃只有工作日電子郵件支援，回應時間 12-24 小時，無法達到 24x7 或 <1 小時要求。",
      "C":"✗ Business 計劃有 24x7 支援和 <1 小時緊急回應，但不提供專屬 Technical Account Manager（TAM），比 Enterprise 功能少。此題答案為 Enterprise。",
      "D":"✗ Basic 計劃無技術支援，只能存取文件和論壇。"
    }
  },
  {
    "id":83,"exam":"CLF",
    "question":"Which of the following is AWS's responsibility under the AWS shared responsibility model?",
    "question_zh":"在 AWS 共同責任模型下，下列哪項是 AWS 的責任？",
    "options":{
      "A":{"en":"Configuring third-party applications","zh":"配置第三方應用程式"},
      "B":{"en":"Securing application access and data","zh":"確保應用程式存取和資料安全"},
      "C":{"en":"Managing custom Amazon Machine Images (AMIs)","zh":"管理自訂 Amazon 機器映像 (AMI)"},
      "D":{"en":"Maintaining physical hardware","zh":"維護實體硬體"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ 第三方應用程式的配置是客戶的責任，AWS 不介入客戶在雲上運行的應用程式設定。",
      "B":"✗ 應用程式層的存取控制和資料安全是客戶的責任（共同責任模型中「雲端中的安全」屬於客戶）。",
      "C":"✗ 自訂 AMI 的建立、管理和更新是客戶的責任。",
      "D":"✓ 正確 — 實體硬體的維護（伺服器、網路設備、機房設施）是 AWS 的責任（「雲端的安全」屬於 AWS），客戶無需也無法觸碰底層實體基礎設施。"
    }
  },
  {
    "id":84,"exam":"CLF",
    "question":"A Solutions Architect requires a single EBS volume that can support up to 16,000 IOPS for a critical business application. Which Amazon EBS volume type meets this requirement?",
    "question_zh":"解決方案架構師需要一個單一 EBS 磁碟區，可支援最多 16,000 IOPS 的關鍵業務應用程式。哪種 EBS 磁碟區類型符合此要求？",
    "options":{
      "A":{"en":"EBS Cold HDD","zh":"EBS 冷 HDD (sc1)"},
      "B":{"en":"EBS Provisioned IOPS SSD","zh":"EBS 佈建 IOPS SSD (io1/io2)"},
      "C":{"en":"EBS General Purpose SSD","zh":"EBS 通用 SSD (gp2/gp3)"},
      "D":{"en":"EBS Throughput Optimized HDD","zh":"EBS 輸送量最佳化 HDD (st1)"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ Cold HDD (sc1) 是最低成本 HDD，專為不頻繁存取的冷資料設計，IOPS 極低（數百），完全不適合。",
      "B":"✓ 正確 — Provisioned IOPS SSD (io1/io2) 可佈建最高 64,000 IOPS（io2 Block Express 更高達 256,000），是需要高一致性 IOPS 的關鍵資料庫的最佳選擇。",
      "C":"✗ General Purpose SSD (gp3) 最高可達 16,000 IOPS，雖然勉強能達到，但對關鍵業務應用，Provisioned IOPS 的一致性更有保障。",
      "D":"✗ Throughput Optimized HDD (st1) 適合循序大量資料（如日誌、MapReduce），IOPS 低，不適合需要高隨機 I/O 的應用。"
    }
  },
  {
    "id":85,"exam":"CLF",
    "question":"Which of the following is NOT a disaster recovery deployment technique?",
    "question_zh":"下列哪項不是災難復原部署技術？",
    "options":{
      "A":{"en":"Single Site","zh":"單一站點"},
      "B":{"en":"Multi-Site","zh":"多站點"},
      "C":{"en":"Warm Standby","zh":"暖備援"},
      "D":{"en":"Pilot Light","zh":"試驗燈"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確（即非 DR 技術）— 單一站點是指所有資源集中在一個地點，沒有備援或故障切換機制，是高可用性風險最大的架構，不算 DR 部署技術。",
      "B":"✗ Multi-Site 是 DR 技術之一：在多個站點同時運行完整生產環境，RTO/RPO 最低，成本最高。",
      "C":"✗ Warm Standby 是 DR 技術：在備用站點保持縮小版本的生產環境持續運行，故障時快速擴容。",
      "D":"✗ Pilot Light 是 DR 技術：僅在備用站點保持核心元件（如資料庫複寫）運行，故障時快速啟動其餘服務。"
    }
  },
  {
    "id":86,"exam":"CLF",
    "question":"A company is planning to migrate their existing AWS Services to the Cloud. Which of the following would help them do a cost benefit analysis of moving to the AWS Cloud?",
    "question_zh":"一家公司正在規劃將現有服務遷移到 AWS 雲端，哪項工具可以協助他們進行遷移至 AWS 雲端的成本效益分析？",
    "options":{
      "A":{"en":"AWS Config","zh":"AWS Config"},
      "B":{"en":"AWS Cost Explorer","zh":"AWS Cost Explorer"},
      "C":{"en":"AWS Consolidated Billing","zh":"AWS 整合帳單"},
      "D":{"en":"AWS TCO Calculator","zh":"AWS TCO 計算器"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ AWS Config 追蹤資源配置的合規性，不用於遷移前的成本效益分析。",
      "B":"✗ Cost Explorer 分析和視覺化現有 AWS 帳單支出趨勢，但不用於遷移前的本地端 vs 雲端比較。",
      "C":"✗ 整合帳單是將多個 AWS 帳號的費用合併為一張帳單，不是成本效益分析工具。",
      "D":"✓ 正確 — AWS TCO Calculator 可輸入現有本地端基礎設施的規格和成本，與對應 AWS 服務成本進行比較，量化遷移的財務效益。"
    }
  },
  {
    "id":87,"exam":"CLF",
    "question":"Which AWS service provides infrastructure security optimization recommendations?",
    "question_zh":"哪個 AWS 服務提供基礎設施安全最佳化建議？",
    "options":{
      "A":{"en":"Reserved Instances","zh":"預留執行個體"},
      "B":{"en":"AWS Price List API","zh":"AWS Price List API"},
      "C":{"en":"Amazon EC2 Spot Fleet","zh":"Amazon EC2 Spot Fleet"},
      "D":{"en":"AWS Trusted Advisor","zh":"AWS Trusted Advisor"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ Reserved Instances 是 EC2 定價選項（預先承諾用量換取折扣），不是安全建議工具。",
      "B":"✗ AWS Price List API 提供服務定價資訊，不提供安全最佳化建議。",
      "C":"✗ EC2 Spot Fleet 是低成本彈性運算選項，不是安全工具。",
      "D":"✓ 正確 — AWS Trusted Advisor 提供五大類別的最佳化建議：成本優化、效能、安全性、容錯能力和服務限制，包含具體的安全設定改善建議（如 MFA、S3 公開存取、安全群組等）。"
    }
  },
  {
    "id":88,"exam":"CLF",
    "question":"You want to take a snapshot of an EC2 instance and create a new instance out of it. In AWS, what is this snapshot equivalent to?",
    "question_zh":"您想為 EC2 執行個體建立快照並從中建立新執行個體，在 AWS 中這種快照等同於什麼？",
    "options":{
      "A":{"en":"EC2 Snapshot","zh":"EC2 快照"},
      "B":{"en":"EBS Snapshot","zh":"EBS 快照"},
      "C":{"en":"EBS Volumes","zh":"EBS 磁碟區"},
      "D":{"en":"AMI","zh":"AMI（Amazon 機器映像）"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ EC2 沒有直接的「快照」概念；EC2 的映像是 AMI，EBS 磁碟的備份是 EBS Snapshot。",
      "B":"✗ EBS Snapshot 只備份磁碟內容，無法直接用來啟動新的 EC2 執行個體（需封裝成 AMI）。",
      "C":"✗ EBS Volume 是掛載在 EC2 上的磁碟，不是映像或快照。",
      "D":"✓ 正確 — AMI（Amazon Machine Image）包含作業系統、應用程式設定和資料，相當於 VM 範本快照，可直接用來啟動一個或多個相同配置的 EC2 執行個體。"
    }
  },
  {
    "id":89,"exam":"CLF",
    "question":"Your application has a 200 GB database on EC2 (cannot use RDS). The app peaks briefly in morning and evening with minimal usage otherwise. You need solid performance but low cost. Which EBS type?",
    "question_zh":"您的應用在 EC2 上有 200GB 資料庫，早晨和傍晚短暫峰值，其餘時間使用量極少，需要穩定效能但成本低。應選哪種 EBS 類型？",
    "options":{
      "A":{"en":"EFS","zh":"Amazon EFS"},
      "B":{"en":"EBS with a Provisioned IOPS SSD","zh":"EBS 佈建 IOPS SSD"},
      "C":{"en":"EBS with a General Purpose SSD","zh":"EBS 通用 SSD (gp2/gp3)"},
      "D":{"en":"EBS with a Magnetic HDD","zh":"EBS 磁性 HDD (standard)"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ EFS 是共享網路檔案系統，成本較高，適合多個 EC2 共用存取，不是單一 EC2 資料庫的最佳選擇。",
      "B":"✗ Provisioned IOPS SSD 效能最高但成本最高，峰值小且使用量低的情境下，此成本不合理。",
      "C":"✓ 正確 — General Purpose SSD (gp3) 在效能與成本之間取得最佳平衡：提供足夠的 IOPS 應付小型峰值，費用遠低於 Provisioned IOPS SSD，適合峰值不極端的資料庫工作負載。",
      "D":"✗ Magnetic HDD 效能最低，延遲高，不適合資料庫應用（即使峰值不大）。"
    }
  },
  {
    "id":90,"exam":"CLF",
    "question":"What is the concept of an AWS region?",
    "question_zh":"AWS 區域的概念是什麼？",
    "options":{
      "A":{"en":"It is a collection of Compute capacity","zh":"它是運算容量的集合"},
      "B":{"en":"It is the same as an Availability Zone","zh":"它與可用區域相同"},
      "C":{"en":"It is a geographical area divided into Availability Zones","zh":"它是劃分為多個可用區域的地理區域"},
      "D":{"en":"It is a collection of Edge locations","zh":"它是邊緣站點的集合"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ 雖然區域包含運算容量，但此描述不完整且不準確，Region 的定義重點在地理位置與 AZ 結構。",
      "B":"✗ Region 和 AZ 是不同層級的概念：一個 Region 包含多個 AZ（通常 3 個以上），AZ 是 Region 的子單位。",
      "C":"✓ 正確 — AWS Region 是特定地理位置（如 us-east-1 = 美東維吉尼亞），每個 Region 包含 2 個以上的 Availability Zone，這些 AZ 之間物理隔離但透過低延遲網路互連。",
      "D":"✗ Edge Location 是 CloudFront 的節點，分布在全球用於快取內容，不等於 Region。"
    }
  },
  {
    "id":91,"exam":"CLF",
    "question":"You have a set of developers that need to use .NET to call AWS Services. Which of the following tools can be used to achieve this purpose?",
    "question_zh":"您有一組開發人員需要使用 .NET 呼叫 AWS 服務，下列哪項工具可達成此目的？",
    "options":{
      "A":{"en":"AWS IAM","zh":"AWS IAM"},
      "B":{"en":"AWS SDK","zh":"AWS SDK"},
      "C":{"en":"AWS CLI","zh":"AWS CLI"},
      "D":{"en":"AWS Console","zh":"AWS Management Console"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ IAM 管理身分與存取權限，不是開發工具，無法在程式碼中直接呼叫 AWS API。",
      "B":"✓ 正確 — AWS SDK（Software Development Kit）提供多種程式語言的函式庫，包含 .NET（AWS SDK for .NET），讓開發者在程式碼中直接呼叫 AWS 服務 API。",
      "C":"✗ AWS CLI 是命令列工具，適合腳本和手動操作，但 .NET 程式碼中需要用 SDK 而非 CLI。",
      "D":"✗ AWS Management Console 是網頁圖形介面，無法被 .NET 程式碼直接調用。"
    }
  },
  {
    "id":92,"exam":"CLF",
    "question":"Which of the following is used to derive the costs for moving artifacts from on-premises to AWS?",
    "question_zh":"下列哪項用於計算將工件從本地端遷移至 AWS 的成本？",
    "options":{
      "A":{"en":"AWS TCO Calculator","zh":"AWS TCO 計算器"},
      "B":{"en":"AWS Config","zh":"AWS Config"},
      "C":{"en":"AWS Consolidated Billing","zh":"AWS 整合帳單"},
      "D":{"en":"AWS Cost Explorer","zh":"AWS Cost Explorer"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — AWS TCO Calculator 用於比較本地端與 AWS 的總擁有成本，計算遷移後的財務影響，是遷移成本分析的標準工具。",
      "B":"✗ Config 監控資源合規性，與遷移成本估算無關。",
      "C":"✗ 整合帳單合併多帳號費用，不用於遷移前成本預測。",
      "D":"✗ Cost Explorer 分析現有 AWS 帳單，不適用於遷移前的本地端 vs 雲端比較。"
    }
  },
  {
    "id":93,"exam":"CLF",
    "question":"You have a growing fleet of EC2 instances using EBS volumes for data storage. Each instance needs access to all other instances' data, and your custom replication scripts are growing increasingly complex. What would you recommend?",
    "question_zh":"您有越來越多的 EC2 執行個體使用 EBS 儲存資料，每個執行個體都需要存取其他執行個體的資料，且複寫腳本日益複雜。您建議使用什麼？",
    "options":{
      "A":{"en":"Service Catalog","zh":"AWS Service Catalog"},
      "B":{"en":"EBS","zh":"Amazon EBS"},
      "C":{"en":"DynamoDB","zh":"Amazon DynamoDB"},
      "D":{"en":"EFS","zh":"Amazon EFS"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ Service Catalog 管理 IT 服務目錄，與共享儲存需求無關。",
      "B":"✗ EBS 是區塊儲存，每個 EBS 磁碟區只能掛載到一個 EC2（除 io2 Multi-Attach），無法原生實現多執行個體共享，需要複雜複寫腳本。",
      "C":"✗ DynamoDB 是鍵值/文件 NoSQL 資料庫，不是檔案共享解決方案。",
      "D":"✓ 正確 — Amazon EFS（Elastic File System）是共享的 NFS 檔案系統，可同時掛載到多個 EC2 執行個體，所有執行個體共用同一個檔案系統，完全消除自訂複寫腳本的需求。"
    }
  },
  {
    "id":94,"exam":"CLF",
    "question":"A company wants to store data that is not frequently accessed. What is the best and most cost-effective solution?",
    "question_zh":"一家公司想要儲存不常存取的資料，最佳且最具成本效益的解決方案是什麼？",
    "options":{
      "A":{"en":"AWS Storage Gateway","zh":"AWS Storage Gateway"},
      "B":{"en":"Amazon Elastic Block Store (Amazon EBS)","zh":"Amazon EBS"},
      "C":{"en":"Amazon Simple Storage Service (Amazon S3)","zh":"Amazon S3"},
      "D":{"en":"Amazon S3 Glacier","zh":"Amazon S3 Glacier"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ Storage Gateway 是混合雲儲存閘道，連接本地端與 AWS，成本和複雜度較高，不是單純冷資料儲存的首選。",
      "B":"✗ EBS 是高效能區塊儲存，成本較高，適合頻繁存取的工作負載，不適合冷資料。",
      "C":"✗ S3 Standard 適合頻繁存取；不頻繁存取的資料應使用 S3-IA 或 Glacier 等低成本層級。",
      "D":"✓ 正確 — Amazon S3 Glacier 及 Glacier Deep Archive 是業界成本最低的長期封存儲存，每 GB 費率遠低於 S3 Standard，專為不頻繁存取的資料設計。"
    }
  },
  {
    "id":95,"exam":"CLF",
    "question":"Your company has just started using AWS Cloud resources. They want to get an idea of the costs being incurred so far. How can this be achieved?",
    "question_zh":"您的公司剛開始使用 AWS 雲端資源，想了解目前產生的費用。如何達成？",
    "options":{
      "A":{"en":"By seeing the AWS CloudTrail logs","zh":"透過查看 AWS CloudTrail 日誌"},
      "B":{"en":"By using the AWS Cost and Usage Reports Explorer","zh":"使用 AWS 成本和用量報告 (Cost and Usage Reports)"},
      "C":{"en":"By going to the Amazon EC2 dashboard","zh":"前往 Amazon EC2 儀表板"},
      "D":{"en":"By using the AWS Trusted Advisor dashboard","zh":"使用 AWS Trusted Advisor 儀表板"}
    },
    "correct":["B"],"multi":False,
    "explanations":{
      "A":"✗ CloudTrail 記錄 API 呼叫的稽核日誌，不顯示帳單費用。",
      "B":"✓ 正確 — AWS Cost and Usage Reports（成本和用量報告）以及 Cost Explorer 提供詳細的費用明細、使用量趨勢和預測，是了解 AWS 帳單的主要工具。",
      "C":"✗ EC2 儀表板只顯示 EC2 相關資源狀態，不涵蓋整體 AWS 費用。",
      "D":"✗ Trusted Advisor 提供最佳化建議包含成本節省機會，但不是查看當前帳單費用的工具。"
    }
  },
  {
    "id":96,"exam":"CLF",
    "question":"You have a large archive of documents that must be backed up. They are accessed very infrequently but must be delivered within 10 minutes of a retrieval request. What is the most cost-effective option?",
    "question_zh":"您有大量需要備份的文件，非常少被存取，但取回時必須在 10 分鐘內交付。最具成本效益的選項是什麼？",
    "options":{
      "A":{"en":"Glacier","zh":"Amazon S3 Glacier（標準取回）"},
      "B":{"en":"S3-IA","zh":"S3 Standard-IA"},
      "C":{"en":"Glacier with Expedited Retrieval","zh":"S3 Glacier 快速取回"},
      "D":{"en":"S3","zh":"Amazon S3 Standard"}
    },
    "correct":["C"],"multi":False,
    "explanations":{
      "A":"✗ Glacier 標準取回需 3-5 小時，不符合 10 分鐘的要求。",
      "B":"✗ S3-IA（不頻繁存取）可即時取回，但成本高於 Glacier，且題目強調成本效益。",
      "C":"✓ 正確 — Glacier 快速取回（Expedited Retrieval）可在 1-5 分鐘內取得資料，符合 10 分鐘要求，同時 Glacier 的儲存成本遠低於 S3，是成本與速度的最佳平衡。",
      "D":"✗ S3 Standard 雖然存取速度快，但儲存成本最高，不符合「最具成本效益」的要求。"
    }
  },
  {
    "id":97,"exam":"CLF",
    "question":"Which of the following can be used to view one bill when you have multiple AWS accounts?",
    "question_zh":"擁有多個 AWS 帳號時，下列哪項可用來查看單一帳單？",
    "options":{
      "A":{"en":"IAM","zh":"IAM"},
      "B":{"en":"Cost Explorer","zh":"Cost Explorer"},
      "C":{"en":"Combined Billing","zh":"合併帳單"},
      "D":{"en":"Consolidated Billing","zh":"整合帳單（Consolidated Billing）"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ IAM 管理身分與存取權限，不涉及帳單合併。",
      "B":"✗ Cost Explorer 分析和視覺化費用，但不是帳號整合的機制。",
      "C":"✗ 「Combined Billing」不是 AWS 的正式術語。",
      "D":"✓ 正確 — Consolidated Billing（整合帳單）是 AWS Organizations 的功能，將組織中所有帳號的費用合併為一張帳單，並可享受合計用量帶來的批量折扣。"
    }
  },
  {
    "id":98,"exam":"CLF",
    "question":"A company is deploying a two-tier, highly available web application. The application needs storage for artifacts such as photos and videos. Which service should be used?",
    "question_zh":"一家公司正在部署兩層高可用性 Web 應用程式，需要儲存照片和影片等工件。應使用哪個服務？",
    "options":{
      "A":{"en":"Amazon EBS volume","zh":"Amazon EBS 磁碟區"},
      "B":{"en":"Amazon EC2 instance store","zh":"Amazon EC2 執行個體存放區"},
      "C":{"en":"Amazon RDS instance","zh":"Amazon RDS 執行個體"},
      "D":{"en":"Amazon S3","zh":"Amazon S3"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ EBS 是區塊儲存，掛載到特定 EC2，不適合跨多個 EC2 共用的照片/影片儲存，且在高可用性架構中跨 AZ 共用有限制。",
      "B":"✗ 執行個體存放區是暫時性儲存，EC2 停止後資料消失，完全不適合需要持久化的媒體檔案。",
      "C":"✗ RDS 是關聯式資料庫服務，不適合儲存大型二進位檔案（照片、影片）。",
      "D":"✓ 正確 — Amazon S3 是高度可用的物件儲存，儲存照片和影片等非結構化資料是最典型的 S3 使用場景，支援跨 AZ 複寫和靜態網站託管，天然符合高可用性需求。"
    }
  },
  {
    "id":99,"exam":"CLF",
    "question":"Which component of AWS global infrastructure does Amazon CloudFront use to ensure low-latency delivery?",
    "question_zh":"Amazon CloudFront 使用 AWS 全球基礎設施的哪個元件來確保低延遲傳遞？",
    "options":{
      "A":{"en":"Amazon Virtual Private Cloud (Amazon VPC)","zh":"Amazon VPC"},
      "B":{"en":"AWS Availability Zones","zh":"AWS 可用區域"},
      "C":{"en":"AWS Regions","zh":"AWS 區域"},
      "D":{"en":"AWS Edge Locations","zh":"AWS 邊緣站點"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ VPC 是虛擬私有網路，用於隔離和管理 AWS 資源，不是 CloudFront 的傳遞節點。",
      "B":"✗ AZ 是 Region 內的資料中心群組，提供高可用性，但不是 CloudFront 用於低延遲的組件。",
      "C":"✗ Region 是地理區域，CloudFront 的源站可能在 Region，但傳遞內容到使用者的是 Edge Location。",
      "D":"✓ 正確 — CloudFront 使用遍布全球 400+ 個城市的 Edge Location（邊緣站點）快取並傳遞內容，讓使用者從最近的邊緣節點獲取資料，大幅降低延遲。"
    }
  },
]
