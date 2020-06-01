# find_invalid_link

language: [English Version](README_en.md)

我在 `Python3.7.5` 环境下使用 `pip` 安装了 `requests`、`requests-file`、`beautifulsoup4`。

安装 `requests-file` 是因为我要检查的 URL 是 `file:///` 形式的开头 (即 file 协议，详见
[这里](https://github.com/ZhuangZhu-74/open/tree/master/URI))。

编写这个脚本的主要原因是，当我阅读 `JMeter` 安装目录下的 `printable_docs/usermanual/component_reference.html` ，发现访问 `BeanShell_Assertion`
章节时， `Parameters` 表格 `Reset*` 行 `Desc` 列的单元格超链接错误，于是我决定编写一个脚本查看所有的html文件是否有类似的问题。

该 bug 已经上传到 [ASF Bugzilla](https://bz.apache.org/bugzilla/) ，[点击这里查看Bug的处理进度](https://bz.apache.org/bugzilla/show_bug.cgi?id=64302)。
