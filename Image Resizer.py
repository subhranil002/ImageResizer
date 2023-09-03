import cv2


def imageResizer(source, destination, scale_percent):
    print("Initializing...")
    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

    new_height = int(src.shape[0] * scale_percent/100)
    new_width = int(src.shape[1] * scale_percent/100)

    print("Resizing...")
    output = cv2.resize(src, (new_width, new_height))

    cv2.imwrite(destination, output)
    cv2.waitKey(0)

    print("Successfully Resized!")


# Configurable Parameters
source = "example.jpeg"
destination = "newIamge.jpeg"
scale_percent = 50

imageResizer(source, destination, scale_percent)
