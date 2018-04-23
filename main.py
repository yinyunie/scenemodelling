if __name__ == '__main__':
    import argparse
    import cv2
    import numpy as np
    from lib import vtkdraw

    parser = argparse.ArgumentParser(description="Auto modelling of 3D indoor scene from a single image.")
    parser.add_argument("-i", "--img", dest="imgname", type=str, metavar="IMAGE",
                        help="Give the address of source image")
    parser.add_argument("-f", "--file", dest = "file", type=str, metavar="FILE",
                        help="Give the folder path of the preliminary result of layout prediction.")

    args = parser.parse_args()

    # Read the source file
    try:
        image = cv2.imread(args.imgname)
        layout = np.load(args.file + '/layout.npy')
        K = np.load(args.file + '/K.npy')
        vps = np.load(args.file + '/vps.npy')
        linelabels = np.load(args.file + '/linelabel.npy')
        label_vp = np.load(args.file + '/label_vp.npy')
    except IOError:
        print 'Cannot open the image file, please check the image address.'

    # draw vps
    scene = vtkdraw.Scene(K, vps)
    scene.draw()

    print "Debug"

