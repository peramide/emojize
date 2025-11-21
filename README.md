# Emojize 📝➡️😄

A simple Python program that converts **emoji codes** (like `:thumbs_up:` or `:smile_cat:`) into their corresponding **emoji characters** (👍, 😸).
This makes it easier to type emojis on laptops and desktops using text shortcuts.

---

## 🚀 Features

* Converts emoji codes and aliases into real emojis.
* Uses the [`emoji`](https://pypi.org/project/emoji/) Python package.
* Supports both standard codes and aliases like:

  * `:thumbs_up:` → 👍
  * `:thumbsup:` → 👍
  * `:1st_place_medal:` → 🥇

---

## 📦 Installation

First, install the required dependency:

```bash
pip install emoji
```

Clone this repository:

```bash
git clone https://github.com/yourusername/emojize.git
cd emojize
```

---

## 🧠 How It Works

The program:

1. Prompts the user to enter text containing emoji codes.
2. Uses the `emoji.emojize()` function to replace recognized codes.
3. Prints the converted text.

Example code logic:

```python
import emoji

text = input("Input: ")
print("Output:", emoji.emojize(text, language='alias'))
```

---

## ▶️ Usage

Run the program:

```bash
python emojize.py
```

### Example Runs

**Input:**

```
:1st_place_medal:
```

**Output:**

```
🥇
```

**Input:**

```
:money_bag:
```

**Output:**

```
💰
```

**Input:**

```
:smile_cat:
```

**Output:**

```
😸
```

---

## 📚 Resources

* Full emoji code list with aliases:
  [https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias)
* Emoji Python module documentation:
  [https://pypi.org/project/emoji/](https://pypi.org/project/emoji/)

---

