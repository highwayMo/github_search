# git_search

受到[weixiao9188/wechat_push: 利用微信推送CVE-2020 (github.com)](https://github.com/weixiao9188/wechat_push)该项目的启发动手改了改符合了个人的使用需求

## 如何使用

这是一个**命令行**工具，引用了简洁的**click**模块。

使用`--help`命令输出帮助信息

```
python github_search.py --help
Usage: github_search.py [OPTIONS]

Options:
  -p, --page TEXT  Number of messages
  -k, --keys TEXT  Key for message  [required]
  --help           Show this message and exit.

```

仅仅**2**个**简单**的选项

`page`选项提供 `all` 参数，传递**all**参数将搜索该**key**的所有**message**

``` 
python git_search.py -p all -k A
```

`keys`选项的参数可以传递多次，同时记录每次的值而不是只记录最后一个值。

```
python git_search.py -p 5 -k A -k B
```

搜索结束，所有的信息将会输出在**终端**上，并存入该**key**命名的**csv**文件，仅保存从未搜索过的结果。

## 更新

因为在使用中发现自己并不是每次都想保存到**csv**中，有时仅仅想搜索🔍而已。所以增添一个保存选项。

同样通过`--help`命令输出帮助信息

```
>python github_search.py --help
Usage: github_search.py [OPTIONS]

Options:
  -p, --page TEXT              Number of messages
  -k, --keys TEXT              Key for message  [required]
  -s, --save / -ns, --no-save  Save scv
  --help                       Show this message and exit.
```

新选项`save/no-save`非常的简单，默认是`no-save` 。如果需要保存至该**key**命名的**csv**文件中，在最后输入`-s`选项即可。

```
python github_search.py -p 3 -k A -k B -s
```

