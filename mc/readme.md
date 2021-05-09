##Dependencies

```bash
arm-none-eabi-gcc //for cross compiling
qemu-arm //for running arm outputs
```

##How to make and run

```bash
make file=<filename> //to make(build/compile) the file
make run file=<filename> //to run it use 
make clean file=filename //to clean ones outputs use
```

####Example
 (here hw is the name of the file )

```bash
make file=hw
make run file=hw
make clean file=hw
```