import random
import time
import os
import sys

class ChristmasTree:
    def __init__(self):
        # Professional color palette with precise RGB codes
        self.colors = {
            'green': [
                '\033[38;2;34;139;34m',   # Forest Green
                '\033[38;2;50;205;50m',   # Lime Green
                '\033[38;2;46;125;50m',   # Medium Green
                '\033[38;2;102;205;170m', # Medium Aquamarine
            ],
            'lights': [
                '\033[38;2;255;215;0m',   # Gold
                '\033[38;2;255;0;0m',     # Red
                '\033[38;2;0;191;255m',   # Deep Sky Blue
                '\033[38;2;255;255;255m', # White
                '\033[38;2;255;105;180m', # Hot Pink
                '\033[38;2;138;43;226m',  # Blue Violet
                '\033[38;2;255;165;0m',   # Orange
            ],
            'glow': [
                '\033[38;2;255;255;224m', # Light Yellow (glow)
                '\033[38;2;240;255;255m', # Azure (glow)
                '\033[38;2;255;250;250m', # Snow (glow)
            ],
            'star': '\033[38;2;255;223;0m',     # Golden
            'trunk': '\033[38;2;101;67;33m',     # Brown
            'shadow': '\033[38;2;80;50;20m',     # Dark Brown
            'reset': '\033[0m'
        }
        
        self.width = 50
        self.tree_structure = [
            {'rows': 4, 'start_width': 5},
            {'rows': 5, 'start_width': 7},
            {'rows': 6, 'start_width': 11},
            {'rows': 7, 'start_width': 15},
        ]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def get_tree_char(self, position, width, layer_type='body'):
        """Get appropriate character based on position"""
        if position == 0:
            return '/'
        elif position == width - 1:
            return '\\'
        else:
            return random.choice(['▲', '◆', '●', '■'])
    
    def get_ornament(self, frame, position):
        """Generate ornament with glow effect"""
        ornament_types = ['◉', '●', '◆', '★', '♦', '◈', '✦']
        
        # Create pulsing effect
        pulse = (frame + position) % 6
        
        if pulse < 2:
            color = random.choice(self.colors['glow'])
            char = random.choice(['◉', '★', '✦'])
        else:
            color = random.choice(self.colors['lights'])
            char = random.choice(ornament_types)
        
        return color + char + self.colors['reset']
    
    def draw_star(self, frame):
        """Draw animated star at top"""
        star_frames = [
            "    ✧    \n   ✧★✧   \n    ✧    ",
            "   ✧✧✧   \n  ✧ ★ ✧  \n   ✧✧✧   ",
            "  ✧   ✧  \n ✧  ★  ✧ \n  ✧   ✧  "
        ]
        
        current_star = star_frames[frame % len(star_frames)]
        star_color = self.colors['glow'][frame % len(self.colors['glow'])]
        
        lines = current_star.split('\n')
        for line in lines:
            spaces = (self.width - len(line)) // 2
            print(" " * spaces + star_color + line + self.colors['reset'])
        print()
    
    def draw_tree_layer(self, layer_config, layer_index, frame):
        """Draw a single layer of the tree"""
        rows = layer_config['rows']
        start_width = layer_config['start_width']
        
        for row in range(rows):
            current_width = start_width + (row * 2)
            spaces = (self.width - current_width) // 2
            line = ""
            
            # Build the row
            for pos in range(current_width):
                # Determine if this position gets an ornament
                ornament_chance = 0.15 if row > 1 else 0.08
                
                if random.random() < ornament_chance:
                    line += self.get_ornament(frame, pos + row)
                else:
                    # Green foliage with subtle variation
                    green_color = self.colors['green'][(frame + pos + row) % len(self.colors['green'])]
                    char = self.get_tree_char(pos, current_width)
                    line += green_color + char + self.colors['reset']
            
            print(" " * spaces + line)
        
        # Add spacing between layers for definition
        if layer_index < len(self.tree_structure) - 1:
            print()
    
    def draw_trunk(self):
        """Draw tree trunk"""
        trunk_height = 4
        trunk_width = 6
        spaces = (self.width - trunk_width) // 2
        
        for i in range(trunk_height):
            trunk_line = ""
            for j in range(trunk_width):
                # Add texture to trunk
                if j == 0 or j == trunk_width - 1:
                    color = self.colors['shadow']
                else:
                    color = self.colors['trunk']
                trunk_line += color + '█' + self.colors['reset']
            
            print(" " * spaces + trunk_line)
    
    def draw_ground(self, frame):
        """Draw ground with presents and sparkles"""
        print()
        
        # Presents
        present_colors = [
            '\033[38;2;220;20;60m',   # Crimson
            '\033[38;2;30;144;255m',  # Dodger Blue
            '\033[38;2;255;215;0m',   # Gold
            '\033[38;2;186;85;211m',  # Medium Orchid
        ]
        
        ground_line = " " * 12
        for i in range(4):
            color = present_colors[i % len(present_colors)]
            ground_line += color + "🎁 " + self.colors['reset']
            ground_line += "  " * random.randint(2, 4)
        
        print(ground_line)
        
        # Ground sparkles
        sparkle_line = ""
        sparkle_chars = ['·', '✧', '✦', '⋆', '*']
        for i in range(self.width + 15):
            if random.random() < 0.06:
                color = random.choice(self.colors['glow'] + self.colors['lights'][:3])
                char = random.choice(sparkle_chars)
                sparkle_line += color + char + self.colors['reset']
            else:
                sparkle_line += " "
        
        print(sparkle_line)
    
    def draw_message(self, frame):
        """Draw festive message"""
        messages = [
            "✨ Merry Christmas & Happy New Year! ✨",
            "🌟 Merry Christmas & Happy New Year! 🌟",
            "💫 Merry Christmas & Happy New Year! 💫",
        ]
        
        message = messages[frame % len(messages)]
        spaces = (self.width - len(message) + 15) // 2
        
        color = self.colors['lights'][frame % len(self.colors['lights'])]
        print("\n")
        print(" " * spaces + color + "═" * 45 + self.colors['reset'])
        print(" " * (spaces + 2) + message)
        
        # Creator credit
        creator_text = "Created by: Bhavesh Rathod"
        creator_spaces = (self.width - len(creator_text) + 15) // 2
        print(" " * creator_spaces + self.colors['star'] + creator_text + self.colors['reset'])
        
        print(" " * spaces + color + "═" * 45 + self.colors['reset'])
    
    def render(self, frame=0):
        """Render the complete tree"""
        self.clear_screen()
        print("\n")
        
        # Draw star
        self.draw_star(frame)
        
        # Draw tree layers
        for idx, layer in enumerate(self.tree_structure):
            self.draw_tree_layer(layer, idx, frame)
        
        # Draw trunk
        self.draw_trunk()
        
        # Draw ground decorations
        self.draw_ground(frame)
        
        # Draw message
        self.draw_message(frame)
        
        print("\n")
    
    def animate(self, duration=None):
        """Animate the tree"""
        try:
            print("\n" + "═" * 60)
            print("    🎄 Professional Christmas Tree Animation 🎄")
            print("    Press Ctrl+C to stop the animation")
            print("═" * 60 + "\n")
            time.sleep(2)
            
            frame = 0
            start_time = time.time()
            
            while True:
                self.render(frame)
                time.sleep(0.35)
                frame += 1
                
                if duration and (time.time() - start_time) > duration:
                    break
                    
        except KeyboardInterrupt:
            self.clear_screen()
            self.render(0)
            print("\n" + "═" * 60)
            print("    🎄 Thank you! Wishing you a wonderful holiday! 🎄")
            print("═" * 60 + "\n")

# Run the animation
if __name__ == "__main__":
    tree = ChristmasTree()
    tree.animate()