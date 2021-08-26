# Bored of your terminal? Try some :mage_man: **Magic**

> ## What is **Magic** ?
>
> **Magic** is a tool that styles your terminal.

> ## How does it work?
>
> Basically it wraps your text with specific codes that tells the terminal to style this text.

> ## Why would I use it?
>
> Well just think how many times you've changed your terminal theme in the past. And how sick of it you're that you're searching for such thing in the first place. :laughing:

# Alright enough of the FAQs lets talk code!

## <span style="font-size:medium">class</span> **<span style="color:orangeRed">Style</span>**

> - #### **<span style="color:#009dff">default</span>**
> - #### **<span style="color:#009dff">bright</span>**
> - #### **<span style="color:#009dff">underlined</span>**
> - #### **<span style="color:#009dff">blinking</span>**
> - #### **<span style="color:#009dff">fixed_color</span>**

## <span style="font-size:medium">class</span> **<span style="color:orangeRed">Color</span>**

> - #### **<span style="color:#009dff">black</span>**
> - #### **<span style="color:#009dff">red</span>**
> - #### **<span style="color:#009dff">green</span>**
> - #### **<span style="color:#009dff">yellow</span>**
> - #### **<span style="color:#009dff">blue</span>**
> - #### **<span style="color:#009dff">magenta</span>**
> - #### **<span style="color:#009dff">cyan</span>**
> - #### **<span style="color:#009dff">white</span>**
> - #### **<span style="color:#009dff">reset</span>**

## <span style="font-size:medium">class</span> **<span style="color:orangeRed">Highlight</span>**

> - #### **<span style="color:#009dff">black</span>**
> - #### **<span style="color:#009dff">red</span>**
> - #### **<span style="color:#009dff">green</span>**
> - #### **<span style="color:#009dff">yellow</span>**
> - #### **<span style="color:#009dff">blue</span>**
> - #### **<span style="color:#009dff">magenta</span>**
> - #### **<span style="color:#009dff">cyan</span>**
> - #### **<span style="color:#009dff">white</span>**

---

## <span style="font-size:medium">class</span> **<span style="color:orangeRed">Print</span>**

- ### **<span style="color:#009dff">text</span>** - This allows you to print styled text with some extra values.

```py
 Print.text(
   text = "This is an example for Print.text",
   style = Style.bold,
   color = Color.green,
   end_with_new_line = True)
```

> **Output: <span style="color:green">This is an example for Print.text</span>**

- ### **<span style="color:#009dff">type</span>** - This prints the text with a style based on their value type.

```py
Print.type(420)
```

> **Output: <span style="color:#035096">420</span>**

## <span style="font-size:medium">class</span> **<span style="color:orangeRed">Get</span>**

- ### **<span style="color:#009dff">styled_text</span>** - This returns a string of text with the specified style.

```py
styled_text = Get.styled_text(
    text = "This is a test for styled_text",
    style = Style.bright,
    color = Color.magenta
)

print(styled_text)
```

> **Output: <span style="color:magenta">This is a test for styled_text</span>**

- ### **<span style="color:#009dff">layout</span>** - This returns the style code of a style.

```py
layout = Get.layout(
    style = Style.underlined,
    color = Color.red,
    highlight = Highlight.green
)

print(layout + "This is a test for layout" + Color.reset)
```

> **Output: <mark style="background-color:green; color:red; text-decoration: underline">This is a test for layout</mark>**
