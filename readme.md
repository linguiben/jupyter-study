
http://vscode.github.net.cn/docs/python/environments  # VS Code 中的 Python 环境

此项目的内容主要是照抄或者参考了：[同济子豪兄](https://space.bilibili.com/1900783/#/)<br>

```python
1. (cmd + shift + p), 搜索 Python: Create Environment，选择python版本，vscode将开始自动创建venv
2. 激活venv, (cmd + shift + p)，搜索 python: Select Interpreter
   ** 若无法自动激活(例如使用了power shell)，则手动激活： 
   .\.venv\Srcipts\active.bat # windows
   source .venv/bin/activate
3. 激活venv后，使用pip安装依赖包: 
   pip install <package_name> 
     or pip install -r requirement.txt(若有此文件)
4. 查看已安装列表: 
    pip list
5. deactivate #退出venv

6. 生成依赖列表
   pip freeze > requirement.txt
```
