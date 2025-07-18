![Demo]([dog_task_bar.mp4)](https://drive.google.com/file/d/1gETpoxtaAzy1ympYuKl4NDCrPNnAe4st/view?usp=drive_link))

# 🐶 Desktop Dog for Windows

An animated dog that sits just above your Windows taskbar and **runs whenever you move your mouse!**

This little friend is inspired by the Google Dino but designed to **idle peacefully** and spring to life with cute run animations when your mouse moves.

---

## 🚀 Features

- 🐾 Always visible — even when the taskbar is not transparent.
- 📍 Fixed position at bottom-left of the screen.
- 🏃‍♂️ Dog runs when mouse moves.
- 🛑 Static dog when mouse is still.
- 🔄 Runs **automatically at every system startup** (if enabled).
- 😌 No console window or taskbar clutter.

---

## 📸 Preview

| Idle | Running |
|------|---------|
| ![idle-dog](dog_idle.gif) | ![run-dog](dog_run.gif) |

---

## 📁 Folder Structure

```
desktop-dog/
├──idle.gif
├── run.gif
├── desktop_dog.py
├── README.md
```

---

## 💻 Requirements

- Python 3.8+
- `PyQt5`
- `pyautogui`

### Install dependencies:
```bash
pip install pyqt5 pyautogui
```

---

## ▶️ Run Manually

```bash
pythonw desktop_dog.py
```

> Use `pythonw` to run without a console window.

---

## 🧠 Autostart on Windows

To launch the dog automatically every time you boot:

### Step 1: Open Startup Folder

Press `Win + R` and type:
```
shell:startup
```

### Step 2: Add a Shortcut

Right-click → **New → Shortcut**

**Target:**
```bash
pythonw "C:\Full\Path\To\desktop_dog.py"
```

Or if using `.exe`:
```bash
"C:\Full\Path\To\desktop_dog.exe"
```

Save the shortcut inside the Startup folder.

---

## 🔧 Convert to `.exe` (Optional)

To run on any Windows PC without Python installed:

### Install PyInstaller:
```bash
pip install pyinstaller
```

### Build executable:
```bash
pyinstaller --noconsole --onefile desktop_dog.py
```

- The final `.exe` will be in the `dist/` folder.

---

## 🙋‍♂️ Credits & Notes

- Developed by **Prajwal P**.
- Inspired by YouTube :[ mewtru](https://www.youtube.com/@mewtru)

---

