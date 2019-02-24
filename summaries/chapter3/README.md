# Chapter 3

`fork()` is called to process a program on multi processes and creates a new process according to following steps.  
1. Create a memory region for a new child process and copy the memory of the parent process to the new memory.
2. The return value of `fork()` is different between parent and child.  
   Fork the processes by using this behavior and run different codes.

The kernel's processing flow to run a task is following.  
1. Read the target file and expand data on memory on the current process.
2. Override the memory of the current process by the data of a new process.
3. Run a new task.

In other words, when run a new task the number of processes doesn't increase but also a process is replaced by another process.  
To run another program we call `execve()` and it provides the function described above.

When we create a new process we usually call `exec()` after `fork()`.  
Now I confirm the fork-and-exec flow.
```bash
root@84ecd6f3285c:/home/scripts/chapter3% cc -o fork-and-exec fork-and-exec.c
root@84ecd6f3285c:/home/scripts/chapter3% ./fork-and-exec
I'm parent! my pid is 231 and the pid of my child is 232.
I'm child! my pid is 232.
root@84ecd6f3285c:/home/scripts/chapter3% hello
```
`_exit()` which runs the `exit_group()` system call is called at the end of program and collects memory allocated it's process.  
We usually call `exit()` in a standard C library instead of `_exit()`.

## References
- [［試して理解］Linuxのしくみ～実験と図解で学ぶOSとハードウェアの基礎知識](https://gihyo.jp/book/2018/978-4-7741-9607-7)
- [LINUX PROCESSES AND SIGNALS](https://www.bogotobogo.com/Linux/linux_process_and_signals.php)