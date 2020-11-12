private void button1_Click(object sender, EventArgs e)
{
    BigInteger inputInt;
    BigInteger outputInt;
    if (!BigInteger.TryParse(textBox1.Text, out inputInt))
    {
        richTextBox1.Text = "Must input an integer (failed BigInteger.TryParse()).";
    }
    else
    {
        outputInt = inputInt;
        if (outputInt.ToString().Length > 10000)
        {
            richTextBox1.Text = "Output more than 10,000 characters long.";
        }
        else
        {
            outputInt = outputInt * outputInt;
            textBox1.Text = Convert.ToString(outputInt);
            richTextBox1.Text = "Success!";
        }
    }
}