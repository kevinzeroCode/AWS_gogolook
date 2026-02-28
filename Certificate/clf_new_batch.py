
NEW_CLF = [
  {
    "id":51,"exam":"CLF",
    "question":"Which AWS Cloud service is used to enable Multi-Factor Authentication (MFA)?",
    "question_zh":"哪個 AWS 雲端服務用於開啟多因素驗證 (MFA)？",
    "options":{
      "A":{"en":"Amazon Inspector","zh":"Amazon Inspector"},
      "B":{"en":"AWS Config","zh":"AWS Config"},
      "C":{"en":"Amazon Elastic Compute Cloud (Amazon EC2)","zh":"Amazon EC2"},
      "D":{"en":"AWS Identity and Access Management (IAM)","zh":"AWS 身分識別與存取管理 (IAM)"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ Amazon Inspector 是自動化漏洞掃描服務，用於檢查 EC2 / 容器的安全漏洞，與 MFA 設定無關。",
      "B":"✗ AWS Config 追蹤資源配置合規性，不負責身分驗證或 MFA 管理。",
      "C":"✗ Amazon EC2 是虛擬伺服器（運算）服務，不負責帳戶安全設定。",
      "D":"✓ 正確 — MFA 是透過 AWS IAM 啟用的。IAM 控制使用者身分和存取權限，MFA 設定在 IAM 的使用者或角色頁面完成。"
    }
  },
  {
    "id":52,"exam":"CLF",
    "question":"Which EBS volume type is most appropriate for a large, high-performance database workload?",
    "question_zh":"哪種 EBS 磁碟區類型最適合大型高效能資料庫工作負載？",
    "options":{
      "A":{"en":"EBS Provisioned IOPS SSD (io1/io2)","zh":"EBS 佈建 IOPS SSD (io1/io2)"},
      "B":{"en":"EBS Throughput Optimized HDD (st1)","zh":"EBS 輸送量最佳化 HDD (st1)"},
      "C":{"en":"EBS Magnetic (standard)","zh":"EBS 磁性 HDD (standard)"},
      "D":{"en":"EBS General Purpose SSD (gp2/gp3)","zh":"EBS 通用 SSD (gp2/gp3)"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Provisioned IOPS SSD (io1/io2) 提供最高效能與一致的低延遲 IOPS，專為需要穩定高 I/O 的大型資料庫（Oracle、SQL Server、MySQL）設計，可佈建最高 64,000 IOPS。",
      "B":"✗ Throughput Optimized HDD 適合大量循序讀取（如大數據、日誌處理），但資料庫需要隨機 I/O，HDD 無法提供足夠低的延遲。",
      "C":"✗ Magnetic (standard) 是最舊的 EBS 類型，效能最低，不適合任何高需求工作負載。",
      "D":"✗ General Purpose SSD (gp3) 是日常工作負載的好選擇，但對於需要極高一致 IOPS 的大型資料庫，不如 Provisioned IOPS SSD 可靠。"
    }
  },
  {
    "id":53,"exam":"CLF",
    "question":"Your company uses VM Templates to spin up virtual machines on-premises. Which AWS feature serves a similar purpose for EC2 instances?",
    "question_zh":"您的公司使用 VM 範本在本地佈建虛擬機器，哪個 AWS 功能在 EC2 上提供類似用途？",
    "options":{
      "A":{"en":"EBS Snapshots","zh":"EBS 快照"},
      "B":{"en":"Amazon VMware","zh":"Amazon VMware"},
      "C":{"en":"EBS Volumes","zh":"EBS 磁碟區"},
      "D":{"en":"Amazon Machine Images (AMIs)","zh":"Amazon 機器映像 (AMI)"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ EBS 快照是磁碟區的備份點，只儲存磁碟內容，無法獨立啟動一台新 EC2 執行個體（需要封裝成 AMI 才行）。",
      "B":"✗ Amazon VMware（AWS VMware Cloud on AWS）是用來把 VMware 工作負載遷移到 AWS 的服務，不是 EC2 的映像機制。",
      "C":"✗ EBS 磁碟區是儲存區塊，相當於硬碟本身，不包含作業系統設定或應用程式配置。",
      "D":"✓ 正確 — AMI (Amazon Machine Image) 包含作業系統、應用程式、資料和配置，等同於 VM 範本。用一個 AMI 可以快速啟動多個完全相同的 EC2 執行個體。"
    }
  },
  {
    "id":54,"exam":"CLF",
    "question":"Which term describes 'creating systems that scale to the required capacity based on changes in demand'?",
    "question_zh":"哪個術語描述「根據需求變化，建立可擴展到所需容量的系統」？",
    "options":{
      "A":{"en":"Elasticity","zh":"彈性 (Elasticity)"},
      "B":{"en":"Disaster Recovery","zh":"災難復原 (Disaster Recovery)"},
      "C":{"en":"Aggregation","zh":"聚合 (Aggregation)"},
      "D":{"en":"Decoupling","zh":"解耦 (Decoupling)"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — 彈性 (Elasticity) 是指系統能根據需求自動向上/向外擴展（scale up/out），也能在需求降低時自動縮減，避免資源浪費。AWS Auto Scaling 就是實現彈性的核心服務。",
      "B":"✗ 災難復原是指在系統故障後恢復服務的能力，關注的是可用性和資料復原，不是按需求伸縮。",
      "C":"✗ 聚合是將多個資源或資料彙整的概念，與動態容量調整無關。",
      "D":"✗ 解耦是指降低系統各元件間的依賴性（例如用 SQS 解耦前後端），是架構設計原則，不是容量管理概念。"
    }
  },
  {
    "id":55,"exam":"CLF",
    "question":"When using On-Demand EC2 instances, which of the following is a FALSE statement about costing?",
    "question_zh":"使用隨需 EC2 執行個體時，關於計費哪項說法是錯誤的？",
    "options":{
      "A":{"en":"You are charged per second based on the hourly rate","zh":"您按每秒計費（以小時費率為基準）"},
      "B":{"en":"You pay for only what you use","zh":"您只需為實際使用量付費"},
      "C":{"en":"You pay no upfront costs for the instance","zh":"執行個體無需支付任何預付費用"},
      "D":{"en":"You must pay termination fees if you terminate the instance","zh":"若終止執行個體，需支付終止費用"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✓ 正確陳述 — Linux 執行個體確實按秒計費（最低 60 秒），以小時費率換算。",
      "B":"✓ 正確陳述 — 隨需模式就是用多少付多少，完全彈性。",
      "C":"✓ 正確陳述 — 隨需執行個體無需預付款，啟動即用，停止即停費。",
      "D":"✗ 正確選項（錯誤陳述）— 隨需執行個體沒有終止費用。您停止或終止後就停止計費，AWS 不收取任何中途終止的違約金。"
    }
  },
  {
    "id":56,"exam":"CLF",
    "question":"Which is the least expensive option for long-term data archival?",
    "question_zh":"哪個選項是長期資料封存的最低成本方案？",
    "options":{
      "A":{"en":"Amazon EFS (Elastic File System)","zh":"Amazon EFS (彈性檔案系統)"},
      "B":{"en":"Amazon Redshift","zh":"Amazon Redshift"},
      "C":{"en":"EBS Snapshots","zh":"EBS 快照"},
      "D":{"en":"Amazon S3 Glacier","zh":"Amazon S3 Glacier"}
    },
    "correct":["D"],"multi":False,
    "explanations":{
      "A":"✗ EFS 是共享 NFS 檔案系統，每 GB 費用遠高於 Glacier，適合頻繁存取，不適合封存。",
      "B":"✗ Redshift 是資料倉儲（Data Warehouse）服務，用於大規模分析查詢，成本高，不是封存解決方案。",
      "C":"✗ EBS 快照儲存在 S3 上，成本比 Glacier 高，且主要用途是 EBS 磁碟區備份，非長期封存。",
      "D":"✓ 正確 — Amazon S3 Glacier（尤其是 Glacier Deep Archive）提供業界最低成本的長期封存儲存，每 GB 費用極低，適合需要保存多年但鮮少存取的資料。"
    }
  },
  {
    "id":57,"exam":"CLF",
    "question":"What AWS service lets you host a Domain Name System (DNS)?",
    "question_zh":"哪個 AWS 服務可讓您託管網域名稱系統 (DNS)？",
    "options":{
      "A":{"en":"Amazon Route 53","zh":"Amazon Route 53"},
      "B":{"en":"AWS VPN","zh":"AWS VPN"},
      "C":{"en":"Amazon VPC","zh":"Amazon VPC"},
      "D":{"en":"AWS Direct Connect","zh":"AWS Direct Connect"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Amazon Route 53 是 AWS 的可擴展高可用 DNS 網路服務，支援公有/私有 DNS 託管、網域註冊和健康檢查。名稱來自 DNS 使用的 TCP/UDP port 53。",
      "B":"✗ AWS VPN 提供加密的網路連線（站台到站台或用戶端 VPN），不是 DNS 服務。",
      "C":"✗ Amazon VPC 是虛擬私有網路（定義子網路、路由表等），VPC 內部有 DNS 解析功能，但不是「託管 DNS 的服務」。",
      "D":"✗ AWS Direct Connect 提供從您的資料中心到 AWS 的專用實體網路連線，不是 DNS 服務。"
    }
  },
  {
    "id":58,"exam":"CLF",
    "question":"You need to host a high-volume Oracle database on EC2 (cannot use RDS due to a custom plug-in). Which EBS volume type should you choose?",
    "question_zh":"您需要在 EC2 上託管高流量 Oracle 資料庫（因自訂外掛無法使用 RDS），應選擇哪種 EBS 磁碟區類型？",
    "options":{
      "A":{"en":"Provisioned IOPS SSD (io1/io2)","zh":"佈建 IOPS SSD (io1/io2)"},
      "B":{"en":"Throughput Optimized HDD (st1)","zh":"輸送量最佳化 HDD (st1)"},
      "C":{"en":"General Purpose SSD (gp2/gp3)","zh":"通用 SSD (gp2/gp3)"},
      "D":{"en":"Cold HDD (sc1)","zh":"冷 HDD (sc1)"}
    },
    "correct":["A"],"multi":False,
    "explanations":{
      "A":"✓ 正確 — Oracle 資料庫需要高一致性的低延遲隨機 I/O。Provisioned IOPS SSD 可佈建高達 64,000 IOPS，保證一致效能，是資料庫的最佳選擇，也是 AWS 針對 I/O 密集型資料庫的官方建議。",
      "B":"✗ Throughput Optimized HDD (st1) 適合大量循序讀取（MapReduce、日誌、ETL），無法提供資料庫所需的低延遲隨機 IOPS。",
      "C":"✗ General Purpose SSD (gp3) 雖然對許多工作負載足夠，但對高流量 Oracle 資料庫而言，無法保證一致的高 IOPS 效能。",
      "D":"✗ Cold HDD (sc1) 是最低成本的 HDD，用於不頻繁存取的冷資料，完全不適合高效能資料庫。"
    }
  },
]
