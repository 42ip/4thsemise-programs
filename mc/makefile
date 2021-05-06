$(file): $(file).o
	arm-none-eabi-ld $(file).o -o $(file)

$(file).o: $(file).s
	arm-none-eabi-as $(file).s -o $(file).o

run:
	qemu-arm $(file)

clean: 
	rm -f $(file).o $(file) *.core