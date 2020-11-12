using System;
using System.Collections;

class XorEncrypt {
    public static void Main() {
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