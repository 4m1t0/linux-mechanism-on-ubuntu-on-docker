# Chapter 5

`free` command shows the total memory of the system and the used memory.
```bash
root@84ecd6f3285c:/home/scripts/chapter5% free
              total        used        free      shared  buff/cache   available
Mem:        2046748      268468      156560         748     1621720     1617564
Swap:       1048572           0     1048572
```
`buff/cache` field shows the memory which is used by buffer cache and page cache.  
When the value of `free` field decrease, this field is released by _kernel_ and increases the `free`.  
`available` field is the memory we are actually able to use.  
This field is sum of `free` and the releasable memory by _kernel_.

When _kernel_ cannot relase any memory and no free space is, memory management system kills some processes and get free spaces.  
This mechanism is called _OOM (Out of Memory) Killer_.

In this chapter we focus how to allocate memory to processes by memory management systems.  
To understand actual allocation process, we have to understand virtual memory.  
So we focus a simple case which puts virtual memory behind and the problems caused by the case.

_Kernel_ allocates memory to processes at the following scene.
- when the process is created
- allocating memory dynamically to the process after it is created

The first case is already described in Chapter 3, so we discuss the second case here.  
When the process needs more memory, it calls a system call for acquiring memory.  
Then _kernel_ cuts out required memory and allocate the start address of it.  
The above procedures have some problems shown in the following.
- memory fragmentation
- being able to access other memory for other processes
- be difficult to deal with multi processes

Virtual memory solves above issues.  
_Kernel_ passes physical address to memory in the simple case, but virtual address in actual.  
Virtual address has a page table held in _kernel_'s memory region it maps a virtual address space to a physical address space.  
Processes doesn't doesn't share their page tables each other, so a process cannot override other page tables.  
When we refer a virtual address not having physical address, systems cause `Segmentation fault`.
```bash
root@84ecd6f3285c:/home/scripts/chapter5% cc -o segv segv.c
root@84ecd6f3285c:/home/scripts/chapter5% ./segv
before invalid access
Segmentation fault
```

