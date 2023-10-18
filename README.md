# Stego-tree
Heres how you can decode that silly tree in Wikipedias Steganography section as depicted below: <br>
<br>
*"Image of a tree with a steganographically hidden image. The hidden image is revealed by removing all but the two least significant bits of each color component and a subsequent normalization. The hidden image is shown below."*

<img width="255" alt="Screenshot 2023-10-18 at 10 57 58 AM" src="https://github.com/katstews/Stego-tree/assets/112781868/eb2909be-a041-4168-9585-68474030b29d">

## Uh yeah that cool and all, but how tf do I do that? 
So suprisingly, googling didn't actually take that long (THANK GOD). I was super worried I wouldn't find a soultion, but then I came upon a god send of an article on "Steganography" and how it actually works inserting an image inside an image. (https://towardsdatascience.com/steganography-hiding-an-image-inside-another-77ca66b2acb1) Bless you **Kelvin Salton do Prado**. 
<br>
So basically, every pixel has 3 layers of color on top of it. Red, Green, and Blue. You need this 3 colors to create a pixel, and a pixel could a wide variety of colors.<br> <img width="697" alt="Screenshot 2023-10-18 at 11 06 02 AM" src="https://github.com/katstews/Stego-tree/assets/112781868/bb9505cc-0763-4e90-a514-12c40afbf11c"> <br>

