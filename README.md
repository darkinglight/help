find backend api common -name "*.php" -exec 'cat' {} \; > tmp.txt
／／批量插入配置文件
sed -i "45i \    location ^~/active {\n\
        alias /data/www/paydayloan-active/dist;\n\
    }\n\
    location = /active/.*/index.html {\n\
        alias /data/www/paydayloan-active/dist/index.html;\n\
        add_header Cache-Control no-store;\n\
    }" /usr/local/services/nginx/conf/sites-available/www.tengqiaotech.com.conf
sed -n '44,60p' /usr/local/services/nginx/conf/sites-available/www.tengqiaotech.com.conf


http://www.jianshu.com/p/e0139fe4a1f1  //坦克大战

http://blog.csdn.net/miao0916/article/details/59113489  swoole websocket 弹幕

1. Webbench
　　Webbench是一个在linux下使用的非常简单的网站压测工具。它使用fork()模拟多个客户端同时访问我们设定的URL，测试网站在压力下工作的性能，最多可以模拟3万个并发连接去测试网站的负载能力。Webbench使用C语言编写, 代码实在太简洁，源码加起来不到600行。
　　下载链接：http://home.tiscali.cz/~cz210552/webbench.html
　　2. Tinyhttpd
　　tinyhttpd是一个超轻量型Http Server，使用C语言开发，全部代码只有502行(包括注释)，附带一个简单的Client，可以通过阅读这段代码理解一个 Http Server 的本质。
　　下载链接：http://sourceforge.net/projects/tinyhttpd/
　　3. cJSON
　　cJSON是C语言中的一个JSON编解码器，非常轻量级，C文件只有500多行，速度也非常理想。
　　cJSON也存在几个弱点，虽然功能不是非常强大，但cJSON的小身板和速度是最值得赞赏的。其代码被非常好地维护着，结构也简单易懂，可以作为一个非常好的C语言项目进行学习。
　　项目主页: http://sourceforge.net/projects/cjson/
　　4. CMockery
　　cmockery是google发布的用于C单元测试的一个轻量级的框架。它很小巧，对其他开源包没有依赖，对被测试代码侵入性小。cmockery的源代码行数不到3K，你阅读一下will_return和mock的源代码就一目了然了。
　　主要特点：
　　免费且开源，google提供技术支持；
　　轻量级的框架，使测试更加快速简单；
　　避免使用复杂的编译器特性，对老版本的编译器来讲，兼容性好;
　　并不强制要求待测代码必须依赖C99标准，这一特性对许多嵌入式系统的开发很有用
　　下载链接：http://code.google.com/p/cmockery/downloads/list
　　5. Libev
　　libev是一个开源的事件驱动库，基于epoll，kqueue等OS提供的基础设施。其以高效出名，它可以将IO事件，定时器，和信号统一起来，统一放在事件处理这一套框架下处理。基于Reactor模式，效率较高，并且代码精简（4.15版本8000多行），是学习事件驱动编程的很好的资源。
　　下载链接：http://software.schmorp.de/pkg/libev.html
　　6. Memcached
　　Memcached 是一个高性能的分布式内存对象缓存系统，用于动态Web应用以减轻数据库负载。它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提供动态数据库驱动网站的速度。Memcached 基于一个存储键/值对的 hashmap。Memcached-1.4.7的代码量还是可以接受的，只有10K行左右。
　　下载地址：http://memcached.org/
　　7. Lua
　　Lua很棒，Lua是巴西人发明的，这些都令我不爽，但是还不至于脸红，最多眼红。
　　让我脸红的是Lua的源代码，百分之一百的ANSI C，一点都不掺杂。在任何支持ANSI C编译器的平台上都可以轻松编译通过。我试过，真是一点废话都没有。Lua的代码数量足够小，5.1.4仅仅1.5W行，去掉空白行和注释估计能到1W行。
　　下载地址：http://www.lua.org/
　　8. SQLite
　　SQLite是一个开源的嵌入式关系数据库，实现自包容、零配置、支持事务的SQL数据库引擎。 其特点是高度便携、使用方便、结构紧凑、高效、可靠。足够小，大致3万行C代码，250K。
　　下载地址：http://www.sqlite.org/ 。
　　9. UNIX v6
　　UNIX V6 的内核源代码包括设备驱动程序在内 约有1 万行，这个数量的源代码，初学者是能够充分理解的。有一种说法是一个人所能理解的代码量上限为1 万行，UNIX V6的内核源代码从数量上看正好在这个范围之内。看到这里，大家是不是也有“如果只有1万行的话没准儿我也能学会”的想法呢？
　　另一方面，最近的操作系统，例如Linux 最新版的内核源代码据说超过了1000 万行。就算不是初学者，想完全理解全部代码基本上也是不可能的。
　　下载地址：http://minnie.tuhs.org/cgi-bin/utree.pl?file=V6
　　10. NETBSD
　　NetBSD是一个免费的，具有高度移植性的UNIX-like操作系统，是现行可移植平台最多的操作系统，可以在许多平台上执行，从64bit alpha服务器到手持设备和嵌入式设备。NetBSD计划的口号是：”Of course it runs NetBSD”。它设计简洁，代码规范，拥有众多先进特性，使得它在业界和学术界广受好评。由于简洁的设计和先进的特征，使得它在生产和研究方面，都有卓越的表现，而且它也有受使用者支持的完整的源代码。许多程序都可以很容易地通过NetBSD Packages Collection获得。



