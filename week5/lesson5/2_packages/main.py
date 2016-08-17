import dir1.dir2.mod

# в действительности происходит следующее:
# import dir1
# import dir1.dir2
# import dir1.dir2.mod

# повторного выполнения кода не происходит
import dir1.dir2.mod


# полный путь к файлу, из которого модуль был создан (загружен)
print(dir1.__file__)

# список файловых путей, в которых находится пакет. 
print(dir1.__path__)

# from string import ascii_letters
# вызовет ошибку, так как будет импортироваться пакет string из текущей 
# директории
