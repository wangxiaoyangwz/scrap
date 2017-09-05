# UnicodeEncodeError: 'ascii' codec can't encode character
  http://blog.csdn.net/jim7424994/article/details/22675759

>解决办法如下  

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')