# find_invalid_link

language: [English Version](README_en.md)

我使用了Python3.7.5 并且使用pip安装了requests、requests-file、beautifulsoup4 。

编写这个脚本的主要原因是，当我阅读JMeter安装目录下的 printable_docs/usermanual/component_reference.html ，发现访问 BeanShell_Assertion
章节中 Parameters 表格 Reset* 行 Desc 列 的单元格超链接错误，于是我决定编写一个脚本查看所有的html文件是否有类似的问题。
