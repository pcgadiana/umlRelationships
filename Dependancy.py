String content;

    Document(String content) {
        this.content = content;
    }
}

class Printer {
    void print(Document document) {
        System.out.println("Printing: " + document.content);
    }
}

public class Main {
    public static void main(String[] args) {
        Document document = new Document("Hello World!");
        Printer printer = new Printer();

        printer.print(document);
    }
}