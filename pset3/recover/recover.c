#include <stdio.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    int counter = 0;

    //check if user wrote 2 strings
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }
    if (argc == 2)
    {
        //Opening a memory card
        FILE *file = fopen(argv[1], "r");
        if (file == NULL)
        {
            fprintf(stderr, "Could not open %s.\n", argv[1]);
            return 2;
        }

        FILE *img = NULL;

        unsigned char buffer[512];
        char filename[8];
        bool symbol = false;

        //reads 512 bytes by 1, and checking first 4 symbols
        while (fread (buffer, 512, 1, file) == 1)
        {
            //checking first 4 bits
            if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
            {
                if (symbol == true)
                {
                    fclose (img);
                }
                else
                {
                    symbol = true;
                }
                //writing down file name and open image
                sprintf(filename, "%03i.jpg", counter);
                img = fopen(filename, "w");
                counter ++;
            }
            //writing down 512 bytes by one
            if(symbol == true)
            {
                //writing down 512 bytes by one
                fwrite(&buffer, 512, 1, img);
            }
        }
        //closing files
        fclose(file);
        fclose(img);
        return 0;
    }
}
