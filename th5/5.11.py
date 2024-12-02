print ("Nguyễn Danh Ánh")
print ("235752021610023")
print ("###########")
import numpy as np
data = np.array([('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.1), ('Pit', 5, 40.11)],
                dtype=[('Name', 'U10'), ('Class', 'i4'), ('Height', 'f4')])

sorted_data = np.sort(data, order=['Class', 'Height'])
print(sorted_data)
