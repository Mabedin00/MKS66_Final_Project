all:
	python3 main.py masterpiece.mdl.java
	convert -delay 6 -loop 0 anim/*.png anim/movie.gif
	animate anim/movie.gif

clean:
	rm anim/*.png
	rm anim/*.gif
