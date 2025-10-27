# MCP AdSense Ultimate Server

<div align="center">

**🚀 Powerful AdSense MCP Server | 强大的AdSense MCP服务器**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/chre3/adsense)
[![Python](https://img.shields.io/badge/python-3.8+-green.svg)](https://python.org)
[![Test Coverage](https://img.shields.io/badge/test%20coverage-100%25-brightgreen.svg)](https://github.com/chre3/adsense)

**📖 Documentation | 文档**
- [English Documentation](README_EN.md) | [中文文档](README_CN.md)

</div>

---

## 🎯 Core Tools

| Tool | Function | Status |
|------|----------|--------|
| `manage_accounts` | 💼 Account Management (4 functions) | ✅ 100% |
| `manage_ad_units` | 📦 Ad Unit Management (5 functions) | ✅ 100% |
| `manage_channels` | 📡 Channel Management (5 functions) | ✅ 100% |
| `get_reports` | 📊 Report Analysis (Multi-dimensional) | ✅ 100% |
| `manage_ad_clients` | 🖥️ Ad Client Management (2 functions) | ✅ 100% |
| `manage_sites` | 🌐 Site Management (4 functions) | ✅ 100% |
| `manage_policy_issues` | 🔒 Policy Issues Management (2 functions) | ✅ 100% |
| `manage_saved_reports` | 📋 Saved Reports Management (2 functions) | ✅ 100% |
| `get_help` | ❓ Help Information | ✅ 100% |

## 📋 Feature Overview

### 💼 Account Management
- ✅ List all AdSense accounts
- ✅ Get account details
- ✅ View payment information
- ✅ List account alerts

### 📦 Ad Unit Management
- ✅ List all ad units
- ✅ Get ad unit details
- ✅ Create new ad units
- ✅ Update existing ad units
- ✅ Delete ad units

### 📡 Channel Management
- ✅ URL channel management
- ✅ Custom channel management (CRUD)
- ✅ Channel listing and details
- ✅ Create, update, delete custom channels

### 📊 Report Analysis
- ✅ Performance data queries
- ✅ Revenue report generation
- ✅ Multi-dimensional data analysis
- ✅ Date, ad unit, channel dimensions
- ✅ Flexible filtering and sorting
- ✅ Multiple metrics support

### 🖥️ Ad Client Management
- ✅ List all ad clients
- ✅ Get ad client details

### 🌐 Site Management
- ✅ List all sites
- ✅ Get site details
- ✅ Approve sites
- ✅ Generate OAuth tokens

### 🔒 Policy Issues Management
- ✅ List policy issues
- ✅ Get policy issue details

### 📋 Saved Reports Management
- ✅ List saved reports
- ✅ Generate saved reports

## ⚡ Quick Start

```bash
# Install
pip install -r requirements.txt

# Run
python -m mcp_adsense_ultimate
```

## 🎯 Key Benefits

- ✅ **Complete Coverage**: All AdSense API core functions
- ✅ **Smart Validation**: Auto parameter validation & error handling
- ✅ **AI Optimized**: Clear parameters & intelligent error handling
- ✅ **Flexible Queries**: Support for multi-dimensional & multi-metric queries
- ✅ **Full CRUD**: Complete create, read, update, delete operations

## 📋 Requirements

- Python 3.8+
- Google AdSense Management API
- Google Auth Library

## 🔑 Authentication Setup

Set up authentication credentials in environment variables:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

Or add to MCP configuration:

```json
{
  "scopes": [
    "https://www.googleapis.com/auth/adsense.readonly",
    "https://www.googleapis.com/auth/adsense"
  ]
}
```

## 📊 Report Metrics and Dimensions

### Available Metrics (40+ Metrics)
- `AD_REQUESTS` - Ad requests
- `MATCHED_AD_REQUESTS` - Matched ad requests
- `TOTAL_IMPRESSIONS` - Total impressions
- `IMPRESSIONS` - Impressions
- `INDIVIDUAL_AD_IMPRESSIONS` - Individual ad impressions
- `CLICKS` - Clicks
- `PAGE_VIEWS` - Page views
- `AD_REQUESTS_COVERAGE` - Ad requests coverage
- `PAGE_VIEWS_SPAM_RATIO` - Page views spam ratio
- `AD_REQUESTS_SPAM_RATIO` - Ad requests spam ratio
- `MATCHED_AD_REQUESTS_SPAM_RATIO` - Matched ad requests spam ratio
- `IMPRESSIONS_SPAM_RATIO` - Impressions spam ratio
- `INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO` - Individual ad impressions spam ratio
- `CLICKS_SPAM_RATIO` - Clicks spam ratio
- `PAGE_VIEWS_CTR` - Page views click-through rate
- `AD_REQUESTS_CTR` - Ad requests CTR
- `MATCHED_AD_REQUESTS_CTR` - Matched ad requests CTR
- `IMPRESSIONS_CTR` - Impressions CTR
- `INDIVIDUAL_AD_IMPRESSIONS_CTR` - Individual ad impressions CTR
- `ACTIVE_VIEW_MEASURABILITY` - Active view measurability
- `ACTIVE_VIEW_VIEWABILITY` - Active view viewability
- `ACTIVE_VIEW_TIME` - Active view time
- `ESTIMATED_EARNINGS` - Estimated earnings
- `TOTAL_EARNINGS` - Total earnings
- `PAGE_VIEWS_RPM` - Page views RPM (revenue per thousand)
- `AD_REQUESTS_RPM` - Ad requests RPM
- `MATCHED_AD_REQUESTS_RPM` - Matched ad requests RPM
- `IMPRESSIONS_RPM` - Impressions RPM
- `INDIVIDUAL_AD_IMPRESSIONS_RPM` - Individual ad impressions RPM
- `COST_PER_CLICK` - Cost per click
- `ADS_PER_IMPRESSION` - Ads per impression
- `WEBSEARCH_RESULT_PAGES` - Web search result pages
- `FUNNEL_REQUESTS` - Funnel requests
- `FUNNEL_IMPRESSIONS` - Funnel impressions
- `FUNNEL_CLICKS` - Funnel clicks
- `FUNNEL_RPM` - Funnel RPM

### Available Dimensions (35+ Dimensions)
- `ACCOUNT_NAME` - Account name
- `AD_CLIENT_ID` - Ad client ID
- `AD_CLIENT_NAME` - Ad client name
- `AD_FORMAT_CODE` - Ad format code
- `AD_FORMAT_NAME` - Ad format name
- `AD_PLACEMENT_CODE` - Ad placement code
- `AD_PLACEMENT_NAME` - Ad placement name
- `AD_UNIT_ID` - Ad unit ID
- `AD_UNIT_NAME` - Ad unit name
- `AD_UNIT_SIZE_CODE` - Ad unit size code
- `AD_UNIT_SIZE_NAME` - Ad unit size name
- `BID_TYPE_CODE` - Bid type code
- `BID_TYPE_NAME` - Bid type name
- `BUYER_NETWORK_ID` - Buyer network ID
- `BUYER_NETWORK_NAME` - Buyer network name
- `CITY_CODE` - City code
- `CITY_NAME` - City name
- `CONTENT_PLATFORM_CODE` - Content platform code
- `CONTENT_PLATFORM_NAME` - Content platform name
- `COUNTRY_CODE` - Country code
- `COUNTRY_NAME` - Country name
- `CREATIVE_SIZE_CODE` - Creative size code
- `CREATIVE_SIZE_NAME` - Creative size name
- `CUSTOM_CHANNEL_ID` - Custom channel ID
- `CUSTOM_CHANNEL_NAME` - Custom channel name
- `DATE` - Date
- `DEVICE_CATEGORY_NAME` - Device category name
- `DOMAIN_NAME` - Domain name
- `HOST_NAME` - Host name
- `MONTH` - Month
- `OS_NAME` - Operating system name
- `PAGE_URL` - Page URL
- `PLATFORM_TYPE_CODE` - Platform type code
- `PLATFORM_TYPE_NAME` - Platform type name
- `PRODUCT_CODE` - Product code
- `PRODUCT_NAME` - Product name
- `REGION_CODE` - Region code
- `REGION_NAME` - Region name
- `URL_CHANNEL_ID` - URL channel ID
- `URL_CHANNEL_NAME` - URL channel name
- `WEEK` - Week

---

<div align="center">

**Made with ❤️ for AI-powered AdSense analytics**

[View Full Documentation](README_EN.md) | [查看完整文档](README_CN.md)

</div>