值得推荐的C/C++框架和库
 发表于 2014-12-13 |  分类于 c/c++ | 
 Webbench是一个在linux下使用的非常简单的网站压测工具。它使用fork()模拟多个客户端同时访问我们设定的URL，测试网站在压力下工作的性能，最多可以模拟3万个并发连接去测试网站的负载能力。Webbench使用C语言编写, 代码实在太简洁，源码加起来不到600行。
 值得学习的C语言开源项目
 Libevent

 libev是一个开源的事件驱动库，基于epoll，kqueue等OS提供的基础设施。其以高效出名，它可以将IO事件，定时器，和信号统一起来，统一放在事件处理这一套框架下处理。基于Reactor模式，效率较高，并且代码精简（4.15版本8000多行），是学习事件驱动编程的很好的资源。

 下载链接：https://github.com/libevent/libevent

 Memcached

 Memcached 是一个高性能的分布式内存对象缓存系统，用于动态Web应用以减轻数据库负载。它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提供动态数据库驱动网站的速度。Memcached 基于一个存储键/值对的 hashmap。Memcached-1.4.7的代码量还是可以接受的，只有10K行左右。
 下载地址：http://memcached.org/

 Redis

 Redis 是一个使用 C 语言写成的，开源的 key-value 数据库。Redis支持的操作和数据类型比Memcached要多，现在主要用于缓存，支持主从同步机制，Redis的学习可以参考<>一书。

 下载地址：http://redis.io/

 Webbench

 Webbench是一个在linux下使用的非常简单的网站压测工具。它使用fork()模拟多个客户端同时访问我们设定的URL，测试网站在压力下工作的性能，最多可以模拟3万个并发连接去测试网站的负载能力。Webbench使用C语言编写, 代码实在太简洁，源码加起来不到600行。

 下载链接：https://github.com/LippiOuYang/WebBenchl

 APR（Apache Portable Runtime）

 这是由 Apache 社区维护的 C 开源库，主要提供操作系统相关的功能（文件系统、进程、线程、用户、IPC）。此外还提供了一些网络相关的功能。

 APR 原先是 Apache Web 服务器的一个组成部分，后来独立出来，成为一个单独的开源项目。
 主页：https://apr.apache.org

 NGINX

 Nginx是由俄罗斯软件工程师Igor Sysoev开发的一个高性能的HTTP和反向代理服务器，具备IMAP/POP3和SMTP服务器功能。Nginx最大的特点是对高并发的支持和高效的负载均衡，在高并发的需求场景下，是Apache服务器不错的替代品。目前，包括新浪、腾讯等知名网站已经开始使用Nginx作为Web应用服务器。
 主页：http://nginx.org/en/download.html

 Tinyhttpd

 tinyhttpd是一个超轻量型Http Server，使用C语言开发，全部代码只有502行(包括注释)，附带一个简单的Client，可以通过阅读这段代码理解一个 Http Server 的本质。

 下载链接：https://github.com/LippiOuYang/Tinyhttpd

 cJSON

 cJSON是C语言中的一个JSON编解码器，非常轻量级，C文件只有500多行，速度也非常理想。
 cJSON也存在几个弱点，虽然功能不是非常强大，但cJSON的小身板和速度是最值得赞赏的。其代码被非常好地维护着，结构也简单易懂，可以作为一个非常好的C语言项目进行学习。

 项目主页:http://sourceforge.net/projects/cjson/

 CMockery

 cmockery是google发布的用于C单元测试的一个轻量级的框架。它很小巧，对其他开源包没有依赖，对被测试代码侵入性小。cmockery的源代码行数不到3K，你阅读一下will_return和mock的源代码就一目了然了。
 主要特点：

 免费且开源，google提供技术支持；
 轻量级的框架，使测试更加快速简单；
 避免使用复杂的编译器特性，对老版本的编译器来讲，兼容性好;
 并不强制要求待测代码必须依赖C99标准，这一特性对许多嵌入式系统的开发很有用
 下载链接：http://code.google.com/p/cmockery/downloads/list

 Lua

 Lua很棒，Lua是巴西人发明的，这些都令我不爽，但是还不至于脸红，最多眼红。
 让我脸红的是Lua的源代码，百分之一百的ANSI C，一点都不掺杂。在任何支持ANSI C编译器的平台上都可以轻松编译通过。我试过，真是一点废话都没有。Lua的代码数量足够小，5.1.4仅仅1.5W行，去掉空白行和注释估计能到1W行。
 下载地址：http://www.lua.org/

 SQLite

 SQLite是一个开源的嵌入式关系数据库，实现自包容、零配置、支持事务的SQL数据库引擎。 其特点是高度便携、使用方便、结构紧凑、高效、可靠。足够小，大致3万行C代码，250K。
 下载地址：http://www.sqlite.org/ 。

 UNIX v6

 UNIX V6 的内核源代码包括设备驱动程序在内 约有1 万行，这个数量的源代码，初学者是能够充分理解的。有一种说法是一个人所能理解的代码量上限为1 万行，UNIX V6的内核源代码从数量上看正好在这个范围之内。看到这里，大家是不是也有“如果只有1万行的话没准儿我也能学会”的想法呢？
 另一方面，最近的操作系统，例如Linux 最新版的内核源代码据说超过了1000 万行。就算不是初学者，想完全理解全部代码基本上也是不可能的。

 下载地址：http://minnie.tuhs.org/cgi-bin/utree.pl?file=V6

 NETBSD

 NetBSD是一个免费的，具有高度移植性的 UNIX-like 操作系统，是现行可移植平台最多的操作系统，可以在许多平台上执行，从 64bit alpha 服务器到手持设备和嵌入式设备。NetBSD计划的口号是：”Of course it runs NetBSD”。它设计简洁，代码规范，拥有众多先进特性，使得它在业界和学术界广受好评。由于简洁的设计和先进的特征，使得它在生产和研究方面，都有卓越的表现，而且它也有受使用者支持的完整的源代码。许多程序都可以很容易地通过NetBSD Packages Collection获得。

 下载地址：http://www.netbsd.org/

 值得学习的C++开源项目
 LevelDb

 LevelDb是谷歌两位大神级别的工程师发起的开源项目，简而言之，LevelDb是能够处理十亿级别规模Key-Value型数据持久性存储的C++ 程序库。
 它是一个持久化存储的KV系统，和Redis这种内存型的KV系统不同，LevelDb不会像Redis一样狂吃内存，而是将大部分数据存储到磁盘上。
 　　其次，LevleDb在存储数据时，是根据记录的key值有序存储的，就是说相邻的key值在存储文件中是依次顺序存储的，而应用可以自定义key大小比较函数，LevleDb会按照用户定义的比较函数依序存储这些记录。

 主页:https://github.com/google/leveldb

 Boost.Asio

 它是异步输入输出的核心。 名字本身就说明了一切：Asio 意即异步输入/输出。该库可以让 C++ 异步地处理数据，且平台独立。异步数据处理就是指，任务触发后不需要等待它们完成。相反，Boost.Asio 会在任务完成时触发一个应用。异步任务的主要优点在于，在等待任务完成时不需要阻塞应用程序，可以去执行其它任务。

 异步任务的典型例子是网络应用。如果数据被发送出去了，比如发送至 Internet，通常需要知道数据是否发送成功。 如果没有一个象 Boost.Asio 这样的库，就必须对函数的返回值进行求值。但是，这样就要求待至所有数据发送完毕，并得到一个确认或是错误代码。而使用 Boost.Asio，这个过程被分为两个单独的步骤：第一步是作为一个异步任务开始数据传输。 一旦传输完成，不论成功或是错误，应用程序都会在第二步中得到关于相应的结果通知.主要的区别在于，应用程序无需阻塞至传输完成，而可以在这段时间里执行其它操作。

 主页：http://www.boost.org/doc/libs/1_58_0/doc/html/boost_asio.html

 SGI STL

 SGI STL是STL代码的经典实现版本，虽然很多编译器不直接使用这个版本，但是很多却在此基础之上进行改进的。比如GNU C++的标准库就是在此基础之上改进的。这份代码还有一个好处是有注释，代码书写非常规范，只要花些时间读懂它并非难事。

 主页：https://www.sgi.com/tech/stl/download.html

 Muduo

 muduo 是一个基于 Reactor 模式的现代 C++ 网络库，它采用非阻塞 IO 模型，基于事件驱动和回调，原生支持多核多线程，适合编写 Linux 服务端多线程网络应用程序。

 主页:https://github.com/chenshuo/muduo

 C++ 资源大全
 关于 C++ 框架、库和资源的一些汇总列表，内容包括：标准库、Web应用框架、人工智能、数据库、图片处理、机器学习、日志、代码分析等。

  

  标准库

  C++标准库，包括了STL容器，算法和函数等。


  C++ Standard Library：是一系列类和函数的集合，使用核心语言编写，也是C++ISO自身标准的一部分。

  Standard Template Library：标准模板库

  C POSIX library ： POSIX系统的C标准库规范

  ISO C++ Standards Committee ：C++标准委员会


   


   框架


   C++通用框架和库



   Apache C++ Standard Library：是一系列算法，容器，迭代器和其他基本组件的集合

   ASL ：Adobe源代码库提供了同行的评审和可移植的C++源代码库。

   Boost ：大量通用C++库的集合。

   BDE ：来自于彭博资讯实验室的开发环境。

   Cinder：提供专业品质创造性编码的开源开发社区。

   Cxxomfort：轻量级的，只包含头文件的库，将C++ 11的一些新特性移植到C++03中。

   Dlib：使用契约式编程和现代C++科技设计的通用的跨平台的C++库。

   EASTL ：EA-STL公共部分

   ffead-cpp ：企业应用程序开发框架

   Folly：由Facebook开发和使用的开源C++库

   JUCE ：包罗万象的C++类库，用于开发跨平台软件

   libPhenom：用于构建高性能和高度可扩展性系统的事件框架。

   LibSourcey ：用于实时的视频流和高性能网络应用程序的C++11 evented IO

   LibU ： C语言写的多平台工具库

   Loki ：C++库的设计，包括常见的设计模式和习语的实现。

   MiLi ：只含头文件的小型C++库

   openFrameworks ：开发C++工具包，用于创意性编码。

   Qt ：跨平台的应用程序和用户界面框架

   Reason ：跨平台的框架，使开发者能够更容易地使用Java，.Net和Python，同时也满足了他们对C++性能和优势的需求。

   ROOT ：具备所有功能的一系列面向对象的框架，能够非常高效地处理和分析大量的数据，为欧洲原子能研究机构所用。

   STLport：是STL具有代表性的版本

   STXXL：用于额外的大型数据集的标准模板库。

   Ultimate++ ：C++跨平台快速应用程序开发框架

   Windows Template Library：用于开发Windows应用程序和UI组件的C++库

   Yomm11 ：C++11的开放multi-methods.

https://www.cnblogs.com/netfocus/archive/2011/10/10/2204949.html

https://docs.python.org/3/tutorial/modules.html

https://www.html5rocks.com/en/tutorials/webrtc/basics/#toc-history
