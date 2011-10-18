
all: house-prices.png

2004-05-trend: 2004-trend.py
	python 2004-trend.py

house-prices.png: gnuplot-script real-estate-prices 2004-05-trend
	gnuplot gnuplot-script