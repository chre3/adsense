# MCP AdSense 终极服务器

<div align="center">

**🚀 强大的AdSense MCP服务器 | Powerful AdSense MCP Server**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/chre3/adsense)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Test Coverage](https://img.shields.io/badge/test%20coverage-100%25-brightgreen.svg)](https://github.com/chre3/adsense)

**📖 Documentation | 文档**
- [English Documentation](README_EN.md) | [中文文档](README_CN.md)

</div>

---

## 🎯 核心工具

| 工具 | 功能 | 状态 |
|------|------|------|
| `manage_accounts` | 💼 账户管理 (4个功能) | ✅ 100% |
| `manage_ad_units` | 📦 广告单元管理 (5个功能) | ✅ 100% |
| `manage_channels` | 📡 渠道管理 (5个功能) | ✅ 100% |
| `get_reports` | 📊 报告分析 (多维度) | ✅ 100% |
| `manage_ad_clients` | 🖥️ 广告客户端管理 (2个功能) | ✅ 100% |
| `manage_sites` | 🌐 网站管理 (4个功能) | ✅ 100% |
| `manage_policy_issues` | 🔒 政策问题管理 (2个功能) | ✅ 100% |
| `manage_saved_reports` | 📋 已保存报告管理 (2个功能) | ✅ 100% |
| `get_help` | ❓ 帮助信息 | ✅ 100% |

## 📋 功能概览

### 💼 账户管理
- ✅ 列出所有AdSense账户
- ✅ 获取账户详细信息
- ✅ 查看付款信息
- ✅ 列出账户警报

### 📦 广告单元管理
- ✅ 列出所有广告单元
- ✅ 获取广告单元详情
- ✅ 创建新广告单元
- ✅ 更新广告单元
- ✅ 删除广告单元

### 📡 渠道管理
- ✅ URL渠道管理
- ✅ 自定义渠道管理 (完整CRUD)
- ✅ 渠道列表和详情
- ✅ 创建、更新、删除自定义渠道

### 📊 报告分析
- ✅ 性能数据查询
- ✅ 收益报告生成
- ✅ 多维度数据分析
- ✅ 日期、广告单元、渠道等维度
- ✅ 灵活的过滤和排序
- ✅ 多种指标支持

### 🖥️ 广告客户端管理
- ✅ 列出所有广告客户端
- ✅ 获取广告客户端详情

### 🌐 网站管理
- ✅ 列出所有网站
- ✅ 获取网站详情
- ✅ 批准网站
- ✅ 生成OAuth令牌

### 🔒 政策问题管理
- ✅ 列出政策问题
- ✅ 获取政策问题详情

### 📋 已保存报告管理
- ✅ 列出已保存报告
- ✅ 生成已保存报告

## ⚡ 快速开始

```bash
# 安装
pip install -r requirements.txt

# 运行
python -m mcp_adsense_ultimate
```

## 🎯 关键优势

- ✅ **完整覆盖**: AdSense API所有核心功能
- ✅ **智能验证**: 自动参数验证和错误处理
- ✅ **AI优化**: 清晰的参数和智能错误处理
- ✅ **灵活查询**: 支持多维度和多指标查询
- ✅ **完整CRUD**: 支持创建、读取、更新、删除操作

## 📋 要求

- Python 3.8+
- Google AdSense Management API
- Google Auth Library

## 🔑 认证设置

需要在环境变量中设置认证凭据：

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

或者在MCP配置中添加：

```json
{
  "scopes": [
    "https://www.googleapis.com/auth/adsense.readonly",
    "https://www.googleapis.com/auth/adsense"
  ]
}
```

## 📊 报告指标和维度

### 可用指标（40+个）
- `AD_REQUESTS` - 广告请求
- `MATCHED_AD_REQUESTS` - 匹配请求
- `TOTAL_IMPRESSIONS` - 总展示
- `IMPRESSIONS` - 展示
- `INDIVIDUAL_AD_IMPRESSIONS` - 广告展示
- `CLICKS` - 点击
- `PAGE_VIEWS` - 页面浏览
- `AD_REQUESTS_COVERAGE` - 请求覆盖率
- `PAGE_VIEWS_SPAM_RATIO` - 页面浏览垃圾比例
- `AD_REQUESTS_SPAM_RATIO` - 请求垃圾比例
- `MATCHED_AD_REQUESTS_SPAM_RATIO` - 匹配请求垃圾比例
- `IMPRESSIONS_SPAM_RATIO` - 展示垃圾比例
- `INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO` - 广告展示垃圾比例
- `CLICKS_SPAM_RATIO` - 点击垃圾比例
- `PAGE_VIEWS_CTR` - 页面浏览点击率
- `AD_REQUESTS_CTR` - 请求点击率
- `MATCHED_AD_REQUESTS_CTR` - 匹配请求点击率
- `IMPRESSIONS_CTR` - 展示点击率
- `INDIVIDUAL_AD_IMPRESSIONS_CTR` - 广告展示点击率
- `ACTIVE_VIEW_MEASURABILITY` - 有效观看可测量性
- `ACTIVE_VIEW_VIEWABILITY` - 有效观看可见性
- `ACTIVE_VIEW_TIME` - 有效观看时间
- `ESTIMATED_EARNINGS` - 估算收入
- `TOTAL_EARNINGS` - 总收入
- `PAGE_VIEWS_RPM` - 页面浏览RPM
- `AD_REQUESTS_RPM` - 请求RPM
- `MATCHED_AD_REQUESTS_RPM` - 匹配请求RPM
- `IMPRESSIONS_RPM` - 展示RPM
- `INDIVIDUAL_AD_IMPRESSIONS_RPM` - 广告展示RPM
- `COST_PER_CLICK` - 每次点击费用
- `ADS_PER_IMPRESSION` - 每展示广告数
- `WEBSEARCH_RESULT_PAGES` - 搜索结果页
- `FUNNEL_REQUESTS` - 漏斗请求
- `FUNNEL_IMPRESSIONS` - 漏斗展示
- `FUNNEL_CLICKS` - 漏斗点击
- `FUNNEL_RPM` - 漏斗RPM

### 可用维度（35+个）
- `ACCOUNT_NAME` - 账户名
- `AD_CLIENT_ID` - 广告客户端ID
- `AD_CLIENT_NAME` - 广告客户端名
- `AD_FORMAT_CODE` - 广告格式代码
- `AD_FORMAT_NAME` - 广告格式名
- `AD_PLACEMENT_CODE` - 广告位置代码
- `AD_PLACEMENT_NAME` - 广告位置名
- `AD_UNIT_ID` - 广告单元ID
- `AD_UNIT_NAME` - 广告单元名
- `AD_UNIT_SIZE_CODE` - 广告单元尺寸代码
- `AD_UNIT_SIZE_NAME` - 广告单元尺寸名
- `BID_TYPE_CODE` - 出价类型代码
- `BID_TYPE_NAME` - 出价类型名
- `BUYER_NETWORK_ID` - 买方网络ID
- `BUYER_NETWORK_NAME` - 买方网络名
- `CITY_CODE` - 城市代码
- `CITY_NAME` - 城市名
- `CONTENT_PLATFORM_CODE` - 内容平台代码
- `CONTENT_PLATFORM_NAME` - 内容平台名
- `COUNTRY_CODE` - 国家代码
- `COUNTRY_NAME` - 国家名
- `CREATIVE_SIZE_CODE` - 创意尺寸代码
- `CREATIVE_SIZE_NAME` - 创意尺寸名
- `CUSTOM_CHANNEL_ID` - 自定义渠道ID
- `CUSTOM_CHANNEL_NAME` - 自定义渠道名
- `DATE` - 日期
- `DEVICE_CATEGORY_NAME` - 设备类别
- `DOMAIN_NAME` - 域名
- `HOST_NAME` - 主机名
- `MONTH` - 月份
- `OS_NAME` - 操作系统
- `PAGE_URL` - 页面URL
- `PLATFORM_TYPE_CODE` - 平台类型代码
- `PLATFORM_TYPE_NAME` - 平台类型名
- `PRODUCT_CODE` - 产品代码
- `PRODUCT_NAME` - 产品名
- `REGION_CODE` - 区域代码
- `REGION_NAME` - 区域名
- `URL_CHANNEL_ID` - URL渠道ID
- `URL_CHANNEL_NAME` - URL渠道名
- `WEEK` - 周

---

<div align="center">

**为AI驱动的AdSense分析而制作 ❤️**

[View Full Documentation](README_EN.md) | [查看完整文档](README_CN.md)

</div>
