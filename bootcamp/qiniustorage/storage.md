编写自定义存储系统¶
如果你需要提供自定义文件存储 – 一个普遍的例子是在某个远程系统上储存文件 – 你可以通过定义一个自定义的储存类来实现。你需要遵循以下步骤：

1. 你的自定义储存类必须是django.core.files.storage.Storage的子类：

from django.core.files.storage import Storage

class MyStorage(Storage):
    ...
2. Django必须能够不带任何参数来实例化你的储存类。这意味着任何设置都应该从django.conf.settings中获取。

```python
from django.conf import settings
from django.core.files.storage import Storage

class MyStorage(Storage):
    def __init__(self, option=None):
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS
        ...
```
3. 你的储存类必须实现 _open() 和 _save()方法，以及任何适合于你的储存类的其它方法。更多这类方法请见下文。

另外，如果你的类提供本地文件存储，它必须覆写path()方法。

4. 你的储存类必须是 可以析构的，所以它在迁移中的一个字段上使用的时候可以被序列化。只要你的字段拥有自己可以序列化的参数，你就可以为它使用django.utils.deconstruct.deconstructible类装饰器（这也是Django用在FileSystemStorage上的东西）。

默认情况下，下面的方法会抛出NotImplementedError异常，并且必须覆写它们。

+ Storage.delete()
+ Storage.exists()
+ Storage.listdir()
+ Storage.size()
+ Storage.url()
然而要注意，并不是这些方法全部都需要，可以故意省略一些。可以不必实现每个方法而仍然能拥有一个可以工作的储存类。

比如，如果在特定的储存后端中，列出内容的开销比较大，你可以决定不实现Storage.listdir。

另一个例子是只处理写入文件的后端。这种情况下，你不需要实现上面的任意一种方法。

根本上来说，需要实现哪种方法取决于你。如果不去实现一些方法，你会得到一个不完整（可能是不能用的）的接口。

你也会经常想要使用特意为自定义储存对象设计的钩子。它们是：

_open(name, mode='rb')¶
必需的。

被Storage.open()调用，这是储存类用于打开文件的实际工具。它必须返回File对象，在大多数情况下，你会想要返回一些子类，它们实现了后端储存系统特定的逻辑。

_save(name, content)¶
被Storage.save()调用。name必须事先通过get_valid_name() 和 get_available_name()过滤，并且content自己必须是一个File对象。

应该返回被保存文件的真实名称（通常是传进来的name，但是如果储存需要修改文件名称，则返回新的名称来代替）。

get_valid_name(name)¶
返回适用于当前储存系统的文件名。传递给该方法的name参数是发送给服务器的原始文件名称，并移除了所有目录信息。你可以覆写这个方法，来自定义非标准的字符将会如何转换为安全的文件名称。

Storage提供的代码只会保留原始文件名中的数字和字母字符、英文句号和下划线，并移除其它字符。

get_available_name(name, max_length=None)¶
返回在储存系统中可用的文件名称，可能会顾及到提供的文件名称。传给这个方法的name参数需要事先过滤为储存系统有效的文件名称，根据上面描述的get_valid_name() 方法。

如果提供了max_length，文件名称长度不会超过它。如果不能找到可用的、唯一的文件名称，会抛出SuspiciousFileOperation 异常。

如果name命名的文件已存在，一个下划线加上随机7个数字或字母的字符串会添加到文件名称的末尾，扩展名之前。

Changed in Django 1.7:
之前，下划线和一位数字（比如"_1", "_2"，以及其他）会添加到文件名称的末尾，直到目标目录中发现了可用的名称。一些恶意的用户会利用这一确定性的算法来进行dos攻击。 这一变化也在1.6.6， 1.5.9， 和 1.4.14中出现。
Changed in Django 1.8:
新增了max_length参数。