cpp_vs_python.png : CamiloBalaguera_Graficas.py
	python3 CamiloBalaguera_Graficas.py

gen_times.out : CamiloBalaguera_Graficas.py
	c++ CamiloBalaguera_GenerarTiempos.cpp -o gen_times.out

CamiloBalaguera_Graficas.py : times_cpp.csv
	./.gen_times.out >> times_cpp.csv

CamiloBalaguera_Graficas.py : times_python.csv
	./.gen_times.out >> times_cpp.csv


