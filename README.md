# Stego-tree
Heres how you can decode that silly tree in Wikipedias Steganography section as depicted below: <br>
<br>
*"Image of a tree with a steganographically hidden image. The hidden image is revealed by removing all but the two least significant bits of each color component and a subsequent normalization. The hidden image is shown below."*

<img width="255" alt="Screenshot 2023-10-18 at 10 57 58 AM" src="https://github.com/katstews/Stego-tree/assets/112781868/eb2909be-a041-4168-9585-68474030b29d">

## Uh yeah that cool and all, but how tf do I do that? 
So suprisingly, googling didn't actually take that long (THANK GOD). I was super worried I wouldn't find a soultion, but then I came upon a god send of an article on "Steganography" and how it actually works inserting an image inside an image. (https://towardsdatascience.com/steganography-hiding-an-image-inside-another-77ca66b2acb1) Bless you **Kelvin Salton do Prado**. 
<br>

So basically, every pixel has 3 layers of color on top of it. Red, Green, and Blue. You need this 3 colors to create a pixel, and a pixel could a wide variety of colors.<br> <img width="697" alt="Screenshot 2023-10-18 at 11 06 02 AM" src="https://github.com/katstews/Stego-tree/assets/112781868/bb9505cc-0763-4e90-a514-12c40afbf11c"> <br>

R, G, and B will all be a different decimal value, which we will represent in binary form. We know that binary number is made up of 8 bits, and the rightmost bit is the **least** signif bit and the leftmost is the **most** signif bit. Meaning if we change the last bit, the value will not change *that* much. At most, by **ONE**. <br>
<img width="697" alt="Screenshot 2023-10-18 at 11 10 15 AM" src="https://github.com/katstews/Stego-tree/assets/112781868/d59eb8be-da0a-4f35-9cd1-1553fa2b58e6"> <br>
As the image above, if we changed the last big of 10110001 -> 10110000, it would be the val 176. <br> 

We are going to take advantage of that and manipulate the least significant bit in the pixel map to insert our image there. <br>

<img width="697" alt="Screenshot 2023-10-18 at 11 11 35 AM" src="https://github.com/katstews/Stego-tree/assets/112781868/a968e475-06bc-468f-8e44-109ce04f55e9">
The code in the repo follow the image right above. Knowing that we keep the last two least signifcant bits in the tree png, we are going to take those values and tack on 6 0's, to create a new byte. 

