import img2pdf, sys, os

if __name__ == '__main__':
    if sys.argv[1] is not None:
        dir = sys.argv[1]
    else:
        dir = os.getcwd()

    with open("images.pdf", "wb") as f:
        images = []

        for fname in os.listdir(dir):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(dir, fname)
            if os.path.isdir(path):
                continue
            images.append(path)
        f.write(img2pdf.convert(images))