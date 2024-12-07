public class Block {
    private boolean valid;
    private int tag;

    public Block() {
        this.valid = false;
        this.tag = 0;
    }

    // getter and setters
    public boolean isValid() {
        return valid;
    }

    public void setValid(boolean valid) {
        this.valid = valid;
    }

    public int getTag() {
        return tag;
    }

    public void setTag(int tag) {
        this.tag = tag;
    }
}