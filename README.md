# Matrix Rain Effect

A Python script that simulates the classic "Matrix rain" effect in the terminal. This animation is achieved using Python's `curses` library.

## Features
- Generates random Japanese katakana characters that flow from top to bottom, creating a mesmerizing rain effect.
- Easy to customize and run on various operating systems with terminal support.

## Requirements
- **Python 3.x**
- **curses library** (included with Python on Linux and macOS, may require additional installation on Windows)

## Installation

### Linux / macOS
1. Clone the repository:
   
```bash
   git clone https://github.com/mahdinetk/matrix-rain-effect.git
   cd matrix-rain-effect
  ```

2. Run the script:
   
```bash
   python3 matrix-rain(1).py
  ```


### Windows
1. Install the `windows-curses` package to enable the curses library:
   
```bash
   pip install windows-curses
  ```

2. Clone the repository and run the script as above:
   
```bash
   git clone https://github.com/mahdinetk/matrix-rain-effect.git
   cd matrix-rain-effect
   python matrix-rain.py
```  


## Usage
1. Launch the script in the terminal.
2. **Do not resize the terminal window while the script is running**
3. Press `q` to exit the animation.

## Customization
- Modify the `letters` variable to change the characters used in the rain.
- Adjust the `time.sleep` interval in the main loop to change the rain speed.
