# Taobao Flash Buy | 淘宝自动抢单工具

English | [简体中文](README.md)

> **⚠️ Maintenance Status: ARCHIVED**
>
> This project is no longer maintained. This means:
> - No new features will be added
> - No bugs will be fixed
> - No dependency updates will be made
> - No issues or pull requests will be addressed
>
> You can still use and fork this project, but do so at your own risk.

A Python-based automatic purchase tool for Taobao, featuring a PyQt5 GUI interface that supports timed automatic purchasing of items in your shopping cart.

## Features

- Graphical user interface for easy operation
- Scheduled automatic purchase functionality
- Automatic selection of all items in shopping cart
- Voice prompt features for clear operation guidance
- Automated login, checkout, and order submission process

## Tech Stack

- Python 3.x
- PyQt5 + Qt Designer
- Selenium WebDriver
- pyttsx3 for voice synthesis

## Requirements

- Python 3.x
- Chrome Browser
- ChromeDriver (must match your Chrome browser version)
- Required Python packages:
  - PyQt5
  - selenium
  - pyttsx3

## Installation

1. Clone or download this project
2. Install required Python packages:

```bash
pip install PyQt5 selenium pyttsx3
```

3. Download ChromeDriver matching your Chrome browser version
4. Place ChromeDriver in the correct directory (default: D:\python)

## Usage

1. Run `GuiMain.py` to start the program
2. Set the purchase time in the interface
3. The program will automatically open Taobao website and prompt for login
4. Complete Taobao account login within 15 seconds
5. Program will automatically navigate to the shopping cart page
6. When the set time is reached, the program will execute the purchase process

## Important Notes

- Ensure desired items are added to cart before using
- Test ChromeDriver functionality beforehand
- Login must be completed within the specified time
- This tool is for educational and research purposes only
- Please comply with Taobao platform rules and terms when using

## Project Structure

```
├── GuiMain.py        # Main program entry
├── gui.py           # GUI implementation
├── gui.ui          # Qt Designer interface file
├── chromedriver.exe # Chrome browser driver
└── README.md       # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feedback and feature suggestions are welcome. If you'd like to contribute code:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## Disclaimer

This tool is for educational and research purposes only. Users bear all responsibility for any consequences of using this tool. Please ensure your usage complies with Taobao platform rules and terms.
