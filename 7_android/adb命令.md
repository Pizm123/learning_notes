* adb命令

  * 事件输入
  
  ```shell
  # 单击屏幕
  adb shell input tap [x] [y]
  # 按键
  adb shell input keyevent [key]
  # 滑动
  # 表示从屏幕坐标（100，500）开始，滑动到(100,1450)结束，整个过程耗时100ms
  adb shell input swipe 100 500 100 1450 100
  ```
  
  * keyevent表
  
  
  | 含义 |                                |
  | :--- | ------------------------------ |
  | 3    | HOME 键                        |
  | 4    | 返回键                         |
  | 5    | 打开拨号应用                   |
  | 6    | 挂断电话                       |
  | 24   | 增加音量                       |
  | 25   | 降低音量                       |
  | 26   | 电源键                         |
  | 27   | 拍照（需要在相机应用里）       |
  | 64   | 打开浏览器                     |
  | 82   | 菜单键                         |
  | 85   | 播放/暂停                      |
  | 86   | 停止播放                       |
  | 87   | 播放下一首                     |
  | 88   | 播放上一首                     |
  | 122  | 移动光标到行首或列表顶部       |
  | 123  | 移动光标到行末或列表底部       |
  | 126  | 恢复播放                       |
  | 127  | 暂停播放                       |
  | 164  | 静音                           |
  | 176  | 打开系统设置                   |
  | 187  | 切换应用                       |
  | 207  | 打开联系人                     |
  | 208  | 打开日历                       |
  | 209  | 打开音乐                       |
  | 210  | 打开计算器                     |
  | 220  | 降低屏幕亮度                   |
  | 221  | 提高屏幕亮度                   |
  | 223  | 系统休眠                       |
  | 224  | 点亮屏幕                       |
  | 231  | 打开语音助手                   |
  | 276  | 如果没有 wakelock 则让系统休眠 |
  
* ADBKeyBoard命令

  ```shell
  # 输入中文
  adb shell am broadcast -a ADB_INPUT_TEXT --es msg '你好? Hello?'
  # 切换adbKeyBoard输入法
  adb shell ime set com.android.adbkeyboard/.AdbIME 
  # 输入法列表
  adb shell ime list -a  
  # 切换其他输入法
  adb shell ime set com.google.android.inputmethod.pinyin/.PinyinIME 
  ```

* conda命令

  ```shell
  # 激活paddle_env环境
  conda activate paddle_env
  # 查看当前python的位置
  where python
  # 打包
  pyinstaller app.py
  ```
