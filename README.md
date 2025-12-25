# 🎄 Professional Glowing Christmas Tree

A beautiful, animated Christmas tree created entirely in Python with dynamic RGB colors, pulsing ornaments, and smooth animations.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

## ✨ Features

- **Dynamic RGB Color Animations**: True RGB color codes (38;2;R;G;B) for precise, vibrant colors
- **Pulsing Ornament Effects**: Ornaments glow and pulse with synchronized timing
- **Multi-layer Tree Structure**: Four distinct layers with increasing complexity
- **Animated Star**: Three-frame star animation at the tree top
- **Textured Trunk**: Realistic trunk with shadow effects
- **Ground Decorations**: Presents and sparkling ground effects
- **Smooth Animations**: Optimized frame timing for fluid motion
- **Professional Code Architecture**: Clean, object-oriented design with modular components

## 🎥 Demo

The tree features:
- Rotating green shades for depth and realism
- Multi-colored ornaments (gold, red, blue, pink, violet, orange)
- Glowing effects with white highlights
- Animated star with rotating patterns
- Ground sparkles and presents
- Festive messages with creator credit

## 📋 Requirements

- Python 3.6 or higher
- Terminal with ANSI color support (most modern terminals)
- No external dependencies required - uses only Python standard library!

### Supported Terminals
- ✅ macOS Terminal
- ✅ iTerm2
- ✅ Linux Terminal (GNOME Terminal, Konsole, etc.)
- ✅ Windows Terminal
- ✅ Windows PowerShell
- ⚠️ CMD (limited color support)

## 🚀 Installation

1. **Clone or download the script:**
```bash
# Download the file
wget https://github.com/br-bit3194/python-glowing-christmas-tree
# or
curl -O https://github.com/br-bit3194/python-glowing-christmas-tree
```

2. **Make it executable (optional on Unix-like systems):**
```bash
chmod +x christmas_tree.py
```

3. **Run it:**
```bash
python christmas_tree.py
# or
python3 christmas_tree.py
```

## 💻 Usage

### Basic Usage
Simply run the script to start the animation:
```bash
python christmas_tree.py
```

Press `Ctrl+C` to stop the animation gracefully.

### Advanced Usage
You can customize the tree by modifying the `ChristmasTree` class parameters:

```python
from christmas_tree import ChristmasTree

# Create a tree instance
tree = ChristmasTree()

# Customize parameters
tree.width = 60  # Adjust tree width
tree.tree_structure = [
    {'rows': 5, 'start_width': 5},
    {'rows': 6, 'start_width': 9},
    # Add more layers...
]

# Run animation
tree.animate()
```

## 🏗️ Code Architecture

### Class Structure

```
ChristmasTree
├── __init__()           # Initialize colors and tree structure
├── clear_screen()       # Clear terminal screen
├── get_tree_char()      # Generate tree foliage characters
├── get_ornament()       # Create ornaments with glow effects
├── draw_star()          # Draw animated star
├── draw_tree_layer()    # Render individual tree layers
├── draw_trunk()         # Draw tree trunk with texture
├── draw_ground()        # Draw presents and sparkles
├── draw_message()       # Display festive message
├── render()             # Compose complete tree frame
└── animate()            # Main animation loop
```

### Color System

The tree uses precise RGB color codes for professional appearance:

```python
colors = {
    'green': [...]      # 4 shades of green for depth
    'lights': [...]     # 7 ornament colors
    'glow': [...]       # 3 glow effect colors
    'star': '...'       # Golden star color
    'trunk': '...'      # Brown trunk
    'shadow': '...'     # Dark brown shadow
}
```

### Tree Structure

Configurable layer system:
```python
tree_structure = [
    {'rows': 4, 'start_width': 5},   # Top layer
    {'rows': 5, 'start_width': 7},   # Second layer
    {'rows': 6, 'start_width': 11},  # Third layer
    {'rows': 7, 'start_width': 15},  # Bottom layer
]
```

## 🎨 Customization Guide

### Changing Colors

Modify the RGB values in the `colors` dictionary:
```python
'green': [
    '\033[38;2;R;G;Bm',  # Replace R, G, B with your values (0-255)
]
```

### Adjusting Animation Speed

Change the sleep duration in the `animate()` method:
```python
time.sleep(0.35)  # Decrease for faster, increase for slower
```

### Adding More Ornaments

Adjust the ornament probability in `draw_tree_layer()`:
```python
ornament_chance = 0.15  # Increase for more ornaments (0.0 to 1.0)
```

### Modifying Tree Size

Change the tree structure and width:
```python
self.width = 50  # Overall tree width
self.tree_structure = [...]  # Add/modify layers
```

## 📝 Code Examples

### Single Frame Render
```python
tree = ChristmasTree()
tree.render(frame=0)  # Render frame 0
```

### Timed Animation
```python
tree = ChristmasTree()
tree.animate(duration=30)  # Run for 30 seconds
```

### Custom Message
Modify the `draw_message()` method to add your own text:
```python
def draw_message(self, frame):
    messages = [
        "✨ Your Custom Message Here! ✨",
        "🌟 Happy Holidays from Your Team! 🌟",
    ]
    # ... rest of the code
```

## 🐛 Troubleshooting

### Colors Not Displaying
- Ensure your terminal supports ANSI colors
- Try using Windows Terminal instead of CMD on Windows
- Update your terminal emulator

### Animation Flickering
- Reduce animation speed (increase sleep time)
- Close other terminal applications
- Check CPU usage

### Script Won't Run
```bash
# Check Python version
python --version  # Should be 3.6+

# Try python3 instead of python
python3 christmas_tree.py
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new animation patterns
- Improve color schemes
- Add new decorations
- Optimize performance
- Fix bugs

## 📄 License

MIT License - Feel free to use and modify for personal or commercial projects.

## 👨‍💻 Author

**Bhavesh Rathod**

Created with ❤️ and Python

## 🙏 Acknowledgments

- Thanks to the Python community
- Inspired by the holiday spirit
- ASCII art traditions

## 📞 Contact

For questions, suggestions, or collaborations:
- LinkedIn: https://www.linkedin.com/in/bhaveshkumar-rathod/
- GitHub: https://github.com/br-bit3194
- Email: bhavesh3194@gmail.com

---

## 🎄 Merry Christmas & Happy Coding! 🎄

*"Making spirits bright, one line of code at a time!"*

---

**Star ⭐ this repo if you enjoyed the project!**