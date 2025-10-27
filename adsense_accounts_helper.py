#!/usr/bin/env python3
"""
AdSense账户列表获取助手 - 修复版本
使用googleapiclient.discovery而不是google.adsense_v2
"""

import os
import sys
import json
from googleapiclient.discovery import build
from google.auth import default

def get_adsense_accounts(project_id=None):
    """
    获取AdSense账户列表
    
    Args:
        project_id (str): Google Cloud项目ID，如果为None则从环境变量获取
    
    Returns:
        dict: 包含账户列表和状态信息的字典
    """
    try:
        if not project_id:
            project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
            if not project_id:
                return {
                    "success": False,
                    "error": "未设置GOOGLE_CLOUD_PROJECT环境变量",
                    "suggestion": "请先使用 set-gcloud-project 命令设置项目"
                }
        
        print(f"当前项目: {project_id}")
        print("🔍 正在获取AdSense账户列表...")
        
        # 使用Application Default Credentials
        try:
            credentials, project = default(scopes=[
                "https://www.googleapis.com/auth/adsense.readonly"
            ])
            print("✅ 使用Application Default Credentials认证成功")
        except Exception as auth_error:
            return {
                "success": False,
                "error": f"认证失败: {str(auth_error)}",
                "suggestion": "请确保已运行: gcloud auth application-default login"
            }
        
        # 创建AdSense服务
        service = build("adsense", "v2", credentials=credentials)
        
        # 获取账户列表
        print("\n📊 获取AdSense账户列表...")
        
        try:
            # 列出所有账户
            request = service.accounts().list()
            response = request.execute()
            
            accounts = response.get("accounts", [])
            print(f"找到 {len(accounts)} 个AdSense账户:")
            
            if not accounts:
                return {
                    "success": False,
                    "error": "未找到任何AdSense账户",
                    "suggestion": "请确保:\n1. 已正确设置Google Cloud项目\n2. 已启用AdSense API\n3. 账户有访问AdSense的权限\n4. 在AdSense控制台中创建了账户"
                }
            
            # 处理账户信息
            account_list = []
            for i, account in enumerate(accounts, 1):
                account_info = {
                    "index": i,
                    "display_name": account.get("displayName", "未知"),
                    "account_id": account.get("name", "").split("/")[-1],
                    "state": account.get("state", "未知"),
                    "create_time": account.get("createTime", "未知"),
                    "update_time": account.get("updateTime", "未知")
                }
                account_list.append(account_info)
                
                print(f"\n{i}. 账户名称: {account_info['display_name']}")
                print(f"   账户ID: {account_info['account_id']}")
                print(f"   状态: {account_info['state']}")
                print(f"   创建时间: {account_info['create_time']}")
                print(f"   更新时间: {account_info['update_time']}")
                
                # 建议使用第一个账户
                if i == 1:
                    print(f"\n   💡 建议使用第一个账户: {account_info['account_id']}")
                    print(f"      可以运行: ./chre3.sh set-adsense-account <user_id> {account_info['account_id']}")
                    print()
            
            return {
                "success": True,
                "project_id": project_id,
                "account_count": len(accounts),
                "accounts": account_list,
                "suggested_account": account_list[0]["account_id"] if account_list else None
            }
        
        except Exception as api_error:
            return {
                "success": False,
                "error": f"获取AdSense账户列表失败: {str(api_error)}",
                "suggestion": "可能的原因:\n1. 权限不足\n2. API未启用\n3. 账户中没有AdSense账户\n4. 需要AdSense API v2权限"
            }
    
    except Exception as e:
        return {
            "success": False,
            "error": f"获取AdSense账户列表失败: {str(e)}",
            "suggestion": "可能的解决方案:\n1. 检查认证文件是否存在\n2. 确保已启用AdSense API\n3. 检查账户权限\n4. 在AdSense控制台中创建账户"
        }

def main():
    """主函数，用于命令行调用"""
    result = get_adsense_accounts()
    
    if result["success"]:
        print("\n✅ AdSense账户列表获取完成")
        # 输出JSON格式的结果供其他程序使用
        print("\n--- JSON结果 ---")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"\n❌ {result['error']}")
        print(f"💡 {result['suggestion']}")
        sys.exit(1)

if __name__ == "__main__":
    main()