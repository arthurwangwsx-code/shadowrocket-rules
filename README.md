# Shadowrocket Rules / 回国分流

为马来西亚使用 Shadowrocket + 中国 TXY 节点设计。**不包含任何节点凭证**。

## 订阅

- [小小优趣精准分流](https://raw.githubusercontent.com/arthurwangwsx-code/shadowrocket-rules/main/xiaoxiaoyouqu.conf)
- [中国大陆通用分流](https://raw.githubusercontent.com/arthurwangwsx-code/shadowrocket-rules/main/back-cn.conf)

在 Shadowrocket **底部「配置」** 中添加 URL（不要在首页的节点 Subscribe 中添加），选择配置后，首页选择 TXY 节点，将「全局路由」设为「配置」，开启连接。更新仓库后，在配置页面刷新下载。

## 规则范围与验证状态

`xiaoxiaoyouqu.conf` 是安全的精准分流**基础配置**：海外直连，待核验的小小优趣域名暂不强行猜测。请先在 Shadowrocket 「数据」中开启代理日志，临时使用 TXY 全局代理，分别完成启动、登录、选集、播放、拖动进度条，记录请求主机名和匹配策略，去除账号令牌和私人 IP 后再提交规则。只有验证的域名才能进入 `rules/xiaoxiaoyouqu.list`，然后同步更新主配置。未经抓包验证不承诺视频可播放。

`back-cn.conf` 为通用兜底：LAN 直连、常见海外服务直连、中国域名与大陆 IP 走 TXY、其他直连。由于 CDN 和地理定位不一定只看域名/IP，仍需实测。

## 开发

`python3 scripts/validate.py` 校验语法、兜底、敏感内容、域名重复。新增规则时先加测试再提交。规则文件按每个 App 拆分，避免无关流量进入代理。不要把节点订阅、密码、UUID、token 提交到 Git。

## 排障

如「无法订阅」，先确认使用「配置」入口、Raw URL 可在 Safari 打开、文件为纯文本 `.conf`。如 App 无法播放，查看数据日志中是否仍有 DIRECT 的视频/鉴权/CDN 域名；若均走 PROXY 仍失败，核验 TXY 中国出口 IP、DNS、账号区域和服务端限制。
