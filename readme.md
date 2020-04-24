English | [简体中文](readme_zh-CN.md)

# QssStylesheetEditor

[![Build Status](https://api.travis-ci.com/hustlei/QssStylesheetEditor.svg?branch=master)](https://travis-ci.com/hustlei/QssStylesheetEditor)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/220d511b3ab146d0b03fef0245e00525)](https://www.codacy.com/manual/hustlei/QssStylesheetEditor?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hustlei/QssStylesheetEditor&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/hustlei/QssStylesheetEditor/badge.svg?branch=master)](https://coveralls.io/github/hustlei/QssStylesheetEditor?branch=master)
[<img alt="Platform:win|osx|linux" src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/badge/platform.svg?sanitize=true" onerror="this.src='https://hustlei.github.io/assets/badge/platform.svg';this.onerror=null" />](https://travis-ci.com/hustlei/QssStylesheetEditor)

<br>

QssStylesheetEditor is a powerful qt stylesheet(QSS) editor.
Real-time preview, automatically completion, and user can define custom variables.


> **Now I want to change a new name for QssStylesheetEditor, welcome everyone to vote: <https://github.com/hustlei/QssStylesheetEditor/issues/4>**


# screenshot

![GUI(v1.5) screeshot](https://hustlei.github.io/software/QssStylesheetEditor/screenshot/en/QssStylesheetEditor_v1.5.png  "GUI(v1.5)")

# Features

+ Qss code highlight and code folding
+ Automatic completion
+ In-time preview
+ Almost all of the qtwidgets can be previewed
+ Customize variables and reference in Qss
+ Change variable color through color dialog box
+ Reference image by relative path
+ Reference image in resource files
+ Switch different system themes (xp, vista etc.)
+ Internationalization
  + Now Chinese and English translations are available

# Platform

+ Windows (maybe won't run on xp)
+ macOS
+ Linux
+ UNIX


# Usage

Follow the steps as below, or install the binary installation package:

1. download [QssStylesheetEditor-1.6-py3-none-any.whl](https://github.com/hustlei/QssStylesheetEditor/releases)
2. run `pip install QssStylesheetEditor-1.6-py3-none-any.whl` install QssStylesheetEditor
3. run `qsseditor` or `QssStylesheetEditor` the app will started

If you are windows 64bit user, binary package and installer is available now.

+ [QssStylesheetEditor1.6_win64_installer.exe](https://github.com/hustlei/QssStylesheetEditor/releases)
+ QssStylesheetEditor1.6_win64_portable.7z [[Download]](https://pan.baidu.com/s/1d8QJH6EbGcZXi7GjbkPlsQ) (security code: j7fc)


> Alternatively, manually install the package is ok too
> 
>> 1. install python3: following <http://python.org/>
>> 2. install dependencies:
>>     - preimport: `pip install preimport`
>>     - tomlconfig: `pip install tomlconfig`
>>     - CodeEditor: `pip install CodeEditor`
>> 3. download and unzip package:
>>     + download [QssStylesheetEditor_v1.6.zip](https://github.com/hustlei/QssStylesheetEditor/releases)
>>     + unzip and change dir to QssStylesheetEditor_v1.6 `cd QssStylesheetEditor_v1.6`
>> 4. Run QssStylesheetEditor:
>>     + double click qsseditor.pyw
>>     + or run `python qsseditor.pyw`


## Using custom variable 

In QssStylesheetEditor, users can define and use custom variables in QSS. 

Using following statement to define new variable:

~~~js
/*example of custom variable definition*/
$background = #fff;  /* define var with name "background" */
$text = red; /* define var with name "text" */
~~~

A variable definition end with a ";".

Reference defined variable as following:

~~~css
/* example of custom variable reference */
QWidget
{
    color: $text; /* reference variable text*/
    background-color: $background; /* reference variable background*/
}
~~~


Users can export the code to qss file without vars by the "File>Export" menu.


**Variable Color pick dialog**

When a variable is defined in QssStylesheetEditor, the variable will be automatically displayed in the color pannel. You can click the color button to select the variable color through the color pick-up box.

<img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/ColorDlg_v1.3.png" style="max-height:480px;max-width:960px"/>

> If an undefined variable is referenced, it will be automatically recognized and displayed in the color panel too. 

## Image reference path

When images are use in the qss code, if the url is relative,  QssStylesheetEditor will find the image file in the folder where the qss code file is.

~~~css
background-image: url("img/close.png");
/* the img folder must be in the same directory of the qss code file*/
~~~


## image in resource file

If your image files is converted to resource file by pyrcc5(pyrcc5 xxx.qrc -o xxxresource.py).

You can reference images in the resource file as following:

~~~css
background-image: url(":/img/close.png");
~~~

QssStylesheetEditor will search the resource file filename.py(filename must be same of qss file) in the directory of the currently opened qss stylesheet code file and loads it automatically.

# screenshot

<div><span><b>AutoComplete</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/AutoComplete.png" alt="AutoComplete" style="max-height:480px;max-width:960px"/>

<div><span><b>QssStylesheetEditor on macOS</b></span></div>
    <img src="https://hustlei.github.io/software/QssStylesheetEditor/screenshot/en/QssStylesheetEditor_mac_v1.5.png" alt="Gui on macOS" style="max-height:480px;max-width:960px"/>

<div><span><b>QssStylesheetEditor GUI V1.2</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/QssStylesheetEditor_v1.2.png" alt="v1.2" style="max-height:480px;max-width:960px"/>
<div><span><b>QssStylesheetEditor GUI V1.0</b></span></div>
    <img src="https://raw.githubusercontent.com/hustlei/QssStylesheetEditor/master/docs/assets/screenshot/QssStylesheetEditor_v1.0.png" alt="v1.0" style="max-height:480px;max-width:960px"/>


# License
You can use this software for free in open source projects that are licensed under the GPL. but there is an exception: if you only use it to generate qss file for commercial product, the product's source code can be shipped with whatever license you want.

If you don't want to open your code up to the public, you can purchase a commercial license for USD 10 per developer, and also should purchase a commercial license for PyQt5.
