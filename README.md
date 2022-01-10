Converts simple png icon-like pictures with one colour and transparent or white background to 
colours specified in the list "colours". Also converts white background to transparent.

The resulting image has only one colour + transparent background! All resulting images are saved 
in folders named by their respective colours. The program should create the folders if they aren't 
there already.

I used it to recolour dice images for a dice rolling app, but it should it be flexible enough to 
recolour other one-colour png images/icons by only changing these variables:

colours = list of colours for the picture to be recoloured into
transparent_img_names = names of source images with transparent background (except the .png)
non_trans_img_names = names of source images with non-transparent background (except the .png)
source_folder = the folder where all the source images are stored
