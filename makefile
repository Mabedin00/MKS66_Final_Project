all:
	python3 main.py $(NAME).java
	convert -delay 6 -loop 0 anim/*.png anim/movie.gif
	animate anim/movie.gif

clean:
	rm anim/*.png
	rm anim/*.gif
