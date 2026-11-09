class Beaker {
    Beaker() {
        System.out.println("Beaker created.");
    }
}

class Tray {
    Beaker[] beakers;

    Tray() {
        beakers = new Beaker[5];

        for (int i = 0; i < 5; i++) {
            beakers[i] = new Beaker();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Tray tray = new Tray();
    }
}