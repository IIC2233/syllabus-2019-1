from PIL import Image


def get_pixels(image_path):
    img = Image.open(image_path, "r")
    w, h = img.size
    pixels_matrix = list(img.getdata())
    plte = get_image_plte(image_path)
    if plte:
        pixels_matrix = [plte[index] for index in pixels_matrix]
    return [pixels_matrix[n:n+w] for n in range(0, w*h, w)]


def get_image_plte(image_path):
    with open(image_path, "rb") as file:
        for number in [137, 80, 78, 71, 13, 10, 26, 10]:
            if int.from_bytes(file.read(1), byteorder="big") != number:
                return
        size, type_of_chunk, data, src = read_chunk(file)
        while(type_of_chunk != "IDAT"):
            if type_of_chunk == "PLTE":
                return get_plte_from_data(data, size)
            size, type_of_chunk, data, src = read_chunk(file)


def read_chunk(file):
    size = int.from_bytes(file.read(4), byteorder="big")
    type_of_chunk = file.read(4).decode("ASCII")
    data = file.read(size)
    crc = file.read(4)
    return size, type_of_chunk, data, crc


def get_plte_from_data(data, size):
    data = [int.from_bytes(data[i:i+1], "big") for i in range(size)]
    return [(data[i], data[i+1], data[i+2]) for i in range(0, size, 3)]
