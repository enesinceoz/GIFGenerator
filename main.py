from PIL import Image

filenames= ['cat1.jpg', 'cat2.jpg', 'cat3.jpg']

images = [Image.open(filename) for filename in filenames]
frame_duration = 500

images[0].save('team.gif',save_all=True , append_images=images[1:], duration= frame_duration, loop= 0)
