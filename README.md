# 过孔缝合生成器 / Via Stitching Generator (KiCad 10)

KiCad 10 可用的 PCB 铺铜区过孔缝合插件（Via Stitching），界面已汉化。

本项目是基于 [jsreynaud/kicad-action-scripts](https://github.com/jsreynaud/kicad-action-scripts) 中 `ViaStitching` 插件的兼容性分支，修复了 KiCad 10 下插件无法运行的问题，并只保留这一个工具。

## 功能

在 PCB 编辑器中为指定网络的铺铜区生成缝合过孔，支持四种排列方式：

| 排列方式 | 说明 |
|---|---|
| 矩形 | 在铺铜区内按网格放置过孔（默认） |
| 同心圆 | 沿铺铜区边界向内逐圈放置 |
| 沿轮廓 | 只沿铺铜区边界放置 |
| 沿轮廓（无孔） | 沿边界放置，忽略内部挖孔 |

生成的过孔会自动归入名为 `ViaStitching <网络名>` 的组，选中其中一个即可整组删除。

## 相对上游修复的问题

- `BOARD.GetBoardPolygonOutlines()` 在 KiCad 10 新增了必填参数 `aInferOutlineIfNecessary`，旧调用会直接抛 `TypeError`。
- 版本判断使用字符串比较（`"10.0.6" < "7"` 结果为 `True`），导致 KiCad 10 走了 KiCad 5/6 的旧代码分支。
- `GetPriority()` 已被 `GetAssignedPriority()` 取代。
- `PCB_VIA.GetWidth()` 在 KiCad 10 需要传入层参数，否则触发断言。
- 多层板使用同心圆/沿轮廓模式时错误提示 “No areas to fill”。
- 参数对话框中的 `wx.EXPAND|wx.ALIGN_RIGHT` 在 KiCad 10 的 wxWidgets 构建下触发 sizer 断言。
- 菜单名、对话框、提示与日志全部汉化。

## 从本仓库安装（KiCad PCM）

> 需要 KiCad 10.0。仓库必须能通过 HTTPS 公开访问（本仓库为 public）。

1. 打开 KiCad 的 **插件与内容管理器**（Plugin and Content Manager）。
2. 切到 **管理仓库 / Manage Repositories**。
3. 添加以下仓库地址：

   ```
   https://raw.githubusercontent.com/Cube-Line/kicad-via-stitching/main/repository.json
   ```

   > 注意：这里要填 `repository.json`，不是 `packages.json`。KiCad 要求仓库入口是一个 Repository 描述文件，`packages.json` 只是它引用的包列表。
   >
   > 如果 `raw.githubusercontent.com` 访问不畅，可改用 jsDelivr 镜像：
   >
   > ```
   > https://cdn.jsdelivr.net/gh/Cube-Line/kicad-via-stitching@main/repository.json
   > ```
   >
   > jsDelivr 有缓存（通常最长 12 小时），刚发布新版本后可能短暂看到旧版本；需要立即刷新时可访问
   > `https://purge.jsdelivr.net/gh/Cube-Line/kicad-via-stitching@main/` 清理缓存。

4. 回到 **插件 / Plugins** 标签页，找到 **Via Stitching Generator (KiCad 10)**，点击安装。
5. 重启 PCB 编辑器（pcbnew），在 **工具 → 外部插件** 或工具栏中找到 **过孔缝合生成器**。

> 如果之前安装过官方的 “Via Stitching and more tools”（来自 `kicad-action-scripts`）包，请先在 PCM 中卸载它，否则菜单里会出现两个同名工具。

## 手动安装（不使用 PCM）

1. 下载 Release 中的 `kicad-via-stitching-<版本>-pcm.zip` 并解压。
2. 把解压出的 `plugins/ViaStitching` 目录整体复制到 KiCad 的用户插件目录：
   - Windows：`%USERPROFILE%\Documents\KiCad\10.0\3rdparty\plugins\`
   - Linux：`~/.local/share/kicad/10.0/3rdparty/plugins/`
   - macOS：`~/Documents/KiCad/10.0/3rdparty/plugins/`
3. 在 `plugins/` 目录下新建（或确认存在）`__init__.py`，内容为：

   ```python
   from . import ViaStitching
   ```

4. 重启 pcbnew 或执行 **工具 → 外部插件 → 刷新插件**。

## 使用说明

1. PCB 中先画好板框，并放置好需要缝合的铺铜区（例如 GND）。
2. 打开 **过孔缝合生成器**。
3. 设置过孔铜径、钻孔、安全间距、网格间距，选择网络与排列方式。
4. 点击 **运行**。
5. 完成后按提示重新填充铺铜区（`B` 或 **编辑 → 填充所有区域**），让过孔与铜皮正确连接。

可选参数：

- **随机偏移**：轻微打散过孔位置，降低大面积铜皮因热膨胀受力集中的风险。
- **仅在选中的铺铜区内**：只处理当前选中的铺铜区。
- **忽略其他层的区域**：多层板中只考虑当前层。
- **同网络走线上也放置**：在属于同一网络的走线上也放置过孔。

## 开发与发布

生成 PCM 压缩包并刷新 `packages.json` / `repository.json`：

```bash
python3 tools/build_pcm.py
```

> 压缩包使用固定时间戳，同样内容重复构建会得到完全相同的 SHA-256，因此 `packages.json` 里的校验值不会因重新打包而失效。

发布新版本：

1. 修改 `metadata.json` 中 `versions[0].version`。
2. 运行 `python3 tools/build_pcm.py` 生成 `dist/kicad-via-stitching-<版本>-pcm.zip`，并更新 `packages.json`、`repository.json`。
3. 提交并推送（提交信息中带上版本号）。
4. 创建 tag `v<版本>` 与对应 GitHub Release。
5. 把生成的 zip 作为 Release 附件上传（文件名需与 `packages.json` 中的 `download_url` 一致）。
6. 确认 `packages.json` 中的 `download_sha256` / `download_size` / `install_size` 与附件一致后推送。

`.github/workflows/publish.yml` 会在推送 `v*` tag 时校验 `dist/` 中的压缩包与 `packages.json` 一致，然后创建 Release 并上传该文件。

## 目录结构

```
.
├── metadata.json              # 包元数据（会打进 PCM zip）
├── packages.json              # PCM 包列表（PackageArray）
├── repository.json            # PCM 仓库入口（Manage Repositories 里填这个）
├── dist/                      # 构建产物（release 附件）
├── plugins/
│   ├── __init__.py
│   └── ViaStitching/
│       ├── FillArea.py        # 核心逻辑
│       ├── FillAreaAction.py  # 插件入口
│       ├── FillAreaDialog.py  # 参数对话框
│       └── ...
└── tools/build_pcm.py         # 构建脚本
```

## 许可

原始插件版权归 JS Reynaud 所有，遵循 GPL-2.0-or-later。本分支同样以 GPL-2.0-or-later 发布，详见 [LICENSE](LICENSE)。
