using System;
using System.Collections;

class XorEncrypt {


    static void Main () {
        string _stringInput;
        int _keyInput;

        byte[] 

        for (;;) { //get input to encrypt
            Console.Write("Input String :");
            string input = Console.ReadLine();
            for (int i = 0; i < input.Length; i++) {
                if (input[i] > 256) {
                    Console.Write("Invalid String (not an 8 bit character set).");
                    continue;
                }
            }
            break;
        }

        for (;;) { //get a value from 0 to 255 for the key
            Console.Write("Input Key    :");
            string input = Console.ReadLine();
            if(Int32.TryParse(input, intInput)) {
                Console.WriteLine("Input must be integer.");
                continue;
            }
            if (keyInputInt > 255 || keyInputInt < 0) {
                Console.WriteLine("Must be between 0 and 255.");
                continue;
            }
            break;
        }


    }
}

XorEncrypt.Main();