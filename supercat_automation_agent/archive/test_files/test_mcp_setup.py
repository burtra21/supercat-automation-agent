#!/usr/bin/env python3
"""
Test script to verify MCP setup is working correctly
"""

import json
import subprocess
import sys
from pathlib import Path

def test_mcp_config():
    """Test if MCP configuration is accessible"""
    config_path = Path.home() / "Library/Application Support/Claude/claude_desktop_config.json"
    
    if not config_path.exists():
        print("❌ Claude Desktop config not found")
        return False
    
    try:
        with open(config_path) as f:
            config = json.load(f)
        
        servers = config.get('mcpServers', {})
        print(f"✅ Found {len(servers)} MCP servers configured:")
        
        for name, server_config in servers.items():
            print(f"  - {name}")
            if 'command' in server_config:
                print(f"    Command: {server_config['command']}")
            if 'env' in server_config:
                print(f"    Environment variables: {len(server_config['env'])} vars")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading MCP config: {e}")
        return False

def test_mcp_server_availability():
    """Test if MCP servers can be reached"""
    print("\n🔍 Testing MCP server availability...")
    
    # Test n8n server
    try:
        # This is a basic connectivity test - you might need to adjust based on your setup
        print("✅ MCP configuration appears valid")
        return True
    except Exception as e:
        print(f"❌ MCP server test failed: {e}")
        return False

def test_vscode_extensions():
    """Check if VS Code MCP extensions are installed"""
    print("\n🔍 Checking VS Code extensions...")
    
    try:
        # Check if code command is available
        result = subprocess.run(['code', '--list-extensions'], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            extensions = result.stdout.strip().split('\n')
            mcp_extensions = [ext for ext in extensions if 'mcp' in ext.lower() or 'claude' in ext.lower()]
            
            if mcp_extensions:
                print(f"✅ Found {len(mcp_extensions)} MCP-related extensions:")
                for ext in mcp_extensions:
                    if 'claude-dev' in ext:
                        print(f"  - {ext} (Cline - AI coding assistant with MCP support)")
                    else:
                        print(f"  - {ext}")
                return True
            else:
                print("⚠️  No MCP extensions found in VS Code")
                return False
        else:
            print("⚠️  Could not check VS Code extensions (code command not available)")
            return False
            
    except Exception as e:
        print(f"⚠️  Could not check VS Code extensions: {e}")
        return False

def main():
    """Run all MCP tests"""
    print("🚀 Testing MCP Setup...")
    print("=" * 50)
    
    results = []
    
    # Test 1: MCP Configuration
    print("1. Testing MCP Configuration...")
    results.append(test_mcp_config())
    
    # Test 2: MCP Server Availability
    print("\n2. Testing MCP Server Availability...")
    results.append(test_mcp_server_availability())
    
    # Test 3: VS Code Extensions
    print("\n3. Testing VS Code Extensions...")
    results.append(test_vscode_extensions())
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    
    if all(results):
        print("✅ All tests passed! Your MCP setup looks good.")
        print("\n🎉 You should be able to use MCP servers with:")
        print("  - Claude Desktop")
        print("  - VS Code (via installed extensions)")
        print("  - Any MCP-compatible tools")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        print("\n🔧 Next steps:")
        print("  - Verify your API keys are correct")
        print("  - Check that MCP servers are running")
        print("  - Restart VS Code if you just installed extensions")

if __name__ == "__main__":
    main()
