import os
import glob
import shutil
import urllib.request

from multiprocessing import Pool

img_dir = os.path.join('data/images')  # data root
os.makedirs(img_dir, exist_ok=True)

broken_links = [os.path.basename(img)[:-4]
                for img in glob.glob('data/metadata/image_url/broken_links/*.jpg')]


def run(line):
    image_id, image_url = line.strip().split('\t')
    image_id, image_url = image_id.strip(), image_url.strip()

    dst_path = os.path.join('data/images/{}.jpg'.format(image_id))
#    if not os.path.exists()
    if not os.path.exists(dst_path):
        print(dst_path)
        if image_id in broken_links:
            shutil.copy(
                os.path.join('data/metadata/image_url/broken_links/{}.jpg',format(image_id)),
                dst_path
            )
        else:
            try:
                urllib.request.urlretrieve(
                    image_url,
                    dst_path
                )
            except Exception as err:
                print("[{}] {}: {}".format(err, image_id, image_url))


if __name__ == '__main__':

    pool = Pool(4)
    lines = []
    for target in ['dress', 'shirt', 'toptee']:
        with open('data/metadata/image_url/asin2url.{}.txt'.format(target), 'r') as f:
            lines.extend(f.readlines())

    print("Total number of images: {}".format(len(lines)))
    pool.map(run, lines)

    print("Fashion IQ dataset has been downloaded.")
