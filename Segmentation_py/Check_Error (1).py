import Doan1
from matplotlib import pyplot as plt
S = []
Centers = []
White_pixel =[]


Dientich1, Dientich2, Vitritam1, Vitritam2, Pixeltrang1, Pixeltrang2 = Doan1.Img_processing("D:\Tai Lieu\Do an 1\c79267f2e1b830e669a9.jpg", "D:\Tai Lieu\Do an 1\hinh.jpg")

Dodoitam, TileS, Chenhlech = Doan1.Caculate(Dientich2, Dientich1, Vitritam2, Vitritam1, Pixeltrang2, Pixeltrang1)
Doan1.Compare(Dodoitam, TileS, Chenhlech)