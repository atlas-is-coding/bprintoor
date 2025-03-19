# BPrinter | Printer

[![PyPI version](https://badge.fury.io/py/bprinter.svg)](https://badge.fury.io/py/bprinter)
[![Python](https://img.shields.io/pypi/pyversions/bprinter.svg)](https://pypi.org/project/bprinter/)
[![License](https://img.shields.io/github/license/danilhodos/bprinter.svg)](https://github.com/danilhodos/bprinter/blob/main/LICENSE)

[English](#english)

<a name="english"></a>
## 🌈 BPrinter - Powerful Cross-Platform Terminal Styling Library

BPrinter is a feature-rich library for terminal text styling that works seamlessly across Windows, macOS, and Linux.

### 📦 Installation

```bash
pip install bprinter
```

### 🚀 Quick Start

```python
from bprinter import Color, Background, Style

# Simple color usage
print(Color.RED + "Red text" + Style.RESET)

# Combining styles
print(Color.BLUE + Background.WHITE + Style.BOLD + "Bold blue text on white background" + Style.RESET)

# Using context manager
with Style.color('red'):
    print("This text is red")
    print("And this one too")
```

### ✨ Features

- 🎨 16 basic colors and 256 extended colors
- 🖌 RGB color support
- ✏️ Text styling (bold, italic, underline, etc.)
- 🔤 ASCII art generation
- 📝 Markdown-like text formatting
- 🖥 Cross-platform compatibility
- 🎯 Simple and intuitive API
- 🛠 Extensible architecture

### 🎨 Advanced Usage

#### Logging with Styles

```python
from bprinter import BPrinter

bp = BPrinter(show_time=True)

bp.success("Operation completed successfully!")
bp.error("An error occurred")
bp.warning("Warning: Low memory")
bp.info("Processing data...")
bp.debug("Debug information")
```

#### ASCII Art

```python
from bprinter import ASCIIArtGenerator

# Create ASCII art
print(ASCIIArtGenerator.render("Hello!", color="red"))

# Preview different fonts
print(ASCIIArtGenerator.preview_fonts("ABC"))
```

#### Text Formatting

```python
from bprinter import Printer

printer = Printer(enable_formatting=True)

printer("This is **bold** and _italic_ text")
printer("Use `code` and {red|colored text}")
```

### 📚 Documentation

For detailed documentation and examples, visit our [GitHub repository](https://github.com/DGaliaf/bprinter).

---

## 📄 License

MIT License 
