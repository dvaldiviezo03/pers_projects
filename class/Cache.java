import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Vector;

public class Cache {
    // atr
    private String name;
    private int addressSize, wordSize, blockSize, numLines, hits, misses, requests;
    private Vector<Block> blocks = new Vector<Block>();
    private String semester;

    public Cache(String name, String semester, int addressSize, int wordSize, int blockSize, int numLines) {
        this.name = name;
        this.semester = semester;
        this.addressSize = addressSize;
        this.wordSize = wordSize;
        this.blockSize = blockSize;
        this.numLines = numLines;

        this.hits = 0;
        this.misses = 0;
        this.requests = 0;

        for (int i = 0; i < this.numLines; i++) {
            this.blocks.addElement(new Block());
        }
    }

    // print method to print the cache informations
    public void print() {
        String output = "";
        // calc whole size of C.M
        int dmcSize = (this.numLines * ((this.blockSize * 32) + 32));
        long memByte = (long) Math.pow(2, this.addressSize);

        output += "********** " + this.name + " Cache Size Report **********\n";
        output += " Memory   : " + ((int) (memByte / 4)) + " words of " + this.wordSize + " bits (" + (memByte)
                + " bytes)\n";
        output += " Cache    : " + this.numLines + " lines with 1 word tag and " + this.blockSize + " words data each ("
                + (dmcSize / 8) + " bytes)\n";
        output += "\n";

        System.out.println(output);
    }

    public void readLocation(int address) {
        String output = "";
        int blockNum = (address / (this.blockSize * 4));
        int totalBlocks = (int) ((Math.pow(2, this.addressSize - (int) (Math.log(this.blockSize * 4) / Math.log(2))))
                - 1);
        int offset = (address % ((int) Math.pow(2, (int) (Math.log(this.blockSize * 4) / Math.log(2)))));
        int offsetBits = (int) (Math.log(this.blockSize * 4) / Math.log(2));
        int index = (blockNum % this.numLines);
        int indexBits = (int) (Math.log(this.numLines) / Math.log(2));
        int tagBits = (32 - (offsetBits + indexBits + 2));
        int tag = (address / ((int) (Math.pow(2, this.blockSize))));

        output += " Read mem   :" + address + " (" + binary(address, this.addressSize) + ")\n";
        output += " Block num  :" + blockNum + " (" + binary(blockNum, Integer.bitCount(totalBlocks)) + ")\n";
        output += " Offset     :" + offset + " (" + binary(offset, offsetBits) + ")\n";
        output += " Index      :" + index + " (" + binary(index, indexBits) + ")\n";
        output += " Tag        :" + tag + " (" + binary(tag, tagBits) + ")\n";

        if (this.blocks.elementAt(index).isValid() && this.blocks.elementAt(index).getTag() == tag) {
            this.hits++;
            output += "\n Result: ** Hit **";
        } else {
            this.misses++;
            this.blocks.elementAt(index).setValid(true);
            this.blocks.elementAt(index).setTag(tag);
            output += "\n Result: Miss";
        }

        this.requests++;
        System.out.println(output);
    }

    public void stats() {
        NumberFormat fmt = new DecimalFormat("#0.00");
        String output = "";

        double hitRatio = (((double) this.hits / (double) this.requests) * 100);
        double missRatio = (((double) this.misses / (double) this.requests) * 100);

        output += "********** \n";
        output += "********** " + this.name + " Cache Status Report\n";
        output += "********** " + this.semester + "\n";
        output += "********** ";
        output += "\n\t" + "Requests: " + this.requests;
        output += "\n\t" + "Hits: " + this.hits + " (" + fmt.format(hitRatio) + "%)";
        output += "\n\t" + "Misses: " + this.misses + " (" + fmt.format(missRatio) + "%)";
        output += "\n";

        System.out.println(output);
    }

    private String binary(int x, int size) {
        return String.format("%32s", Integer.toBinaryString(x)).replace(" ", "0").substring(32 - size);
    }
}
