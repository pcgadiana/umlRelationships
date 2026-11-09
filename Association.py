class Student {
    String name = "John";
}

class Teacher {
    void teach(Student student) {
        System.out.println("Teacher teaches " + student.name);
    }
}

public class Main {
    public static void main(String[] args) {
        Teacher teacher = new Teacher();
        Student student = new Student();

        teacher.teach(student);
    }
}