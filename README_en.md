# find_invalid_link

I used Python3.7.5 and installed `requests`, `requests-file`, `beautifulsoup4`.

Install requests-file because the URL I want to check is the beginning of the form file:/// 
(file protocol, see [here](https://tools.ietf.org/html/rfc8089)).

Write the script the main reason is that, when I read "printable_docs/usermanual/component_reference.html" under JMeter install directory, on visit "BeanShell_Assertion" section, In the "Parameters" table "Reset*" row, the cell hyperlink in the "Desc" column is wrong, so I decided to write a script to see if all the html files have similar problems.

The bug has been uploaded to [ASF Bugzilla](https://bz.apache.org/bugzilla/), [click here](https://bz.apache.org/bugzilla/show_bug.cgi?id=64302) to view the progress of the bug.
