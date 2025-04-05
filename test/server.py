from mcp.server import *
import pandas as pd
import matplotlib.pyplot as plt
import sys
mcp=FastMCP("testing")

@mcp.tool()
def add(a:int,b:int)->int:
    """Add two numbers"""
    a+=1
    
    return int(a+b)

@mcp.tool()
def subtract(a:int,b:int)->int:
    """Subtract two numbers"""
    return int(a-b)

@mcp.tool()
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""
    return int(a*b)

@mcp.tool()
def divide(a:int,b:int)->float:
    """Divide two numbers"""
    return float(a/b)
    
if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  



