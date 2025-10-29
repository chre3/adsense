#!/usr/bin/env python3
"""
MCP AdSense 增强终极优化版服务器 - 包含所有AdSense功能
支持账户管理、广告单元管理、报告分析、渠道管理等完整功能
"""

import os
import sys
import json
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta

# Google AdSense imports
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.auth import default

class MCPAdSenseEnhancedUltimateServer:
    """Google AdSense 增强终极优化版MCP服务器"""
    
    def __init__(self):
        self.account_id = os.getenv("GOOGLE_ADSENSE_ACCOUNT_ID")
        self.default_ad_client_id = None  # 将存储默认的广告客户端ID
        
        print("🎯 MCP AdSense 增强终极优化版 v1.0 已初始化", file=sys.stderr)
        print(f"   📊 账户ID: {self.account_id if self.account_id else '未设置'}", file=sys.stderr)
        print("   🚀 增强版 - 完整AdSense功能支持!", file=sys.stderr)

    def _get_credentials(self):
        """获取Google认证凭据，优先使用GOOGLE_APPLICATION_CREDS环境变量指定的文件"""
        try:
            # 检查是否设置了GOOGLE_APPLICATION_CREDS环境变量
            creds_path = os.getenv('GOOGLE_APPLICATION_CREDS')
            if creds_path and os.path.exists(creds_path):
                print(f"✅ 使用指定的认证文件: {creds_path}", file=sys.stderr)
                credentials = service_account.Credentials.from_service_account_file(
                    creds_path,
                    scopes=[
                        "https://www.googleapis.com/auth/adsense.readonly",
                        "https://www.googleapis.com/auth/adsense"
                    ]
                )
                return credentials, None
            else:
                # 如果没有设置环境变量或文件不存在，使用默认的Application Default Credentials
                print("⚠️ 未设置GOOGLE_APPLICATION_CREDS环境变量，使用默认认证", file=sys.stderr)
                return default(scopes=[
                    "https://www.googleapis.com/auth/adsense.readonly",
                    "https://www.googleapis.com/auth/adsense"
                ])
        except Exception as e:
            print(f"❌ 认证失败: {str(e)}", file=sys.stderr)
            raise ValueError(f"无法获取认证凭据: {str(e)}")

    def _get_adsense_service(self):
        """获取AdSense API服务对象"""
        try:
            credentials, project = self._get_credentials()
            service = build('adsense', 'v2', credentials=credentials)
            return service
        except Exception as e:
            raise ValueError(f"无法初始化AdSense服务: {str(e)}")

    def handle_initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """处理MCP初始化请求"""
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {
                    "listChanged": True
                },
                "resources": {
                    "subscribe": True,
                    "listChanged": True
                },
                "prompts": {
                    "listChanged": True
                }
            },
            "serverInfo": {
                "name": "adsense-enhanced-ultimate",
                "version": "1.0.0",
                "description": "增强终极优化版Google AdSense MCP服务器，完整功能支持"
            }
        }

    def handle_tools_list(self) -> Dict[str, Any]:
        """处理工具列表请求"""
        tools = [
            # 账户管理工具
            {
                "name": "manage_accounts",
                "description": "管理AdSense账户 - 包括查看账户列表、账户详情、付款信息、警报等账户管理功能。注意：如果环境变量GOOGLE_ADSENSE_ACCOUNT_ID已设置，通常不需要调用list操作，可以直接使用环境变量中的账户ID进行其他操作",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["list", "get", "get_payments", "list_alerts"],
                            "description": "操作类型：list(列出所有账户 - 仅在需要确认或获取多个账户时使用), get(获取账户详情), get_payments(获取付款信息), list_alerts(列出警报)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（对于get、get_payments和list_alerts操作必需）。如果不提供，将自动使用环境变量GOOGLE_ADSENSE_ACCOUNT_ID的值"
                        }
                    },
                    "required": ["action"]
                }
            },
            
            # 广告单元管理工具
            {
                "name": "manage_ad_units",
                "description": "管理广告单元 - 包括列出广告单元、获取广告单元详情、创建广告单元等功能。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取，无需手动传递",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["list", "get", "create", "patch", "delete"],
                            "description": "操作类型：list(列出广告单元), get(获取详情), create(创建广告单元), patch(更新广告单元), delete(删除广告单元)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（可选，将自动从环境变量GOOGLE_ADSENSE_ACCOUNT_ID获取）。通常不需要显式传递此参数"
                        },
                        "ad_client_id": {
                            "type": "string",
                            "description": "广告客户端ID（可选，如果不提供将自动使用默认客户端ID）"
                        },
                        "ad_unit_id": {
                            "type": "string",
                            "description": "广告单元ID（对于get操作必需）"
                        },
                        "ad_unit_name": {
                            "type": "string",
                            "description": "广告单元名称（对于create操作必需）"
                        },
                        "ad_unit_type": {
                            "type": "string",
                            "enum": ["DISPLAY", "IN_FEED", "IN_ARTICLE", "MATCHED_CONTENT"],
                            "description": "广告单元类型（对于create操作）",
                            "default": "DISPLAY"
                        },
                        "size": {
                            "type": "string",
                            "enum": ["SIZE_320_50", "SIZE_320_100", "SIZE_300_250", "SIZE_250_250", 
                                    "SIZE_200_200", "SIZE_336_280", "SIZE_300_600", "SIZE_728_90", 
                                    "SIZE_160_600", "SIZE_300_1050", "SIZE_970_250", "SIZE_970_90", 
                                    "SIZE_970_200", "SIZE_728_280", "SIZE_468_60", "SIZE_320_480", "RESPONSIVE"],
                            "description": "广告单元尺寸（对于create操作）",
                            "default": "RESPONSIVE"
                        }
                    },
                    "required": ["action"]
                }
            },
            
            # 域名和渠道管理工具
            {
                "name": "manage_channels",
                "description": "管理渠道和域名 - 包括列出URL渠道、自定义渠道、创建和管理渠道等功能。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "channel_type": {
                            "type": "string",
                            "enum": ["url_channels", "custom_channels"],
                            "description": "渠道类型：url_channels(URL渠道), custom_channels(自定义渠道)",
                            "default": "url_channels"
                        },
                        "action": {
                            "type": "string",
                            "enum": ["list", "get", "create", "patch", "delete"],
                            "description": "操作类型：list(列出渠道), get(获取详情), create(创建渠道), patch(更新渠道), delete(删除渠道)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（可选，将自动从环境变量GOOGLE_ADSENSE_ACCOUNT_ID获取）"
                        },
                        "ad_client_id": {
                            "type": "string",
                            "description": "广告客户端ID（可选，如果不提供将自动使用默认客户端ID）"
                        },
                        "channel_id": {
                            "type": "string",
                            "description": "渠道ID（对于get、patch、delete操作必需）"
                        },
                        "channel_name": {
                            "type": "string",
                            "description": "渠道名称（对于create和patch操作可选）"
                        }
                    },
                    "required": ["channel_type", "action"]
                }
            },
            
            # 报告分析工具
            {
                "name": "get_reports",
                "description": "获取AdSense性能报告 - 查询广告单元、日期、国家等多维度的展示、点击、收入等数据。使用步骤：1)调用manage_ad_units获取广告单元的reportingDimensionId；2)使用filters过滤特定广告单元（格式：AD_UNIT_ID==ca-pub-xxx:123456）；3)必须提供date_range或start_date+end_date。注意：如果返回rows为空数组，表示查询时间范围内确实没有数据，不要再修改参数扩大范围搜索，直接向用户说明该广告单元在此时间范围内无数据。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（可选，将自动从环境变量GOOGLE_ADSENSE_ACCOUNT_ID获取）"
                        },
                        "start_date": {
                            "type": "string",
                            "description": "开始日期（格式：YYYY-MM-DD）。与end_date一起使用自定义日期范围，如果不提供date_range参数，则必须提供此参数和end_date"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "结束日期（格式：YYYY-MM-DD）。与start_date一起使用自定义日期范围，如果不提供date_range参数，则必须提供此参数和start_date"
                        },
                        "metrics": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "指标列表。所有可用指标：AD_REQUESTS(广告请求), MATCHED_AD_REQUESTS(匹配请求), TOTAL_IMPRESSIONS(总展示), IMPRESSIONS(展示), INDIVIDUAL_AD_IMPRESSIONS(广告展示), CLICKS(点击), PAGE_VIEWS(页面浏览), AD_REQUESTS_COVERAGE(请求覆盖率), PAGE_VIEWS_SPAM_RATIO(页面浏览垃圾比例), AD_REQUESTS_SPAM_RATIO(请求垃圾比例), MATCHED_AD_REQUESTS_SPAM_RATIO(匹配请求垃圾比例), IMPRESSIONS_SPAM_RATIO(展示垃圾比例), INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO(广告展示垃圾比例), CLICKS_SPAM_RATIO(点击垃圾比例), PAGE_VIEWS_CTR(页面浏览点击率), AD_REQUESTS_CTR(请求点击率), MATCHED_AD_REQUESTS_CTR(匹配请求点击率), IMPRESSIONS_CTR(展示点击率), INDIVIDUAL_AD_IMPRESSIONS_CTR(广告展示点击率), ACTIVE_VIEW_MEASURABILITY(有效观看可测量性), ACTIVE_VIEW_VIEWABILITY(有效观看可见性), ACTIVE_VIEW_TIME(有效观看时间), ESTIMATED_EARNINGS(估算收入), TOTAL_EARNINGS(总收入), PAGE_VIEWS_RPM(页面浏览RPM), AD_REQUESTS_RPM(请求RPM), MATCHED_AD_REQUESTS_RPM(匹配请求RPM), IMPRESSIONS_RPM(展示RPM), INDIVIDUAL_AD_IMPRESSIONS_RPM(广告展示RPM), COST_PER_CLICK(每次点击费用), ADS_PER_IMPRESSION(每展示广告数), WEBSEARCH_RESULT_PAGES(搜索结果页), FUNNEL_REQUESTS(漏斗请求), FUNNEL_IMPRESSIONS(漏斗展示), FUNNEL_CLICKS(漏斗点击), FUNNEL_RPM(漏斗RPM)。不指定则返回默认三个指标",
                            "default": ["ESTIMATED_EARNINGS", "PAGE_VIEWS", "CLICKS"]
                        },
                        "dimensions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "维度列表。所有可用维度：ACCOUNT_NAME(账户名), AD_CLIENT_ID(广告客户端ID), AD_CLIENT_NAME(广告客户端名), AD_FORMAT_CODE(广告格式代码), AD_FORMAT_NAME(广告格式名), AD_PLACEMENT_CODE(广告位置代码), AD_PLACEMENT_NAME(广告位置名), AD_UNIT_ID(广告单元ID), AD_UNIT_NAME(广告单元名), AD_UNIT_SIZE_CODE(广告单元尺寸代码), AD_UNIT_SIZE_NAME(广告单元尺寸名), BID_TYPE_CODE(出价类型代码), BID_TYPE_NAME(出价类型名), BUYER_NETWORK_ID(买方网络ID), BUYER_NETWORK_NAME(买方网络名), CITY_CODE(城市代码), CITY_NAME(城市名), CONTENT_PLATFORM_CODE(内容平台代码), CONTENT_PLATFORM_NAME(内容平台名), COUNTRY_CODE(国家代码), COUNTRY_NAME(国家名), CREATIVE_SIZE_CODE(创意尺寸代码), CREATIVE_SIZE_NAME(创意尺寸名), CUSTOM_CHANNEL_ID(自定义渠道ID), CUSTOM_CHANNEL_NAME(自定义渠道名), DATE(日期), DEVICE_CATEGORY_NAME(设备类别), DOMAIN_NAME(域名), HOST_NAME(主机名), MONTH(月份), OS_NAME(操作系统), PAGE_URL(页面URL), PLATFORM_TYPE_CODE(平台类型代码), PLATFORM_TYPE_NAME(平台类型名), PRODUCT_CODE(产品代码), PRODUCT_NAME(产品名), REGION_CODE(区域代码), REGION_NAME(区域名), URL_CHANNEL_ID(URL渠道ID), URL_CHANNEL_NAME(URL渠道名), WEEK(周)。常用：DATE, AD_UNIT_ID, AD_UNIT_NAME, COUNTRY_CODE",
                            "default": ["DATE"]
                        },
                        "filters": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "过滤器。格式：'维度==值' 或 '维度!=值'。重要：AD_UNIT_ID需要使用完整的reportingDimensionId格式（如'ca-pub-xxx:123456789'），可通过manage_ad_units获取。例如：['AD_UNIT_ID==ca-pub-xxx:123456789', 'COUNTRY_CODE==US', 'COUNTRY_CODE!=GB']"
                        },
                        "sort": {
                            "type": "string",
                            "description": "排序字段和方向。使用'+'或省略前缀表示升序，使用'-'表示降序。例如：'DATE'或'+DATE'（按日期升序），'-ESTIMATED_EARNINGS'（按收入降序），'-CLICKS'（按点击量降序）。可选任何metrics或dimensions字段名",
                            "default": "DATE"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "返回结果数量限制。注意：AdSense API可能有自己的限制，如果指定limit可能不会生效",
                            "default": 100
                        },
                        "date_range": {
                            "type": "string",
                            "enum": ["TODAY", "YESTERDAY", "MONTH_TO_DATE", "YEAR_TO_DATE", "LAST_7_DAYS", "LAST_30_DAYS"],
                            "description": "预定义的日期范围。可选值：TODAY(今天), YESTERDAY(昨天), MONTH_TO_DATE(本月至今), YEAR_TO_DATE(本年至今), LAST_7_DAYS(最近7天), LAST_30_DAYS(最近30天)。如果指定此参数，start_date和end_date将被忽略"
                        }
                    },
                    "required": []
                }
            },
            
            # 广告客户端管理工具
            {
                "name": "manage_ad_clients",
                "description": "管理广告客户端 - 包括列出所有广告客户端、获取广告客户端详情等功能。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["list", "get"],
                            "description": "操作类型：list(列出所有广告客户端), get(获取详情)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（可选，将自动从环境变量GOOGLE_ADSENSE_ACCOUNT_ID获取）"
                        },
                        "ad_client_id": {
                            "type": "string",
                            "description": "广告客户端ID（对于get操作必需）"
                        }
                    },
                    "required": ["action"]
                }
            },
            
            # 网站管理工具
            {
                "name": "manage_sites",
                "description": "管理AdSense网站 - 包括列出网站、批准网站、获取网站详情等功能。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["list", "get", "approve", "token_oauth_domain"],
                            "description": "操作类型：list(列出网站), get(获取详情), approve(批准网站), token_oauth_domain(生成OAuth令牌)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（必需，如果不提供将使用环境变量GOOGLE_ADSENSE_ACCOUNT_ID）"
                        },
                        "site_url": {
                            "type": "string",
                            "description": "网站标识符（对于get、approve和token_oauth_domain操作必需）。应该是从list操作返回的name字段中的站点标识部分，例如从'accounts/pub-xxx/sites/example.com'提取'example.com'"
                        }
                    },
                    "required": ["action"]
                }
            },
            
            # Policy Issues管理工具
            {
                "name": "manage_policy_issues",
                "description": "管理政策问题 - 列出账户的政策问题、获取政策问题详情等。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["list", "get"],
                            "description": "操作类型：list(列出政策问题), get(获取详情)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（必需，如果不提供将使用环境变量GOOGLE_ADSENSE_ACCOUNT_ID）"
                        },
                        "policy_issue_id": {
                            "type": "string",
                            "description": "政策问题ID（对于get操作必需）。应该是从list操作返回的policy issue的完整name，或name中的ID部分"
                        }
                    },
                    "required": ["action"]
                }
            },
            
            # Saved Reports管理工具
            {
                "name": "manage_saved_reports",
                "description": "管理已保存的报告 - 列出已保存的报告、生成已保存的报告等。account_id将从环境变量GOOGLE_ADSENSE_ACCOUNT_ID自动获取",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["list", "generate"],
                            "description": "操作类型：list(列出已保存报告), generate(生成已保存报告)",
                            "default": "list"
                        },
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（必需，如果不提供将使用环境变量GOOGLE_ADSENSE_ACCOUNT_ID）"
                        },
                        "saved_report_id": {
                            "type": "string",
                            "description": "已保存报告ID（对于generate操作必需）。应该是从list操作返回的saved report的完整name，或name中的ID部分"
                        }
                    },
                    "required": ["action"]
                }
            },
            
            # 获取默认广告客户端ID工具
            {
                "name": "get_default_ad_client_id",
                "description": "获取默认的广告客户端ID - 自动获取账户中的第一个可用广告客户端ID",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "账户ID（可选，将自动从环境变量GOOGLE_ADSENSE_ACCOUNT_ID获取）"
                        }
                    },
                    "required": []
                }
            },
            
            # 帮助工具
            {
                "name": "get_help",
                "description": "获取AdSense增强终极优化版帮助信息和使用指南",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        ]
        
        return {"tools": tools}

    def _get_account_id(self, account_id: str = None) -> str:
        """获取账户ID，优先使用参数，其次使用环境变量。自动格式化账户ID为正确格式"""
        # 优先使用传入的account_id
        if account_id:
            # 如果传入的已经是完整格式，直接返回
            if account_id.startswith("accounts/"):
                return account_id
            # 如果是pub-xxx格式，转换为accounts/pub-xxx
            if account_id.startswith("pub-"):
                return f"accounts/{account_id}"
            return account_id
        
        # 使用环境变量
        if self.account_id:
            # 如果环境变量是完整格式，直接返回
            if self.account_id.startswith("accounts/"):
                return self.account_id
            # 如果是pub-xxx格式，转换为accounts/pub-xxx
            if self.account_id.startswith("pub-"):
                return f"accounts/{self.account_id}"
            return self.account_id
        
        return None

    def _clean_account_id(self, account_id: str) -> str:
        """清理账户ID，确保格式正确，去掉重复的accounts/前缀"""
        if not account_id:
            return account_id
        # 去掉重复的accounts/前缀
        return account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id

    def _get_default_ad_client_id(self, account_id: str) -> str:
        """获取默认的广告客户端ID"""
        try:
            if self.default_ad_client_id:
                return self.default_ad_client_id
                
            service = self._get_adsense_service()
            clean_account_id = self._clean_account_id(account_id)
            
            # 获取广告客户端列表
            ad_clients = service.accounts().adclients().list(
                parent=f"accounts/{clean_account_id}"
            ).execute()
            
            # 找到第一个可用的广告客户端
            for client in ad_clients.get('adClients', []):
                client_id = client.get('name', '').split('/')[-1]  # 提取ca-pub-xxx部分
                if client_id and client_id.startswith('ca-pub-'):
                    self.default_ad_client_id = client_id
                    return client_id
            
            return None
        except Exception as e:
            print(f"⚠️ 获取默认广告客户端ID失败: {str(e)}", file=sys.stderr)
            return None

    def get_default_ad_client_id(self, account_id: str = None) -> Dict[str, Any]:
        """获取默认的广告客户端ID"""
        try:
            # 获取账户ID
            if not account_id:
                account_id = self._get_account_id()
                if not account_id:
                    return {
                        "success": False,
                        "error": "未提供账户ID，且环境变量GOOGLE_ADSENSE_ACCOUNT_ID未设置"
                    }
            
            # 获取默认客户端ID
            default_client_id = self._get_default_ad_client_id(account_id)
            
            if not default_client_id:
                return {
                    "success": False,
                    "error": "无法获取默认广告客户端ID，请检查账户是否有可用的广告客户端"
                }
            
            return {
                "success": True,
                "default_ad_client_id": default_client_id,
                "message": f"默认广告客户端ID: {default_client_id}",
                "usage": f"在调用manage_ad_units或manage_channels时，可以使用此ID作为ad_client_id参数"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"获取默认广告客户端ID失败: {str(e)}"
            }

    def handle_tools_call(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """处理工具调用请求"""
        try:
            # 获取账户ID，优先使用参数，其次使用环境变量
            account_id = self._get_account_id(arguments.get("account_id"))
            
            if name == "get_help":
                return self.get_help()
            elif name == "manage_accounts":
                return self.manage_accounts(
                    arguments.get("action", "list"),
                    account_id
                )
            elif name == "manage_ad_units":
                return self.manage_ad_units(
                    arguments.get("action", "list"),
                    account_id,
                    arguments.get("ad_client_id"),
                    arguments.get("ad_unit_id"),
                    arguments.get("ad_unit_name"),
                    arguments.get("ad_unit_type", "DISPLAY"),
                    arguments.get("size", "RESPONSIVE")
                )
            elif name == "manage_channels":
                return self.manage_channels(
                    arguments.get("channel_type", "url_channels"),
                    arguments.get("action", "list"),
                    account_id,
                    arguments.get("ad_client_id"),
                    arguments.get("channel_id"),
                    arguments.get("channel_name")
                )
            elif name == "get_reports":
                return self.get_reports(
                    account_id,
                    arguments.get("start_date"),
                    arguments.get("end_date"),
                    arguments.get("metrics"),
                    arguments.get("dimensions"),
                    arguments.get("filters"),
                    arguments.get("sort", "DATE"),
                    arguments.get("limit", 100),
                    arguments.get("date_range")
                )
            elif name == "manage_ad_clients":
                return self.manage_ad_clients(
                    arguments.get("action", "list"),
                    account_id,
                    arguments.get("ad_client_id")
                )
            elif name == "manage_sites":
                return self.manage_sites(
                    arguments.get("action", "list"),
                    account_id,
                    arguments.get("site_url")
                )
            elif name == "manage_policy_issues":
                return self.manage_policy_issues(
                    arguments.get("action", "list"),
                    account_id,
                    arguments.get("policy_issue_id")
                )
            elif name == "manage_saved_reports":
                return self.manage_saved_reports(
                    arguments.get("action", "list"),
                    account_id,
                    arguments.get("saved_report_id")
                )
            elif name == "get_default_ad_client_id":
                return self.get_default_ad_client_id(account_id)
            else:
                return {"error": f"Unknown tool: {name}"}
        except Exception as e:
            return {"error": str(e)}

    def get_help(self) -> Dict[str, Any]:
        """获取帮助信息"""
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps({
                        "success": True,
                        "message": "AdSense增强终极优化版MCP服务器帮助",
                        "data": {
                            "server": "🎯 MCP AdSense 增强终极优化版",
                            "version": "1.0.0",
                            "total_functions": 8,
                            "tools": [
                                {"name": "manage_accounts", "description": "账户管理 - 账户列表、详情、付款信息、警报"},
                                {"name": "manage_ad_units", "description": "广告单元管理 - 列出、获取、创建广告单元"},
                                {"name": "manage_channels", "description": "渠道管理 - URL渠道、自定义渠道管理"},
                                {"name": "get_reports", "description": "报告分析 - 性能报告、收益报告等多维度分析"},
                                {"name": "manage_ad_clients", "description": "广告客户端管理 - 广告客户端列表和详情"},
                                {"name": "manage_sites", "description": "网站管理 - 网站列表、批准、OAuth令牌"},
                                {"name": "manage_policy_issues", "description": "政策问题管理 - 政策问题列表和详情"},
                                {"name": "manage_saved_reports", "description": "已保存报告管理 - 列出和生成已保存报告"},
                                {"name": "get_default_ad_client_id", "description": "获取默认广告客户端ID - 自动获取账户中的第一个可用广告客户端ID"},
                                {"name": "get_help", "description": "帮助信息"}
                            ],
                            "metrics": {
                                "available": "支持所有AdSense API v2官方指标（60+个），包括：收入类、展示类、点击类、请求类、浏览量类、CTR类、RPM类、CPI类等。完整列表见：https://developers.google.com/adsense/management/metrics-dimensions",
                                "description": "常用指标类别：\n- 收入：ESTIMATED_EARNINGS(估算收入), TOTAL_EARNINGS(总收入)\n- 展示：IMPRESSIONS, INDIVIDUAL_AD_IMPRESSIONS\n- 点击：CLICKS\n- 浏览：PAGE_VIEWS, WEBSEARCH_RESULT_PAGES\n- 请求：AD_REQUESTS, MATCHED_AD_REQUESTS\n- CTR：PAGE_VIEWS_CTR, IMPRESSIONS_CTR, MATCHED_AD_REQUESTS_CTR等\n- RPM：PAGE_VIEWS_RPM, IMPRESSIONS_RPM, MATCHED_AD_REQUESTS_RPM等\n- CPI：COST_PER_CLICK\n完整列表请访问官方文档"
                            },
                            "dimensions": {
                                "available": "支持所有AdSense API v2官方维度（50+个），包括：账户、客户端、广告单元、日期、国家地区、平台、广告格式、渠道、产品、主机等。完整列表见：https://developers.google.com/adsense/management/metrics-dimensions",
                                "description": "常用维度类别：\n- 日期：DATE, MONTH, WEEK\n- 广告单元：AD_UNIT_ID, AD_UNIT_NAME, AD_UNIT_SIZE_CODE/NAME\n- 客户端：AD_CLIENT_ID, AD_CLIENT_NAME\n- 国家地区：COUNTRY_CODE/NAME, REGION_CODE/NAME, CITY_CODE/NAME\n- 平台：CONTENT_PLATFORM_CODE/NAME, DEVICE_CATEGORY_NAME, OS_NAME\n- 广告格式：AD_FORMAT_CODE/NAME, AD_PLACEMENT_CODE/NAME\n- 渠道：CUSTOM_CHANNEL_ID, URL_CHANNEL_ID\n- 产品：PRODUCT_NAME\n- 主机：HOST_NAME\n完整列表请访问官方文档"
                            },
                            "usage_tips": [
                                "使用 manage_accounts 管理账户信息",
                                "使用 manage_ad_units 管理广告单元",
                                "使用 manage_channels 管理渠道和域名",
                                "使用 get_reports 获取性能报告",
                                "使用 manage_ad_clients 查看广告客户端",
                                "所有操作都需要先列出账户获取account_id"
                            ]
                        },
                        "timestamp": datetime.now().isoformat()
                    }, ensure_ascii=False, indent=2)
                }
            ]
        }

    def manage_accounts(self, action: str, account_id: str = None) -> Dict[str, Any]:
        """管理AdSense账户"""
        try:
            service = self._get_adsense_service()
            
            # 验证必需参数
            if action in ["get", "get_payments", "list_alerts"] and not account_id:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": f"操作 '{action}' 需要 account_id 参数",
                                "hint": "请提供 account_id 参数或设置环境变量 GOOGLE_ADSENSE_ACCOUNT_ID"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            if action == "list":
                # 列出所有账户
                accounts = service.accounts().list().execute()
                account_list = []
                for account in accounts.get('accounts', []):
                    account_list.append({
                        "name": account.get('name'),
                        "displayName": account.get('displayName'),
                        "pendingTasks": account.get('pendingTasks', [])
                    })
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list",
                                "accounts": account_list,
                                "total": len(account_list)
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "get" and account_id:
                # 获取账户详情
                account = service.accounts().get(name=account_id).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "get",
                                "account": {
                                    "name": account.get('name'),
                                    "displayName": account.get('displayName'),
                                    "pendingTasks": account.get('pendingTasks', []),
                                    "premium": account.get('premium', False),
                                    "createTime": account.get('createTime'),
                                    "timeZone": account.get('timeZone'),
                                    "currencyCode": account.get('currencyCode'),
                                    "accountType": account.get('accountType'),
                                    "state": account.get('state')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "get_payments" and account_id:
                # 获取付款信息
                payments = service.accounts().listPayments(name=account_id).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "get_payments",
                                "payments": payments.get('payments', [])
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "list_alerts" and account_id:
                # 列出警报
                clean_account_id = self._clean_account_id(account_id)
                alerts = service.accounts().alerts().list(parent=f"accounts/{clean_account_id}").execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list_alerts",
                                "alerts": alerts.get('alerts', [])
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数或操作不支持"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def manage_ad_units(self, action: str, account_id: str, ad_client_id: str = None,
                       ad_unit_id: str = None, ad_unit_name: str = None, 
                       ad_unit_type: str = "DISPLAY", size: str = "RESPONSIVE") -> Dict[str, Any]:
        """管理广告单元"""
        try:
            service = self._get_adsense_service()
            
            # 如果没有提供客户端ID，尝试获取默认的
            if not ad_client_id:
                ad_client_id = self._get_default_ad_client_id(account_id)
                if not ad_client_id:
                    return {
                        "success": False,
                        "error": "未提供广告客户端ID，且无法获取默认客户端ID。请先调用manage_ad_clients获取可用的客户端ID。"
                    }
            
            # 验证必需参数
            if not account_id:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数: account_id",
                                "hint": "请提供 account_id 参数或设置环境变量 GOOGLE_ADSENSE_ACCOUNT_ID"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            if action in ["get", "patch", "delete"] and not ad_unit_id:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": f"操作 '{action}' 需要 ad_unit_id 参数"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            if action == "create" and not ad_unit_name:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "操作 'create' 需要 ad_unit_name 参数"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            if action == "list":
                # 列出广告单元
                # 确保account_id格式正确，去掉重复的accounts/前缀
                clean_account_id = self._clean_account_id(account_id)
                ad_units = service.accounts().adclients().adunits().list(
                    parent=f"accounts/{clean_account_id}/adclients/{ad_client_id}"
                ).execute()
                
                unit_list = []
                for unit in ad_units.get('adUnits', []):
                    unit_list.append({
                        "name": unit.get('name'),
                        "displayName": unit.get('displayName'),
                        "adUnitId": unit.get('adUnitId'),
                        "state": unit.get('state'),
                        "adType": unit.get('contentAdsSettings', {}).get('type'),
                        "size": unit.get('contentAdsSettings', {}).get('size')
                    })
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list",
                                "ad_units": unit_list,
                                "total": len(unit_list)
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "get" and ad_unit_id:
                # 获取广告单元详情
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                ad_unit = service.accounts().adclients().adunits().get(
                    name=f"accounts/{clean_account_id}/adclients/{ad_client_id}/adunits/{ad_unit_id}"
                ).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "get",
                                "ad_unit": {
                                    "name": ad_unit.get('name'),
                                    "displayName": ad_unit.get('displayName'),
                                    "adUnitId": ad_unit.get('adUnitId'),
                                    "state": ad_unit.get('state'),
                                    "contentAdsSettings": ad_unit.get('contentAdsSettings', {}),
                                    "reportingDimensionId": ad_unit.get('reportingDimensionId')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "create" and ad_unit_name:
                # 创建广告单元
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                ad_unit = service.accounts().adclients().adunits().create(
                    parent=f"accounts/{clean_account_id}/adclients/{ad_client_id}",
                    body={
                        "displayName": ad_unit_name,
                        "contentAdsSettings": {
                            "size": size,
                            "type": ad_unit_type
                        }
                    }
                ).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "create",
                                "ad_unit": {
                                    "name": ad_unit.get('name'),
                                    "displayName": ad_unit.get('displayName'),
                                    "adUnitId": ad_unit.get('adUnitId')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "patch" and ad_unit_id:
                # 更新广告单元
                update_body = {}
                if ad_unit_name:
                    update_body["displayName"] = ad_unit_name
                if size:
                    update_body["contentAdsSettings"] = {"size": size}
                if ad_unit_type:
                    if "contentAdsSettings" not in update_body:
                        update_body["contentAdsSettings"] = {}
                    update_body["contentAdsSettings"]["type"] = ad_unit_type
                
                if not update_body:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": False,
                                    "error": "必须提供至少一个要更新的字段"
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                ad_unit = service.accounts().adclients().adunits().patch(
                    name=f"accounts/{clean_account_id}/adclients/{ad_client_id}/adunits/{ad_unit_id}",
                    body=update_body
                ).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "patch",
                                "ad_unit": {
                                    "name": ad_unit.get('name'),
                                    "displayName": ad_unit.get('displayName'),
                                    "adUnitId": ad_unit.get('adUnitId'),
                                    "state": ad_unit.get('state')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "delete" and ad_unit_id:
                # 删除广告单元
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                service.accounts().adclients().adunits().delete(
                    name=f"accounts/{clean_account_id}/adclients/{ad_client_id}/adunits/{ad_unit_id}"
                ).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "delete",
                                "message": "广告单元已成功删除"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数或操作不支持"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def manage_channels(self, channel_type: str, action: str, account_id: str, ad_client_id: str = None,
                       channel_id: str = None, channel_name: str = None) -> Dict[str, Any]:
        """管理渠道"""
        try:
            service = self._get_adsense_service()
            
            # 如果没有提供客户端ID，尝试获取默认的
            if not ad_client_id:
                ad_client_id = self._get_default_ad_client_id(account_id)
                if not ad_client_id:
                    return {
                        "success": False,
                        "error": "未提供广告客户端ID，且无法获取默认客户端ID。请先调用manage_ad_clients获取可用的客户端ID。"
                    }
            
            if channel_type == "url_channels":
                if action == "list":
                    # 列出URL渠道
                    clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                    url_channels = service.accounts().adclients().urlchannels().list(
                        parent=f"accounts/{clean_account_id}/adclients/{ad_client_id}"
                    ).execute()
                    
                    channel_list = []
                    for channel in url_channels.get('urlChannels', []):
                        channel_list.append({
                            "name": channel.get('name'),
                            "uriPattern": channel.get('uriPattern'),
                            "reportingDimensionId": channel.get('reportingDimensionId')
                        })
                    
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": True,
                                    "action": "list",
                                    "channel_type": "url_channels",
                                    "channels": channel_list,
                                    "total": len(channel_list)
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
            
            elif channel_type == "custom_channels":
                if action == "list":
                    # 列出自定义渠道
                    clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                    custom_channels = service.accounts().adclients().customchannels().list(
                        parent=f"accounts/{clean_account_id}/adclients/{ad_client_id}"
                    ).execute()
                    
                    channel_list = []
                    for channel in custom_channels.get('customChannels', []):
                        channel_list.append({
                            "name": channel.get('name'),
                            "displayName": channel.get('displayName'),
                            "customChannelId": channel.get('customChannelId'),
                            "reportingDimensionId": channel.get('reportingDimensionId')
                        })
                    
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": True,
                                    "action": "list",
                                    "channel_type": "custom_channels",
                                    "channels": channel_list,
                                    "total": len(channel_list)
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                
                elif action == "get" and channel_id:
                    # 获取自定义渠道详情
                    clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                    channel = service.accounts().adclients().customchannels().get(
                        name=f"accounts/{clean_account_id}/adclients/{ad_client_id}/customchannels/{channel_id}"
                    ).execute()
                    
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": True,
                                    "action": "get",
                                    "channel": {
                                        "name": channel.get('name'),
                                        "displayName": channel.get('displayName'),
                                        "customChannelId": channel.get('customChannelId'),
                                        "reportingDimensionId": channel.get('reportingDimensionId')
                                    }
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                
                elif action == "create":
                    if not channel_name:
                        return {
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps({
                                        "success": False,
                                        "error": "操作 'create' 需要 channel_name 参数"
                                    }, ensure_ascii=False, indent=2)
                                }
                            ]
                        }
                    # 创建自定义渠道
                    clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                    channel = service.accounts().adclients().customchannels().create(
                        parent=f"accounts/{clean_account_id}/adclients/{ad_client_id}",
                        body={"displayName": channel_name}
                    ).execute()
                    
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": True,
                                    "action": "create",
                                    "channel": {
                                        "name": channel.get('name'),
                                        "displayName": channel.get('displayName'),
                                        "customChannelId": channel.get('customChannelId')
                                    }
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                
                elif action == "patch" and channel_id:
                    # 更新自定义渠道
                    if not channel_name:
                        return {
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps({
                                        "success": False,
                                        "error": "操作 'patch' 需要 channel_name 参数"
                                    }, ensure_ascii=False, indent=2)
                                }
                            ]
                        }
                    
                    clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                    channel = service.accounts().adclients().customchannels().patch(
                        name=f"accounts/{clean_account_id}/adclients/{ad_client_id}/customchannels/{channel_id}",
                        body={"displayName": channel_name}
                    ).execute()
                    
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": True,
                                    "action": "patch",
                                    "channel": {
                                        "name": channel.get('name'),
                                        "displayName": channel.get('displayName'),
                                        "customChannelId": channel.get('customChannelId')
                                    }
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                
                elif action == "delete" and channel_id:
                    # 删除自定义渠道
                    clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                    service.accounts().adclients().customchannels().delete(
                        name=f"accounts/{clean_account_id}/adclients/{ad_client_id}/customchannels/{channel_id}"
                    ).execute()
                    
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": True,
                                    "action": "delete",
                                    "message": "自定义渠道已成功删除"
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
            
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({
                            "success": False,
                            "error": "不支持的操作或渠道类型"
                        }, ensure_ascii=False, indent=2)
                    }
                ]
            }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def get_reports(self, account_id: str, start_date: str = None, end_date: str = None,
                   metrics: List[str] = None, dimensions: List[str] = None,
                   filters: List[str] = None, sort: str = "DATE", limit: int = 100,
                   date_range: str = None) -> Dict[str, Any]:
        """获取AdSense报告"""
        if filters is None:
            filters = []
        if metrics is None:
            metrics = ["ESTIMATED_EARNINGS", "PAGE_VIEWS", "CLICKS"]
        if dimensions is None:
            dimensions = ["DATE"]
        
        try:
            service = self._get_adsense_service()
            
            # 构建报告请求
            if date_range:
                # 使用预定义的日期范围
                request_body = {
                    "dateRange": date_range,
                    "metrics": metrics,
                    "dimensions": dimensions
                }
            else:
                # 使用自定义日期范围
                if not start_date or not end_date:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": json.dumps({
                                    "success": False,
                                    "error": "必须提供start_date和end_date，或使用date_range参数"
                                }, ensure_ascii=False, indent=2)
                            }
                        ]
                    }
                
                # 对于自定义日期范围，直接设置startDate和endDate，不设置dateRange字段
                request_body = {
                    "startDate": {
                        "year": int(start_date.split('-')[0]),
                        "month": int(start_date.split('-')[1]),
                        "day": int(start_date.split('-')[2])
                    },
                    "endDate": {
                        "year": int(end_date.split('-')[0]),
                        "month": int(end_date.split('-')[1]),
                        "day": int(end_date.split('-')[2])
                    },
                    "metrics": metrics,
                    "dimensions": dimensions
                }
            
            if filters:
                request_body["filters"] = filters
            
            if sort:
                # orderBy应该是字符串数组格式，如["+DATE"]或["-ESTIMATED_EARNINGS"]
                # + 表示升序，- 表示降序
                if sort.startswith('-'):
                    # 降序
                    request_body["orderBy"] = [f"-{sort[1:]}"]
                else:
                    # 升序
                    request_body["orderBy"] = [f"+{sort}"]
            
            if limit and limit > 0:
                request_body["limit"] = limit
            
            # 调用API
            clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
            
            # AdSense API v2的generate方法需要将参数展开传递，而不是使用body参数
            reports = service.accounts().reports().generate(
                account=f"accounts/{clean_account_id}",
                **request_body
            ).execute()
            
            # 处理报告数据
            rows = []
            for row in reports.get('rows', []):
                row_data = {}
                for i, cell in enumerate(row.get('cells', [])):
                    dim_index = i if i < len(dimensions) else None
                    metric_index = i - len(dimensions) if i >= len(dimensions) else None
                    
                    if dim_index is not None:
                        row_data[dimensions[dim_index]] = {
                            "value": cell.get('value'),
                            "label": cell.get('label')
                        }
                    elif metric_index is not None:
                        row_data[metrics[metric_index]] = {
                            "value": cell.get('value'),
                            "label": cell.get('label')
                        }
                rows.append(row_data)
            
            result = {
                "success": True,
                "account": account_id,
                "start_date": start_date,
                "end_date": end_date,
                "date_range": date_range,
                "metrics": metrics,
                "dimensions": dimensions,
                "filters": filters if filters else None,
                "total_rows": len(rows),
                "rows": rows
            }
            
            # 如果没有数据，添加友好的提示信息
            if len(rows) == 0:
                date_info = f"日期范围: {date_range}" if date_range else f"日期范围: {start_date} 到 {end_date}"
                result["message"] = f"查询成功，但在指定的{date_info}内没有数据。这表示该广告单元在此时间范围内确实没有展示、点击或收入数据。"
            
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(result, ensure_ascii=False, indent=2)
                    }
                ]
            }
            
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def manage_ad_clients(self, action: str, account_id: str, ad_client_id: str = None) -> Dict[str, Any]:
        """管理广告客户端"""
        try:
            service = self._get_adsense_service()
            
            if action == "list":
                # 列出所有广告客户端
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                ad_clients = service.accounts().adclients().list(
                    parent=f"accounts/{clean_account_id}"
                ).execute()
                
                client_list = []
                for client in ad_clients.get('adClients', []):
                    client_list.append({
                        "name": client.get('name'),
                        "adClientId": client.get('adClientId'),
                        "productCode": client.get('productCode'),
                        "reportingDimensionId": client.get('reportingDimensionId'),
                        "state": client.get('state')
                    })
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list",
                                "ad_clients": client_list,
                                "total": len(client_list)
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "get" and ad_client_id:
                # 获取广告客户端详情
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                ad_client = service.accounts().adclients().get(
                    name=f"accounts/{clean_account_id}/adclients/{ad_client_id}"
                ).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "get",
                                "ad_client": {
                                    "name": ad_client.get('name'),
                                    "adClientId": ad_client.get('adClientId'),
                                    "productCode": ad_client.get('productCode'),
                                    "reportingDimensionId": ad_client.get('reportingDimensionId'),
                                    "state": ad_client.get('state')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数或操作不支持"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def manage_sites(self, action: str, account_id: str, site_url: str = None) -> Dict[str, Any]:
        """管理AdSense网站"""
        try:
            service = self._get_adsense_service()
            
            if action == "list":
                # 列出所有网站
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                sites = service.accounts().sites().list(parent=f"accounts/{clean_account_id}").execute()
                
                site_list = []
                for site in sites.get('sites', []):
                    site_list.append({
                        "name": site.get('name'),
                        "reportingDimensionId": site.get('reportingDimensionId'),
                        "uriPattern": site.get('uriPattern'),
                        "state": site.get('state')
                    })
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list",
                                "sites": site_list,
                                "total": len(site_list)
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "get" and site_url:
                # 获取网站详情
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                site = service.accounts().sites().get(name=f"accounts/{clean_account_id}/sites/{site_url}").execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "get",
                                "site": {
                                    "name": site.get('name'),
                                    "reportingDimensionId": site.get('reportingDimensionId'),
                                    "uriPattern": site.get('uriPattern'),
                                    "state": site.get('state')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "approve" and site_url:
                # 批准网站
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                site = service.accounts().sites().approve(name=f"accounts/{clean_account_id}/sites/{site_url}").execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "approve",
                                "site": {
                                    "name": site.get('name'),
                                    "state": site.get('state')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "token_oauth_domain" and site_url:
                # 生成OAuth令牌
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                result = service.accounts().sites().tokenOauthDomain(name=f"accounts/{clean_account_id}/sites/{site_url}").execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "token_oauth_domain",
                                "token": result.get('token', '')
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数或操作不支持"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def manage_policy_issues(self, action: str, account_id: str, policy_issue_id: str = None) -> Dict[str, Any]:
        """管理政策问题"""
        try:
            service = self._get_adsense_service()
            
            if action == "list":
                # 列出所有政策问题
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                policy_issues = service.accounts().policyIssues().list(parent=f"accounts/{clean_account_id}").execute()
                
                issue_list = []
                for issue in policy_issues.get('policyIssues', []):
                    issue_list.append({
                        "name": issue.get('name'),
                        "reportingDimensionId": issue.get('reportingDimensionId'),
                        "uriPattern": issue.get('uriPattern'),
                        "actionable": issue.get('actionable'),
                        "issue": issue.get('issue')
                    })
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list",
                                "policy_issues": issue_list,
                                "total": len(issue_list)
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "get" and policy_issue_id:
                # 获取政策问题详情
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                policy_issue = service.accounts().policyIssues().get(
                    name=f"accounts/{clean_account_id}/policyIssues/{policy_issue_id}"
                ).execute()
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "get",
                                "policy_issue": {
                                    "name": policy_issue.get('name'),
                                    "reportingDimensionId": policy_issue.get('reportingDimensionId'),
                                    "uriPattern": policy_issue.get('uriPattern'),
                                    "actionable": policy_issue.get('actionable'),
                                    "issue": policy_issue.get('issue')
                                }
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数或操作不支持"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

    def manage_saved_reports(self, action: str, account_id: str, saved_report_id: str = None) -> Dict[str, Any]:
        """管理已保存的报告"""
        try:
            service = self._get_adsense_service()
            
            if action == "list":
                # 列出已保存的报告
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                saved_reports = service.accounts().reports().saved().list(parent=f"accounts/{clean_account_id}").execute()
                
                report_list = []
                for report in saved_reports.get('savedReports', []):
                    report_list.append({
                        "name": report.get('name'),
                        "title": report.get('title'),
                        "createTime": report.get('createTime')
                    })
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "list",
                                "saved_reports": report_list,
                                "total": len(report_list)
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            elif action == "generate" and saved_report_id:
                # 生成已保存的报告
                clean_account_id = account_id.replace("accounts/", "") if account_id.startswith("accounts/") else account_id
                report = service.accounts().reports().saved().generate(
                    name=f"accounts/{clean_account_id}/reports/saved/{saved_report_id}"
                ).execute()
                
                # 处理报告数据
                rows = []
                for row in report.get('rows', []):
                    row_data = {}
                    for cell in row.get('cells', []):
                        row_data[cell.get('columnName')] = cell.get('value')
                    rows.append(row_data)
                
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": True,
                                "action": "generate",
                                "saved_report_id": saved_report_id,
                                "rows": rows
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            
            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({
                                "success": False,
                                "error": "缺少必需参数或操作不支持"
                            }, ensure_ascii=False, indent=2)
                        }
                    ]
                }
                
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"success": False, "error": str(e)}, ensure_ascii=False, indent=2)
                    }
                ]
            }

def main():
    """主函数 - MCP协议服务器"""
    server = MCPAdSenseEnhancedUltimateServer()
    
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            
            try:
                request = json.loads(line.strip())
                method = request.get("method")
                params = request.get("params", {})
                request_id = request.get("id")
                
                if method == "initialize":
                    result = server.handle_initialize(params)
                elif method == "tools/list":
                    result = server.handle_tools_list()
                elif method == "tools/call":
                    result = server.handle_tools_call(
                        params.get("name"),
                        params.get("arguments", {})
                    )
                else:
                    result = {"error": f"Unknown method: {method}"}
                
                response = {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "result": result
                }
                
                print(json.dumps(response))
                sys.stdout.flush()
                
            except json.JSONDecodeError:
                continue
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id") if "request" in locals() else None,
                    "error": {"code": -32603, "message": str(e)}
                }
                print(json.dumps(error_response))
                sys.stdout.flush()
                
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
