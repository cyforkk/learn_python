# 文件夹整理器（file-organizer）

对应规格：`stage-5-projects/exercises/project_spec_02_file_organizer.md`

## 警告

**不要**直接对系统重要目录（桌面全部文件、下载文件夹整盘等）使用 `--apply`。  
先复制一份测试目录，确认 dry-run 结果再执行。

## 运行

```bash
cd projects/file-organizer

# 仅预览（安全）
python organizer.py path/to/test_folder

# 真正移动
python organizer.py path/to/test_folder --apply
```

## 规则

| 扩展名 | 目标子目录 |
|--------|------------|
| jpg/png/gif/webp… | `images/` |
| pdf/doc/txt/md/csv… | `docs/` |
| 其他或无扩展名 | `others/` |

## 自测示例

```bash
mkdir demo_src
echo hi > demo_src/a.txt
echo x > demo_src/b.png
python organizer.py demo_src
python organizer.py demo_src --apply
```
