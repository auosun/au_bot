# au_bot
auosun's bot  
https://t.me/auosun_bot
## 功能
1. 语音转文字
2. 动漫化图片
3. 一言名言

## 添加机器人提示：
```BotFather
help - something Au can do 
voice - how to use Voice to Text
```

## 安装教程：
```
conda install paddlepaddle==1.8.5 -c paddle
pip install paddlehub
```

## 更新日志：
### 1.0.3
1. 删除大量不再使用功能，保留 **语音转文字** 功能 并优化体验 （12-10)
2. 增加 **漫画化图片** 功能；漫画化目前可转化多种风格：新海诚，宫崎骏，今敏小辣椒 (day 12)  
   优化转换速度,开启GPU （day 13
3. 增加 **垃圾清理** ；可直接输入指令 `/trash` 管理员可用 (12-13)
4. 增加 **一言名言** ；`/quoto` 可调用一言接口获取名人名言
5. 增加 **功能开关** ；功能可以在config文件中选择是否调用 (12-22)

### Future
1. **一言名言** 可以配合 `/quoto` 增加更多可选类型 (12-22)
2. **漫画化图片** 多线程调用；不再影响机器人继续工作 (12-22)
----
<details>
  <summary> 旧版本 </summary>

   已经搁置分支 old-version
   #### 1.0.1
   1. 功能开发 语音转文字 （4/5）
   2. 增加错误反馈   
   3. 添加测试机器人 
   4. 功能开发 代理分发 (4/6)
   #### 1.0.2
   1. 增加 某2ray api接口
   2. 设置 某2ray和bot之间的绑定 (5/12)

</details>

----
## 感谢
1. 百度云免费语音识别api
2. paddlehub开源项目：https://github.com/PaddlePaddle/PaddleHub
3. 一言：https://hitokoto.cn/

