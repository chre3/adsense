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
- ✅ Get account details (display name, timezone, currency, account type, etc.)
- ✅ View payment information
- ✅ List account alerts

### 📦 Ad Unit Management
- ✅ List all ad units
- ✅ Get ad unit details (status, type, size, etc.)
- ✅ Create new ad units
- ✅ Update existing ad units (patch)
- ✅ Delete ad units
- ✅ Support for multiple ad types: DISPLAY, IN_FEED, IN_ARTICLE, MATCHED_CONTENT
- ✅ Support for multiple ad sizes: from SIZE_320_50 to RESPONSIVE

### 📡 Channel Management
- ✅ URL channel management: List all URL channels
- ✅ Custom channel management: Complete CRUD operations
- ✅ List, get, create, update, delete custom channels
- ✅ Support for getting channel details

### 📊 Report Analysis
- ✅ Performance data queries (earnings, clicks, page views, etc.)
- ✅ Multi-dimensional data analysis (date, ad unit, country, channel, etc.)
- ✅ Flexible data filtering
- ✅ Custom sorting
- ✅ Support for various report metrics and dimensions

### 🖥️ Ad Client Management
- ✅ List all ad clients
- ✅ Get ad client details

### 🌐 Site Management
- ✅ List all sites
- ✅ Get site details
- ✅ Approve sites
- ✅ Generate OAuth tokens

###ור Policy Issues Management
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

### Available Metrics
- `ESTIMATED_EARNINGS` - Estimated earnings
- `PAGE_VIEWS` - Page views
- `CLICKS` - Clicks
- `CTR` - Click-through rate
- `CPC` - Cost per click
- `RPC` - Revenue per click
- `ECPM` - Earnings per thousand impressions
- `PAGE_VIEWS_RPM` - Page views RPM
- `IMPRESSIONS` - Impressions

### Available Dimensions
- `DATE` - Date
- `AD_UNIT_ID` - Ad unit ID
- `AD_UNIT_NAME` - Ad unit name
- `AD_CLIENT_ID` - Ad client ID
- `AD_CLIENT_NAME` - Ad client name
- `CUSTOM_CHANNEL_ID` - Custom channel ID
- `URL_CHANNEL_ID` - URL channel ID
- `COUNTRY_CODE` - Country code
- `PRODUCT_NAME` - Product name
- `HOST_NAME` - Host name

## 📝 Usage Examples

### View Accounts
```json
{
  "tool": "manage_accounts",
  "arguments": {
    "action": "list"
  }
}
```

### Get Reports
```json
{
  "tool": "get_reports",
  "arguments": {
    "account_id": "accounts/pub-xxxx",
    "start_date": "2024-01-01",
    "end_date": "2024-01-31",
    "metrics": ["ESTIMATED_EARNINGS", "PAGE_VIEWS", "CLICKS"],
    "dimensions": ["DATE"]
  }
}
```

### Create Ad Unit
```json
{
  "tool": "manage_ad_units",
  "arguments": {
    "action": "create",
    "account_id": "accounts/pub-xxxx",
    "ad_client_id": "ca-pub-xxxx",
    "ad_unit_name": "Sidebar Ad",
    "ad_unit_type": "DISPLAY",
    "size": "RESPONSIVE"
  }
}
```

---

<div align="center">

**Made with ❤️ for AI-powered AdSense analytics**

[View Full Documentation](README_EN.md) | [查看完整文档](README_CN.md)

</div>
