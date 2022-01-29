# importing libraries
import dicom2nifti
import os

# get names ofall sub-directories
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders
    
    
folders = fast_scandir('ppmi_dataset/male_pd')
    
# convert dicom to nifti
img = 0
for sub_fold in folders:
    if sub_fold.count('/') > 4:
        try:
            dicom2nifti.dicom_series_to_nifti(sub_fold, os.path.join(path_out, 'img_'+ str(img)))
            img = img + 1
        except:
            pass