Let's confirm the process allocating memory dynamically.
```bash
root@84ecd6f3285c:/home/scripts/chapter5% ./mmap
*** memory map before memory allocation ***
55ee4b3b9000-55ee4b3ba000 r-xp 00000000 08:01 3670795                    /home/scripts/chapter5/mmap
55ee4b5b9000-55ee4b5ba000 r--p 00000000 08:01 3670795                    /home/scripts/chapter5/mmap
55ee4b5ba000-55ee4b5bb000 rw-p 00001000 08:01 3670795                    /home/scripts/chapter5/mmap
55ee4b99e000-55ee4b9bf000 rw-p 00000000 00:00 0                          [heap]
7f74b52d1000-7f74b54b8000 r-xp 00000000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b54b8000-7f74b56b8000 ---p 001e7000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b56b8000-7f74b56bc000 r--p 001e7000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b56bc000-7f74b56be000 rw-p 001eb000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b56be000-7f74b56c2000 rw-p 00000000 00:00 0
7f74b56c2000-7f74b56e9000 r-xp 00000000 08:01 3539572                    /lib/x86_64-linux-gnu/ld-2.27.so
7f74b58e3000-7f74b58e5000 rw-p 00000000 00:00 0
7f74b58e9000-7f74b58ea000 r--p 00027000 08:01 3539572                    /lib/x86_64-linux-gnu/ld-2.27.so
7f74b58ea000-7f74b58eb000 rw-p 00028000 08:01 3539572                    /lib/x86_64-linux-gnu/ld-2.27.so
7f74b58eb000-7f74b58ec000 rw-p 00000000 00:00 0
7ffc663b9000-7ffc663da000 rw-p 00000000 00:00 0                          [stack]
7ffc663fb000-7ffc663fd000 r--p 00000000 00:00 0                          [vvar]
7ffc663fd000-7ffc663ff000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]

*** succeeded to allocate memory: address = 0x7f74aeed1000; size = 0x6400000 ***

*** memory map after memory allocation ***
55ee4b3b9000-55ee4b3ba000 r-xp 00000000 08:01 3670795                    /home/scripts/chapter5/mmap
55ee4b5b9000-55ee4b5ba000 r--p 00000000 08:01 3670795                    /home/scripts/chapter5/mmap
55ee4b5ba000-55ee4b5bb000 rw-p 00001000 08:01 3670795                    /home/scripts/chapter5/mmap
55ee4b99e000-55ee4b9bf000 rw-p 00000000 00:00 0                          [heap]
# added memory
7f74aeed1000-7f74b52d1000 rw-p 00000000 00:00 0
7f74b52d1000-7f74b54b8000 r-xp 00000000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b54b8000-7f74b56b8000 ---p 001e7000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b56b8000-7f74b56bc000 r--p 001e7000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b56bc000-7f74b56be000 rw-p 001eb000 08:01 3539590                    /lib/x86_64-linux-gnu/libc-2.27.so
7f74b56be000-7f74b56c2000 rw-p 00000000 00:00 0
7f74b56c2000-7f74b56e9000 r-xp 00000000 08:01 3539572                    /lib/x86_64-linux-gnu/ld-2.27.so
7f74b58e3000-7f74b58e5000 rw-p 00000000 00:00 0
7f74b58e9000-7f74b58ea000 r--p 00027000 08:01 3539572                    /lib/x86_64-linux-gnu/ld-2.27.so
7f74b58ea000-7f74b58eb000 rw-p 00028000 08:01 3539572                    /lib/x86_64-linux-gnu/ld-2.27.so
7f74b58eb000-7f74b58ec000 rw-p 00000000 00:00 0
7ffc663b9000-7ffc663da000 rw-p 00000000 00:00 0                          [stack]
7ffc663fb000-7ffc663fd000 r--p 00000000 00:00 0                          [vvar]
7ffc663fd000-7ffc663ff000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
```

This dynamic allocation process has the problem uselessly wasting memory.  
_demand paging_ solves this problem by mapping a virtual address space to a physical address space when accessing a virtual address in the virtual address space at first time.

We may sometimes see the lack of memory.  
It is caused by two reasons, the lack of phisical memory and the lack of virtual memory.  
The first one is obvious.  
Another reason is caused when the process uses the max size of virtual memory and requires additional virtual memory.

When systems cannot allocate additional memory because of the lack of physical memory, then systems do _swapping_.  
In linux a unit of swapping is a page, so it is also called _paging_.  
_swapping_ write some memory region on the swap region on a strage device.  
It is called _swap-out_.  
During swap-out, the process read the data to the swap region.  
When some regions are free, _swapping_ gets the swap-outed data from the swap region and the process has on phisical memory.  
It is called _swap-in_.  
Swapping has a problem which is accessing to strages is too late comapring to accessing to physical memory.

This virtual memory strategy with aforementioned simple page table occupies large memory, so computers make it hierarchical to save memory.  
In the hierarchical strategy, a page table has child page tables.  
_Kernel_ allocates a new page table when it comes neccessary and a parent page tables refers it.  
By this strategy total entries of page tables is less than that by the simple strategy.  
Therefore computers don't allocate memory more than necessary.  
The most important point is to decrease total entries of page tables.  

The more the usage of virtual memory increases, the more the usage of physical memory increases.  
In addition, `fork()` will be slow because `fork()` doesn't allocate the physical memory used by the parent process but make a page table of the same size as the page size used by the parent.  
To resolve this issue, _Huge table_ strategy is used.  
This strategy is also based on decreasing page table entries.

## References
- [［試して理解］Linuxのしくみ～実験と図解で学ぶOSとハードウェアの基礎知識](https://gihyo.jp/book/2018/978-4-7741-9607-7)