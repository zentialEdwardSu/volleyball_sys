# volleyball_sys
Front end and backend of the volleybal system



**backend**

```bash
backend/
```

> 使用flask进行推流

`app.py`后端的主函数

`start.py`启动

`stop.py`停止

`video_input.py`配置视频路径

**frontend**

```bash
frontend/
```

> 使用Vite+Vue3+Ts+element-plus 开发的前端框架

`views/workbench/index.vue` 主窗口

`components/sidebar/index.vue`侧边栏



**后端启动方法**

安装依赖

```bash
pip install -r requirements.txt
```



配置视频路径



启动服务

```bash
python app.py
```



**前端启动方式**

安装依赖

```bash
npm install
```



启动开发服务器

```bash
npm run dev
```





**使用**

启动前端和后端之后,访问前端网页



点击`command input`键入 `python start.py`以启动

​												键入`python stop.py`以停止



> 请注意 目前前端显示部分存在问题,并不能实时响应,需点击启用或者禁用流的按钮进行刷新
>
> 同时后端推送也存在问题不能实现实时的停止



