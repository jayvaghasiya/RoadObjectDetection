from PIL import Image

def copy_and_paste_image(source_path, destination_path):
    # Open the source image
    source_image = Image.open(source_path)

    # Create a new canvas (white image) with the same size as the source image
    canvas = Image.new("RGB", source_image.size, (255, 255, 255))

    # Paste the source image onto the canvas at the desired position
    canvas.paste(source_image)

    # Save the new image with the pasted content
    canvas.save(destination_path)


def copy_and_paste_text(source_file, destination_file):
    try:
        # Read the content from the source file
        with open(source_file, 'r') as source:
            content = source.read()

        # Write the content to the destination file
        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Successfully copied content from '{source_file}' to '{destination_file}'.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"Error: {e}")


with open('kitti_train.txt','r')as f:
    train = f.readlines()

for i in train:
    tf = i.split('/')
    name = tf[-1].split('.')[0]
    copy_and_paste_image(i[:-1],f'datasets/train/images/{name}.png')
    copy_and_paste_text(f'labels/{name}.txt',f'datasets/train/labels/{name}.txt')

with open('kitti_test.txt','r')as f:
    test = f.readlines()

for i in test:
    tf = i.split('/')
    name = tf[-1].split('.')[0]
    copy_and_paste_image(i[:-1],f'datasets/test/images/{name}.png')
    copy_and_paste_text(f'labels/{name}.txt',f'datasets/test/labels/{name}.txt')