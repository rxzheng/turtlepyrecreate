import subprocess

def get_fonts():
    try:
        result = subprocess.run(['fc-list'], capture_output=True, text=True)
        output = result.stdout
        fonts = [line.split(":")[0] for line in output.splitlines()]
        return fonts
    except Exception as e:
        print(f"Error: {e}")
        return []

# Print the list of available fonts on macOS
fonts = get_fonts()
for font in fonts:
    print(font)

