# imports
import sys

# each class from every import has to be imported individualy. '*' is used to import all classes.
from byuimage import *

# red < 26 & blue < 30 & green > 50 = green

def reassign_pixel_color(input_pixel: Pixel, output_red: int, output_green: int, output_blue: int):
    
    input_pixel.red = output_red
    input_pixel.green = output_green
    input_pixel.blue = output_blue



def darken(file_path: str, output_file_name: str, percent: float):
    
    new_image = Image(file_path)
    
    for pixel in new_image:
        
        pixel.red *= 1 - percent
        pixel.green *= 1 - percent
        pixel.blue *= 1 - percent
        
    new_image.save(output_file_name)
    
    print("DEBUG: darkened image saved successfully")



def sepia(file_path: str, output_file_name: str):
    
    new_image = Image(file_path)
    
    for pixel in new_image:
        
        true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
        true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
        true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue
        
        reassign_pixel_color(pixel, true_red, true_green, true_blue)
        
        if pixel.red > 255:
            pixel.red = 255
        if pixel.green > 255:
            pixel.green = 255
        if pixel.blue > 255:
            pixel.blue = 255
            
    new_image.save(output_file_name)
    
    print("DEBUG: sepiaed image saved successfully")
    


def grayscale(file_path: str, output_file_name: str):
    
    new_image = Image(file_path)
    
    for pixel in new_image:
        
        average = (pixel.red + pixel.green + pixel.blue) / 3
        
        reassign_pixel_color(pixel, average, average, average)
        
    new_image.save(output_file_name)
    
    print("DEBUG: grayscale image saved successfully")



def make_borders(file_path: str, output_file_name: str, thickness: int, red: int, green: int, blue: int):
    
    original_image = Image(file_path)
    
    new_image = Image.blank(original_image.width + (thickness*2), original_image.height + (thickness*2))
    
    for pixel in new_image:
        
        reassign_pixel_color(pixel, red, green, blue)
    
    for x in range(original_image.width):
        
        for y in range(original_image.height):
            
            old_pixel = original_image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + thickness, y + thickness)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    new_image.save(output_file_name)
    
    print("DEBUG: bordered image saved successfully")
    
    

def flipped(file_path: str, output_file_name: str):
    
    original_image = Image(file_path)
    
    new_image = Image.blank(original_image.width, original_image.height)
    
    # take the bottom line of the first image and make it the top line of the second image
    for y in range(original_image.height):
        
        for x in range(original_image.width):
        
            # original_image.height is 1 out of bounds (since python starts counting at 0), so we have to subtract 1
            old_pixel = original_image.get_pixel(x, original_image.height - y - 1)  # get the bottom line of the first image
            new_pixel = new_image.get_pixel(x, y)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    new_image.save(output_file_name)
    
    print("DEBUG: flipped image saved successfully")
    
    

def mirror(file_path: str, output_file_name: str):
    
    original_image = Image(file_path)
    
    new_image = Image.blank(original_image.width, original_image.height)
    
    # take the bottom line of the first image and make it the top line of the second image
    for y in range(original_image.height):
        
        for x in range(original_image.width):
        
            # original_image.height is 1 out of bounds (since python starts counting at 0), so we have to subtract 1
            old_pixel = original_image.get_pixel(original_image.width - x - 1, y)
            new_pixel = new_image.get_pixel(x, y)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    new_image.save(output_file_name)
    
    print("DEBUG: mirrored image saved successfully")
    
    

def collage(image_1_path: str, image_2_path: str, image_3_path: str, image_4_path: str, output_image_name: str, border_thickness: int):

    image_1_handler = Image(image_1_path)
    image_2_handler = Image(image_2_path)
    image_3_handler = Image(image_3_path)
    image_4_handler = Image(image_4_path)
    
    # border_thickness is being multipleid by 3 because there's an additional border in the middle (so 3 borders total)
    new_image = Image.blank((image_1_handler.width + image_2_handler.width) + (border_thickness*3), (image_1_handler.height + image_3_handler.height) + (border_thickness*3))

    # color borders black
    for pixel in new_image:
        
        reassign_pixel_color(pixel, 0, 0, 0)
    
    # Image 1
    for x in range(image_1_handler.width):
        
        for y in range(image_1_handler.height):
            
            old_pixel = image_1_handler.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + border_thickness, y + border_thickness)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    # Image 2
    for x in range(image_2_handler.width):
        
        for y in range(image_2_handler.height):
            
            old_pixel = image_2_handler.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + border_thickness*2 + image_1_handler.width, y + border_thickness)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    # Image 3
    for x in range(image_3_handler.width):
        
        for y in range(image_3_handler.height):
            
            old_pixel = image_3_handler.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + border_thickness, y + border_thickness*2 + image_1_handler.height)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    # Image 4
    for x in range(image_4_handler.width):
        
        for y in range(image_4_handler.height):
            
            old_pixel = image_4_handler.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + border_thickness*2 + image_3_handler.width, y + border_thickness*2 + image_2_handler.height)
            
            reassign_pixel_color(new_pixel, old_pixel.red, old_pixel.green, old_pixel.blue)
            
    new_image.save(output_image_name)
    
    print("DEBUG: collage saved successfully")



