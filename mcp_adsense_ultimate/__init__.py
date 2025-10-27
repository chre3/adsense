"""
MCP AdSense 增强终极优化版 - 最强大的Google AdSense MCP服务器

这是一个功能完整的MCP服务器，提供完整的Google AdSense管理功能，
包括账户管理、广告单元管理、报告分析、渠道管理等完整覆盖。

特性:
- 🎯 完整的AdSense API功能支持
- 🚀 优化的工具结构，减少重复调用
- 🔐 支持用户认证和服务账户认证
- 📊 报告分析：性能数据、收益分析、趋势分析
- ⚙️ 配置管理：广告单元、自定义渠道、URL渠道
- 💰 账户管理：账户信息、付款信息、警报管理
- 📈 智能参数验证和错误处理
- 🎯 AI大模型友好，参数描述清晰

作者: chre3
版本: 1.0.0
许可证: MIT
"""

__version__ = "1.0.0"
__author__ = "chre3"
__email__ = "chremata3@gmail.com"
__description__ = "增强终极优化版Google AdSense MCP服务器，完整功能支持"

from .server import MCPAdSenseEnhancedUltimateServer

__all__ = ["MCPAdSenseEnhancedUltimateServer"]
