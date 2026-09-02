# Demo MCP Server (FastMCP)

A demo Model Context Protocol (MCP) server implemented using [FastMCP](https://github.com/jlowin/fastmcp) in Python. This server exposes a suite of mathematical, calculation, and utility tools for MCP clients such as Claude Desktop, Cursor, and other AI agents.

---

## 🛠️ Available Tools

The server provides the following tools in [`main.py`](file:///d:/MCP_SERVER_PROJECTS/01-DEMO-MCP-SEREVR/main.py):

| Tool Name | Parameters | Description |
| :--- | :--- | :--- |
| `roll_dice` | `roll_dice: int = 1` | Rolls standard 6-sided dice for the specified number of times |
| `add_numbers` | `a: int, b: int` | Adds two numbers ($a + b$) |
| `subtract_numbers` | `a: int, b: int` | Subtracts the second number from the first ($a - b$) |
| `multiply_numbers` | `a: int, b: int` | Multiplies two numbers ($a \times b$) |
| `divide_numbers` | `a: int, b: int` | Divides $a$ by $b$ (handles divide-by-zero error) |
| `percentage` | `a: float, b: float` | Calculates $(a / b) \times 100$ |
| `square_number` | `a: int` | Returns the square ($a^2$) |
| `cube_number` | `a: int` | Returns the cube ($a^3$) |
| `power_number` | `a: int, b: int` | Returns $a^b$ |
| `factorial_number` | `a: int` | Computes factorial ($a!$) |
| `even_or_odd` | `a: int` | Determines if a number is `Even` or `Odd` |
| `is_prime_number` | `n: int` | Checks whether $n$ is a prime number |

---

## 📋 Prerequisites

Ensure you have **Python >= 3.10** and [**`uv`**](https://github.com/astral-sh/uv) (fast Python package and environment manager) installed.

### 1. Install `uv`

- **Windows (PowerShell):**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
- **macOS / Linux:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Via Pip:**
  ```bash
  pip install uv
  ```

---

## 🚀 Setup & Installation

### Option A: Setup Existing Project

1. **Clone or open the repository folder** in your terminal or VS Code:
   ```bash
   cd 01-DEMO-MCP-SEREVR
   ```
2. **Install dependencies**:
   ```bash
   uv sync
   ```

---

### Option B: Create Project from Scratch

If you are recreating this project from scratch:

1. **Create project folder and navigate inside:**
   ```bash
   mkdir fastmcp-demo-server
   cd fastmcp-demo-server
   ```
2. **Initialize uv project:**
   ```bash
   uv init .
   ```
3. **Add FastMCP dependency:**
   ```bash
   uv add fastmcp
   ```
4. **Verify FastMCP installation:**
   ```bash
   uv run fastmcp version
   ```
5. **Create your server file** (`main.py`) with tools using `@mcp.tool`.

---

## 🧪 Testing the Server (MCP Inspector / Dev Mode)

Use FastMCP's built-in interactive development inspector to test and debug all MCP tools in your browser:

```bash
uv run fastmcp dev main.py
```

- This will launch the **MCP Inspector** in your default web browser.
- You can test tool invocations, inspect schemas, and view real-time logs directly from the UI.

---

## ▶️ Running the Server

To start and run the MCP server directly over standard I/O (stdio):

```bash
uv run fastmcp run main.py
```

Alternatively, run with Python:
```bash
uv run python main.py
```

---

## 🔌 Installing into Claude Desktop

You can automatically register the server into Claude Desktop with a single command:

```bash
uv run fastmcp install claude-desktop main.py
```

### Manual Configuration for Claude Desktop

If you prefer manual configuration, add the following to your `claude_desktop_config.json`:

- **Windows path:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS path:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "demo-server": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "d:\\MCP_SERVER_PROJECTS\\01-DEMO-MCP-SEREVR",
        "fastmcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

Restart Claude Desktop after making configuration changes.
