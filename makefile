graficas.png: graficador.py datos.txt
	python graficador.py
datos.txt: solucion.x
	./solucion.x
solucion.x: burger.cpp
	g++ burger.cpp -o solucion.x
clean:
	rm -rf *.png *.x *.txt  