"""
Colour Code Lookup
Estimate: 30 minutes
Actual:   28 minutes
"""

def main():
    COLOR_CODES = {
        "aliceblue": "#f0f8ff",
        "beige": "#f5f5dc",
        "cadetblue": "#5f9ea0",
        "darkgreen": "#006400",
        "firebrick": "#b22222",
        "gold": "#ffd700",
        "hotpink": "#ff69b4",
        "lightseagreen": "#20b2aa",
        "navajowhite": "#ffdead",
        "royalblue": "#4169e1"
    }

    while True:
        color_name = input("Enter a color name (or blank to stop): ").strip().lower()
        if not color_name:
            break

        color_code = COLOR_CODES.get(color_name, "Unknown")
        print(f"The color code for {color_name} is {color_code}")

if __name__ == "__main__":
    main()
