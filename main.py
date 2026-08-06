import random
from fastmcp import FastMCP
import json

mcp=FastMCP("Simple Calculator Server")

@mcp.tool
def random_number(min_val:int=1,max_val:int=100)->int:
    """
    random number generation
    """
    return random.randint(min_val,max_val)

@mcp.tool
def add(a:float,b:float)->float:
    """add two numbers together.
       Args:
        a:First Number
        b:Second Number 
       Returns:
        sum of a and B 
    """
    return a+b

@mcp.resource("infp://server")
def server_info()->str:
    """ get information about this server"""
    info={
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tool",
        "tools":["add","random_number"],
        "author":"Girish"
    }
    return json.dumps(info,indent=2)

if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)