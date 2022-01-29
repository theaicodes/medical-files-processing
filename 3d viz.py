from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

# print the header of the file
image = nib.load('./scan.nii.gz')
mask = nib.load('./mask.nii.gz')
print("Image shape: ", image.shape)
print("Mask shape: ", mask.shape)
print('\n', "#" * 10, " Image header ", "#" * 10, '\n')
print(image.header) # output header information
print('\n', "#" * 10, " Mask header ", "#" * 10, '\n')
print(mask.header) # output header information

#shape has four parameters scan.nii.gz
width, height, queue = image.dataobj.shape
OrthoSlicer3D(image.dataobj).show()

for num, i in enumerate(range(0, queue, 10), start=1):
    img_arr = image.dataobj[:, :, i]
    plt.subplot(5, 5, num)
    plt.imshow(img_arr, cmap='gray')
plt.show()