def greenscreen_filter(foreground_image_path: str, background_image_path: str, output_image_name: str, threshold: int, factor: float):
    
    # one with greenscreen
    foreground_image = Image(foreground_image_path)
    
    # cool custom background image
    background_image = Image(background_image_path)
    
    for x in range(foreground_image.width):
        
        for y in range(foreground_image.height):
            
            foreground_pixel = foreground_image.get_pixel(x, y)
            background_pixel = background_image.get_pixel(x, y)
            
            # If the pixel is green, change the color to the custom background pixel color
            average = (foreground_pixel.red + foreground_pixel.green + foreground_pixel.blue) / 3 
            
            if foreground_pixel.green >= factor * average and foreground_pixel.green > threshold:
                
                reassign_pixel_color(foreground_pixel, background_pixel.red, background_pixel.green, background_pixel.blue)
                
                
                
    foreground_image.save(output_image_name)
                
                
                
def validate_commands(lst):
    
    # removes the first element from the list
    lst.pop(0)
    
    # * element [0] is now the 'second argument' of the command
    # display image: -d <image_path>
    if lst[0] == '-d' and len(lst) == 2:
        
        image = Image(lst[1])
        
        image.show()
        
        print("DEBUG: image loaded successfully")
        
        
    # darken image: -k <input file> <output file> <percent: float vlaue (1.0 to 0.0)>
    elif lst[0] == '-k' and len(lst) == 4:
        
        darken(lst[1], lst[2], float(lst[3]))  # 'float' converts the string to a float
        
    
    # sepia image: -s <input file> <output file>
    elif lst[0] == '-s' and len(lst) == 3:
    
        sepia(lst[1], lst[2])
        
        
    # grayscale image: -g <input file> <output file>
    elif lst[0] == '-g' and len(lst) == 3:
    
        grayscale(lst[1], lst[2])
        
        
    # image borders: -b <input file> <output file> <thickness> <red> <green> <blue>
    elif lst[0] == '-b' and len(lst) == 7:
        
        make_borders(lst[1], lst[2], int(lst[3]), int(lst[4]), int(lst[5]), int(lst[6]))  # 'int' converts the string to an integer
        
        
    # flipped image: -f <input file> <output file>
    elif lst[0] == '-f' and len(lst) == 3:
    
        flipped(lst[1], lst[2])
        
        
    # mirror image: -m <input file> <output file>
    elif lst[0] == '-m' and len(lst) == 3:
    
        mirror(lst[1], lst[2])
        
        
    # make collage: -c <image 1> <image 2> <image 3> <image 4> <output image> <border thickness>
    elif lst[0] == '-c' and len(lst) == 7:
        
        collage(lst[1], lst[2], lst[3], lst[4], lst[5], int(lst[6]))
        
        
    # greenscreen_filter: -y <foreground image> <background image> <output file> <threshold> <factor>
    elif lst[0] == '-y' and len(lst) == 6:
        
        greenscreen_filter(lst[1], lst[2], lst[3], int(lst[4]), float(lst[5]))  # 'int' converts the string to an integer
    
    
    # error message
    else:
        
        print("\nInvalid format. Try:")
        print("- for display image: -d <image_path>")
        print("- for darken image: -k <input file> <output file> <percent: float vlaue (1.0 to 0.0)>")
        print("- for sepia image: -s <input file> <output file>")
        print("- for grayscale image: -g <input file> <output file>")
        print("- for image borders: -b <input file> <output file> <thickness> <red> <green> <blue>")
        print("- for flipped image: -f <input file> <output file>")
        print("- for mirror image: -m <input file> <output file>")
        print("- for make collage: -c <image 1> <image 2> <image> <image 3> <image 4> <output image> <border thickness>")
        print("- for greenscreen filter: -y <foreground image> <background image> <output file> <threshold> <factor>")
        print("")
        


# this gets executed when the script is run
if __name__ == "__main__":
   
   validate_commands(sys.argv)
   
   print("DEBUG: File ran successfully")