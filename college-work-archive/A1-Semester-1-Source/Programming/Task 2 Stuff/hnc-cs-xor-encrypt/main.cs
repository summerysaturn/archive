using System;
using System.Collections;

class XorEncrypt {
    static byte XorByte (byte _arg1, byte _arg2) {
        BitArray _arg1ba = new BitArray (new byte[] {_arg1});
        BitArray _arg2ba = new BitArray (new byte[] {_arg2});
        byte _xorByteOutput;
        _arg1ba.Xor(_arg2ba);

        _xorByteOutput = BitArrayToByte(_arg1ba);
        return _xorByteOutput;
    }

    static private byte BitArrayToByte (BitArray n) {
        byte[] _tempBA = new byte[1];
        n.CopyTo(_tempBA, 0);
        return _tempBA[0];
    }

    static byte[] EncryptXB (byte[] tempInput, byte tempKey) {
        byte[] _tempOutput = new byte[tempInput.Length];
        for (int i=0;i < tempInput.Length; i++) {
            _tempOutput[i] = XorByte(tempInput[i], tempKey);
        }   

        return _tempOutput;
    }

    public static void Main() {
        string mainInput;
        string keyInput;
        int keyInputInt;

        for (;;) { //get input to encrypt
            Console.Write("Input String :");
            mainInput = Console.ReadLine();
            for (int i = 0; i < mainInput.Length; i++) {
                if (mainInput[i] > 256) {
                    Console.Write("Invalid String (not 8-bit).");
                    continue;
                }
            }
            break;
        }

        for (;;) { //get a value from 0 to 255 for the key
            Console.Write("Input Key    :");
            string input = Console.ReadLine();
            if (!int.TryParse(input, out keyInputInt)) {
                Console.WriteLine("Input must be integer.");
                continue;
            }
            if (keyInputInt > 255 || keyInputInt < 0) {
                Console.WriteLine("Must be between 0 and 255.");
                continue;
            }
            break;
        }

        byte[] _inputByteArray = Encoding.ASCII.GetBytes(mainInput);
        byte _tempKeyByte = Convert.ToByte(keyInputInt);

        byte[] _encryptedBytes = EncryptXB(_inputByteArray, _tempKeyByte);

        string stringOutput = "";
        for (int i = 0; i < _encryptedBytes.Length; i++) {
            stringOutput += _encryptedBytes[i].ToString("X");
        }

        Console.WriteLine(stringOutput);
    }
}

XorEncrypt.Main();