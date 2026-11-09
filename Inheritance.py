class Glassware {
    String material = "Glass";

    void display() {
        System.out.println("This is glassware.");
    }
}

class Beaker extends Glassware {
    void showBeaker() {
        System.out.println("This is a beaker.");
        System.out.println("Material: " + material);
    }
}

public class Main {
    public static void main(String[] args) {
        Beaker b = new Beaker();
        b.display();
        b.showBeaker();
    }
}