from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import time
from PIL import ImageDraw

img = Image.open('chapter1.jpg')

plt.imshow(img)

px = img.load()
print(px)

pix_val = list(img.getdata())

print(pix_val)

pixel = []

coordinates = []

for a in range(0, 1000):
    for b in range(0, 1500):
        rgb = px[a, b]
        coordinates.append([a, b])

column = ['coordinated', 'RGB']
df = pd.DataFrame(zip(coordinates, pix_val), columns=column)
print(df)

list_of_list = [list(t) for t in pix_val]
print(list_of_list)


current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)

list_with_added_number = [[element + generated_number for element in sublist] for sublist in list_of_list]
print(list_with_added_number)

list_of_tuples_after_addition = [tuple(sublist) for sublist in list_with_added_number]
print(list_of_tuples_after_addition)

df = pd.DataFrame(zip(coordinates, list_of_tuples_after_addition), columns=column)
print(df)

output_image = Image.new("RGB", (1000, 1500))
draw = ImageDraw.Draw(output_image)

for row in df.itertuples(index=True, name='Pandas'):
    draw.point(row.coordinated, row.RGB)

name = 'chapter1out'
output_image.save('{}.jpg'.format(name))

imgNew = Image.open('chapter1out.jpg')

plt.imshow(imgNew)

r_values = [sublist[0] for sublist in list_with_added_number]
print(r_values)

sum_r_Values = sum(sublist[0] for sublist in list_with_added_number)
print(sum_r_Values)